import bpy
import bmesh
from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty, BoolProperty
from bpy.types import Operator
from bpy.app.translations import pgettext_iface as _
from typing import Set, List

bl_info = {
    "name": "SVG Importer Plus",
    "author": "KRACT", 
    "version": (1, 0, 1),
    "blender": (4, 2, 0),
    "description": "Enhanced SVG import with automatic mesh conversion and origin centering",
    "location": "File > Import > SVG Importer Plus (.svg)",
    "category": "Import-Export"
}


class SVGMaterialManager:
    """Handles SVG material cleanup operations"""
    
    @staticmethod
    def remove_materials_from_objects(objects: List[bpy.types.Object]) -> None:
        """Remove all materials from specified objects"""
        for obj in objects:
            if obj.data and hasattr(obj.data, 'materials'):
                obj.data.materials.clear()
    
    @staticmethod
    def cleanup_unused_svg_materials() -> int:
        """Remove unused SVG materials from Blender's material database"""
        materials_to_remove = []
        for material in bpy.data.materials:
            if material.name.startswith("SVG") and material.users == 0:
                materials_to_remove.append(material)
        
        for material in materials_to_remove:
            bpy.data.materials.remove(material)
        
        return len(materials_to_remove)
    
    @classmethod
    def remove_svg_materials(cls, objects: List[bpy.types.Object]) -> int:
        """Complete SVG material removal process"""
        cls.remove_materials_from_objects(objects)
        return cls.cleanup_unused_svg_materials()


class SVGPostProcessor:
    """Handles post-processing operations for imported SVG objects"""
    
    def __init__(self, convert_to_mesh: bool = True, center_origin: bool = True):
        self.convert_to_mesh = convert_to_mesh
        self.center_origin = center_origin
        self.converted_count = 0
        self.centered_count = 0
    
    def process_object(self, obj: bpy.types.Object) -> None:
        """Process a single object with mesh conversion and origin centering"""
        bpy.context.view_layer.objects.active = obj
        obj.select_set(True)
        
        try:
            if self.convert_to_mesh and obj.type == 'CURVE':
                self._convert_to_mesh(obj)
            
            if self.center_origin:
                self._center_origin(obj)
        
        finally:
            obj.select_set(False)
    
    def _convert_to_mesh(self, obj: bpy.types.Object) -> None:
        """Convert curve object to mesh"""
        try:
            bpy.ops.object.convert(target='MESH')
            self.converted_count += 1
        except Exception as e:
            raise RuntimeError(f"Failed to convert {obj.name} to mesh: {str(e)}")
    
    def _center_origin(self, obj: bpy.types.Object) -> None:
        """Center object origin to geometry bounds"""
        try:
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
            self.centered_count += 1
        except Exception as e:
            raise RuntimeError(f"Failed to center origin for {obj.name}: {str(e)}")
    
    def get_statistics(self) -> tuple:
        """Get processing statistics"""
        return self.converted_count, self.centered_count

class IMPORT_OT_svg_plus(Operator, ImportHelper):
    """Import SVG with automatic mesh conversion and origin centering"""
    bl_idname = "import_mesh.svg_plus"
    bl_label = "SVG Importer Plus"
    bl_options = {'REGISTER', 'UNDO'}

    filename_ext = ".svg"
    filter_glob: StringProperty(
        default="*.svg",
        options={'HIDDEN'},
        maxlen=255,
    )

    convert_to_mesh: BoolProperty(
        name="Convert to Mesh",
        description="Automatically convert curves to mesh",
        default=True,
    )

    center_origin: BoolProperty(
        name="Center Origin",
        description="Move origin to geometry center",
        default=True,
    )

    def execute(self, context):
        if not self._validate_inputs():
            return {'CANCELLED'}
        
        try:
            original_objects = set(context.scene.objects)
            new_objects = self._import_svg_file(original_objects)
            
            if not new_objects:
                self.report({'WARNING'}, _("No objects were imported"))
                return {'CANCELLED'}
            
            self._process_imported_objects(new_objects)
            self._report_results(new_objects)
            
            return {'FINISHED'}
            
        except Exception as e:
            self.report({'ERROR'}, f"Import failed: {str(e)}")
            return {'CANCELLED'}
    
    def _validate_inputs(self) -> bool:
        """Validate input parameters before processing"""
        import os
        
        if not self.filepath:
            self.report({'ERROR'}, "No file path specified")
            return False
        
        if not os.path.exists(self.filepath):
            self.report({'ERROR'}, f"File does not exist: {self.filepath}")
            return False
        
        if not self.filepath.lower().endswith('.svg'):
            self.report({'ERROR'}, "Selected file is not an SVG file")
            return False
        
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                content = f.read(1024)
                if '<svg' not in content.lower():
                    self.report({'ERROR'}, "File does not appear to be a valid SVG")
                    return False
        except Exception as e:
            self.report({'ERROR'}, f"Cannot read file: {str(e)}")
            return False
        
        return True
    
    def _import_svg_file(self, original_objects: Set[bpy.types.Object]) -> List[bpy.types.Object]:
        """Import SVG file and return newly created objects"""
        try:
            bpy.ops.import_curve.svg(filepath=self.filepath)
        except Exception as e:
            raise RuntimeError(f"Failed to import SVG: {str(e)}")
        
        return [obj for obj in bpy.context.scene.objects if obj not in original_objects]
    
    def _process_imported_objects(self, new_objects: List[bpy.types.Object]) -> None:
        """Process all imported objects with material cleanup and post-processing"""
        SVGMaterialManager.remove_svg_materials(new_objects)
        
        processor = SVGPostProcessor(self.convert_to_mesh, self.center_origin)
        
        for obj in new_objects:
            try:
                processor.process_object(obj)
            except RuntimeError as e:
                self.report({'WARNING'}, str(e))
        
        self.converted_count, self.centered_count = processor.get_statistics()
    
    def _report_results(self, new_objects: List[bpy.types.Object]) -> None:
        """Generate and report import results"""
        total_objects = len(new_objects)
        messages = [f"Imported {total_objects} object(s)"]
        
        if self.convert_to_mesh and self.converted_count > 0:
            messages.append(f"converted {self.converted_count} to mesh")
        
        if self.center_origin and self.centered_count > 0:
            messages.append(f"centered {self.centered_count} origins")
        
        self.report({'INFO'}, _(", ").join(messages))


    def draw(self, context):
        layout = self.layout
        
        layout.use_property_split = True
        layout.use_property_decorate = False
        
        layout.separator()
        layout.label(text=_("Post-Processing Options:"))
        
        layout.prop(self, "convert_to_mesh")
        layout.prop(self, "center_origin")


def menu_func_import(self, context):
    self.layout.operator(IMPORT_OT_svg_plus.bl_idname, text=_("SVG Importer Plus (.svg)"))


class SVGTranslations:
    """Centralized translation management for SVG Importer Plus"""
    
    TRANSLATIONS = {
        "en_US": {},
        "ja_JP": {
            # Operator descriptions
            ("*", "Import SVG with automatic mesh conversion and origin centering"): 
                "自動メッシュ変換と原点中央配置でSVGをインポート",
            ("*", "SVG Importer Plus"): "SVG Importer Plus",
            
            # Property labels and descriptions  
            ("*", "Convert to Mesh"): "メッシュに変換",
            ("*", "Automatically convert curves to mesh"): "カーブを自動的にメッシュに変換",
            ("*", "Center Origin"): "原点を中央に",
            ("*", "Move origin to geometry center"): "原点をジオメトリの中心に移動",
            
            # UI labels
            ("*", "Post-Processing Options:"): "後処理オプション:",
            ("*", "SVG Importer Plus (.svg)"): "SVG Importer Plus (.svg)",
            
            # Status messages
            ("*", "No objects were imported"): "オブジェクトがインポートされませんでした",
            
            # Formatting
            ("*", ", "): "、",
        }
    }
    
    @classmethod
    def get_translations(cls):
        """Get the translation dictionary"""
        return cls.TRANSLATIONS
    
    @classmethod
    def register_translations(cls, module_name: str):
        """Register translations with Blender"""
        try:
            bpy.app.translations.register(module_name, cls.TRANSLATIONS)
        except ValueError:
            pass
    
    @classmethod
    def unregister_translations(cls, module_name: str):
        """Unregister translations from Blender"""
        try:
            bpy.app.translations.unregister(module_name)
        except ValueError:
            pass


def register():
    """アドオン登録"""
    bpy.utils.register_class(IMPORT_OT_svg_plus)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)
    SVGTranslations.register_translations(__name__)


def unregister():
    """アドオン登録解除"""
    SVGTranslations.unregister_translations(__name__)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
    bpy.utils.unregister_class(IMPORT_OT_svg_plus)


if __name__ == "__main__":
    register()
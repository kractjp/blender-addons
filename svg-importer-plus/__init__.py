import bpy
import bmesh
from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty, BoolProperty
from bpy.types import Operator
from bpy.app.translations import pgettext_iface as _

bl_info = {
    "name": "SVG Importer Plus",
    "author": "KRACT", 
    "version": (1, 0, 1),
    "blender": (4, 2, 0),
    "description": "Enhanced SVG import with automatic mesh conversion and origin centering",
    "location": "File > Import > SVG Importer Plus (.svg)",
    "category": "Import-Export"
}

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
        # Store original objects to identify newly imported ones
        original_objects = set(context.scene.objects)
        
        # Import SVG using Blender's built-in importer
        try:
            bpy.ops.import_curve.svg(filepath=self.filepath)
        except Exception as e:
            self.report({'ERROR'}, f"Failed to import SVG: {str(e)}")
            return {'CANCELLED'}
        
        # Find newly imported objects
        new_objects = [obj for obj in context.scene.objects if obj not in original_objects]
        
        if not new_objects:
            self.report({'WARNING'}, _("No objects were imported"))
            return {'CANCELLED'}
        
        # Remove SVG材質 material from all newly imported objects
        self.remove_svg_materials(new_objects)
        
        # Store statistics
        converted_count = 0
        centered_count = 0
        
        # Process each imported object
        for obj in new_objects:
            # Select the object
            bpy.context.view_layer.objects.active = obj
            obj.select_set(True)
            
            # Convert to mesh if it's a curve and conversion is enabled
            if self.convert_to_mesh and obj.type == 'CURVE':
                try:
                    bpy.ops.object.convert(target='MESH')
                    converted_count += 1
                except Exception as e:
                    self.report({'WARNING'}, f"Failed to convert {obj.name} to mesh: {str(e)}")
            
            # Center origin if enabled
            if self.center_origin:
                try:
                    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
                    centered_count += 1
                except Exception as e:
                    self.report({'WARNING'}, f"Failed to center origin for {obj.name}: {str(e)}")
            
            # Deselect for next iteration
            obj.select_set(False)
        
        # Report results
        total_objects = len(new_objects)
        messages = [f"Imported {total_objects} object(s)"]
        
        if self.convert_to_mesh and converted_count > 0:
            messages.append(f"converted {converted_count} to mesh")
        
        if self.center_origin and centered_count > 0:
            messages.append(f"centered {centered_count} origins")
        
        self.report({'INFO'}, _(", ").join(messages))
        
        return {'FINISHED'}

    def remove_svg_materials(self, objects):
        """Remove all materials from imported objects to prevent SVG material assignment"""
        for obj in objects:
            if obj.data and hasattr(obj.data, 'materials'):
                # Clear all materials from the object
                obj.data.materials.clear()
        
        # Clean up unused materials from Blender's material database
        materials_to_remove = []
        for material in bpy.data.materials:
            if material.name.startswith("SVG") and material.users == 0:
                materials_to_remove.append(material)
        
        for material in materials_to_remove:
            bpy.data.materials.remove(material)

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


# Translation dictionary
translations_dict = {
    "en_US": {},
    "ja_JP": {
        ("*", "Import SVG with automatic mesh conversion and origin centering"): "自動メッシュ変換と原点中央配置でSVGをインポート",
        ("*", "SVG Importer Plus"): "SVG Importer Plus",
        ("*", "Convert to Mesh"): "メッシュに変換",
        ("*", "Automatically convert curves to mesh"): "カーブを自動的にメッシュに変換",
        ("*", "Center Origin"): "原点を中央に",
        ("*", "Move origin to geometry center"): "原点をジオメトリの中心に移動",
        ("*", "Post-Processing Options:"): "後処理オプション:",
        ("*", "No objects were imported"): "オブジェクトがインポートされませんでした",
        ("*", ", "): "、",
        ("*", "SVG Importer Plus (.svg)"): "SVG Importer Plus (.svg)",
    }
}


def register():
    """アドオン登録"""
    bpy.utils.register_class(IMPORT_OT_svg_plus)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)
    
    # 翻訳を登録
    try:
        bpy.app.translations.register(__name__, translations_dict)
    except ValueError:
        # 既に登録済みの場合は無視
        pass


def unregister():
    """アドオン登録解除"""
    # 翻訳を解除
    try:
        bpy.app.translations.unregister(__name__)
    except ValueError:
        # 登録されていない場合は無視
        pass
    
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
    bpy.utils.unregister_class(IMPORT_OT_svg_plus)


if __name__ == "__main__":
    register()
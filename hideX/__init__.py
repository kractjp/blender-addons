import bpy
from bpy.props import CollectionProperty
from bpy.types import PropertyGroup
from bpy.app.translations import pgettext_iface as _

bl_info = {
    "name": "hideX",
    "author": "KRACT",
    "version": (1, 0, 0),
    "blender": (4, 2, 0),
    "description": "Advanced object visibility control with H key integration",
    "location": "3D Viewport > Sidebar > Item Tab",
    "category": "3D View"
}

class HIDEX_HiddenObject(PropertyGroup):
    """Property group to store hidden object information"""
    object_pointer: bpy.props.PointerProperty(
        name="Object Pointer",
        type=bpy.types.Object,
        description="Direct reference to the hidden object"
    )
    original_hide_viewport: bpy.props.BoolProperty(name="Original Viewport Hide State")
    original_hide_render: bpy.props.BoolProperty(name="Original Render Hide State")

class HIDEX_OT_hide_selected(bpy.types.Operator):
    """Hide selected objects in viewport and disable in render"""
    bl_idname = "hidex.hide_selected"
    bl_label = "Hide Selected"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        scene = context.scene
        
        if not hasattr(scene, 'hidex_hidden_objects'):
            return {'CANCELLED'}
        
        selected_objects = [obj for obj in context.selected_objects if obj.type in {'MESH', 'CURVE', 'SURFACE', 'META', 'FONT', 'ARMATURE', 'LATTICE', 'EMPTY', 'LIGHT', 'CAMERA'}]
        
        if not selected_objects:
            self.report({'WARNING'}, _("No valid objects selected"))
            return {'CANCELLED'}
        
        hidden_count = 0
        for obj in selected_objects:
            # Store original visibility states
            hidden_obj = scene.hidex_hidden_objects.add()
            hidden_obj.object_pointer = obj
            hidden_obj.original_hide_viewport = obj.hide_viewport
            hidden_obj.original_hide_render = obj.hide_render
            
            # Hide in both viewport and render
            obj.hide_viewport = True
            obj.hide_render = True
            obj.hide_set(True)  # Also use hide_set for viewport
            hidden_count += 1
        
        self.report({'INFO'}, _("Hidden {} objects").format(hidden_count))
        return {'FINISHED'}

class HIDEX_OT_show_object(bpy.types.Operator):
    """Show specific hidden object"""
    bl_idname = "hidex.show_object"
    bl_label = "Show Object"
    bl_options = {'REGISTER', 'UNDO'}
    
    object_index: bpy.props.IntProperty(name="Object Index")
    
    def execute(self, context):
        scene = context.scene
        
        if not hasattr(scene, 'hidex_hidden_objects'):
            return {'CANCELLED'}
        
        # Check if index is valid
        if self.object_index >= len(scene.hidex_hidden_objects):
            self.report({'WARNING'}, _("Invalid object index"))
            return {'CANCELLED'}
        
        hidden_obj = scene.hidex_hidden_objects[self.object_index]
        obj = hidden_obj.object_pointer
        
        if obj is None:
            # Object was deleted, remove from hidden list
            scene.hidex_hidden_objects.remove(self.object_index)
            self.report({'WARNING'}, _("Object no longer exists"))
            return {'CANCELLED'}
        
        # Restore original visibility states
        obj.hide_viewport = hidden_obj.original_hide_viewport
        obj.hide_render = hidden_obj.original_hide_render
        obj.hide_set(hidden_obj.original_hide_viewport)  # Restore viewport visibility
        
        # Remove from hidden list
        scene.hidex_hidden_objects.remove(self.object_index)
        
        self.report({'INFO'}, _("Showed object '{}'").format(obj.name))
        return {'FINISHED'}

class HIDEX_OT_show_all(bpy.types.Operator):
    """Show all hidden objects"""
    bl_idname = "hidex.show_all"
    bl_label = "Show All Hidden"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        scene = context.scene
        
        if not hasattr(scene, 'hidex_hidden_objects'):
            return {'CANCELLED'}
        
        if len(scene.hidex_hidden_objects) == 0:
            self.report({'INFO'}, _("No hidden objects to show"))
            return {'FINISHED'}
        
        shown_count = 0
        # Process in reverse order to avoid index issues when removing items
        for i in range(len(scene.hidex_hidden_objects) - 1, -1, -1):
            hidden_obj = scene.hidex_hidden_objects[i]
            obj = hidden_obj.object_pointer
            
            if obj is not None:
                # Restore original visibility states
                obj.hide_viewport = hidden_obj.original_hide_viewport
                obj.hide_render = hidden_obj.original_hide_render
                obj.hide_set(hidden_obj.original_hide_viewport)  # Restore viewport visibility
                shown_count += 1
            
            # Remove from hidden list
            scene.hidex_hidden_objects.remove(i)
        
        self.report({'INFO'}, _("Showed {} objects").format(shown_count))
        return {'FINISHED'}


class HIDEX_PT_panel(bpy.types.Panel):
    """HideX control panel"""
    bl_label = "hideX"
    bl_idname = "HIDEX_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Item"
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
        # Main buttons
        col = layout.column(align=True)
        col.scale_y = 1.2
        col.operator("hidex.hide_selected", text=_("Hide Selected") + " (H)", icon='HIDE_ON')
        col.operator("hidex.show_all", text=_("Show All Hidden"), icon='HIDE_OFF')
        
        
        layout.separator()
        
        # Hidden objects list
        if bpy.app.translations.locale == 'ja_JP':
            layout.label(text="非表示:")
        else:
            layout.label(text="Hidden:")
        
        if hasattr(scene, 'hidex_hidden_objects') and len(scene.hidex_hidden_objects) > 0:
            box = layout.box()
            for i, hidden_obj in enumerate(scene.hidex_hidden_objects):
                row = box.row(align=True)
                
                # Check if object still exists and get appropriate icon
                obj = hidden_obj.object_pointer
                if obj is not None:
                    # Get object type icon
                    icon_map = {
                        'MESH': 'OUTLINER_OB_MESH',
                        'CURVE': 'OUTLINER_OB_CURVE',
                        'SURFACE': 'OUTLINER_OB_SURFACE',
                        'META': 'OUTLINER_OB_META',
                        'FONT': 'OUTLINER_OB_FONT',
                        'ARMATURE': 'OUTLINER_OB_ARMATURE',
                        'LATTICE': 'OUTLINER_OB_LATTICE',
                        'EMPTY': 'OUTLINER_OB_EMPTY',
                        'LIGHT': 'OUTLINER_OB_LIGHT',
                        'CAMERA': 'OUTLINER_OB_CAMERA',
                    }
                    obj_icon = icon_map.get(obj.type, 'OBJECT_DATA')
                    row.label(text=obj.name, icon=obj_icon, translate=False)
                else:
                    row.label(text=f"({_('deleted')})", icon='ERROR', translate=False)
                
                # Show button for individual object
                op = row.operator("hidex.show_object", text="", icon='HIDE_OFF')
                op.object_index = i
        else:
            box = layout.box()
            box.label(text=_("No hidden objects"), icon='INFO')

# Keymap handling
addon_keymaps = []


# Translation dictionary
translations_dict = {
    "en_US": {},
    "ja_JP": {
        ("*", "Hide Selected"): "選択を非表示",
        ("*", "Show All Hidden"): "すべて表示",
        ("Operator", "Hidden"): "非表示",
        ("*", "No hidden objects"): "非表示オブジェクトなし",
        ("*", "No valid objects selected"): "有効なオブジェクトが選択されていません",
        ("*", "Hidden {} objects"): "{}個のオブジェクトを非表示にしました",
        ("*", "Invalid object index"): "無効なオブジェクトインデックス",
        ("*", "Object no longer exists"): "オブジェクトは存在しません",
        ("*", "Showed object '{}'"): "オブジェクト'{}'を表示しました",
        ("*", "No hidden objects to show"): "表示する非表示オブジェクトがありません",
        ("*", "Showed {} objects"): "{}個のオブジェクトを表示しました",
        ("*", "deleted"): "削除済み",
    }
}

def register():
    """Register addon"""
    bpy.utils.register_class(HIDEX_HiddenObject)
    bpy.utils.register_class(HIDEX_OT_hide_selected)
    bpy.utils.register_class(HIDEX_OT_show_object)
    bpy.utils.register_class(HIDEX_OT_show_all)
    bpy.utils.register_class(HIDEX_PT_panel)
    
    # Add property to scene
    bpy.types.Scene.hidex_hidden_objects = CollectionProperty(type=HIDEX_HiddenObject)
    
    # Register translations
    try:
        bpy.app.translations.register(__name__, translations_dict)
    except ValueError:
        # Already registered, skip
        pass
    
    # Add keymap to override default H key behavior
    wm = bpy.context.window_manager
    if wm.keyconfigs.addon:
        # Override in Object Mode
        km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
        kmi = km.keymap_items.new('hidex.hide_selected', 'H', 'PRESS')
        addon_keymaps.append((km, kmi))
        
        # Override in 3D View Generic
        km = wm.keyconfigs.addon.keymaps.new(name='3D View Generic', space_type='VIEW_3D')
        kmi = km.keymap_items.new('hidex.hide_selected', 'H', 'PRESS')
        addon_keymaps.append((km, kmi))

def unregister():
    """Unregister addon"""
    # Remove keymap
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    
    # Unregister translations
    try:
        bpy.app.translations.unregister(__name__)
    except ValueError:
        # Not registered, skip
        pass
    
    # Remove property from scene
    del bpy.types.Scene.hidex_hidden_objects
    
    bpy.utils.unregister_class(HIDEX_PT_panel)
    bpy.utils.unregister_class(HIDEX_OT_show_all)
    bpy.utils.unregister_class(HIDEX_OT_show_object)
    bpy.utils.unregister_class(HIDEX_OT_hide_selected)
    bpy.utils.unregister_class(HIDEX_HiddenObject)

if __name__ == "__main__":
    register()

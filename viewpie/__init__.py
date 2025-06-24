import bpy
from bpy.types import Menu

bl_info = {
    "name": "Viewpie",
    "author": "KRACT",
    "version": (1, 0, 0),
    "blender": (4, 2, 0),
    "description": "Navigate 3D viewport with an intuitive pie menu for quick view changes",
    "location": "3D Viewport: Q key (customizable)",
    "category": "3D View"
}

# Translation dictionary
translations = {
    "en_US": {
        "Right": "Right",
        "Left": "Left", 
        "Bottom": "Bottom",
        "Top": "Top",
        "Back": "Back",
        "Front": "Front",
        "Camera": "Camera",
        "Perspective/Ortho": "Perspective/Ortho",
        "View Selected": "View Selected",
        "View All": "View All",
        "Center Cursor": "Center Cursor",
        "Basic Views": "Basic Views",
        "Perspective": "Perspective",
        "Orthographic": "Orthographic"
    },
    "ja_JP": {
        "Right": "右面",
        "Left": "左面",
        "Bottom": "底面", 
        "Top": "上面",
        "Back": "背面",
        "Front": "前面",
        "Camera": "カメラ",
        "Perspective/Ortho": "透視/平行",
        "View Selected": "選択オブジェクト表示",
        "View All": "全体表示",
        "Center Cursor": "カーソル中心",
        "Basic Views": "基本ビュー",
        "Perspective": "透視",
        "Orthographic": "平行"
    }
}

def get_translation(text):
    """Get translated text based on current language and UI translation setting"""
    prefs = bpy.context.preferences.view
    
    # Check if translation is enabled in UI
    if not prefs.use_translate_interface:
        # If translation is disabled, always use English
        return translations.get('en_US', {}).get(text, text)
    
    # If translation is enabled, check the system language
    lang = prefs.language
    
    # Map Blender language codes to our translation keys
    lang_map = {
        'ja_JP': 'ja_JP',
        'DEFAULT': 'en_US'
    }
    
    # Get the appropriate language key
    lang_key = lang_map.get(lang, 'en_US')
    
    # Return translated text or original if not found
    return translations.get(lang_key, {}).get(text, text)

class VIEWPIE_OT_set_view(bpy.types.Operator):
    """Set 3D viewport to specific view"""
    bl_idname = "viewpie.set_view"
    bl_label = "Set View"
    
    view_type: bpy.props.StringProperty(name="View Type")
    
    @classmethod
    def poll(cls, context):
        return context.area and context.area.type == 'VIEW_3D'
    
    def execute(self, context):
        view_3d = context.space_data
        region_3d = context.region_data
        
        view_mapping = {
            'FRONT': 'FRONT',
            'BACK': 'BACK',
            'LEFT': 'LEFT',
            'RIGHT': 'RIGHT',
            'TOP': 'TOP',
            'BOTTOM': 'BOTTOM',
            'CAMERA': 'CAMERA'
        }
        
        if self.view_type in view_mapping:
            if self.view_type == 'CAMERA':
                bpy.ops.view3d.view_camera()
            else:
                bpy.ops.view3d.view_axis(type=view_mapping[self.view_type])
        elif self.view_type == 'PERSPECTIVE':
            region_3d.view_perspective = 'PERSP'
        elif self.view_type == 'ORTHOGRAPHIC':
            region_3d.view_perspective = 'ORTHO'
        elif self.view_type == 'SELECTED':
            bpy.ops.view3d.view_selected()
        elif self.view_type == 'ALL':
            bpy.ops.view3d.view_all()
        elif self.view_type == 'CENTER':
            bpy.ops.view3d.view_center_cursor()
        
        return {'FINISHED'}

class VIEWPIE_OT_toggle_projection(bpy.types.Operator):
    """Toggle between perspective and orthographic projection"""
    bl_idname = "viewpie.toggle_projection"
    bl_label = "Toggle Projection"
    
    @classmethod
    def poll(cls, context):
        return context.area and context.area.type == 'VIEW_3D'
    
    def execute(self, context):
        region_3d = context.region_data
        if region_3d.view_perspective == 'PERSP':
            region_3d.view_perspective = 'ORTHO'
            self.report({'INFO'}, "Switched to Orthographic")
        else:
            region_3d.view_perspective = 'PERSP'
            self.report({'INFO'}, "Switched to Perspective")
        
        return {'FINISHED'}

class VIEWPIE_MT_pie_menu(Menu):
    """Viewpie pie menu for viewport navigation"""
    bl_label = "Viewpie"
    bl_idname = "VIEWPIE_MT_pie_menu"
    
    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        
        # Right (3 o'clock) - Left View  
        op = pie.operator("viewpie.set_view", text=get_translation("Left"), icon='TRIA_LEFT')
        op.view_type = 'LEFT'
        
        # Left (9 o'clock) - Right View
        op = pie.operator("viewpie.set_view", text=get_translation("Right"), icon='TRIA_RIGHT')
        op.view_type = 'RIGHT'
        
        # Bottom (6 o'clock) - Bottom View
        op = pie.operator("viewpie.set_view", text=get_translation("Bottom"), icon='TRIA_DOWN')
        op.view_type = 'BOTTOM'
        
        # Top (12 o'clock) - Top View
        op = pie.operator("viewpie.set_view", text=get_translation("Top"), icon='TRIA_UP')
        op.view_type = 'TOP'
        
        # Top-Left (10:30) - Back View
        op = pie.operator("viewpie.set_view", text=get_translation("Back"), icon='LOOP_BACK')
        op.view_type = 'BACK'
        
        # Top-Right (1:30) - Front View
        op = pie.operator("viewpie.set_view", text=get_translation("Front"), icon='LOOP_FORWARDS')
        op.view_type = 'FRONT'
        
        # Bottom-Left (7:30) - Camera View
        op = pie.operator("viewpie.set_view", text=get_translation("Camera"), icon='CAMERA_DATA')
        op.view_type = 'CAMERA'
        
        # Bottom-Right (4:30) - Toggle Projection
        pie.operator("viewpie.toggle_projection", text=get_translation("Perspective/Ortho"), icon='VIEW_PERSPECTIVE')

class VIEWPIE_MT_pie_menu_extended(Menu):
    """Extended Viewpie pie menu with additional options"""
    bl_label = "Viewpie Extended"
    bl_idname = "VIEWPIE_MT_pie_menu_extended"
    
    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        
        # Right (3 o'clock) - View Selected
        op = pie.operator("viewpie.set_view", text=get_translation("View Selected"), icon='ZOOM_SELECTED')
        op.view_type = 'SELECTED'
        
        # Left (9 o'clock) - View All
        op = pie.operator("viewpie.set_view", text=get_translation("View All"), icon='VIEWZOOM')
        op.view_type = 'ALL'
        
        # Bottom (6 o'clock) - Center View
        op = pie.operator("viewpie.set_view", text=get_translation("Center Cursor"), icon='PIVOT_CURSOR')
        op.view_type = 'CENTER'
        
        # Top (12 o'clock) - Main Pie Menu
        pie.menu("VIEWPIE_MT_pie_menu", text=get_translation("Basic Views"), icon='VIEW3D')
        
        # Top-Left (10:30) - Perspective
        op = pie.operator("viewpie.set_view", text=get_translation("Perspective"), icon='VIEW_PERSPECTIVE')
        op.view_type = 'PERSPECTIVE'
        
        # Top-Right (1:30) - Orthographic
        op = pie.operator("viewpie.set_view", text=get_translation("Orthographic"), icon='VIEW_ORTHO')
        op.view_type = 'ORTHOGRAPHIC'
        
        # Bottom-Left (7:30) - Camera View
        op = pie.operator("viewpie.set_view", text=get_translation("Camera"), icon='CAMERA_DATA')
        op.view_type = 'CAMERA'
        
        # Bottom-Right (4:30) - Empty for future expansion
        pie.separator()

class VIEWPIE_OT_call_pie_menu(bpy.types.Operator):
    """Call Viewpie pie menu"""
    bl_idname = "viewpie.call_pie_menu"
    bl_label = "Viewpie Pie Menu"
    
    extended: bpy.props.BoolProperty(
        name="Extended Menu",
        description="Show extended pie menu with additional options",
        default=False
    )
    
    @classmethod
    def poll(cls, context):
        return context.area and context.area.type == 'VIEW_3D'
    
    def execute(self, context):
        if self.extended:
            bpy.ops.wm.call_menu_pie(name="VIEWPIE_MT_pie_menu_extended")
        else:
            bpy.ops.wm.call_menu_pie(name="VIEWPIE_MT_pie_menu")
        return {'FINISHED'}

# Keymap management
addon_keymaps = []

def register():
    """Register addon"""
    bpy.utils.register_class(VIEWPIE_OT_set_view)
    bpy.utils.register_class(VIEWPIE_OT_toggle_projection)
    bpy.utils.register_class(VIEWPIE_OT_call_pie_menu)
    bpy.utils.register_class(VIEWPIE_MT_pie_menu)
    bpy.utils.register_class(VIEWPIE_MT_pie_menu_extended)
    
    # Add keymap
    wm = bpy.context.window_manager
    if wm.keyconfigs.addon:
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
        
        # Basic pie menu (Q key)
        kmi1 = km.keymap_items.new(
            'viewpie.call_pie_menu',
            type='Q',
            value='PRESS'
        )
        kmi1.properties.extended = False
        addon_keymaps.append((km, kmi1))
        
        # Extended pie menu (Shift+Q)
        kmi2 = km.keymap_items.new(
            'viewpie.call_pie_menu',
            type='Q',
            value='PRESS',
            shift=True
        )
        kmi2.properties.extended = True
        addon_keymaps.append((km, kmi2))

def unregister():
    """Unregister addon"""
    bpy.utils.unregister_class(VIEWPIE_OT_set_view)
    bpy.utils.unregister_class(VIEWPIE_OT_toggle_projection)
    bpy.utils.unregister_class(VIEWPIE_OT_call_pie_menu)
    bpy.utils.unregister_class(VIEWPIE_MT_pie_menu)
    bpy.utils.unregister_class(VIEWPIE_MT_pie_menu_extended)
    
    # Remove keymap
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

if __name__ == "__main__":
    register()
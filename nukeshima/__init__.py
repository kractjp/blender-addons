import bpy

bl_info = {
    "name": "Nukeshima",
    "author": "KRACT",
    "version": (1, 0, 0),
    "blender": (4, 2, 0),
    "description": "Silent deletion without annoying confirmation dialogs - just nuke it instantly",
    "location": "3D Viewport: X key (replaces default delete)",
    "category": "3D View"
}

# Translation dictionary
translations = {
    "en_US": {
        "Delete Vertices": "Delete Vertices",
        "Delete Edges": "Delete Edges", 
        "Delete Faces": "Delete Faces",
        "Delete Objects": "Delete Objects",
        "Dissolve Vertices": "Dissolve Vertices",
        "Dissolve Edges": "Dissolve Edges",
        "Dissolve Faces": "Dissolve Faces",
        "Limited Dissolve": "Limited Dissolve",
        "Edge Collapse": "Edge Collapse",
        "Edge Loops": "Edge Loops",
        "Only Edges & Faces": "Only Edges & Faces",
        "Only Faces": "Only Faces"
    },
    "ja_JP": {
        "Delete Vertices": "頂点を削除",
        "Delete Edges": "辺を削除",
        "Delete Faces": "面を削除", 
        "Delete Objects": "オブジェクトを削除",
        "Dissolve Vertices": "頂点を融解",
        "Dissolve Edges": "辺を融解",
        "Dissolve Faces": "面を融解",
        "Limited Dissolve": "制限融解",
        "Edge Collapse": "辺を潰す",
        "Edge Loops": "辺ループ",
        "Only Edges & Faces": "辺と面のみ",
        "Only Faces": "面のみ"
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

class NUKESHIMA_OT_silent_delete(bpy.types.Operator):
    """Silent delete without confirmation dialogs"""
    bl_idname = "nukeshima.silent_delete"
    bl_label = "Silent Delete"
    bl_options = {'REGISTER', 'UNDO'}
    
    delete_type: bpy.props.StringProperty(name="Delete Type")
    
    @classmethod
    def poll(cls, context):
        return context.area and context.area.type == 'VIEW_3D'
    
    def execute(self, context):
        # Object mode - delete selected objects
        if context.mode == 'OBJECT':
            if context.selected_objects:
                bpy.ops.object.delete(use_global=False, confirm=False)
            return {'FINISHED'}
        
        # Edit mode - delete based on selection mode and type
        if context.mode == 'EDIT_MESH':
            mesh = context.edit_object.data
            
            # Check what's selected
            import bmesh
            bm = bmesh.from_edit_mesh(mesh)
            
            selected_verts = [v for v in bm.verts if v.select]
            selected_edges = [e for e in bm.edges if e.select]
            selected_faces = [f for f in bm.faces if f.select]
            
            if not (selected_verts or selected_edges or selected_faces):
                return {'CANCELLED'}
            
            # Execute the appropriate delete operation
            if self.delete_type == 'VERT':
                bpy.ops.mesh.delete(type='VERT')
            elif self.delete_type == 'EDGE':
                bpy.ops.mesh.delete(type='EDGE')
            elif self.delete_type == 'FACE':
                bpy.ops.mesh.delete(type='FACE')
            elif self.delete_type == 'EDGE_FACE':
                bpy.ops.mesh.delete(type='EDGE_FACE')
            elif self.delete_type == 'ONLY_FACE':
                bpy.ops.mesh.delete(type='ONLY_FACE')
            elif self.delete_type == 'DISSOLVE_VERTS':
                bpy.ops.mesh.dissolve_verts()
            elif self.delete_type == 'DISSOLVE_EDGES':
                bpy.ops.mesh.dissolve_edges()
            elif self.delete_type == 'DISSOLVE_FACES':
                bpy.ops.mesh.dissolve_faces()
            elif self.delete_type == 'DISSOLVE_LIMITED':
                bpy.ops.mesh.dissolve_limited()
            elif self.delete_type == 'EDGE_COLLAPSE':
                bpy.ops.mesh.edge_collapse()
            elif self.delete_type == 'EDGE_LOOPS':
                bpy.ops.mesh.delete(type='EDGE_LOOP')
            else:
                # Smart delete based on selection
                if selected_faces:
                    bpy.ops.mesh.delete(type='FACE')
                elif selected_edges:
                    bpy.ops.mesh.delete(type='EDGE')
                elif selected_verts:
                    bpy.ops.mesh.delete(type='VERT')
            
            return {'FINISHED'}
        
        return {'CANCELLED'}

class NUKESHIMA_MT_delete_menu(bpy.types.Menu):
    """Nukeshima delete menu"""
    bl_label = "Nukeshima Delete"
    bl_idname = "NUKESHIMA_MT_delete_menu"
    
    def draw(self, context):
        layout = self.layout
        
        if context.mode == 'OBJECT':
            # Object mode - simple delete
            op = layout.operator("nukeshima.silent_delete", text=get_translation("Delete Objects"), icon='X')
            op.delete_type = 'OBJECT'
        
        elif context.mode == 'EDIT_MESH':
            # Edit mode - full delete menu
            
            # Standard delete operations
            layout.label(text="Delete:", icon='X')
            
            op = layout.operator("nukeshima.silent_delete", text=get_translation("Delete Vertices"), icon='VERTEXSEL')
            op.delete_type = 'VERT'
            
            op = layout.operator("nukeshima.silent_delete", text=get_translation("Delete Edges"), icon='EDGESEL')
            op.delete_type = 'EDGE'
            
            op = layout.operator("nukeshima.silent_delete", text=get_translation("Delete Faces"), icon='FACESEL')
            op.delete_type = 'FACE'
            
            layout.separator()
            
            op = layout.operator("nukeshima.silent_delete", text=get_translation("Only Edges & Faces"), icon='MESH_DATA')
            op.delete_type = 'EDGE_FACE'
            
            op = layout.operator("nukeshima.silent_delete", text=get_translation("Only Faces"), icon='MESH_DATA')
            op.delete_type = 'ONLY_FACE'
            
            layout.separator()
            
            # Dissolve operations
            layout.label(text="Dissolve:", icon='MOD_DECIM')
            
            op = layout.operator("nukeshima.silent_delete", text=get_translation("Dissolve Vertices"), icon='VERTEXSEL')
            op.delete_type = 'DISSOLVE_VERTS'
            
            op = layout.operator("nukeshima.silent_delete", text=get_translation("Dissolve Edges"), icon='EDGESEL')
            op.delete_type = 'DISSOLVE_EDGES'
            
            op = layout.operator("nukeshima.silent_delete", text=get_translation("Dissolve Faces"), icon='FACESEL')
            op.delete_type = 'DISSOLVE_FACES'
            
            op = layout.operator("nukeshima.silent_delete", text=get_translation("Limited Dissolve"), icon='MOD_DECIM')
            op.delete_type = 'DISSOLVE_LIMITED'
            
            layout.separator()
            
            # Additional operations
            op = layout.operator("nukeshima.silent_delete", text=get_translation("Edge Collapse"), icon='EDGESEL')
            op.delete_type = 'EDGE_COLLAPSE'
            
            op = layout.operator("nukeshima.silent_delete", text=get_translation("Edge Loops"), icon='EDGESEL')
            op.delete_type = 'EDGE_LOOPS'

class NUKESHIMA_OT_smart_delete(bpy.types.Operator):
    """Smart delete - automatically chooses best delete method"""
    bl_idname = "nukeshima.smart_delete"
    bl_label = "Smart Delete"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        return context.area and context.area.type == 'VIEW_3D'
    
    def execute(self, context):
        # Object mode - delete selected objects
        if context.mode == 'OBJECT':
            if context.selected_objects:
                bpy.ops.object.delete(use_global=False, confirm=False)
            return {'FINISHED'}
        
        # Edit mode - smart selection-based delete
        if context.mode == 'EDIT_MESH':
            mesh = context.edit_object.data
            
            import bmesh
            bm = bmesh.from_edit_mesh(mesh)
            
            selected_verts = [v for v in bm.verts if v.select]
            selected_edges = [e for e in bm.edges if e.select]
            selected_faces = [f for f in bm.faces if f.select]
            
            if not (selected_verts or selected_edges or selected_faces):
                return {'CANCELLED'}
            
            # Smart delete logic: prioritize faces > edges > vertices
            if selected_faces:
                bpy.ops.mesh.delete(type='FACE')
            elif selected_edges:
                bpy.ops.mesh.delete(type='EDGE')
            elif selected_verts:
                bpy.ops.mesh.delete(type='VERT')
            
            return {'FINISHED'}
        
        return {'CANCELLED'}

# Keymap management
addon_keymaps = []

def register():
    """Register addon"""
    bpy.utils.register_class(NUKESHIMA_OT_silent_delete)
    bpy.utils.register_class(NUKESHIMA_OT_smart_delete)
    bpy.utils.register_class(NUKESHIMA_MT_delete_menu)
    
    # Add keymap with higher priority
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        # Object mode keymap
        km_object = kc.keymaps.new(name='Object Mode', space_type='EMPTY')
        
        # X key for smart delete in object mode
        kmi_obj = km_object.keymap_items.new(
            'nukeshima.smart_delete',
            type='X',
            value='PRESS'
        )
        addon_keymaps.append((km_object, kmi_obj))
        
        # Shift+X for menu in object mode
        kmi_obj2 = km_object.keymap_items.new(
            'wm.call_menu',
            type='X',
            value='PRESS',
            shift=True
        )
        kmi_obj2.properties.name = "NUKESHIMA_MT_delete_menu"
        addon_keymaps.append((km_object, kmi_obj2))
        
        # Mesh edit mode keymap
        km_mesh = kc.keymaps.new(name='Mesh', space_type='EMPTY')
        
        # X key for smart delete in edit mode
        kmi_mesh = km_mesh.keymap_items.new(
            'nukeshima.smart_delete',
            type='X',
            value='PRESS'
        )
        addon_keymaps.append((km_mesh, kmi_mesh))
        
        # Shift+X for menu in edit mode
        kmi_mesh2 = km_mesh.keymap_items.new(
            'wm.call_menu',
            type='X',
            value='PRESS',
            shift=True
        )
        kmi_mesh2.properties.name = "NUKESHIMA_MT_delete_menu"
        addon_keymaps.append((km_mesh, kmi_mesh2))

def unregister():
    """Unregister addon"""
    bpy.utils.unregister_class(NUKESHIMA_OT_silent_delete)
    bpy.utils.unregister_class(NUKESHIMA_OT_smart_delete)
    bpy.utils.unregister_class(NUKESHIMA_MT_delete_menu)
    
    # Remove keymap
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

if __name__ == "__main__":
    register()
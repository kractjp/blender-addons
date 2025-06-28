import bpy
import bmesh
import os
from mathutils import Vector
from bpy.app.translations import pgettext_iface as _
import bpy.utils.previews

bl_info = {
    "name": "Vexer",
    "author": "KRACT",
    "version": (1, 0, 0),
    "blender": (4, 2, 0),
    "description": "Add vertices and edges progressively (1D->2D->3D)",
    "location": "Add > Mesh > Vexer",
    "category": "Add Mesh"
}

# Custom icon collection
preview_collections = {}


class VEXER_OT_add_point(bpy.types.Operator):
    """Add a single vertex (0D -> 1D)"""
    bl_idname = "mesh.vexer_add_point"
    bl_label = "Point"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        mesh = bpy.data.meshes.new("Point")
        obj = bpy.data.objects.new("Point", mesh)
        
        bm = bmesh.new()
        bm.verts.new((0, 0, 0))
        bm.to_mesh(mesh)
        bm.free()
        
        context.collection.objects.link(obj)
        bpy.context.view_layer.objects.active = obj
        obj.select_set(True)
        
        return {'FINISHED'}

class VEXER_OT_add_line(bpy.types.Operator):
    """Add two vertices connected by an edge (1D)"""
    bl_idname = "mesh.vexer_add_line"
    bl_label = "Line"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        mesh = bpy.data.meshes.new("Line")
        obj = bpy.data.objects.new("Line", mesh)
        
        bm = bmesh.new()
        v1 = bm.verts.new((-1, 0, 0))
        v2 = bm.verts.new((1, 0, 0))
        bm.edges.new([v1, v2])
        bm.to_mesh(mesh)
        bm.free()
        
        context.collection.objects.link(obj)
        bpy.context.view_layer.objects.active = obj
        obj.select_set(True)
        
        return {'FINISHED'}

class VEXER_OT_add_triangle(bpy.types.Operator):
    """Add three vertices forming a triangle (2D)"""
    bl_idname = "mesh.vexer_add_triangle"
    bl_label = "Triangle"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        mesh = bpy.data.meshes.new("Triangle")
        obj = bpy.data.objects.new("Triangle", mesh)
        
        bm = bmesh.new()
        v1 = bm.verts.new((0, 1, 0))
        v2 = bm.verts.new((-1, -1, 0))
        v3 = bm.verts.new((1, -1, 0))
        
        bm.edges.new([v1, v2])
        bm.edges.new([v2, v3])
        bm.edges.new([v3, v1])
        
        bm.to_mesh(mesh)
        bm.free()
        
        context.collection.objects.link(obj)
        bpy.context.view_layer.objects.active = obj
        obj.select_set(True)
        
        return {'FINISHED'}


def menu_func_plane(self, context):
    """Add point and line after plane"""
    # Force Japanese text if locale is Japanese
    if bpy.app.translations.locale == 'ja_JP':
        self.layout.operator("mesh.vexer_add_point", text="頂点", icon='VERTEXSEL')
        self.layout.operator("mesh.vexer_add_line", text="辺", icon='EDGESEL')
    else:
        self.layout.operator("mesh.vexer_add_point", text="Point", icon='VERTEXSEL')
        self.layout.operator("mesh.vexer_add_line", text="Line", icon='EDGESEL')

def menu_func_torus(self, context):
    """Add triangle after torus"""
    pcoll = preview_collections.get("main")
    
    # Force Japanese text if locale is Japanese
    if bpy.app.translations.locale == 'ja_JP':
        if pcoll and "triangle" in pcoll:
            self.layout.operator("mesh.vexer_add_triangle", text="三角形", icon_value=pcoll["triangle"].icon_id)
        else:
            self.layout.operator("mesh.vexer_add_triangle", text="三角形", icon='MESH_PLANE')
    else:
        if pcoll and "triangle" in pcoll:
            self.layout.operator("mesh.vexer_add_triangle", text="Triangle", icon_value=pcoll["triangle"].icon_id)
        else:
            self.layout.operator("mesh.vexer_add_triangle", text="Triangle", icon='MESH_PLANE')

# Translation dictionary
translations_dict = {
    "en_US": {},
    "ja_JP": {
        ("Operator", "Point"): "頂点",
        ("Operator", "Line"): "辺", 
        ("Operator", "Triangle"): "三角形",
    }
}

def register():
    """Register addon"""
    bpy.utils.register_class(VEXER_OT_add_point)
    bpy.utils.register_class(VEXER_OT_add_line)
    bpy.utils.register_class(VEXER_OT_add_triangle)
    
    # Load custom icons
    pcoll = bpy.utils.previews.new()
    icons_dir = os.path.join(os.path.dirname(__file__), "icons")
    
    # Load triangle icon specifically
    triangle_path = os.path.join(icons_dir, "triangle.png")
    if os.path.exists(triangle_path):
        pcoll.load("triangle", triangle_path, 'IMAGE')
    
    preview_collections["main"] = pcoll
    
    # Register translations first
    try:
        bpy.app.translations.register(__name__, translations_dict)
    except ValueError:
        pass
    
    # Add to menu with specific positioning
    bpy.types.VIEW3D_MT_mesh_add.prepend(menu_func_plane)
    bpy.types.VIEW3D_MT_mesh_add.append(menu_func_torus)

def unregister():
    """Unregister addon"""
    # Unregister translations
    try:
        bpy.app.translations.unregister(__name__)
    except ValueError:
        pass
    
    # Remove custom icons
    for pcoll in preview_collections.values():
        bpy.utils.previews.remove(pcoll)
    preview_collections.clear()
        
    bpy.types.VIEW3D_MT_mesh_add.remove(menu_func_plane)
    bpy.types.VIEW3D_MT_mesh_add.remove(menu_func_torus)
    bpy.utils.unregister_class(VEXER_OT_add_triangle)
    bpy.utils.unregister_class(VEXER_OT_add_line)
    bpy.utils.unregister_class(VEXER_OT_add_point)

if __name__ == "__main__":
    register()
import bpy
import bmesh
from mathutils import Matrix

bl_info = {
    "name": "Viewcam",
    "author": "KRACT",
    "version": (1, 0, 0),
    "blender": (4, 2, 0),
    "description": "Set current viewport view to active camera instantly",
    "location": "3D Viewport Header, shortcut: Ctrl+Shift+C",
    "category": "Camera"
}

class VIEWCAM_OT_set_view_to_camera(bpy.types.Operator):
    """Set current viewport view to active camera"""
    bl_idname = "viewcam.set_view_to_camera"
    bl_label = "View to Camera"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        # 3Dビューポートにいるかチェック
        return context.area and context.area.type == 'VIEW_3D'
    
    def execute(self, context):
        # アクティブなカメラを取得
        camera = context.scene.camera
        if not camera:
            self.report({'WARNING'}, "No active camera in scene")
            return {'CANCELLED'}
        
        # 現在の3Dビューの情報を取得
        area = context.area
        region = None
        region_3d = None
        
        for region in area.regions:
            if region.type == 'WINDOW':
                region_3d = region.data
                break
        
        if not region_3d:
            self.report({'ERROR'}, "Could not find 3D viewport region")
            return {'CANCELLED'}
        
        # 現在のビューマトリックスを取得
        view_matrix = region_3d.view_matrix.copy()
        
        # ビューマトリックスをワールド座標のカメラ変換マトリックスに変換
        # view_matrix は world_to_view 変換なので、逆行列を取ってカメラの位置・回転を取得
        camera_matrix = view_matrix.inverted()
        
        # カメラオブジェクトの変換を設定
        camera.matrix_world = camera_matrix
        
        # 変更を更新
        context.view_layer.update()
        
        self.report({'INFO'}, f"Camera '{camera.name}' set to current view")
        return {'FINISHED'}


def draw_viewcam_button(self, context):
    """3Dビューポートヘッダーにボタンを描画"""
    layout = self.layout
    
    # カメラが存在する場合のみボタンを表示
    if context.scene.camera:
        layout.operator("viewcam.set_view_to_camera", text="", icon='CAMERA_DATA', emboss=False)


# キーマップ用の変数
addon_keymaps = []

def register():
    """アドオン登録"""
    bpy.utils.register_class(VIEWCAM_OT_set_view_to_camera)
    bpy.types.VIEW3D_HT_header.append(draw_viewcam_button)
    
    # キーボードショートカットを追加
    wm = bpy.context.window_manager
    if wm.keyconfigs.addon:
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
        kmi = km.keymap_items.new(
            'viewcam.set_view_to_camera',
            type='C',
            value='PRESS',
            ctrl=True,
            shift=True
        )
        addon_keymaps.append((km, kmi))


def unregister():
    """アドオン登録解除"""
    bpy.utils.unregister_class(VIEWCAM_OT_set_view_to_camera)
    bpy.types.VIEW3D_HT_header.remove(draw_viewcam_button)
    
    # キーボードショートカットを削除
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()


if __name__ == "__main__":
    register()
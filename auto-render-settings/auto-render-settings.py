import bpy
import os
from bpy.app.handlers import persistent

bl_info = {
    "name": "Auto Render Settings",
    "author": "KRACT™",
    "version": (1, 7),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > Render Tab",
    "description": "Sets render output settings based on project file name via UI button or on save.",
    "category": "Auto Render Settings",
}

# 設定処理本体
def set_render_settings():
    filepath = bpy.data.filepath
    if not filepath:
        print("[Auto Render Settings] Filepath is empty. Save the project first.")
        return

    project_name = os.path.splitext(os.path.basename(filepath))[0]
    render = bpy.context.scene.render

    # 出力パスの設定
    render.filepath = f"//render/{project_name}/{project_name}_####"

    # 出力フォーマットの設定
    render.image_settings.file_format = 'OPEN_EXR'
    render.image_settings.color_mode = 'RGBA'
    render.image_settings.color_depth = '32'  # Float (Full)

    print(f"[Auto Render Settings] Render settings applied for project '{project_name}'.")

# UI パネル
class AUTO_RENDER_PT_panel(bpy.types.Panel):
    bl_label = "Auto Render Settings"
    bl_idname = "AUTO_RENDER_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Render'

    def draw(self, context):
        layout = self.layout
        layout.operator("auto_render.set_settings", icon='RENDER_ANIMATION')

# オペレーター
class AUTO_RENDER_OT_set_settings(bpy.types.Operator):
    bl_idname = "auto_render.set_settings"
    bl_label = "Apply Auto Render Settings"
    bl_description = "Set render settings based on project filename"

    def execute(self, context):
        set_render_settings()
        return {'FINISHED'}

# 保存時ハンドラー
@persistent
def auto_render_on_save(dummy):
    print("[Auto Render Settings] Save detected. Applying settings...")
    set_render_settings()

# 登録クラス一覧
classes = (
    AUTO_RENDER_PT_panel,
    AUTO_RENDER_OT_set_settings,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    if auto_render_on_save not in bpy.app.handlers.save_post:
        bpy.app.handlers.save_post.append(auto_render_on_save)
        print("[Auto Render Settings] Save handler registered.")

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    if auto_render_on_save in bpy.app.handlers.save_post:
        bpy.app.handlers.save_post.remove(auto_render_on_save)
        print("[Auto Render Settings] Save handler unregistered.")

if __name__ == "__main__":
    register()

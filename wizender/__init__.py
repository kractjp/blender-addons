import bpy
import os
from bpy.app.handlers import persistent
from bpy.props import StringProperty, EnumProperty

bl_info = {
    "name": "Wizender",
    "author": "KRACT",
    "version": (1, 0, 1),
    "blender": (4, 2, 0),
    "location": "Properties > Output Properties > Wizender",
    "description": "Sets render output settings based on project file name via UI button or on save.",
    "category": "Render",
    "support": "COMMUNITY",
    "doc_url": "",
    "tracker_url": "",
    "warning": "",
}

# アドオンPreferences設定クラス
class WIZENDER_AddonPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__
    # 出力パス設定
    output_path: StringProperty(
        name="Output Path",
        description="Render output path (Default: //render/{project_name}/{project_name}_####)",
        default="//render/{project_name}/{project_name}_####",
        subtype='DIR_PATH'
    )
    
    # ファイルフォーマット設定
    file_format: EnumProperty(
        name="File Format",
        description="Output file format",
        items=[
            ('OPEN_EXR', 'OpenEXR', 'OpenEXR format (Default)'),
            ('PNG', 'PNG', 'PNG format'),
            ('JPEG', 'JPEG', 'JPEG format'),
            ('TIFF', 'TIFF', 'TIFF format'),
        ],
        default='OPEN_EXR'
    )
    
    # カラーモード設定
    color_mode: EnumProperty(
        name="Color Mode",
        description="Color mode setting",
        items=[
            ('RGBA', 'RGBA', 'RGBA (with alpha channel)'),
            ('RGB', 'RGB', 'RGB (color only)'),
            ('BW', 'BW', 'Grayscale'),
        ],
        default='RGBA'
    )
    
    # カラー深度設定
    color_depth: EnumProperty(
        name="Color Depth",
        description="Color depth setting",
        items=[
            ('32', '32-bit Float', '32-bit floating point (Full)'),
            ('16', '16-bit Half Float', '16-bit half precision floating point'),
            ('8', '8-bit', '8-bit integer'),
        ],
        default='32'
    )
    
    def draw(self, context):
        layout = self.layout
        
        # 設定セクション
        box = layout.box()
        box.label(text="Render Global Settings", icon='RENDER_ANIMATION')
        
        # 出力パス設定
        box.prop(self, "output_path")
        box.label(text="* {project_name} will be replaced with project name", icon='INFO')
        
        # ファイルフォーマット設定
        box.prop(self, "file_format")
        box.prop(self, "color_mode")
        box.prop(self, "color_depth")
        
        # 使用方法の説明
        layout.separator()
        box = layout.box()
        box.label(text="Usage", icon='QUESTION')
        box.label(text="• Settings are applied automatically when saving projects")
        box.label(text="• Manual execution available from Properties > Output Properties > Wizender")

# 設定処理本体
def set_render_settings():
    """Set render settings based on project filename and addon preferences"""
    filepath = bpy.data.filepath
    if not filepath:
        print("[Wizender] Filepath is empty. Save the project first.")
        return

    project_name = os.path.splitext(os.path.basename(filepath))[0]
    render = bpy.context.scene.render
    
    # アドオンPreferencesから設定を取得
    addon_prefs = bpy.context.preferences.addons[__name__].preferences

    # 出力パスの設定（プロジェクト名をプレースホルダーに置換）
    output_path = addon_prefs.output_path.replace("{project_name}", project_name)
    render.filepath = output_path

    # 出力フォーマットの設定
    render.image_settings.file_format = addon_prefs.file_format
    render.image_settings.color_mode = addon_prefs.color_mode
    render.image_settings.color_depth = addon_prefs.color_depth

    print(f"[Wizender] Render global settings applied for project '{project_name}'.")
    print(f"  - Output path: {output_path}")
    print(f"  - Format: {addon_prefs.file_format}")
    print(f"  - Color mode: {addon_prefs.color_mode}")
    print(f"  - Color depth: {addon_prefs.color_depth}")

# アウトプットプロパティパネル
class WIZENDER_PT_output_panel(bpy.types.Panel):
    bl_label = "Wizender"
    bl_idname = "WIZENDER_PT_output_panel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "output"
    bl_parent_id = "RENDER_PT_output"

    def draw(self, context):
        layout = self.layout
        
        # 現在の設定表示
        addon_prefs = context.preferences.addons[__name__].preferences
        
        box = layout.box()
        box.label(text="Current Global Settings", icon='INFO')
        
        row = box.row()
        row.label(text="Output Path:")
        row.label(text=addon_prefs.output_path)
        
        row = box.row()
        row.label(text="Format:")
        row.label(text=addon_prefs.file_format)
        
        row = box.row()
        row.label(text="Color Mode:")
        row.label(text=addon_prefs.color_mode)
        
        row = box.row()
        row.label(text="Color Depth:")
        row.label(text=addon_prefs.color_depth)
        
        layout.separator()
        
        # 実行ボタン
        layout.operator("wizender.set_settings", icon='RENDER_ANIMATION', text="Apply Wizender Settings")
        
        layout.separator()
        
        # 設定変更案内
        box = layout.box()
        box.label(text="To change settings:", icon='SETTINGS')
        box.label(text="Edit > Preferences > Add-ons > Wizender")

# オペレーター
class WIZENDER_OT_set_settings(bpy.types.Operator):
    bl_idname = "wizender.set_settings"
    bl_label = "Apply Wizender Settings"
    bl_description = "Set render global settings based on project filename"

    def execute(self, context):
        set_render_settings()
        return {'FINISHED'}

# 保存時ハンドラー
@persistent
def auto_render_on_save(dummy):
    print("[Wizender] Save detected. Applying settings...")
    set_render_settings()

# 登録クラス一覧
classes = (
    WIZENDER_AddonPreferences,
    WIZENDER_PT_output_panel,
    WIZENDER_OT_set_settings,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    if auto_render_on_save not in bpy.app.handlers.save_post:
        bpy.app.handlers.save_post.append(auto_render_on_save)
        print("[Wizender] Save handler registered.")

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    if auto_render_on_save in bpy.app.handlers.save_post:
        bpy.app.handlers.save_post.remove(auto_render_on_save)
        print("[Wizender] Save handler unregistered.")

if __name__ == "__main__":
    register()

import bpy
from bpy_extras.io_utils import ExportHelper
import os
import re

bl_info = {
    "name": "Versave",
    "author": "KRACT",
    "version": (1, 0, 0),
    "blender": (4, 2, 0),
    "description": "Enhanced incremental save with proper versioning format (_v prefix for numbered files)",
    "location": "File > Save (Cmd+S), Save As (Cmd+Alt+S)",
    "category": "System"
}

class VERSAVE_OT_save_initial(bpy.types.Operator, ExportHelper):
    """Enhanced initial save with _v1 versioning format"""
    bl_idname = "versave.save_initial"
    bl_label = "Save (Enhanced)"
    bl_options = {'REGISTER'}
    
    # ExportHelperを使用してファイル拡張子を設定
    filename_ext = ".blend"
    filter_glob: bpy.props.StringProperty(
        default="*.blend",
        options={'HIDDEN'},
    )
    
    def execute(self, context):
        # 現在のファイルパスを取得
        current_filepath = bpy.data.filepath
        
        if current_filepath:
            # 既存ファイルの場合は通常の保存
            bpy.ops.wm.save_mainfile()
            return {'FINISHED'}
        
        # 新規ファイルの場合、選択されたファイルパスで保存
        filepath = self.filepath
        
        # ファイル名に_v1が含まれていない場合は追加
        if not filepath.endswith('.blend'):
            filepath += '.blend'
        
        base_directory = os.path.dirname(filepath)
        filename = os.path.basename(filepath)
        name, ext = os.path.splitext(filename)
        
        # _v1が含まれていない場合は追加
        if not re.search(r'_v\d+$', name):
            name = f"{name}_v1"
        
        # プロジェクト名を取得（_v1を除外）
        project_name = re.sub(r'_v\d+$', '', name)
        
        # プロジェクトディレクトリを作成
        project_dir = os.path.join(base_directory, project_name)
        
        try:
            # プロジェクトディレクトリとサブフォルダを作成
            os.makedirs(project_dir, exist_ok=True)
            os.makedirs(os.path.join(project_dir, 'render'), exist_ok=True)
            os.makedirs(os.path.join(project_dir, 'tex'), exist_ok=True)
            
            # プロジェクトディレクトリ内にblendファイルを保存
            final_filepath = os.path.join(project_dir, name + ext)
            
            bpy.ops.wm.save_as_mainfile(filepath=final_filepath)
            self.report({'INFO'}, f"Created project: {project_name}/ with {os.path.basename(final_filepath)}")
        except Exception as e:
            self.report({'ERROR'}, f"Failed to create project: {str(e)}")
            return {'CANCELLED'}
        
        return {'FINISHED'}
    
    def invoke(self, context, event):
        # 現在のファイルパスを取得
        current_filepath = bpy.data.filepath
        
        if current_filepath:
            # 既存ファイルの場合は通常の保存
            bpy.ops.wm.save_mainfile()
            return {'FINISHED'}
        
        # 新規ファイルの場合、デフォルトのファイル名を"untitled_v1.blend"に設定
        self.filepath = "untitled_v1.blend"
        
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

class VERSAVE_OT_save_incremental(bpy.types.Operator):
    """Enhanced incremental save with proper versioning format"""
    bl_idname = "versave.save_incremental"
    bl_label = "Save Incremental (Enhanced)"
    bl_options = {'REGISTER'}
    
    def execute(self, context):
        # 現在のファイルパスを取得
        current_filepath = bpy.data.filepath
        
        if not current_filepath:
            # ファイルが保存されていない場合は通常の保存ダイアログを表示
            bpy.ops.wm.save_as_mainfile('INVOKE_DEFAULT')
            return {'FINISHED'}
        
        # ファイル名とディレクトリを分離
        directory = os.path.dirname(current_filepath)
        filename = os.path.basename(current_filepath)
        name, ext = os.path.splitext(filename)
        
        # 新しいファイル名を生成
        new_name = self.generate_versioned_filename(name)
        new_filepath = os.path.join(directory, new_name + ext)
        
        # ファイルを保存
        try:
            bpy.ops.wm.save_as_mainfile(filepath=new_filepath)
            self.report({'INFO'}, f"Saved as: {os.path.basename(new_filepath)}")
        except Exception as e:
            self.report({'ERROR'}, f"Failed to save file: {str(e)}")
            return {'CANCELLED'}
        
        return {'FINISHED'}
    
    def generate_versioned_filename(self, name):
        """ファイル名にバージョン番号を追加/インクリメント"""
        
        # パターン1: _v + 数字 で終わる場合 (例: abc_v2 -> abc_v3)
        version_pattern = r'^(.+)_v(\d+)$'
        match = re.match(version_pattern, name)
        
        if match:
            base_name = match.group(1)
            version_num = int(match.group(2))
            return f"{base_name}_v{version_num + 1}"
        
        # パターン2: 数字のみで終わる場合 (例: abc1 -> abc_v2)
        number_pattern = r'^(.+?)(\d+)$'
        match = re.match(number_pattern, name)
        
        if match:
            base_name = match.group(1)
            current_num = int(match.group(2))
            # 数字のみの場合は _v を挿入してインクリメント
            return f"{base_name}_v{current_num + 1}"
        
        # パターン3: 数字が含まれていない場合 (例: abc -> abc_v2)
        # 元のファイルを_v1として扱い、_v2から付与
        return f"{name}_v2"


# キーマップ用の変数
addon_keymaps = []

def register():
    """アドオン登録"""
    bpy.utils.register_class(VERSAVE_OT_save_initial)
    bpy.utils.register_class(VERSAVE_OT_save_incremental)
    
    # キーボードショートカットを追加
    wm = bpy.context.window_manager
    if wm.keyconfigs.addon:
        km = wm.keyconfigs.addon.keymaps.new(name='Window', space_type='EMPTY')
        
        # Cmd+S をオーバーライド（初回保存時に_v1付き）
        kmi_save = km.keymap_items.new(
            'versave.save_initial',
            type='S',
            value='PRESS',
            oskey=True  # macOSのCommandキー
        )
        addon_keymaps.append((km, kmi_save))
        
        # Cmd+Alt+S をオーバーライド（インクリメンタル保存）
        kmi_incremental = km.keymap_items.new(
            'versave.save_incremental',
            type='S',
            value='PRESS',
            oskey=True,  # macOSのCommandキー
            alt=True
        )
        addon_keymaps.append((km, kmi_incremental))

def unregister():
    """アドオン登録解除"""
    bpy.utils.unregister_class(VERSAVE_OT_save_incremental)
    bpy.utils.unregister_class(VERSAVE_OT_save_initial)
    
    # キーボードショートカットを削除
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

if __name__ == "__main__":
    register()
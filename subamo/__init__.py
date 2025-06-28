import bpy
import os
import shutil
import datetime
from bpy.app.handlers import persistent
from bpy.props import IntProperty
from bpy.app.translations import pgettext_iface as _

bl_info = {
    "name": "Subamo",
    "author": "KRACT",
    "version": (1, 0, 1),
    "blender": (4, 2, 0),
    "description": "Automatically organize Blender backup files (.blend1 to .blend32) into a backup subdirectory",
    "location": "File > Save",
    "category": "System"
}




class SUBAMO_OT_delete_backup(bpy.types.Operator):
    """Delete selected backup file"""
    bl_idname = "subamo.delete_backup"
    bl_label = "Delete Backup"
    bl_options = {'REGISTER', 'UNDO'}
    
    backup_index: IntProperty()
    
    def execute(self, context):
        current_filepath = bpy.data.filepath
        if not current_filepath:
            self.report({'WARNING'}, _("No file currently open"))
            return {'CANCELLED'}
        
        current_dir = os.path.dirname(current_filepath)
        current_filename = os.path.basename(current_filepath)
        base_name = os.path.splitext(current_filename)[0]
        backup_dir = os.path.join(current_dir, "backup")
        
        backup_extensions = [f'.blend{i}' for i in range(1, 33)]  # .blend1 to .blend32
        
        if self.backup_index < len(backup_extensions):
            ext = backup_extensions[self.backup_index]
            backup_filename = base_name + ext
            backup_filepath = os.path.join(backup_dir, backup_filename)
            
            if os.path.exists(backup_filepath):
                try:
                    os.remove(backup_filepath)
                    self.report({'INFO'}, _("Deleted {}").format(backup_filename))
                except Exception as e:
                    self.report({'ERROR'}, _("Failed to delete backup: {}").format(str(e)))
                    return {'CANCELLED'}
            else:
                self.report({'WARNING'}, _("Backup file not found"))
                return {'CANCELLED'}
        
        return {'FINISHED'}

class SUBAMO_OT_open_backup(bpy.types.Operator):
    """Open selected backup file"""
    bl_idname = "subamo.open_backup"
    bl_label = "Open Backup"
    bl_options = {'REGISTER'}
    
    backup_index: IntProperty()
    
    def execute(self, context):
        current_filepath = bpy.data.filepath
        if not current_filepath:
            self.report({'WARNING'}, _("No file currently open"))
            return {'CANCELLED'}
        
        current_dir = os.path.dirname(current_filepath)
        current_filename = os.path.basename(current_filepath)
        base_name = os.path.splitext(current_filename)[0]
        backup_dir = os.path.join(current_dir, "backup")
        
        backup_extensions = [f'.blend{i}' for i in range(1, 33)]  # .blend1 to .blend32
        
        if self.backup_index < len(backup_extensions):
            ext = backup_extensions[self.backup_index]
            backup_filename = base_name + ext
            backup_filepath = os.path.join(backup_dir, backup_filename)
            
            if os.path.exists(backup_filepath):
                try:
                    bpy.ops.wm.open_mainfile(filepath=backup_filepath)
                    self.report({'INFO'}, _("Opened {}").format(backup_filename))
                except Exception as e:
                    self.report({'ERROR'}, _("Failed to open backup: {}").format(str(e)))
                    return {'CANCELLED'}
            else:
                self.report({'WARNING'}, _("Backup file not found"))
                return {'CANCELLED'}
        
        return {'FINISHED'}

def organize_backup_files(current_filepath):
    """現在のファイルパスに基づいてバックアップファイルを整理"""
    if not current_filepath:
        return 0
    
    # 現在のファイルのディレクトリとベース名を取得
    current_dir = os.path.dirname(current_filepath)
    current_filename = os.path.basename(current_filepath)
    base_name = os.path.splitext(current_filename)[0]
    
    # backupフォルダのパスを作成
    backup_dir = os.path.join(current_dir, "backup")
    
    # バックアップファイルの拡張子リスト（Blenderの最大32個に対応）
    backup_extensions = [f'.blend{i}' for i in range(1, 33)]  # .blend1 to .blend32
    
    moved_count = 0
    
    # 各バックアップファイルをチェック
    for ext in backup_extensions:
        backup_filename = base_name + ext
        backup_filepath = os.path.join(current_dir, backup_filename)
        
        # バックアップファイルが存在する場合
        if os.path.exists(backup_filepath):
            # backupフォルダが存在しない場合は作成
            if not os.path.exists(backup_dir):
                os.makedirs(backup_dir)
            
            # バックアップファイルをbackupフォルダに移動
            destination_path = os.path.join(backup_dir, backup_filename)
            
            # 同名ファイルが既に存在する場合は上書き
            if os.path.exists(destination_path):
                os.remove(destination_path)
            
            shutil.move(backup_filepath, destination_path)
            moved_count += 1
    
    return moved_count


@persistent
def save_post_handler(dummy):
    """ファイル保存後にバックアップファイルを自動整理"""
    try:
        current_filepath = bpy.data.filepath
        if current_filepath:
            organize_backup_files(current_filepath)
    except Exception as e:
        print(f"Subamo: Error organizing backup files: {str(e)}")

class SUBAMO_PT_panel(bpy.types.Panel):
    """Subamo パネル"""
    bl_label = "Subamo"
    bl_idname = "SUBAMO_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tool"
    
    def draw(self, context):
        layout = self.layout
        
        # 現在のファイル情報を表示
        current_filepath = bpy.data.filepath
        if current_filepath:
            current_dir = os.path.dirname(current_filepath)
            current_filename = os.path.basename(current_filepath)
            base_name = os.path.splitext(current_filename)[0]
            backup_dir = os.path.join(current_dir, "backup")
            
            layout.label(text=_("Backup Files:"))
            
            if os.path.exists(backup_dir):
                # 同じプロジェクトのバックアップファイル一覧を取得
                backup_extensions = [f'.blend{i}' for i in range(1, 33)]  # .blend1 to .blend32
                backup_files = []
                
                for i, ext in enumerate(backup_extensions):
                    backup_filename = base_name + ext
                    backup_filepath = os.path.join(backup_dir, backup_filename)
                    
                    if os.path.exists(backup_filepath):
                        # ファイル情報を取得
                        stat = os.stat(backup_filepath)
                        modified_time = datetime.datetime.fromtimestamp(stat.st_mtime)
                        backup_files.append({
                            'index': i,
                            'number': ext[6:],  # .blend1 -> 1
                            'filename': backup_filename,
                            'datetime': modified_time.strftime("%m/%d %H:%M"),
                            'size': round(stat.st_size / 1024 / 1024, 1)  # MB
                        })
                
                # バックアップファイルを新しい順にソート（番号が大きい = 新しい）
                backup_files.sort(key=lambda x: int(x['number']), reverse=True)
                
                if backup_files:
                    # Versave風のリスト表示
                    box = layout.box()
                    
                    col = box.column(align=False)
                    max_visible_rows = 10  # 最大表示数（32個まで対応するため少し増加）
                    
                    for i, backup in enumerate(backup_files[:max_visible_rows]):
                        # アイテム間の間隔
                        if i > 0:
                            col.separator(factor=0.3)
                        
                        row = col.row(align=True)
                        
                        # バックアップアイコン
                        row.label(text="", icon='FILE_BACKUP')
                        
                        # バックアップ番号（固定幅・番号大きい=新しい）
                        number_col = row.column()
                        number_col.ui_units_x = 2.0  # 2桁対応のため幅を拡張
                        number_col.label(text=f"#{backup['number']}")
                        
                        # 日時（固定幅）
                        date_col = row.column()
                        date_col.ui_units_x = 4.0
                        date_col.label(text=backup['datetime'])
                        
                        # ファイルサイズ（固定幅・右寄せ）
                        size_col = row.column()
                        size_col.ui_units_x = 3.5
                        size_col.alignment = 'RIGHT'
                        size_col.label(text=f"{backup['size']}MB")
                        
                        # スペーサー
                        row.separator()
                        
                        # 開くボタン
                        open_op = row.operator("subamo.open_backup", text="", icon='FILE_FOLDER')
                        open_op.backup_index = backup['index']

                        layout.separator()
                        
                        # 削除ボタン
                        delete_op = row.operator("subamo.delete_backup", text="", icon='TRASH')
                        delete_op.backup_index = backup['index']
                    
                    # 表示されていないファイルがある場合の表示
                    if len(backup_files) > max_visible_rows:
                        col.separator(factor=0.3)
                        col.label(text=f"... {_('... and {} more files').format(len(backup_files) - max_visible_rows)}")
                    
                    # 統計情報
                    layout.separator(factor=0.5)
                    stats_row = layout.row()
                    stats_row.scale_y = 0.8
                    total_size = sum(backup['size'] for backup in backup_files)
                    stats_row.label(text=_("Total: {} files, {:.1f}MB").format(len(backup_files), total_size))
                    
                else:
                    layout.label(text="No backup files found")
            else:
                layout.label(text="No backup folder")
        else:
            layout.label(text="No file open")

# 翻訳辞書
translations_dict = {
    "en_US": {},
    "ja_JP": {
        ("*", "Project Settings:"): "プロジェクト設定:",
        ("*", "Backup Count: {} (synced)"): "バックアップ数: {} (同期済)",
        ("*", "Backup Count: {} (needs sync)"): "バックアップ数: {} (同期必要)",
        ("*", "Auto Save: {} min"): "自動保存: {}分",
        ("*", "Auto Save: Disabled"): "自動保存: 無効",
        ("*", "Change Settings"): "設定変更",
        ("*", "Note: Settings are saved per project"): "注意: 設定はプロジェクトごとに保存され、Blenderのバックアップ作成設定も連動します",
        ("*", "Project settings updated"): "プロジェクト設定を更新しました",
        ("*", "Backup Files:"): "バックアップファイル:",
        ("*", "Date"): "日時",
        ("*", "Size"): "サイズ",
        ("*", "Actions"): "アクション",
        ("*", "... and {} more files"): "... 他{}個のファイル",
        ("*", "Total: {} files, {:.1f}MB"): "合計: {}ファイル, {:.1f}MB",
        ("*", "No backup files found"): "バックアップファイルがありません",
        ("*", "No backup folder"): "バックアップフォルダがありません",
        ("*", "No file open"): "ファイルが開かれていません",
        ("*", "No file currently open"): "現在ファイルが開かれていません",
        ("*", "Deleted {}"): "{}を削除しました",
        ("*", "Failed to delete backup: {}"): "バックアップの削除に失敗: {}",
        ("*", "Backup file not found"): "バックアップファイルが見つかりません",
        ("*", "Opened {}"): "{}を開きました",
        ("*", "Failed to open backup: {}"): "バックアップのオープンに失敗: {}",
    }
}

def register():
    """アドオン登録"""
    bpy.utils.register_class(SUBAMO_OT_delete_backup)
    bpy.utils.register_class(SUBAMO_OT_open_backup)
    bpy.utils.register_class(SUBAMO_PT_panel)
    
    # 翻訳を登録（既に登録済みの場合はスキップ）
    try:
        bpy.app.translations.register(__name__, translations_dict)
    except ValueError:
        # 既に登録済みの場合は無視
        pass
    
    # ファイル保存後のハンドラーを追加
    bpy.app.handlers.save_post.append(save_post_handler)

def unregister():
    """アドオン登録解除"""
    # ハンドラーを削除
    if save_post_handler in bpy.app.handlers.save_post:
        bpy.app.handlers.save_post.remove(save_post_handler)
    
    # 翻訳を解除
    try:
        bpy.app.translations.unregister(__name__)
    except ValueError:
        # 登録されていない場合は無視
        pass
    
    bpy.utils.unregister_class(SUBAMO_PT_panel)
    bpy.utils.unregister_class(SUBAMO_OT_open_backup)
    bpy.utils.unregister_class(SUBAMO_OT_delete_backup)

if __name__ == "__main__":
    register()
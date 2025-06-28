import bpy
from bpy_extras.io_utils import ExportHelper
import os
import re

def get_text(key):
    """Get localized text based on Blender's language setting"""
    texts = {
        "en_US": {
            "no_file_open": "No file currently open",
            "no_versions_found": "No version files found",
            "project": "Project",
            "available_versions": "Available Versions:",
            "opened": "Opened",
            "failed_to_open": "Failed to open file",
            "saved_as": "Saved as",
            "failed_to_save": "Failed to save file",
            "created_project": "Created project",
            "failed_to_create": "Failed to create project",
            "unsaved_changes": "Unsaved Changes",
            "save_before_open": "Do you want to save the current file before opening another version?",
            "save": "Save",
            "dont_save": "Don't Save",
            "cancel": "Cancel",
            "version": "Version",
            "filename": "Filename",
            "status": "Status",
            "current": "Current",
            "file_size": "Size",
            "modified": "Modified",
            "version_manager": "Version Manager",
            "open_version": "Open Version",
            "please_save_project": "Please save the project first"
        },
        "ja_JP": {
            "no_file_open": "現在開いているファイルがありません",
            "no_versions_found": "バージョンファイルが見つかりません",
            "project": "プロジェクト",
            "available_versions": "利用可能なバージョン:",
            "opened": "開きました",
            "failed_to_open": "ファイルを開けませんでした",
            "saved_as": "保存しました",
            "failed_to_save": "ファイルを保存できませんでした",
            "created_project": "プロジェクトを作成しました",
            "failed_to_create": "プロジェクトを作成できませんでした",
            "unsaved_changes": "未保存の変更",
            "save_before_open": "別のバージョンを開く前に現在のファイルを保存しますか？",
            "save": "保存",
            "dont_save": "保存しない",
            "cancel": "キャンセル",
            "version": "バージョン",
            "filename": "ファイル名",
            "status": "状態",
            "current": "現在",
            "file_size": "サイズ",
            "modified": "更新日時",
            "version_manager": "バージョン管理",
            "open_version": "バージョンを開く",
            "please_save_project": "プロジェクトを保存してください"
        }
    }
    
    # Get Blender's language preference
    prefs = bpy.context.preferences
    lang = prefs.view.language
    
    # Default to English if language not supported
    if lang not in texts:
        lang = "en_US"
    
    return texts[lang].get(key, key)

bl_info = {
    "name": "Versave",
    "author": "KRACT",
    "version": (1, 0, 1),
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
            self.report({'INFO'}, f"{get_text('created_project')}: {project_name}/ with {os.path.basename(final_filepath)}")
        except Exception as e:
            self.report({'ERROR'}, f"{get_text('failed_to_create')}: {str(e)}")
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

class VERSAVE_OT_open_version(bpy.types.Operator):
    """Open specific version using Blender's default file open behavior"""
    bl_idname = "versave.open_version"
    bl_label = "Open Version"
    
    @classmethod
    def description(cls, context, properties):
        return get_text("open_version")
    bl_options = {'REGISTER', 'UNDO'}
    
    filepath: bpy.props.StringProperty(
        name="File Path",
        description="Path to version file to open",
        default=""
    )
    
    def execute(self, context):
        try:
            # This is the simplest approach - Blender will handle save confirmation automatically
            # when opening a file if there are unsaved changes
            bpy.ops.wm.open_mainfile(filepath=self.filepath)
            self.report({'INFO'}, f"{get_text('opened')}: {os.path.basename(self.filepath)}")
            return {'FINISHED'}
        except Exception as e:
            self.report({'ERROR'}, f"{get_text('failed_to_open')}: {str(e)}")
            return {'CANCELLED'}


class VERSAVE_OT_version_manager(bpy.types.Operator):
    """Version manager to display and manage file versions"""
    bl_idname = "versave.version_manager"
    bl_label = "Version Manager"
    bl_options = {'REGISTER', 'UNDO'}
    
    selected_version: bpy.props.StringProperty(
        name="Selected Version",
        description="Selected version file",
        default=""
    )
    
    def execute(self, context):
        if self.selected_version:
            try:
                bpy.ops.wm.open_mainfile(filepath=self.selected_version)
                self.report({'INFO'}, f"{get_text('opened')}: {os.path.basename(self.selected_version)}")
            except Exception as e:
                self.report({'ERROR'}, f"{get_text('failed_to_open')}: {str(e)}")
                return {'CANCELLED'}
        return {'FINISHED'}
    
    def invoke(self, context, event):
        # Check if file is saved first
        current_filepath = bpy.data.filepath
        if not current_filepath:
            self.report({'INFO'}, f"{get_text('version_manager')}: {get_text('no_file_open')}")
            return {'CANCELLED'}
        
        # Check if there are unsaved changes
        if bpy.data.is_dirty:
            self.report({'INFO'}, f"{get_text('version_manager')}: {get_text('please_save_project')}")
            return {'CANCELLED'}
        
        return context.window_manager.invoke_popup(self, width=220)
    
    def draw(self, context):
        layout = self.layout
        
        current_filepath = bpy.data.filepath
        if not current_filepath:
            layout.label(text=get_text("no_file_open"), icon='ERROR')
            return
        
        
        directory = os.path.dirname(current_filepath)
        filename = os.path.basename(current_filepath)
        name, ext = os.path.splitext(filename)
        
        project_name = re.sub(r'_v\d+$', '', name)
        
        versions = self.get_version_files(directory, project_name)
        
        if not versions:
            layout.label(text=get_text("no_versions_found"), icon='INFO')
            return
        
        layout.label(text=get_text("version_manager"), icon='PRESET')
        # layout.separator(factor=0.5)
        
        box = layout.box()
        
        col = box.column(align=False)
        for version_file in versions:
            version_name = os.path.basename(version_file)
            
            # Extract version number for display
            match = re.search(r'_v(\d+)\.blend$', version_name)
            version_num = match.group(1) if match else "?"
            
            # File size calculation
            try:
                file_size = os.path.getsize(version_file)
                if file_size > 1024*1024:
                    size_text = f"{file_size/(1024*1024):.1f}MB"
                elif file_size > 1024:
                    size_text = f"{file_size/1024:.1f}KB"
                else:
                    size_text = f"{file_size}B"
            except OSError:
                size_text = "?MB"
            
            # Create row for each version with spacing
            if versions.index(version_file) > 0:
                col.separator(factor=0.3)
            row = col.row(align=True)
            
            if version_file == current_filepath:
                # Current file indicator
                row.label(text="", icon='RADIOBUT_ON')
                
                # Version number with fixed width
                version_col = row.column()
                version_col.ui_units_x = 2.5
                version_col.label(text=f"v{version_num}")
                
                # File size with fixed width
                size_col = row.column()
                size_col.ui_units_x = 3.5
                size_col.alignment = 'RIGHT'
                size_col.label(text=size_text)
                
                # Small spacer
                row.separator()
                
                # Disabled open button for current file
                op = row.operator("versave.open_version", text="", icon='FILE_BLEND')
                op.filepath = version_file
                row.enabled = False
            else:
                # Status icon placeholder
                row.label(text="", icon='RADIOBUT_OFF')
                
                # Version number with fixed width
                version_col = row.column()
                version_col.ui_units_x = 2.5
                version_col.label(text=f"v{version_num}")
                
                # File size with fixed width
                size_col = row.column()
                size_col.ui_units_x = 3.5
                size_col.alignment = 'RIGHT'
                size_col.label(text=size_text)
                
                # Small spacer
                row.separator()
                
                # Open button
                op = row.operator("versave.open_version", text="", icon='FILE_BLEND')
                op.filepath = version_file
    
    def get_version_files(self, directory, project_name):
        """Get all version files for the current project"""
        versions = []
        try:
            for file in os.listdir(directory):
                if file.endswith('.blend'):
                    base_name = os.path.splitext(file)[0]
                    if re.match(rf'^{re.escape(project_name)}_v\d+$', base_name):
                        versions.append(os.path.join(directory, file))
            
            versions.sort(key=lambda x: self.extract_version_number(x))
        except OSError:
            pass
        
        return versions
    
    def extract_version_number(self, filepath):
        """Extract version number from filepath for sorting"""
        filename = os.path.basename(filepath)
        name = os.path.splitext(filename)[0]
        match = re.search(r'_v(\d+)$', name)
        return int(match.group(1)) if match else 0

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
            self.report({'INFO'}, f"{get_text('saved_as')}: {os.path.basename(new_filepath)}")
        except Exception as e:
            self.report({'ERROR'}, f"{get_text('failed_to_save')}: {str(e)}")
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
    bpy.utils.register_class(VERSAVE_OT_open_version)
    bpy.utils.register_class(VERSAVE_OT_version_manager)
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
        
        # Cmd+Shift+E でバージョンマネージャーを開く
        kmi_version_manager = km.keymap_items.new(
            'versave.version_manager',
            type='E',
            value='PRESS',
            oskey=True,  # macOSのCommandキー
            shift=True
        )
        addon_keymaps.append((km, kmi_version_manager))

def unregister():
    """アドオン登録解除"""
    bpy.utils.unregister_class(VERSAVE_OT_save_incremental)
    bpy.utils.unregister_class(VERSAVE_OT_version_manager)
    bpy.utils.unregister_class(VERSAVE_OT_open_version)
    bpy.utils.unregister_class(VERSAVE_OT_save_initial)
    
    # キーボードショートカットを削除
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

if __name__ == "__main__":
    register()
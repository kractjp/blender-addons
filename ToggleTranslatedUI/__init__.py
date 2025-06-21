import bpy
import bpy.utils.previews
import os

bl_info = {
    "name": "Toggle Translated UI",
    "author": "Original:Satoshi Yamasaki(yamyam), Converted to 2.83: Toudou++, 4.2: KRACT",
    "version": (3, 1, 0),
    "blender": (2, 83, 0),
    "description": "Toggle International Fonts option to switch translated / non transleted UI with custom icons.",
    "location": "3D Viewport Header, shortcut: END key",
    "wiki_url": "https://www.cgradproject.com/archives/5503/",
    "tracker_url": "",
    "category": "System"}

# カスタムアイコン管理
pcoll = None

def get_icon_id(icon_name):
    global pcoll
    if pcoll and icon_name in pcoll:
        return pcoll[icon_name].icon_id
    return 0

class OBJECT_OT_translatedUI_toggle(bpy.types.Operator):
    """Toggle International Fonts"""
    bl_idname = "object.translatedui_toggle"
    bl_label = "Toggle Translated UI"

    def execute(self, context):
        b = bpy.context.preferences.view.use_translate_interface
        bpy.context.preferences.view.use_translate_interface = not b
        b = bpy.context.preferences.view.use_translate_tooltips
        bpy.context.preferences.view.use_translate_tooltips = not b
        return {'FINISHED'}


def draw_language_toggle(self, context):
    layout = self.layout
    prefs = context.preferences.view
    is_translated = prefs.use_translate_interface
    
    if is_translated:
        jp_icon_id = get_icon_id("ja_JP")
        if jp_icon_id:
            layout.operator("object.translatedui_toggle", text="", icon_value=jp_icon_id, emboss=False)
        else:
            layout.operator("object.translatedui_toggle", text="", icon='WORLD_DATA', emboss=False)
    else:
        us_icon_id = get_icon_id("en_US")
        if us_icon_id:
            layout.operator("object.translatedui_toggle", text="", icon_value=us_icon_id, emboss=False)
        else:
            layout.operator("object.translatedui_toggle", text="", icon='WORLD', emboss=False)


# Registration

def register():
    global pcoll
    
    # カスタムアイコンを読み込み
    pcoll = bpy.utils.previews.new()
    icons_dir = os.path.join(os.path.dirname(__file__), "icons")
    
    if os.path.exists(icons_dir):
        for filename in os.listdir(icons_dir):
            if filename.endswith('.png'):
                icon_name = os.path.splitext(filename)[0]
                icon_path = os.path.join(icons_dir, filename)
                pcoll.load(icon_name, icon_path, 'IMAGE')
    
    bpy.utils.register_class(OBJECT_OT_translatedUI_toggle)
    bpy.types.VIEW3D_HT_header.append(draw_language_toggle)
    kc = bpy.context.window_manager.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name="Window", space_type="EMPTY")
#        kmi = km.keymap_items.new('object.translatedui_toggle', 'SPACE', 'PRESS', shift=True)
        kmi = km.keymap_items.new('object.translatedui_toggle', 'END', 'PRESS')


def unregister():
    global pcoll
    
    bpy.utils.unregister_class(OBJECT_OT_translatedUI_toggle)
    bpy.types.VIEW3D_HT_header.remove(draw_language_toggle)
    kc = bpy.context.window_manager.keyconfigs.addon
    if kc:
        km = kc.keymaps["Window"]
        for kmi in km.keymap_items:
            if kmi.idname == 'object.translatedui_toggle':
                km.keymap_items.remove(kmi)
                break
    
    # カスタムアイコンをクリーンアップ
    if pcoll:
        bpy.utils.previews.remove(pcoll)

if __name__ == "__main__":
    register()

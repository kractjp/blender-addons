# Wizender

A magical Blender add-on that automatically configures render output settings based on the project filename.

## Features

- **Automatic Setup**: Automatically applies render settings when saving projects
- **Customizable Settings**: Configure output path, file format, color mode, and color depth
- **Persistent Preferences**: Settings are saved and maintained across Blender sessions
- **Manual Control**: Apply settings manually from the Properties panel
- **Project Name Placeholders**: Use `{project_name}` in output paths for dynamic naming

## Installation

### Traditional Add-on Installation (Blender 3.0+)
1. Download `wizender_v1.0.0.zip`
2. Go to **Edit > Preferences > Add-ons**
3. Click **Install** and select the ZIP file
4. Enable **Wizender**

### Extension Installation (Blender 4.2+)
1. Go to **Edit > Preferences > Extensions**
2. Click **Install Extension**
3. Select `wizender_v1.0.0.zip` and install

### Drag & Drop Installation (Blender 4.2+)
1. Drag and drop `wizender_v1.0.0.zip` into the Blender viewport
2. Click **Install** in the confirmation dialog

## Usage

### Configuration
1. Go to **Edit > Preferences > Add-ons**
2. Find **Wizender** and expand it
3. Configure your preferred settings:
   - **Output Path**: Render output directory (use `{project_name}` for dynamic naming)
   - **File Format**: Choose from OpenEXR, PNG, JPEG, or TIFF
   - **Color Mode**: RGBA, RGB, or Grayscale
   - **Color Depth**: 32-bit Float, 16-bit Half Float, or 8-bit

### Automatic Application
Settings are automatically applied when you save your project.

### Manual Application
1. Go to **Properties > Output Properties**
2. Expand the **Wizender** panel
3. Click **Apply Settings**

## Default Settings

- **Output Path**: `//render/{project_name}/{project_name}_####`
- **File Format**: OpenEXR
- **Color Mode**: RGBA
- **Color Depth**: 32-bit Float

## Requirements

- Blender 4.2 or later
- No external dependencies

## Technical Specifications

### Architecture
- **Core Logic**: `set_render_settings()` function handles the main functionality
- **AddonPreferences**: `WIZENDER_AddonPreferences` provides persistent settings storage
- **UI Panel**: `WIZENDER_PT_output_panel` provides user interface in Properties panel
- **Operator**: `WIZENDER_OT_set_settings` executes the render settings application
- **Handler**: `auto_render_on_save()` automatically triggers on file save with `@persistent` decorator

### Extension System Support
- Traditional add-on installation (Blender 3.0+)
- New extension system (Blender 4.2+) support
- Metadata management via `blender_manifest.toml`
- ZIP file drag-and-drop installation support

## License

This project is licensed under the GPL 3.0 or later license. See the LICENSE file for details.

## Support

For bug reports and feature requests, please visit the project repository.
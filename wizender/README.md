# Wizender

A magical Blender add-on that automatically configures render output settings based on the project filename.

## Features

- **Automatic Setup**: Automatically applies render settings when saving projects
- **Customizable Settings**: Configure output path, file format, color mode, and color depth
- **Persistent Preferences**: Settings are saved and maintained across Blender sessions
- **Manual Control**: Apply settings manually from the 3D Viewport sidebar
- **Project Name Placeholders**: Use `{project_name}` in output paths for dynamic naming

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
1. Open the 3D Viewport sidebar (press `N`)
2. Navigate to the **Wizender** tab
3. Click **Apply Settings**

## Default Settings

- **Output Path**: `//render/{project_name}/{project_name}_####`
- **File Format**: OpenEXR
- **Color Mode**: RGBA
- **Color Depth**: 32-bit Float

## Requirements

- Blender 4.2 or later
- No external dependencies

## License

This project is licensed under the GPL 3.0 or later license. See the LICENSE file for details.

## Support

For bug reports and feature requests, please visit the project repository.
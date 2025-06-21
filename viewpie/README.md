# Viewpie

A powerful Blender add-on that revolutionizes 3D viewport navigation with an intuitive pie menu system. Navigate through different views with lightning speed using radial menus that put all essential viewpoints at your fingertips.

## Features

- **Dual Pie Menu System**: Basic and Extended pie menus for different workflow needs
- **8-Direction Navigation**: Access Front, Back, Left, Right, Top, Bottom, Camera, and Projection toggle
- **Blender Default Shortcuts**: All menu items show corresponding numpad shortcuts (e.g., Camera = Numpad 0)
- **Multilingual Support**: Full Japanese and English language support
- **Extended Controls**: Additional options for View Selected, View All, Center Cursor, and projection modes
- **Smart Keyboard Shortcuts**: 
  - `Q` - Basic pie menu with essential views
  - `Shift+Q` - Extended pie menu with advanced options
- **Instant View Switching**: Single-click access to any viewport orientation
- **Projection Toggle**: Quick switch between Perspective and Orthographic modes
- **Camera Integration**: Direct access to camera view from the pie menu
- **Context-Aware**: Only works in 3D Viewport for focused functionality

## Installation

### Method 1: Remote Repository (Recommended)
1. Go to `Edit > Preferences > Extensions`
2. Click the dropdown arrow next to "Repositories"
3. Click "Add Remote Repository"
4. Enter the repository URL: `https://extensions.kract.jp/api/v1/extensions/`
5. Click "Add Repository"
6. Browse and install "Viewpie" from the repository

### Method 2: Drag and Drop (Blender 4.2+)
1. Download the add-on as a ZIP file
2. Simply drag and drop the ZIP file into Blender
3. The add-on will be automatically installed and enabled

### Method 3: Traditional Installation
1. Download the add-on files
2. Go to `Edit > Preferences > Add-ons`
3. Click `Install...` and select the ZIP file
4. Enable the "Viewpie" add-on

## Usage

### Basic Pie Menu (Q Key)

Press `Q` in the 3D Viewport to open the basic Viewpie pie menu:

- **→ Right (Numpad 3)** (3 o'clock): Right side view
- **← Left (Numpad Ctrl+3)** (9 o'clock): Left side view  
- **↓ Bottom (Numpad Ctrl+7)** (6 o'clock): Bottom view
- **↑ Top (Numpad 7)** (12 o'clock): Top view
- **↖ Back (Numpad Ctrl+1)** (10:30): Back view
- **↗ Front (Numpad 1)** (1:30): Front view
- **📷 Camera (Numpad 0)** (7:30): Camera view
- **👁 Perspective/Ortho (Numpad 5)** (4:30): Toggle projection mode

### Extended Pie Menu (Shift+Q)

Press `Shift+Q` for advanced navigation options:

- **🎯 View Selected (Numpad .)** (3 o'clock): Focus on selected objects
- **🌐 View All (Home)** (9 o'clock): Frame all objects in scene
- **⊕ Center Cursor** (6 o'clock): Center view on 3D cursor
- **📋 Basic Views** (12 o'clock): Access to basic pie menu
- **👁 Perspective** (10:30): Force perspective mode
- **📐 Orthographic** (1:30): Force orthographic mode
- **📷 Camera (Numpad 0)** (7:30): Camera view
- **Future Expansion** (4:30): Reserved for additional features

## Workflow Examples

### Modeling Workflow
1. Press `Q` → Select "Front" to work on front details
2. Press `Q` → Select "Right" to check side profile
3. Press `Q` → Select "Top" to adjust top view
4. Press `Shift+Q` → "View Selected" to focus on current selection

### Animation/Layout Workflow
1. Press `Q` → "Camera" to check final composition
2. Press `Q` → "Perspective/Ortho" to toggle projection as needed
3. Press `Shift+Q` → "View All" to see entire scene layout
4. Use directional views for precise positioning

### Architectural Visualization
1. Use Front/Back/Left/Right views for elevation work
2. Top view for floor plan adjustments
3. Camera view for final presentation angles
4. View Selected to focus on specific building elements

## Key Benefits

- **Speed**: No more hunting through View menu or remembering numpad shortcuts
- **Efficiency**: All view options accessible with single key press + mouse direction
- **Intuitive**: Radial layout matches spatial thinking
- **Customizable**: Two-tier system adapts to different complexity needs
- **Professional**: Streamlines viewport navigation for faster modeling and animation

## Technical Details

### Pie Menu Layout Philosophy
- **Cardinal Directions**: Top/Bottom/Left/Right occupy main compass points
- **Diagonal Positions**: Front/Back views in upper diagonals for easy access
- **Special Functions**: Camera and projection controls in lower positions
- **Logical Grouping**: Related functions positioned near each other

### Projection Handling
- **Smart Toggle**: Automatically switches between Perspective and Orthographic
- **Force Modes**: Extended menu allows forcing specific projection types
- **Visual Feedback**: Clear indication of current projection mode

### Context Sensitivity
- **3D Viewport Only**: Menu only appears in 3D Viewport areas
- **Error Handling**: Graceful handling of edge cases (no camera, etc.)
- **Performance**: Lightweight implementation with minimal overhead

## Keyboard Shortcuts Summary

| Shortcut | Function | Menu Type |
|----------|----------|-----------|
| `Q` | Basic Viewpie pie menu | Essential views and projection toggle with numpad shortcuts |
| `Shift+Q` | Extended Viewpie pie menu | Advanced navigation and view options |

### Blender Default Shortcuts Reference

All pie menu items correspond to Blender's default numpad shortcuts:

| View | Numpad Shortcut | Pie Menu Position |
|------|----------------|-------------------|
| Front | `Numpad 1` | Top-Right (1:30) |
| Back | `Numpad Ctrl+1` | Top-Left (10:30) |
| Right | `Numpad 3` | Right (3:00) |
| Left | `Numpad Ctrl+3` | Left (9:00) |
| Perspective/Ortho | `Numpad 5` | Bottom-Right (4:30) |
| Top | `Numpad 7` | Top (12:00) |
| Bottom | `Numpad Ctrl+7` | Bottom (6:00) |
| Camera | `Numpad 0` | Bottom-Left (7:30) |
| View Selected | `Numpad .` | Extended Menu |
| View All | `Home` | Extended Menu |

## Compatibility

- **Blender Version**: 4.2.0 or later
- **Language Support**: English and Japanese (日本語)
- **Viewport**: Works in all 3D Viewport shading modes
- **Render Engines**: Compatible with Cycles, Eevee, and Workbench
- **Platform**: Cross-platform (Windows, macOS, Linux)
- **Input Methods**: Full numpad and non-numpad keyboard support

## Tips for Maximum Efficiency

1. **Muscle Memory**: Practice the pie directions to build muscle memory
2. **Quick Gestures**: Fast Q + mouse direction for instant view changes
3. **Combine with Selection**: Use View Selected frequently for focused work
4. **Camera Workflow**: Quick Q → Camera for constant composition checking
5. **Projection Awareness**: Toggle projection based on task requirements

## Troubleshooting

- **Menu not appearing**: Ensure you're in a 3D Viewport area
- **Camera view empty**: Make sure scene has an active camera object
- **Shortcuts conflict**: Check if Q key is used by other add-ons
- **Projection issues**: Try forcing specific projection mode from extended menu

## Future Enhancements

The Viewpie system is designed for expansion:
- Additional pie menu layouts
- Custom view presets
- Animation timeline integration
- Multi-viewport synchronization
- User-defined shortcuts

## Support

For issues, feature requests, or questions, please create an issue in the project repository.

## License

This project is licensed under the GPL 3.0 or later license.
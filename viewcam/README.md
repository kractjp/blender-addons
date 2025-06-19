# Viewcam

A Blender add-on that instantly sets the current 3D viewport view to the active camera and provides camera view navigation controls. Perfect for quickly positioning cameras while working in the viewport.

## Features

- **One-click camera positioning**: Set current viewport view to active camera instantly
- **Auto camera view switching**: Automatically switches to camera view after positioning
- **Lock Camera to View toggle**: Toggle "Lock Camera to View" function when in camera view
- **Viewport header integration**: Camera icon button in 3D Viewport header
- **Cross-platform keyboard shortcuts**: 
  - macOS: Cmd+Shift+C / Cmd+Shift+Alt+C
  - Windows/Linux: Ctrl+Shift+C / Ctrl+Shift+Alt+C
- **Smart UI**: Button only appears when a camera exists in the scene
- **Blender 4.2+ drag-and-drop installation**: Modern extension system support
- **Non-destructive**: Works with any camera object in your scene

## Installation

### Method 1: Drag and Drop (Blender 4.2+)
1. Download the add-on as a ZIP file
2. Simply drag and drop the ZIP file into Blender
3. The add-on will be automatically installed and enabled

### Method 2: Traditional Installation
1. Download the add-on files
2. Go to `Edit > Preferences > Add-ons`
3. Click `Install...` and select the ZIP file
4. Enable the "Viewcam" add-on

## Usage

### Set View to Camera

#### Method 1: Header Button
1. Navigate to your desired view in the 3D Viewport
2. Look for the camera icon in the 3D Viewport header
3. Click the camera icon to set the active camera to match your current view
4. The viewport will automatically switch to camera view

#### Method 2: Keyboard Shortcut
1. Navigate to your desired view in the 3D Viewport
2. Press **Cmd+Shift+C** (macOS) or **Ctrl+Shift+C** (Windows/Linux)
3. The active camera will be set to match your current view
4. The viewport will automatically switch to camera view

### Toggle Lock Camera to View

When you're in camera view, you can toggle the "Lock Camera to View" function:

1. Make sure you're in camera view (press Numpad 0 or use View > Camera)
2. Press **Cmd+Shift+Alt+C** (macOS) or **Ctrl+Shift+Alt+C** (Windows/Linux)
3. This will toggle "Lock Camera to View" on/off, allowing you to navigate within the camera view

## How It Works

### Set View to Camera Function
Viewcam captures the current 3D viewport's:
- **Position**: Where you're looking from
- **Rotation**: The direction you're looking
- **Perspective**: The viewing angle

It then applies this exact transformation to your scene's active camera and automatically switches to camera view, making it easy to position cameras precisely where you want them.

### Lock Camera to View Function
This feature enables "Lock Camera to View" mode, which allows you to navigate within the camera view. When enabled:
- Moving the viewport will move the camera
- The camera follows your navigation movements
- Perfect for fine-tuning camera positions while seeing the actual camera framing

## Use Cases

- **Architectural visualization**: Quickly set up camera angles while navigating through a building, then fine-tune with Lock Camera to View
- **Product rendering**: Position cameras for different product shots and adjust framing precisely
- **Animation**: Set keyframe camera positions during animation blocking with immediate camera view feedback
- **Scene composition**: Explore different camera angles before committing to a shot, with real-time camera adjustment
- **Cinematography**: Use Lock Camera to View for smooth camera movements and framing adjustments

## Technical Requirements

- **Blender Version**: 4.2.0 or later
- **Active Camera**: Scene must have an active camera object
- **3D Viewport**: Must be used within a 3D Viewport area

## Keyboard Shortcuts Summary

| Shortcut | macOS | Windows/Linux | Function |
|----------|--------|---------------|----------|
| Set View to Camera | **Cmd+Shift+C** | **Ctrl+Shift+C** | Sets current view to camera and switches to camera view |
| Toggle Lock Camera to View | **Cmd+Shift+Alt+C** | **Ctrl+Shift+Alt+C** | Toggles "Lock Camera to View" (only works in camera view) |

## Troubleshooting

- **"No active camera in scene"**: Make sure your scene has a camera object and it's set as the active camera
- **Button not visible**: The camera button only appears when there's an active camera in the scene
- **Unexpected camera position**: Ensure you're using this tool from a 3D Viewport, not other editor types
- **"Must be in camera view to toggle Lock Camera to View"**: The Lock Camera to View toggle only works when you're already in camera view (Numpad 0)
- **Lock Camera to View not working**: Make sure you're in camera view first, then press the toggle shortcut

## Support

For issues, feature requests, or questions, please create an issue in the project repository.

## License

This project is licensed under the GPL 3.0 or later license.

---

**Created by KRACT** - A simple but powerful tool for camera positioning in Blender.
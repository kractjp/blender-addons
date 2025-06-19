# Viewcam

A Blender add-on that instantly sets the current 3D viewport view to the active camera. Perfect for quickly positioning cameras while working in the viewport.

## Features

- **One-click camera positioning**: Set current viewport view to active camera instantly
- **Viewport header integration**: Camera icon button in 3D Viewport header
- **Keyboard shortcut**: Ctrl+Shift+C for quick access
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

### Method 1: Header Button
1. Navigate to your desired view in the 3D Viewport
2. Look for the camera icon in the 3D Viewport header
3. Click the camera icon to set the active camera to match your current view

### Method 2: Keyboard Shortcut
1. Navigate to your desired view in the 3D Viewport
2. Press **Ctrl+Shift+C** to set the active camera to match your current view

## How It Works

Viewcam captures the current 3D viewport's:
- **Position**: Where you're looking from
- **Rotation**: The direction you're looking
- **Perspective**: The viewing angle

It then applies this exact transformation to your scene's active camera, making it easy to position cameras precisely where you want them.

## Use Cases

- **Architectural visualization**: Quickly set up camera angles while navigating through a building
- **Product rendering**: Position cameras for different product shots
- **Animation**: Set keyframe camera positions during animation blocking
- **Scene composition**: Explore different camera angles before committing to a shot

## Technical Requirements

- **Blender Version**: 4.2.0 or later
- **Active Camera**: Scene must have an active camera object
- **3D Viewport**: Must be used within a 3D Viewport area

## Troubleshooting

- **"No active camera in scene"**: Make sure your scene has a camera object and it's set as the active camera
- **Button not visible**: The camera button only appears when there's an active camera in the scene
- **Unexpected camera position**: Ensure you're using this tool from a 3D Viewport, not other editor types

## Support

For issues, feature requests, or questions, please create an issue in the project repository.

## License

This project is licensed under the GPL 3.0 or later license.

---

**Created by KRACT** - A simple but powerful tool for camera positioning in Blender.
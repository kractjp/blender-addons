# Toggle Translated UI

A Blender add-on that allows you to quickly toggle between translated and non-translated user interface with custom language-specific icons.

## Features

- **One-click UI language toggle**: Switch between translated and original English UI instantly
- **Custom language icons**: Visual indicators showing current language state (JP/US icons)
- **Multiple activation methods**: 
  - Click the language icon in 3D Viewport header
  - Use keyboard shortcut (END key)
- **Blender 4.2+ drag-and-drop installation**: Modern extension system support
- **Backward compatibility**: Works with traditional add-on installation

## Installation

### Method 1: Drag and Drop (Blender 4.2+)
1. Download the add-on as a ZIP file
2. Simply drag and drop the ZIP file into Blender
3. The add-on will be automatically installed and enabled

### Method 2: Traditional Installation
1. Download the add-on files
2. Go to `Edit > Preferences > Add-ons`
3. Click `Install...` and select the ZIP file
4. Enable the "Toggle Translated UI" add-on

## Usage

### Using the Header Button
- Look for the language icon in the 3D Viewport header (top bar)
- **JP icon**: Currently showing translated (Japanese) interface
- **US icon**: Currently showing English interface
- Click the icon to toggle between languages

### Using Keyboard Shortcut
- Press the **END** key to toggle the interface language

## What It Does

This add-on toggles two Blender preferences:
- `use_translate_interface`: Controls UI element translation
- `use_translate_tooltips`: Controls tooltip translation

Both settings are synchronized when toggling.

## Technical Requirements

- **Blender Version**: 4.2.0 or later
- **License**: GPL 2.0 or later

## Credits and Original Work

This add-on is based on the original work by **Satoshi Yamasaki (yamyam)** and was later converted for Blender 2.83 by **Toudou++**. The current version has been updated for Blender 4.2+ with modern extension support and custom icons by **KRACT**.

**Original Documentation**: [https://www.cgradproject.com/archives/5503/](https://www.cgradproject.com/archives/5503/)

### Version History
- **v3.1.0**: Blender 4.2+ support, custom JP/US icons, drag-and-drop installation (supported extension)
- **v3.0**: Blender 2.83 compatibility (by Toudou++)
- **Original**: Created by Satoshi Yamasaki (yamyam)

## Support

For issues and questions, please refer to the original documentation or create an issue in the project repository.
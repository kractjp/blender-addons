# Subamo

A simple and efficient Blender add-on that automatically organizes backup files (.blend1, .blend2, etc.) into a dedicated `backup` subdirectory, keeping your project folders clean and organized.

## Problem Solved

Blender's default backup behavior clutters project directories with backup files:
- `project.blend`, `project.blend1`, `project.blend2` all in the same folder
- Backup files mixed with main project files
- Difficult to locate the current working file among backups

**Subamo** fixes this by automatically moving backup files to a dedicated `backup` folder while preserving all backup functionality.

## Features

- **Automatic organization**: Backup files moved to `backup` folder on save
- **File management**: Open and delete backup files directly from the panel
- **File information display**: Shows backup number, creation date, and file size
- **Clean workspace**: Keeps project directories uncluttered
- **Zero maintenance**: Works silently in the background
- **Safe operation**: Preserves all backup files and functionality

## Installation

### Method 1: Remote Repository (Recommended)
1. Go to `Edit > Preferences > Extensions`
2. Click the dropdown arrow next to "Repositories"
3. Click "Add Remote Repository"
4. Enter the repository URL: `https://extensions.kract.jp/api/v1/extensions/`
5. Click "Add Repository"
6. Browse and install "Subamo" from the repository

### Method 2: Drag and Drop (Blender 4.2+)
1. Download the add-on as a ZIP file
2. Simply drag and drop the ZIP file into Blender
3. The add-on will be automatically installed and enabled

### Method 3: Traditional Installation
1. Download the add-on files
2. Go to `Edit > Preferences > Add-ons`
3. Click `Install...` and select the ZIP file
4. Enable the "Subamo" add-on

## Usage

Once installed, Subamo works automatically with minimal user interaction:

### Automatic Organization
- Save your file normally (Cmd+S or Ctrl+S)
- Backup files are automatically moved to the `backup` folder
- No user intervention required

### Backup Management Panel
1. Open the 3D Viewport
2. Press `N` to show the right panel
3. Find the "Subamo" tab
4. View and manage backup files:
   - **#**: Backup number (1, 2, 3, etc.)
   - **Date**: Creation date and time (MM/DD HH:MM)
   - **Size**: File size in MB
   - **Actions**: Open (📁) and Delete (🗑️) buttons

## Backup Settings

Subamo uses Blender's built-in backup settings:
- Go to `Edit > Preferences > Save & Load`
- Set "Save Versions" to your desired number of backup files (1-32)
- Subamo will automatically organize the number of backups you specify

## Folder Structure

**Before Subamo:**

```folder
project_folder/
├── myproject.blend
├── myproject.blend1
├── myproject.blend2
└── myproject.blend3
```

**After Subamo:**

```folder
project_folder/
├── myproject.blend
└── backup/
    ├── myproject.blend1
    ├── myproject.blend2
    └── myproject.blend3
```

## Panel Features

The Subamo panel displays:
- **Backup file list**: Up to 5 most recent backups with scroll indication
- **File details**: Number, date, size, and management actions
- **Total statistics**: File count and total size
- **Action buttons**: Icon-only design for clean interface

## Workflow Examples

### Daily Modeling Workflow
1. Open your project file
2. Work and save regularly (Cmd+S)
3. Backup files automatically organized in `backup/` folder
4. Check panel to see backup history and manage old files
5. Clean project folder with only main .blend file visible

### Project Handoff
1. Share project folder
2. Recipient sees clean structure with main file prominent
3. Backup files safely stored in `backup/` subdirectory
4. All backup functionality preserved

### Backup Recovery
1. Open Subamo panel
2. Browse available backup files with dates
3. Click folder icon to open any previous version
4. No need to navigate file system manually

## Key Benefits

- **Clean workspace**: Project folders stay organized
- **Easy identification**: Main project file is immediately visible
- **Preserved functionality**: All Blender backup features work normally
- **Visual management**: Easy-to-use panel for backup oversight
- **Zero overhead**: No performance impact on saving
- **Professional organization**: Industry-standard folder structure

## Technical Details

### Automatic Processing
- Monitors file save events using Blender's handler system
- Identifies backup files by extension pattern (.blend1, .blend2, etc.)
- Creates `backup/` folder when needed
- Moves files while preserving timestamps and metadata

### Safety Features
- **Non-destructive**: Never deletes backup files automatically
- **Conflict handling**: Overwrites older backups with same name safely
- **Error recovery**: Continues operation if individual moves fail
- **Preserve timestamps**: Maintains original file creation dates

### User Interface
- **Multilingual**: Full English and Japanese support
- **Icon-based actions**: Clean, intuitive interface
- **Responsive design**: Adapts to different panel sizes
- **Visual feedback**: Clear status indicators and file information

## Compatibility

- **Blender Version**: 4.2.0 or later
- **File Types**: Works with all .blend backup files created by Blender
- **Operating Systems**: Cross-platform (Windows, macOS, Linux)
- **Workflow**: Compatible with all Blender save methods and preferences
- **Performance**: Minimal impact on save operations

## Troubleshooting

- **Panel shows "No file open"**: Open a .blend file to see backup information
- **No backup folder**: Backup folder is created automatically when first backup is saved
- **Missing backups**: Check Blender's backup settings in Preferences > Save & Load > Save Versions
- **Permission errors**: Ensure write access to project directory

## Why "Subamo"?

The name combines "**Sub**directory" + "backup" + "**Mo**ve", perfectly describing the add-on's core function: moving backup files to a subdirectory for better organization.

## Use Cases

- **Professional projects**: Maintain clean project structures for client delivery
- **Team collaboration**: Share organized project folders without backup clutter
- **Asset libraries**: Keep backup files out of asset browser views
- **Version control**: Separate backup files from tracked content
- **Educational environments**: Teach clean file organization practices

## Support

For issues, feature requests, or questions, please create an issue in the project repository.

## License

This project is licensed under the GPL 3.0 or later license.
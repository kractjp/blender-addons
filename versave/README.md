# Versave

A Blender add-on that enhances both initial and incremental save functionality by automatically adding proper version formatting with "_v" prefix for consistent file versioning. Now includes an integrated **Version Manager** for easy version switching and project management.

## Problem Solved

Blender's default **Cmd+Alt+S** (incremental save) simply adds numbers to filenames:
- `project.blend` → `project1.blend` → `project2.blend`
- `scene_v2.blend` → `scene_v3.blend` (works correctly)

This creates inconsistent naming when mixing numbered and versioned files. **Versave** fixes this by ensuring consistent "_v" prefixed versioning.

## Features

### Enhanced Save Operations
- **Enhanced initial save**: Cmd+S automatically suggests "_v1" suffix for new files
- **Project structure creation**: Automatically creates project directory with render/ and tex/ folders
- **Consistent versioning**: Automatically adds "_v" prefix for numbered files
- **Smart detection**: Recognizes existing version patterns and handles them appropriately
- **Seamless integration**: Replaces default Cmd+S and Cmd+Alt+S behavior

### Integrated Version Manager
- **Quick version switching**: Cmd+Shift+E opens a compact version manager
- **Visual version overview**: See all project versions with file sizes at a glance
- **One-click switching**: Direct access to any version of your project
- **Save-first protection**: Only works with saved files to prevent data loss
- **Multilingual support**: Available in English and Japanese

### Versioning Patterns
1. `project.blend` → `project_v2.blend` (new file, treats original as _v1)
2. `project1.blend` → `project_v2.blend` (number-only to versioned)
3. `project_v2.blend` → `project_v3.blend` (already versioned)

## Installation

### Method 1: Remote Repository (Recommended)
1. Go to `Edit > Preferences > Extensions`
2. Click the dropdown arrow next to "Repositories"
3. Click "Add Remote Repository"
4. Enter the repository URL: `https://extensions.kract.jp/api/v1/extensions/`
5. Click "Add Repository"
6. Browse and install "Versave" from the repository

### Method 2: Drag and Drop (Blender 4.2+)
1. Download the add-on as a ZIP file
2. Simply drag and drop the ZIP file into Blender
3. The add-on will be automatically installed and enabled

### Method 3: Traditional Installation
1. Download the add-on files
2. Go to `Edit > Preferences > Add-ons`
3. Click `Install...` and select the ZIP file
4. Enable the "Versave" add-on

## Usage

Once installed, Versave automatically enhances both save operations and provides version management:

### Initial Save (Cmd+S)
1. **For new files**: Save dialog will suggest "untitled_v1.blend" by default
2. **Type your project name**: e.g., "myproject" → creates the following structure:

   ```folder
   myproject/
   ├── myproject_v1.blend
   ├── render/
   └── tex/
   ```

3. **For existing files**: Works normally (saves current file)

### Incremental Save (Cmd+Alt+S)
1. **Use incremental save** (`Cmd+Alt+S`)
2. **Versave handles the versioning automatically**

### Version Manager (Cmd+Shift+E)
1. **Open Version Manager**: Press `Cmd+Shift+E` (macOS) or `Ctrl+Shift+E` (Windows/Linux)
2. **View all versions**: See a compact list of all project versions with file sizes
3. **Switch versions**: Click the folder icon next to any version to open it
4. **Current version indicator**: The currently open version is marked with ●
5. **Save requirement**: The version manager only works with saved files - you'll get a notification if you need to save first

### Project Structure Examples

**Initial Save:**
- Input: `myproject` → Creates `myproject/` directory with `myproject_v1.blend`, `render/`, and `tex/` folders

**Incremental Save Examples:**

| Original Filename | After Cmd+Alt+S | Notes |
|-------------------|------------------|-------|
| `project_v1.blend` | `project_v2.blend` | Within project directory |
| `scene1.blend` | `scene_v2.blend` | Converts number to version |
| `model_v3.blend` | `model_v4.blend` | Increments existing version |
| `animation5.blend` | `animation_v6.blend` | Converts number to version |

## Benefits

### Save Operations
- **Consistent file naming**: All versioned files use the same "_v" format
- **Organized project structure**: Each project gets its own directory with render/ and tex/ folders
- **Professional workflow**: Matches industry standard versioning conventions
- **No learning curve**: Uses the same Cmd+Alt+S shortcut you already know

### Version Management
- **Instant version switching**: No need to browse through file dialogs
- **Visual project overview**: See all versions and their sizes at once
- **Data safety**: Save-first protection prevents accidental data loss
- **Compact interface**: Minimalist design that doesn't clutter your workspace
- **Better organization**: Easier to identify and manage version files

## Technical Details

The add-on uses regex patterns to detect and handle different filename formats:
- **Version pattern**: `name_v[number]` - increments the version number
- **Number pattern**: `name[number]` - converts to `name_v[number+1]` format
- **No version**: `name` - treats original as `_v1`, creates `_v2`

## Compatibility

- **Blender Version**: 4.2.0 or later
- **File Types**: Works with all Blender file types (.blend)
- **Operating Systems**: Cross-platform (Windows, macOS, Linux)

## Keyboard Shortcuts

| Shortcut | Function | Description |
|----------|----------|-------------|
| `Cmd+S` (macOS)<br>`Ctrl+S` (Win/Linux) | Enhanced Save | Initial save with _v1 suffix for new files |
| `Cmd+Alt+S` (macOS)<br>`Ctrl+Alt+S` (Win/Linux) | Incremental Save | Smart versioning with _v prefix |
| `Cmd+Shift+E` (macOS)<br>`Ctrl+Shift+E` (Win/Linux) | Version Manager | Open version management popup |

## Frequently Asked Questions

**Q: What happens to my existing numbered files?**  
A: Existing files are not modified. Only new incremental saves will use the enhanced versioning.

**Q: Can I disable this temporarily?**  
A: Yes, simply disable the add-on in Preferences > Add-ons to revert to default behavior.

**Q: Does this work with unsaved files?**  
A: For save operations, if the file hasn't been saved yet, it will open the standard "Save As" dialog. For the Version Manager, you'll get a notification to save the file first.

**Q: Why doesn't the Version Manager appear when I have unsaved changes?**  
A: This is a safety feature to prevent data loss. Save your current work first, then use the Version Manager to switch between versions.

**Q: Can I change the keyboard shortcut for the Version Manager?**  
A: Yes, you can customize it in Blender's Preferences > Keymap, look for "Version Manager" under the Versave section.

## Support

For issues, feature requests, or questions, please create an issue in the project repository.

## License

This project is licensed under the GPL 3.0 or later license.
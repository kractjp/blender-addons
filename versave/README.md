# Versave

A Blender add-on that enhances both initial and incremental save functionality by automatically adding proper version formatting with "_v" prefix for consistent file versioning.

## Problem Solved

Blender's default **Cmd+Alt+S** (incremental save) simply adds numbers to filenames:
- `project.blend` → `project1.blend` → `project2.blend`
- `scene_v2.blend` → `scene_v3.blend` (works correctly)

This creates inconsistent naming when mixing numbered and versioned files. **Versave** fixes this by ensuring consistent "_v" prefixed versioning.

## Features

- **Enhanced initial save**: Cmd+S automatically suggests "_v1" suffix for new files
- **Project structure creation**: Automatically creates project directory with render/ and tex/ folders
- **Consistent versioning**: Automatically adds "_v" prefix for numbered files
- **Smart detection**: Recognizes existing version patterns and handles them appropriately
- **Seamless integration**: Replaces default Cmd+S and Cmd+Alt+S behavior
- **Three versioning patterns**:
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

Once installed, Versave automatically enhances both save operations:

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

- **Consistent file naming**: All versioned files use the same "_v" format
- **Organized project structure**: Each project gets its own directory with render/ and tex/ folders
- **Better organization**: Easier to identify and sort version files
- **Professional workflow**: Matches industry standard versioning conventions
- **No learning curve**: Uses the same Cmd+Alt+S shortcut you already know

## Technical Details

The add-on uses regex patterns to detect and handle different filename formats:
- **Version pattern**: `name_v[number]` - increments the version number
- **Number pattern**: `name[number]` - converts to `name_v[number+1]` format
- **No version**: `name` - treats original as `_v1`, creates `_v2`

## Compatibility

- **Blender Version**: 4.2.0 or later
- **File Types**: Works with all Blender file types (.blend)
- **Operating Systems**: Cross-platform (Windows, macOS, Linux)

## Frequently Asked Questions

**Q: What happens to my existing numbered files?**  
A: Existing files are not modified. Only new incremental saves will use the enhanced versioning.

**Q: Can I disable this temporarily?**  
A: Yes, simply disable the add-on in Preferences > Add-ons to revert to default behavior.

**Q: Does this work with unsaved files?**  
A: If the file hasn't been saved yet, it will open the standard "Save As" dialog, just like Blender's default behavior.

## Support

For issues, feature requests, or questions, please create an issue in the project repository.

## License

This project is licensed under the GPL 3.0 or later license.
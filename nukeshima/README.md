# Nukeshima

A Blender add-on that eliminates annoying confirmation dialogs when deleting objects, vertices, edges, and faces. Just nuke it instantly without the "Are you sure?" interruptions.

## Problem Solved

Blender's default delete behavior (X key) shows confirmation dialogs and menus that interrupt your workflow:
- "Delete selected objects?" confirmation popup
- "Delete vertices/edges/faces?" menu selection
- Multiple clicks required for simple deletions

**Nukeshima** fixes this by providing instant, silent deletion while still maintaining the flexibility of different delete types when needed.

## Features

- **Silent deletion**: No confirmation dialogs - just delete instantly
- **Smart delete**: Automatically chooses the best delete method based on selection
- **Full delete menu**: Access to all delete types (vertices, edges, faces, dissolve, etc.)
- **Multilingual support**: Full English and Japanese interfaces
- **Keyboard shortcuts**:
  - `X` - Smart delete (completely bypasses menu)
  - `Shift+X` - Opens enhanced delete menu (no confirmations)
- **Context-aware**: Works in both Object and Edit modes
- **Safe operation**: Maintains undo functionality for accident recovery

## Installation

### Method 1: Remote Repository (Recommended)
1. Go to `Edit > Preferences > Extensions`
2. Click the dropdown arrow next to "Repositories"
3. Click "Add Remote Repository"
4. Enter the repository URL: `https://extensions.kract.jp/api/v1/extensions/`
5. Click "Add Repository"
6. Browse and install "Nukeshima" from the repository

### Method 2: Drag and Drop (Blender 4.2+)
1. Download the add-on as a ZIP file
2. Simply drag and drop the ZIP file into Blender
3. The add-on will be automatically installed and enabled

### Method 3: Traditional Installation
1. Download the add-on files
2. Go to `Edit > Preferences > Add-ons`
3. Click `Install...` and select the ZIP file
4. Enable the "Nukeshima" add-on

## Usage

### Smart Delete (X) - Recommended
Press `X` for instant, intelligent deletion:

**Object Mode:**
- Deletes selected objects immediately (no confirmation)

**Edit Mode:**
- Automatically chooses the best delete method:
  - Selected faces → Delete faces
  - Selected edges → Delete edges  
  - Selected vertices → Delete vertices

### Delete Menu (Shift+X) - Full Control
Press `Shift+X` to open the enhanced delete menu with all options:

**Object Mode:**
- Delete Objects (instant, no confirmation)

**Edit Mode:**
- **Delete Operations:**
  - Delete Vertices
  - Delete Edges
  - Delete Faces
  - Only Edges & Faces
  - Only Faces

- **Dissolve Operations:**
  - Dissolve Vertices
  - Dissolve Edges
  - Dissolve Faces
  - Limited Dissolve

- **Special Operations:**
  - Edge Collapse
  - Edge Loops

All operations execute immediately without confirmation dialogs.

## Workflow Examples

### Object Modeling Workflow
1. Select unwanted objects
2. Press `X` → Objects deleted instantly
3. Continue modeling without interruption

### Mesh Editing Workflow
1. Select faces/edges/vertices to remove
2. Press `X` → Smart deletion based on selection
3. For specific delete types, press `Shift+X` → Choose operation → Instant deletion

### Clean Modeling Workflow
1. Select topology to clean up
2. Press `Shift+X` → "Dissolve Vertices" or "Limited Dissolve"
3. Instant cleanup without confirmation delays

## Key Benefits

- **Speed**: No confirmation dialogs = faster workflow
- **Efficiency**: Smart delete chooses the right operation automatically
- **Flexibility**: Full menu access when you need specific delete types
- **Safety**: Undo (Ctrl+Z) still works for accident recovery
- **Professional**: Eliminates workflow interruptions during intensive modeling

## Keyboard Shortcuts Summary

| Shortcut | Function | Context |
|----------|----------|---------|
| `X` | Smart delete (bypasses menu completely) | Object & Edit modes |
| `Shift+X` | Enhanced delete menu (no confirmations) | Object & Edit modes |

## Smart Delete Logic

**Object Mode:**
- Deletes all selected objects

**Edit Mode Priority:**
1. **Faces selected** → Delete faces
2. **Edges selected** → Delete edges
3. **Vertices selected** → Delete vertices

This prioritization ensures the most logical deletion based on your current selection.

## Delete Operations Reference

### Standard Delete
- **Delete Vertices**: Removes vertices and connected geometry
- **Delete Edges**: Removes edges and connected faces
- **Delete Faces**: Removes faces only, leaving edges/vertices
- **Only Edges & Faces**: Removes edges and faces, keeps vertices
- **Only Faces**: Removes faces only

### Dissolve Operations
- **Dissolve Vertices**: Removes vertices while maintaining topology
- **Dissolve Edges**: Removes edges while maintaining faces
- **Dissolve Faces**: Removes faces while maintaining edge flow
- **Limited Dissolve**: Intelligent dissolve based on angle threshold

### Special Operations
- **Edge Collapse**: Collapses edges to points
- **Edge Loops**: Deletes entire edge loops

## Technical Details

### Safety Features
- **Undo Support**: All operations support Ctrl+Z undo
- **Context Checking**: Only operates in appropriate modes
- **Selection Validation**: Checks for valid selections before operating

### Performance
- **Lightweight**: Minimal overhead compared to default operations
- **Instant Execution**: No dialog delays or menu animations
- **Smart Detection**: Efficient selection analysis for smart delete

## Compatibility

- **Blender Version**: 4.2.0 or later
- **Language Support**: English and Japanese (日本語)
- **Viewport**: Works in all 3D viewport modes
- **Mesh Types**: Compatible with all mesh objects
- **Undo System**: Full integration with Blender's undo system

## Troubleshooting

- **Nothing happens**: Ensure you have objects/elements selected
- **Wrong delete type**: Use `Shift+X` menu for specific delete operations instead of `X`
- **Accidental deletion**: Use `Ctrl+Z` to undo any deletion
- **Shortcut conflicts**: Check if X key is used by other add-ons

## Why "Nukeshima"?

The name combines "nuke" (to destroy/delete completely) with "shima" (島, Japanese for island), creating a unique and memorable name that reflects the add-on's purpose: to completely eliminate (nuke) the annoying confirmation islands that interrupt your workflow.

## Use Cases

- **Game Asset Modeling**: Fast cleanup and optimization
- **Architectural Modeling**: Quick removal of construction geometry
- **Character Modeling**: Rapid topology adjustments
- **Hard Surface Modeling**: Efficient boolean cleanup
- **Animation Cleanup**: Fast removal of temporary geometry

## Support

For issues, feature requests, or questions, please create an issue in the project repository.

## License

This project is licensed under the GPL 3.0 or later license.
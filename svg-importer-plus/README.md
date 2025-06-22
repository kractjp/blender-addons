# SVG Importer Plus

An enhanced Blender add-on that streamlines SVG import workflow by automatically converting curves to mesh and centering origins, eliminating manual post-processing steps.

## Problem Solved

Blender's default SVG import requires manual post-processing:
- SVG files import as curve objects, not mesh
- Origins are not centered on the geometry
- Requires manual "Convert to Mesh" operation
- Requires manual "Origin to Geometry" operation

**SVG Importer Plus** fixes this by automating both operations in a single import step, saving time and reducing workflow friction.

## Features

- **Enhanced SVG Import**: Custom import operator with post-processing options
- **Automatic mesh conversion**: Converts imported curves to mesh objects automatically
- **Automatic origin centering**: Sets origin to geometry center automatically  
- **Optional processing**: Toggle conversion and centering options as needed
- **Progress feedback**: Clear reporting of import and processing results
- **Multilingual support**: Full English and Japanese interface

## Installation

### Method 1: Remote Repository (Recommended)
1. Go to `Edit > Preferences > Extensions`
2. Click the dropdown arrow next to "Repositories"
3. Click "Add Remote Repository"
4. Enter the repository URL: `https://extensions.kract.jp/api/v1/extensions/`
5. Click "Add Repository"
6. Browse and install "SVG Importer Plus" from the repository

### Method 2: Drag and Drop (Blender 4.2+)
1. Download the add-on as a ZIP file
2. Simply drag and drop the ZIP file into Blender
3. The add-on will be automatically installed and enabled

### Method 3: Traditional Installation
1. Download the add-on files
2. Go to `Edit > Preferences > Add-ons`
3. Click `Install...` and select the ZIP file
4. Enable the "SVG Importer Plus" add-on

## Usage

### Basic Import
1. Go to `File > Import > Scalable Vector Graphics Plus (.svg)`
2. Navigate to your SVG file
3. Configure post-processing options:
   - **Convert to Mesh**: ✓ (recommended)
   - **Center Origin**: ✓ (recommended)  
4. Click "Import SVG Plus"

### Import Options

#### Convert to Mesh
- **Enabled** (default): Automatically converts imported curve objects to mesh
- **Disabled**: Keeps objects as curves (Blender default behavior)

#### Center Origin
- **Enabled** (default): Moves origin to geometry center for each imported object
- **Disabled**: Keeps origin at world center (Blender default behavior)

## Workflow Comparison

### Default Blender Workflow
1. `File > Import > Scalable Vector Graphics (.svg)`
2. Select all imported objects
3. `Object > Convert > Mesh`  
4. `Object > Set Origin > Origin to Geometry`
5. **4 separate steps required**

### SVG Importer Plus Workflow
1. `File > Import > Scalable Vector Graphics Plus (.svg)`
2. Configure options (optional)
3. Import
4. **1 step - done!**

## Import Results

The add-on provides detailed feedback after import:
- Number of objects imported
- Number of objects converted to mesh
- Number of objects with centered origins
- Any warnings or errors encountered

Example: *"Imported 5 object(s), converted 5 to mesh, centered 5 origins"*

## Use Cases

### Logo and Icon Import
- Import SVG logos for product visualization
- Automatic mesh conversion for proper rendering
- Centered origins for easy positioning and scaling

### Technical Drawings
- Import architectural or engineering drawings
- Mesh conversion enables material application
- Centered origins simplify transformation operations

### Graphic Design Elements
- Import decorative elements and shapes
- Ready-to-use mesh objects for animation
- Proper origins for rotation and scaling

### UI Elements for 3D Interfaces
- Import interface icons and buttons
- Mesh format compatible with all Blender tools
- Centered origins for consistent layout

## Technical Details

### Import Process
1. **SVG Import**: Uses Blender's built-in SVG importer
2. **Object Detection**: Identifies newly imported objects
3. **Mesh Conversion**: Converts curve objects to mesh using `object.convert()`
4. **Origin Centering**: Sets origin using `object.origin_set(type='ORIGIN_GEOMETRY')`
5. **Progress Reporting**: Provides detailed feedback on operations

### Safety Features
- **Error Handling**: Graceful handling of conversion failures
- **Object Preservation**: Non-destructive processing with fallback
- **User Control**: Optional processing steps can be disabled
- **Progress Feedback**: Clear indication of successful and failed operations

### Performance
- **Efficient Processing**: Batch operations on all imported objects
- **Minimal Overhead**: Uses standard Blender operations
- **Scalable**: Handles single objects or complex multi-object SVGs

## Compatibility

- **Blender Version**: 4.2.0 or later
- **File Types**: Standard SVG files (.svg)
- **Operating Systems**: Cross-platform (Windows, macOS, Linux)
- **SVG Features**: Compatible with all SVG elements supported by Blender
- **Workflow**: Integrates seamlessly with existing Blender import system

## Troubleshooting

- **No objects imported**: Check if SVG file contains valid vector data
- **Conversion failed**: Some complex curves may not convert properly - use manual conversion
- **Origin centering failed**: Ensure object has geometry for center calculation
- **Import menu missing**: Verify add-on is enabled in Preferences > Add-ons

## Limitations

- **Curve-only processing**: Only converts objects that are imported as curves
- **Geometry dependency**: Origin centering requires valid geometry
- **Blender SVG support**: Limited by Blender's native SVG import capabilities
- **Complex paths**: Very complex SVG paths may require manual cleanup

## Why "SVG Importer Plus"?

The name clearly indicates this is an enhanced version of SVG import functionality, with "Plus" representing the additional automated post-processing features that streamline the workflow.

## Workflow Benefits

- **Time Saving**: Eliminates 2-3 manual steps per import
- **Consistency**: Ensures all imported SVGs have proper mesh format and origins
- **Reduced Errors**: Automated process prevents forgetting conversion steps
- **Professional Workflow**: Standard mesh objects ready for animation and rendering
- **User Friendly**: Single import operation with clear options

## Support

For issues, feature requests, or questions, please create an issue in the project repository.

## License

This project is licensed under the GPL 3.0 or later license.
# Vexer (/ˈveksər/)

A Blender add-on that adds basic geometric primitives with vertices and edges in a progressive dimensional approach (1D→2D→3D), seamlessly integrated into the Add > Mesh menu.

## Features

- **Point (頂点)**: Create a single vertex (0D → 1D)
- **Line (辺)**: Create two vertices connected by an edge (1D)
- **Triangle (三角形)**: Create three vertices forming a triangle (2D)
- **Integrated Menu**: Primitives are logically placed in the Add > Mesh menu
- **Custom Icons**: Support for custom triangle icon (icons/triangle.png)
- **Multilingual**: Japanese/English interface support

## Installation

### Method 1: Remote Repository (Recommended)
1. Go to `Edit > Preferences > Extensions`
2. Click the dropdown arrow next to "Repositories"
3. Click "Add Remote Repository"
4. Enter the repository URL: `https://extensions.kract.jp/api/v1/extensions/`
5. Click "Add Repository"
6. Browse and install "Vexer" from the repository

### Method 2: Drag and Drop (Blender 4.2+)
1. Download the add-on as a ZIP file
2. Simply drag and drop the ZIP file into Blender
3. The add-on will be automatically installed and enabled

### Method 3: Traditional Installation
1. Download the add-on files
2. Go to `Edit > Preferences > Add-ons`
3. Click `Install...` and select the ZIP file
4. Enable the "Vexer" add-on

## Usage

### Basic Usage
1. In the 3D Viewport, press `Shift + A` to open the Add menu
2. Navigate to `Add > Mesh`
3. Find the Vexer primitives:
   - **Point/頂点**: Located after Plane
   - **Line/辺**: Located after Plane
   - **Triangle/三角形**: Located after Torus

### Custom Icons
- Place a `triangle.png` file in the `icons/` folder to use custom triangle icon
- Recommended size: 16x16px or 32x32px PNG format
- Without custom icon, default Blender icons are used

## Menu Integration

The primitives are strategically placed in the Add > Mesh menu:
- **Point & Line**: Positioned after Plane (basic 2D primitive)
- **Triangle**: Positioned after Torus (completing the progression)

## What Gets Created

- **Point**: Single vertex at origin (0,0,0)
- **Line**: Two vertices at (-1,0,0) and (1,0,0) connected by an edge
- **Triangle**: Three vertices forming an equilateral triangle with edges

## Requirements

- Blender 4.2 or later

## License

This project is licensed under the GPL 3.0 or later license.
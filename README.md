# KRACT Blender Extensions Collection

A curated collection of professional Blender extensions designed to enhance your 3D workflow. All extensions are built for Blender 4.2+ with full support for the new extension system, drag-and-drop installation, and multilingual interfaces.

## 🌐 Extension Registry

**https://extensions.kract.jp**

Get all extensions directly from our third-party Blender Extension Registry:

1. Go to `Edit > Preferences > Extensions`
2. Click the dropdown arrow next to "Repositories"
3. Click "Add Remote Repository"
4. Enter: `https://extensions.kract.jp/api/v1/extensions/`
5. Click "Add Repository"
6. Browse and install any extension from the collection

## 📦 Extensions Overview

### 🎯 Viewpie
**Intuitive 3D viewport navigation with pie menus**
- **Hotkeys**: `Q` (basic) / `Shift+Q` (extended)
- **Features**: 8-direction navigation, multilingual support (EN/JP), smart projection toggle
- **Perfect for**: Fast viewport navigation, architectural visualization, animation workflows

### 📷 Viewcam
**Instant camera positioning and navigation**
- **Hotkeys**: `Cmd/Ctrl+Shift+C` (set view to camera) / `Cmd/Ctrl+Shift+Alt+C` (toggle lock)  
- **Features**: One-click camera positioning, "Lock Camera to View" toggle, viewport header integration
- **Perfect for**: Cinematography, product rendering, animation blocking

### 📁 Versave
**Enhanced file versioning system with integrated version manager**
- **Hotkeys**: `Cmd/Ctrl+S` (enhanced save) / `Cmd/Ctrl+Alt+S` (enhanced incremental save) / `Cmd/Ctrl+Shift+E` (version manager)
- **Features**: Automatic "_v" prefix versioning, project structure creation, smart version detection, visual version switching
- **Perfect for**: Professional project organization, consistent file naming, version control, quick version switching

### 🎨 Wizender
**Smart render settings automation**
- **Features**: Auto-configuration on save, project name placeholders, customizable presets
- **Perfect for**: Consistent render output, automated workflows, batch rendering

### 👁️ hideX (/ˈhaɪdeks/)
**Enhanced object visibility control**
- **Hotkeys**: `H` (enhanced hide)
- **Features**: Hide objects from both viewport and render, individual object management, state restoration
- **Perfect for**: Scene organization, render optimization, clean viewport workflows

### 📁 Subamo
**Automatic backup file organization**
- **Features**: Auto-organize backup files into subdirectories, backup management panel, file information display
- **Perfect for**: Clean project folders, backup management, professional project organization

### 🗑️ Nukeshima
**Silent object deletion**
- **Hotkeys**: `X` (smart delete) / `Shift+X` (delete menu)
- **Features**: No confirmation dialogs, smart delete logic, full delete menu access
- **Perfect for**: Fast modeling workflows, cleanup operations, uninterrupted editing

### 📄 SVG Importer Plus
**Enhanced SVG import with automatic mesh conversion**
- **Features**: Import SVG files and convert to mesh objects, automatic origin centering, optimized import workflow
- **Perfect for**: Logo design integration, 2D to 3D conversion, graphic design workflows

### 🔺 Vexer
**Progressive geometric primitive creation**
- **Features**: Create basic geometric primitives with progressive vertex and edge addition (1D→2D→3D)
- **Perfect for**: Basic modeling, educational purposes, geometric foundation building

## 🚀 Installation Methods

### Method 1: Remote Repository (Recommended)
Use our extension registry for automatic updates and easy management.

### Method 2: Drag & Drop (Blender 4.2+)
Simply drag ZIP files into Blender - modern and effortless.

### Method 3: Traditional Installation
Standard add-on installation for older Blender versions.

## 🔧 Development & Deployment

For developers working with these extensions:

### Initial Setup
```bash
npx kract@latest blender init
```

### Package Extensions
Create distribution-ready packages for all extensions:
```bash
npx kract@latest blender package
```

### Deploy to Remote Repository
Deploy packaged extensions to the remote repository:
```bash
npx kract@latest blender deploy
```

**Note**: Initial setup with `kract blender init` is required before packaging and deployment.

## 🎨 Key Features Across Collection

- **🌍 Multilingual Support**: Full English and Japanese interfaces
- **⚡ Modern Extension System**: Blender 4.2+ optimized with drag-and-drop installation
- **🎯 Professional Workflow**: Industry-standard conventions and practices
- **🔧 Seamless Integration**: Natural extension of Blender's existing functionality
- **📱 Smart UI**: Context-aware interfaces that appear when needed
- **⌨️ Intuitive Shortcuts**: Memorable hotkeys that enhance productivity

## 📊 Extension Details

| Extension | Version | Hotkeys | Primary Function |
|-----------|---------|---------|------------------|
| **Viewpie** | 1.0.0 | `Q` / `Shift+Q` | 3D viewport navigation with pie menus |
| **Viewcam** | 1.0.0 | `Cmd/Ctrl+Shift+C` | Camera positioning and navigation |
| **Versave** | 1.0.1 | `Cmd/Ctrl+Alt+S` / `Cmd/Ctrl+Shift+E` | Enhanced file versioning system with version manager |
| **Wizender** | 1.0.1 | Auto on save | Smart render settings automation |
| **hideX** | 1.0.0 | `H` | Enhanced object visibility control |
| **Subamo** | 1.0.1 | Auto on save | Automatic backup file organization |
| **Nukeshima** | 1.0.0 | `X` / `Shift+X` | Silent object deletion |
| **SVG Importer Plus** | 1.0.1 | Import menu | Enhanced SVG import with mesh conversion |
| **Vexer** | 1.0.0 | Add menu | Progressive geometric primitive creation |

## 🎯 Workflow Integration Examples

### 🏗️ Architectural Visualization Workflow
1. **Viewpie**: Navigate through Front/Back/Left/Right views for elevation work
2. **Viewcam**: Set up presentation camera angles with one click
3. **Versave**: Maintain organized project versions with proper naming + quick version switching with `Cmd+Shift+E`
4. **Wizender**: Auto-configure render settings for consistent output

### 🎬 Animation Production Workflow  
1. **Viewpie**: Quick viewport changes during blocking and keyframing
2. **Viewcam**: Camera positioning and "Lock Camera to View" for cinematography
3. **Versave**: Version control for animation iterations + instant access to previous versions
4. **Nukeshima**: Fast object deletion without interrupting animation flow

### 🎨 General 3D Modeling Workflow
1. **Viewpie**: Fast view switching during modeling (Front → Right → Top → Camera)
2. **Viewcam**: Check composition and framing frequently
3. **Versave**: Automatic version management with organized project structure + version manager for quick comparisons
4. **Vexer**: Create basic geometric primitives for modeling foundations
5. **SVG Importer Plus**: Import logos and 2D graphics for 3D integration

## 💡 Pro Tips

- **Combine Viewpie + Viewcam**: Use `Q` for quick view changes, then `Cmd+Shift+C` to match camera
- **Versave + Wizender**: Automatic project organization with render settings applied on save
- **Versave Version Manager**: Save frequently and use `Cmd+Shift+E` to quickly compare different approaches or revert changes
- **SVG + Versave**: Import logos with SVG Importer Plus and maintain clean project versions
- **Vexer + Nukeshima**: Create basic shapes with Vexer, then use silent deletion for rapid iteration
- **Muscle Memory**: Practice pie menu directions for lightning-fast viewport navigation

## 🔧 System Requirements

- **Blender Version**: 4.2.0 or later (some extensions support earlier versions)
- **Operating System**: Cross-platform (Windows, macOS, Linux)
- **Language Support**: English and Japanese (日本語)
- **Installation**: Full extension system support with drag-and-drop

## 📈 Performance & Compatibility

- **Lightweight**: Minimal overhead with smart context-aware activation
- **Non-conflicting**: Designed to work together seamlessly
- **Render Engine**: Compatible with Cycles, Eevee, and Workbench
- **Viewport**: Works across all 3D viewport shading modes

## 🌟 Why Choose KRACT Extensions?

1. **🎯 Purpose-Built**: Each extension solves specific workflow bottlenecks
2. **🔄 Integrated Design**: Extensions work better together than individually
3. **📚 Professional Standards**: Industry-standard conventions and practices
4. **🌍 Global Ready**: Full multilingual support for international workflows
5. **⚡ Modern Architecture**: Built for Blender 4.2+ with future-proof design
6. **🎨 User-Centric**: Intuitive interfaces that enhance rather than complicate

## 📞 Support & Community

- **Issues & Feature Requests**: Create issues in the project repository
- **Documentation**: Individual README files for each extension
- **Updates**: Automatic updates through extension registry
- **Community**: Share workflows and tips with other users

## 📄 License

All extensions in this collection are licensed under **GPL 3.0 or later**.
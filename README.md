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
**Enhanced file versioning system**
- **Hotkeys**: `Cmd/Ctrl+S` (enhanced save) / `Cmd/Ctrl+Alt+S` (enhanced incremental save)
- **Features**: Automatic "_v" prefix versioning, project structure creation, smart version detection
- **Perfect for**: Professional project organization, consistent file naming, version control

### 🌍 Toggle Translated UI
**Quick UI language switching**
- **Hotkeys**: `END` key
- **Features**: One-click EN/JP toggle, custom language icons, header integration
- **Perfect for**: Multilingual workflows, tutorials, international collaboration

### 🎨 Wizender
**Smart render settings automation**
- **Features**: Auto-configuration on save, project name placeholders, customizable presets
- **Perfect for**: Consistent render output, automated workflows, batch rendering

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
| **Versave** | 1.0.0 | `Cmd/Ctrl+Alt+S` | Enhanced file versioning system |
| **Toggle Translated UI** | 3.1.0 | `END` | Quick UI language switching |
| **Wizender** | 1.0.0 | Auto on save | Smart render settings automation |

## 🎯 Workflow Integration Examples

### 🏗️ Architectural Visualization Workflow
1. **Viewpie**: Navigate through Front/Back/Left/Right views for elevation work
2. **Viewcam**: Set up presentation camera angles with one click
3. **Versave**: Maintain organized project versions with proper naming
4. **Wizender**: Auto-configure render settings for consistent output

### 🎬 Animation Production Workflow  
1. **Viewpie**: Quick viewport changes during blocking and keyframing
2. **Viewcam**: Camera positioning and "Lock Camera to View" for cinematography
3. **Toggle Translated UI**: Switch languages for international team collaboration
4. **Versave**: Version control for animation iterations

### 🎨 General 3D Modeling Workflow
1. **Viewpie**: Fast view switching during modeling (Front → Right → Top → Camera)
2. **Viewcam**: Check composition and framing frequently
3. **Versave**: Automatic version management with organized project structure
4. **Wizender**: Consistent render output settings across projects

## 💡 Pro Tips

- **Combine Viewpie + Viewcam**: Use `Q` for quick view changes, then `Cmd+Shift+C` to match camera
- **Versave + Wizender**: Automatic project organization with render settings applied on save
- **Toggle Translated UI**: Switch languages without system changes - perfect for tutorials
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

---

*Transform your Blender workflow with professional-grade extensions designed for efficiency, consistency, and creativity.*
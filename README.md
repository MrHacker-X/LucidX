# LucidX - AI-Powered Image Synthesis Engine

```
           ▄█▀▄            ▄▀▄▄
               ▀▄        ▄▀
          ▄▄▄    █▄▄▄▄▄▄█    ▄▄▄
         ▀   ▀█ █▀  ▐▌  ▀█ █▀   ▀
               ██  ▀▐▌▀  ██
          ▄█▀▀▀████████████▀▀▀█
         █      ██████████     ▀▄
         █▄   █▀  ▀▀▀▀▀▀  ▀█   ▄█
          ▀█   █  v.1.0.5 █   █▀
```


<div align="center">


**An AI-powered image synthesis engine crafted for creators, developers, and visionaries.**

[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Termux-lightgrey.svg)](#compatibility)
[![API](https://img.shields.io/badge/API-Stability%20AI-purple.svg)](https://stability.ai/)
[![Version](https://img.shields.io/badge/version-1.0.5-brightgreen.svg)](#overview)
[![Status](https://img.shields.io/badge/status-stable-success.svg)](#overview)
[![Maintained](https://img.shields.io/badge/maintained-yes-green.svg)](#contributing)
[![Stars](https://img.shields.io/github/stars/VritraSecz/LucidX?style=social)](https://github.com/VritraSecz/LucidX)
[![Forks](https://img.shields.io/github/forks/VritraSecz/LucidX?style=social)](https://github.com/VritraSecz/LucidX)
[![Issues](https://img.shields.io/github/issues/VritraSecz/LucidX)](https://github.com/VritraSecz/LucidX/issues)
[![Contributors](https://img.shields.io/github/contributors/VritraSecz/LucidX)](https://github.com/VritraSecz/LucidX/graphs/contributors)
[![Languages](https://img.shields.io/github/languages/count/VritraSecz/LucidX)](https://github.com/VritraSecz/LucidX)
[![Code Size](https://img.shields.io/github/languages/code-size/VritraSecz/LucidX)](https://github.com/VritraSecz/LucidX)

</div>

## 🆕 What's New in v1.0.5

<div align="center">

### ✨ **Latest Features & Improvements**

</div>

#### 🖥️ **Command Line Arguments Support**
- **`--help` / `-h`**: Get instant help and usage examples without entering the interactive menu
- **`--version` / `-v`**: Quickly check your LucidX version and system information
- **Smart Error Handling**: Prevents multiple arguments and shows helpful error messages
- **Professional CLI**: Standard Unix-style command line interface

#### 🌐 **Global Configuration System**
- **New Config Location**: `~/.config-vritrasecz/lucidx-config.json`
- **JSON Format**: Clean, structured configuration instead of Python files
- **Global Access**: Use your API key from any directory on your system
- **Auto-Creation**: Configuration directory is created automatically
- **Enhanced Security**: Config stored safely in your home directory

#### 🔧 **Enhanced User Experience**
- **Argument Validation**: Detects and handles invalid arguments gracefully
- **Better Error Messages**: More informative error handling throughout the tool
- **Backward Compatibility**: All existing functionality preserved
- **Improved Documentation**: Updated help system with new features

#### 📖 **Usage Examples**
```bash
# Quick help (new!)
python lucidx.py --help

# Check version (new!)
python lucidx.py --version

# Normal interactive mode (unchanged)
python lucidx.py
```

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Style Presets](#-style-presets)
- [Screenshots](#️-screenshots)
- [File Structure](#-file-structure)
- [Output Management](#-output-management)
- [Logging System](#-logging-system)
- [Platform Compatibility](#-platform-compatibility)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [Contact & Support](#-contact--support)
- [License](#-license)

## 🔮 Overview

**LucidX** is a sophisticated AI-powered image synthesis engine that leverages the Stability AI API to transform text prompts into stunning, high-resolution images. Designed with an intuitive command-line interface, LucidX offers creators, developers, and visionaries a powerful tool to bring their imagination to life through advanced AI image generation.

### Key Highlights

- 🎨 **Multi-Style Generation**: Choose from 8 distinctive artistic styles
- 🔧 **Interactive CLI**: User-friendly command-line interface with visual feedback
- 📱 **Cross-Platform**: Native support for Linux and Android (Termux)
- 📊 **Session Management**: Comprehensive logging and progress tracking
- 🛡️ **Secure API Handling**: Safe storage and management of API credentials
- ⚡ **Batch Processing**: Generate multiple variations per prompt automatically

## ✨ Features

### Core Functionality
- **AI Image Generation**: Powered by Stability AI's advanced image synthesis models
- **Multiple Style Presets**: 8 built-in artistic styles including photographic, anime, digital art, and more
- **Batch Generation**: Automatically creates 4 image variations per prompt
- **Smart File Management**: Automatic timestamped file naming and organized storage
- **Session Logging**: Comprehensive activity logs with detailed metadata

### User Experience
- **Interactive Menu System**: Intuitive navigation through all application features
- **Real-time Progress Feedback**: Visual indicators during image generation
- **Graceful Error Handling**: Robust error management with user-friendly messages
- **Interrupt Handling**: Safe Ctrl+C handling with session cleanup
- **Session Summary**: Detailed statistics upon completion

### Security & Configuration
- **Secure API Key Storage**: Encrypted local storage of Stability AI credentials
- **API Key Management**: Easy configuration and updating of API keys
- **Validation**: Input validation and API response verification

## 📋 Requirements

### System Requirements
- **Python**: Version 3.7 or higher
- **Operating System**: Linux (any distribution) or Android with Termux
- **Internet Connection**: Required for Stability AI API access
- **Storage**: Minimum 100MB free space for generated images

### Python Dependencies
```bash
colorama>=0.4.4    # Terminal color formatting
requests>=2.25.1   # HTTP requests for API communication
pathlib            # File path management (built-in)
datetime           # Timestamp generation (built-in)
```

### API Requirements
- **Stability AI API Key**: Required for image generation
- **API Credits**: Sufficient credits in your Stability AI account

## 🚀 Installation

### Method 1: Git Clone (Recommended)
```bash
# Clone the repository
git clone https://github.com/VritraSecz/LucidX.git

# Navigate to project directory
cd LucidX

# Install dependencies
pip3 install -r requirements.txt

# Run the application
python lucidx.py
```

### Method 2: Direct Download
1. Download the project as ZIP from GitHub
2. Extract to your desired location
3. Install dependencies: `pip install colorama requests`
4. Run: `python lucidx.py`

### Method 3: Termux (Android)
```bash
# Update package list
apt update && apt upgrade

# Install Python and Git
apt install python python-pip git

# Clone and setup
git clone https://github.com/VritraSecz/LucidX.git
cd LucidX
pip install -r requirements.txt

# Run
python lucidx.py
```

## ⚙️ Configuration

### API Key Setup

1. **Obtain Stability AI API Key**:
   - Visit [Stability AI Platform](https://platform.stability.ai/)
   - Create an account and generate an API key
   - Ensure you have sufficient credits

2. **Configure in LucidX**:
   - Launch LucidX: `python lucidx.py`
   - Select option `[2] Configure API Key`
   - Enter your API key when prompted
   - Key is securely stored in `core/config.py`

3. **Update Existing Key**:
   - Use the same configuration menu
   - Choose to replace existing key when prompted

### Directory Structure Setup

The application automatically creates necessary directories:

**Linux/PC**:
```
./generated_images/     # Generated images storage
./generation_log.txt    # Session activity log
./last_style.txt        # Temporary style preference
```

**Termux (Android)**:
```
/sdcard/LucidX_Images/  # Generated images storage
./generation_log.txt    # Session activity log
./last_style.txt        # Temporary style preference
```

## 🎯 Usage

### Basic Workflow

1. **Launch Application**
   ```bash
   python lucidx.py
   ```

2. **Configure API Key** (First-time setup)
   - Select option `[2]` from main menu
   - Enter your Stability AI API key

3. **Generate Images**
   - Select option `[1] Image Generation`
   - Choose your preferred style preset (1-8)
   - Enter your text prompt
   - Wait for generation completion

4. **View Results**
   - Images saved automatically with timestamps
   - Session summary displayed after each batch

### Advanced Usage

#### Custom Prompting Tips
- **Be Descriptive**: Use detailed, specific language
- **Add Modifiers**: Include quality terms like "high resolution", "cinematic", "detailed"
- **Style Keywords**: Incorporate style-specific terms that complement your chosen preset
- **Composition**: Describe the scene composition, lighting, and mood

#### Batch Operations
- Each prompt automatically generates 4 variations
- Seeds are incremented for unique results (1234, 1235, 1236, 1237)
- All images use consistent steps (30) for quality

#### Session Management
- View real-time generation progress
- Session statistics available at completion
- Graceful exit with Ctrl+C preserves session data

## 🎨 Style Presets

LucidX offers 8 distinctive artistic styles:

| ID | Style | Description | Best For |
|----|-------|-------------|----------|
| **1** | `photographic` | Realistic, camera-like imagery | Portraits, landscapes, realistic scenes |
| **2** | `anime` | Japanese animation style | Characters, fantasy scenes, stylized art |
| **3** | `digital-art` | Modern digital illustration | Concept art, creative designs, modern aesthetics |
| **4** | `neon-punk` | Cyberpunk aesthetic with neon colors | Futuristic scenes, urban landscapes, sci-fi |
| **5** | `fantasy-art` | Fantasy and magical themes | Mythical creatures, magical scenes, epic art |
| **6** | `pixel-art` | Retro pixelated style | Game assets, retro designs, minimalist art |
| **7** | `isometric` | 3D isometric perspective | Technical illustrations, game environments |
| **8** | `low-poly` | Geometric, minimalist 3D style | Abstract designs, modern minimalism |

### Style Selection Process
- Styles are remembered during the session
- Stored in temporary `last_style.txt` file
- Automatically cleaned up on exit

## 🖼️ Screenshots

### Main Menu + Output Interface
![Main Menu](https://i.ibb.co/BHdPqQSn/Screenshot-From-2025-07-21-02-26-45.png)


## 📁 File Structure

```
LucidX/
├── lucidx.py                # Application entry point
├── core/                  # Core modules directory
│   ├── genx.py            # Image generation engine
│   ├── banr.py            # ASCII art banners
│   ├── colors.py          # Terminal color definitions
│   └── modulex.py         # Utility functions and menus
├── generated_images/      # Output directory (auto-created)
├── generation_log.txt     # Activity log (auto-created)
├── last_style.txt         # Temporary style storage (auto-created)
├── requirements.txt       # Install required python library
└── README.md              # This documentation
```

### Core Module Details

#### `lucidx.py`
- Application entry point
- Main menu navigation
- Signal handling for graceful interruption

#### `core/genx.py`
- Image generation engine
- API communication with Stability AI
- File management and batch processing
- Progress tracking and logging

#### `core/modulex.py`
- Menu systems and user interactions
- API key configuration interface
- Help and documentation displays

#### `core/banr.py`
- ASCII art banners and logos
- Session information display
- Dynamic timestamp generation

#### `core/colors.py`
- Terminal color scheme definitions
- Consistent visual styling across application

## 📂 Output Management

### File Naming Convention
Generated images follow a standardized naming pattern:
```
YYYYMMDD_HHMMSS.png
```
Example: `20241220_143052.png` (December 20, 2024 at 14:30:52)

### Storage Locations

#### Linux/PC Systems
- **Path**: `./generated_images/`
- **Creation**: Automatically created relative to script location
- **Permissions**: Standard user permissions

#### Android (Termux)
- **Path**: `/sdcard/LucidX_Images/`
- **Creation**: Automatically created on SD card storage
- **Access**: Accessible through file manager apps

### Image Specifications
- **Format**: PNG
- **Quality**: High resolution (API dependent)
- **Size**: Variable based on Stability AI model output
- **Metadata**: Generation parameters logged separately

## 📊 Logging System

### Generation Log (`generation_log.txt`)

Each generation session creates detailed log entries:

```
[2024-12-20 14:30:52] Prompt: "sunset over mountain lake" -› 20241220_143052.png
[2024-12-20 14:30:54] Prompt: "sunset over mountain lake" -› 20241220_143054.png
[2024-12-20 14:30:56] Prompt: "sunset over mountain lake" -› 20241220_143056.png
[2024-12-20 14:30:58] Prompt: "sunset over mountain lake" -› 20241220_143058.png
```

### Session Summary

Displayed at the end of each session:
```
:: LucidX Session Summary ::
 › Prompts entered    : 3
 › Images generated   : 12
 › Output directory   : /home/user/LucidX/generated_images
 › Session completed.
```

### Error Logging
- API errors logged with full response details
- Network issues captured with diagnostic information
- File system errors documented with context

## 🖥️ Platform Compatibility

### Linux Distributions
- **Ubuntu/Debian**: Fully supported
- **Fedora/CentOS**: Fully supported  
- **Arch Linux**: Fully supported
- **Kali Linux**: Fully supported (as tested)
- **Alpine Linux**: Compatible with Python 3.7+

### Android (Termux)
- **Installation**: Available through Termux package manager
- **Storage**: Automatic internal storage integration
- **Performance**: Optimized for mobile hardware
- **Permissions**: Handles Android storage permissions

### Requirements by Platform

#### Linux
```bash
sudo apt update
sudo apt install python3 python3-pip
pip3 install colorama requests
```

#### Termux
```bash
pkg update
pkg install python python-pip git
pip install colorama requests
```

## 🔧 Troubleshooting

### Common Issues

#### API Key Problems
**Issue**: "API key not configured" or authentication errors
**Solutions**:
- Verify API key is correctly entered (check for extra spaces)
- Ensure API key is active on Stability AI platform
- Check account credit balance
- Reconfigure using menu option [2]

#### Network Issues
**Issue**: Connection timeout or network errors
**Solutions**:
- Verify internet connectivity
- Check firewall settings
- Try using VPN if blocked in your region
- Ensure stable internet connection during generation

#### File Permission Errors
**Issue**: Cannot save files or create directories
**Solutions**:
- Check write permissions in current directory
- For Termux: Ensure storage permissions are granted
- Run with appropriate user permissions
- Verify sufficient disk space

#### Import Errors
**Issue**: `ModuleNotFoundError` for colorama or requests
**Solutions**:
```bash
pip install --upgrade colorama requests
# or for system-wide installation
pip3 install --upgrade colorama requests
```

### Performance Optimization

#### For Slower Systems
- Close unnecessary applications during generation
- Ensure stable internet connection
- Monitor available RAM and storage

#### For Mobile/Termux
- Use Wi-Fi instead of mobile data for better stability
- Keep device plugged in during long sessions
- Clear app cache if experiencing issues


## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### Ways to Contribute
- 🐛 **Bug Reports**: Submit detailed issue reports
- 💡 **Feature Requests**: Suggest new functionality
- 🔧 **Code Contributions**: Submit pull requests
- 📚 **Documentation**: Improve documentation and examples
- 🎨 **Style Presets**: Suggest new artistic styles

### Development Setup
```bash
# Fork the repository on GitHub
# Clone your fork
git clone https://github.com/yourusername/LucidX.git

# Create a feature branch
git checkout -b feature/your-feature-name

# Make changes and test thoroughly
# Commit with descriptive messages
git commit -m "Add: new feature description"

# Push to your fork and create pull request
git push origin feature/your-feature-name
```

### Code Standards
- Follow PEP 8 Python style guidelines
- Include docstrings for new functions
- Test on both Linux and Termux when possible
- Maintain backward compatibility

### Issue Reporting
When reporting issues, please include:
- Python version
- Operating system and version
- Error messages (full traceback)
- Steps to reproduce
- Expected vs actual behavior

## 📞 Contact & Support

### Developer Information
[![Creator](https://img.shields.io/badge/creator-Alex%20%40%20VritraSec-blue)](https://vritrasec.com)
[![Website](https://img.shields.io/badge/website-VritraSec-blue)](https://vritrasec.com)
[![GitHub](https://img.shields.io/badge/github-VritraSecz-blue)](https://github.com/VritraSecz)

### Community & Support
[![Instagram](https://img.shields.io/badge/instagram-%40haxorlex-blue)](https://instagram.com/haxorlex)
[![YouTube](https://img.shields.io/badge/youtube-%40Technolex-blue)](https://youtube.com/@Technolex)
[![Telegram Channel](https://img.shields.io/badge/telegram-%40LinkCentralX-blue)](https://t.me/LinkCentralX)
[![Support Bot](https://img.shields.io/badge/support-bot-blue)](https://t.me/ethicxbot)

### Getting Help
1. **Check Documentation**: Review this README and built-in help
2. **Search Issues**: Look for existing solutions on GitHub
3. **Community Support**: Ask questions on Telegram channel
4. **Bug Reports**: Submit detailed issues on GitHub
5. **Direct Contact**: Use support bot for urgent issues


## 📄 License

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red)](https://github.com/VritraSecz/LucidX)
[![Free Software](https://img.shields.io/badge/Free%20Software-GNU-blue)](https://www.gnu.org/philosophy/free-sw.html)

</div>

+ **This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.**

<div align="center">

### 🏷️ MIT License Permissions & Limitations

<table>
<tr>
<td align="center" width="50%">

#### ✅ **PERMISSIONS**

<div align="left">

![Commercial Use](https://img.shields.io/badge/✅%20Commercial%20Use-Allowed-brightgreen?style=for-the-badge&logo=dollar-sign&logoColor=white)

![Modification](https://img.shields.io/badge/✅%20Modification-Allowed-brightgreen?style=for-the-badge&logo=edit&logoColor=white)

![Distribution](https://img.shields.io/badge/✅%20Distribution-Allowed-brightgreen?style=for-the-badge&logo=share&logoColor=white)

![Private Use](https://img.shields.io/badge/✅%20Private%20Use-Allowed-brightgreen?style=for-the-badge&logo=lock&logoColor=white)

</div>

</td>
<td align="center" width="50%">

#### ❌ **LIMITATIONS**

<div align="left">

![No Warranty](https://img.shields.io/badge/❌%20No%20Warranty-Provided-red?style=for-the-badge&logo=shield-x&logoColor=white)

![No Liability](https://img.shields.io/badge/❌%20No%20Liability-Accepted-red?style=for-the-badge&logo=alert-triangle&logoColor=white)

</div>



#### ⚠️ **REQUIREMENTS**

<div align="left">

![License Notice](https://img.shields.io/badge/⚠️%20License%20Notice-Required-orange?style=for-the-badge&logo=document-text&logoColor=white)

</div>
</td>
</tr>
</table>

</div>

---

<div align="center">

**LucidX v1.0.5** - *"I don't paint dreams. I compute realities yet to be rendered."*

Made with ❤️ by [VritraSec](https://vritrasec.com)

</div>
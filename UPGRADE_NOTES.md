# LucidX v1.0.5 - Upgrade Notes

## New Features Added

### 1. Command Line Arguments Support
- **`--help` / `-h`**: Display help information and usage examples
- **`--version` / `-v`**: Show version and tool information
- **Multiple argument detection**: Prevents using more than one argument at once
- **Invalid argument handling**: Shows error message for unknown arguments

### 2. Global Configuration System
- **New Config Location**: `~/.config-vritrasecz/lucidx-config.json`
- **JSON Format**: Cleaner and more structured than the old Python format
- **Auto-Creation**: Directory is created automatically during first configuration
- **Global Access**: Config can be accessed from anywhere on the system

## Usage Examples

```bash
# Show help
python lucidx.py --help
python lucidx.py -h

# Show version
python lucidx.py --version  
python lucidx.py -v

# Launch interactive menu (default behavior)
python lucidx.py
```

## Configuration Migration

### Old System (v1.0 - previous)
- Location: `core/config.py`
- Format: `API = "your-key-here"`
- Scope: Local to project directory

### New System (v1.0 - current)
- Location: `~/.config-vritrasecz/lucidx-config.json`
- Format: `{"API": "your-key-here"}`
- Scope: Global user configuration

### Migration Steps
1. Your existing API key will need to be reconfigured using the interactive menu
2. Use option `[2] Configure API Key` from the main menu
3. The system will automatically create the new global config structure

## Backward Compatibility
- The old `core/config.py` file is no longer used but has been backed up as `core/config.py.backup`
- All existing functionality remains the same when launching without arguments
- Interactive menu and all features work exactly as before

## Technical Changes
- Added argument parsing in `lucidx.py`
- Updated `core/modulex.py` for JSON config handling
- Updated `core/genx.py` to load from global config
- Added proper error handling for missing/invalid configurations

## Benefits
- **Professional CLI**: Standard `--help` and `--version` arguments
- **Global Config**: API key accessible from any directory
- **Better Security**: Config stored in user's home directory
- **Cleaner Structure**: JSON format is more maintainable
- **Error Prevention**: Multiple argument detection prevents conflicts

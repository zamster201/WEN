import sys
import os

# Ensure we're running from WEN/
print("Current working dir:", os.getcwd())
print("Python path:", sys.path)

# Try to import ThemeManager
try:
    from core.theme_manager import ThemeManager
    print("✅ Successfully imported ThemeManager from core.theme_manager.")
except ImportError as e:
    print("❌ Import failed:", e)

input("\nPress Enter to exit...")
"""
chrome_hub.py

Handles the "Chrome meatball" submenu in WEN.
Scans open Chrome windows, filters and groups them by domain/category, 
and returns them for display in a pop-up UI.
"""

import win32gui
import json
import os

# Configuration file path
CONFIG_PATH = os.path.join("config", "browser_hub_map.json")

def load_browser_config(browser="chrome"):
    with open(CONFIG_PATH, "r") as f:
        data = json.load(f)
    return data.get(browser, {})

def find_chrome_windows(filter_suffix=" - Google Chrome"):
    """Return a list of (hwnd, title) tuples for Chrome windows."""
    results = []

    def callback(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if title.endswith(filter_suffix):
                results.append((hwnd, title))

    win32gui.EnumWindows(callback, None)
    return results

def group_windows(windows, keyword_map):
    """Return a dictionary of category -> list of titles."""
    grouped = {}
    for hwnd, title in windows:
        for category, keyword in keyword_map.items():
            if keyword.lower() in title.lower():
                grouped.setdefault(category, []).append((hwnd, title))
                break
        else:
            grouped.setdefault("Other", []).append((hwnd, title))
    return grouped

def get_chrome_meatball_data():
    config = load_browser_config("chrome")
    filter_suffix = config.get("filter", " - Google Chrome")
    keywords = config.get("keywords", {})

    windows = find_chrome_windows(filter_suffix)
    grouped = group_windows(windows, keywords)
    return grouped

# For debugging
if __name__ == "__main__":
    from pprint import pprint
    pprint(get_chrome_meatball_data())

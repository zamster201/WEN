---
created: "Jun-07-2025 22:21"
edited:
  - "Jun-07-2025 22:21"
origin: "internal"
source: "generated"
wf_status: "stable"
tags:
  - "CTS"
  - "WEN"
  - "workspace_switcher"
  - "floating_palette"
---

# WEN – Windows Express Nexus

**WEN (Windows Express Nexus)** is a modular, floating control surface designed to provide **rapid, context-sensitive access to active applications and workspace states**. It acts as the **interactive switchboard** for the CTS ecosystem, optimized for speed, clarity, and precision window control.

---

## ✅ Functional Overview

### 🎛 UI Layer

- Floating, borderless, always-on-top window
- Draggable interface using **Tkinter**
- Displays a **4×4 iconized grid** of launch/focus buttons
- Icons rendered from `.png` assets via **Pillow**

### 🔍 Window Interaction

- Click any icon to:
  - Locate a running application window (via `win32gui`)
  - Restore and bring it to the foreground
- No app launching — WEN is for switching, not starting

---

## 🧩 Configuration System

### 🖼 icon_map.json

- Maps app identifiers (e.g., `"chrome"`, `"obsidian"`) to `.png` icon file names
- Location: `wen/config/icon_map.json`

### 🧠 browser_hub_map.json

- Defines browser-specific filters and grouped site keywords
- Enables "meatball" behavior for Chrome, Firefox, Edge, Brave, etc.
- Includes special `"content"` category (YouTube, Spotify, etc.)

---

## 🌐 Chrome “Meatball” Model

- WEN shows a **single Chrome icon**
- Clicking it opens a **submenu** listing active Chrome windows
- Grouped by site patterns (YouTube, Canva, Docs, etc.)
- Derived from `browser_hub_map.json`

---

## 📦 Assets and Tooling

- Icons stored in `wen/assets/icons/`
- Format: `.png` only
- Fully user-extensible
- Image references stored in config only — not in DB

---

## 🔄 CTS Integration

| Module      | Status            | Description |
|-------------|-------------------|-------------|
| CWT         | Read-only consumer | Will display sessions stored in shared DB |
| Phoenix     | No link yet        | May act as trigger from Obsidian interface |
| SVT         | Future possibility | Session/window context capture for memory |
| OTK         | Planned            | Can serve as launch HUD |
| cts_shared  | Light              | Used for DB, icons, filters |

---

## 🧱 Next Development Steps

- Build dynamic Chrome submenu
- Enable grouped window filtering
- Integrate with CWT SQLite layout DB
- Add content-serving categories (🎵/📺)
- Optional: fuzzy search, window close, pinned favorites

---


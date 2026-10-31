# Abigail Morra — Photojournalism Portfolio

An archival broadsheet scan & editorial web app showcasing the 35mm film photography and photojournalism of **Abigail Morra**.

🌐 **Live Website**: [https://abigailmorra.xyz/](https://abigailmorra.xyz/)  
🎓 **Program**: Toronto Metropolitan University (TMU) • School of Image Arts • VISA  
🐾 **Web App Logo & Mascot**: Gilbert the Cat  

---

## 🗞️ Design Aesthetic: Scanned Newspaper & Yves Klein Blue

- **Movable Blue Sticker Hero**: Yves Klein ultramarine cobalt canvas with movable tactile stickers (Gilbert polaroid, vintage camera, ladybug drawing, stars doodle, vinyl record, and 35mm slide mount).
- **Web App Logo**: Gilbert the cat featured as the official web app logo badge, tab favicon, and PWA icon.
- **Archival Broadsheet Scan**: Textured paper crevices, fresh ink tone, four-color registration marks, and torn deckle edge.
- **One Solid Block per Project**:
  - **Assignment 01 — Urban Observations**: 21 curated 35mm urban observations across Toronto transit, streetcars, and architectural details. Features single active plate view with quick-switch filmstrip.
  - **Assignment 02 — Autumn Series**: 13 seasonal neighbourhood studies in mortality, repair, and salvage.
- **Full-Screen Archival Lightbox**: High-resolution inspect modal with keyboard navigation (`←`, `→`, `ESC`).
- **Zero Clutter**: Clean editorial typography letting the photographs speak for themselves.

---

## 📁 Repository Structure

```
AbigailMorra/
├── index.html                  # Handcrafted portfolio web app
├── site.webmanifest            # PWA manifest with Gilbert app icon
├── favicon.ico                 # 32x32 Gilbert favicon
├── favicon.png                 # 64x64 Gilbert favicon
├── apple-touch-icon.png        # 180x180/256x256 Gilbert iOS icon
├── photos/
│   ├── ass1/                   # 21 optimized urban observation plates
│   └── autumn/                 # 13 optimized autumn plates
├── stickers/                   # Tactile hero stickers & Gilbert portraits
│   ├── gilbert_icon_tight.png  # Circular web app logo
│   ├── gilbert_sticker.png     # Polaroid hero sticker
│   ├── camera_sticker.png      # Vintage rangefinder
│   ├── ladybug_sticker.png     # Abigail's original drawing
│   ├── hand_eyes_sticker.png   # Hand framer
│   ├── stars_sticker.png       # Retro starbursts
│   ├── vinyl_sticker.png       # Grooved record
│   └── abigail.jpg             # 35mm slide portrait
└── scripts/
    └── drive_sync_watcher.py   # Autonomous Google Drive monitor & auto-updater
```

---

## 🔄 Automated Google Drive Sync

To monitor Abigail's Google Drive folder and automatically ingest, optimize, commit, and push new photos:

```bash
# Run one-time check and sync:
python3 scripts/drive_sync_watcher.py --once

# Or run continuous background monitor:
python3 scripts/drive_sync_watcher.py --watch --interval 60
```

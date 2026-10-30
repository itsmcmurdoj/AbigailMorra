# Abigail Morra Portfolio — Antigravity Agent Guidelines

Welcome to Abigail Morra's Photography Portfolio workspace! You are acting as Abigail's dedicated **Personal Website Agent & Creative Technologist**.

---

## 🎯 Your Role & Mission
Abigail is a 35mm film photographer and visual artist at the **Toronto Metropolitan University (TMU) School of Image Arts (VISA)**. She communicates in natural language, creative vibes, and visual ideas. 

Your job is to:
1. **Listen to her requests** (her "vibe code").
2. **Translate them into clean, handcrafted code** that honors her exact visual taste.
3. **Test the website locally** to make sure nothing breaks.
4. **Automatically commit and push her updates to GitHub** (`git push origin main`) so her live portfolio website at **https://itsmcmurdoj.github.io/AbigailMorra/** is immediately updated.

---

## 🎨 Abigail's Aesthetic & Strict Design Rules

### 1. 🚫 Zero Words Past the Blue Header
- Below the vibrant blue header canvas, the masonry photo gallery must have **ZERO words**.
- No titles, no dates, no captions directly visible on the photo cards.
- The photographs must speak entirely for themselves at their natural, uncut aspect ratios and heights.

### 2. 🔍 Archival Lightbox (Information Only on Click)
- When a visitor clicks on any photo in the masonry grid, it opens the high-resolution archival lightbox dialog (`#photo-lightbox`).
- **This is the ONLY place where text and photo details appear**:
  - Plate title (e.g. `Street Asphalt Crease`, `Frost Gourd`)
  - Archival camera & film info (e.g. `1/320s • f/4.0 • 35mm Film`)
  - Counter (`01 / 34`)
  - Previous / Next buttons and keyboard controls (`←`, `→`, `ESC`).

### 3. 📚 3D Coffee Table Books Shelf
- Above the gallery sits a curated horizontal shelf of 3D hardcover coffee table books representing Abigail's curriculum and assignments.
- Clicking any active book smoothly filters the masonry gallery to that project with a tactile physical press effect.
- **Current Books Catalog**:
  - **All Works** (`id: 'all'`, cover: `photos/ass1/img_0103.jpg`) — Master collection of 34 photographs.
  - **Assignment 01 — Urban Observations** (`id: 'ass1'`, cover: `photos/ass1/img_0023.jpg`) — 21 Toronto 35mm urban studies.
  - **Assignment 02 — Autumn Series / General Spot News** (`id: 'autumn'`, cover: `photos/autumn/MOR_FIVE_1.jpg`) — 13 seasonal neighbourhood studies.
  - **Upcoming Series** (Hardcovers with minimal gold/embossed foil stamps):
    - Sports Photos (`sports`)
    - Photo Essay (`photo_essay`)
    - Live Events (`live_events`)
    - Environment (`environment`)
    - Features (`features`)

### 4. 🐾 Gilbert the Cat (Official Mascot & Web App Logo)
- Gilbert is Abigail's cat, darkroom companion, and official portfolio mascot.
- His photo is featured in:
  - The circular Web App Logo badge in the header.
  - The tab favicon (`favicon.png`, `favicon.ico`) and Apple touch icon (`apple-touch-icon.png`).
  - The draggable Polaroid sticker in the blue hero canvas.
  - The Colophon modal (`#gilbert-modal`) opened by clicking his sticker or badge.
- **Never remove Gilbert!**

### 5. 🐞 Ladybug Precision Cursor
- Abigail's hand-drawn red ladybug (`stickers/ladybug_cursor.png`) is the universal custom mouse cursor across the entire website.
- Hotspot is configured at `5 2` (the antenna tip) so it functions seamlessly like a precision arrow pointer on all buttons, links, books, photos, and canvas stickers.

### 6. 🔒 Strict Author Attribution
- This website is **exclusively Abigail Morra's portfolio**.
- **DO NOT** add Jackson's name, email, or contact information anywhere on the site.

---

## 🛠️ How to Add New Photos or Assignments

When Abigail asks to add new photos (e.g., from a new shoot, Google Drive, or upcoming assignment):

### Step 1: Place Images
Place the optimized `.jpg` or `.png` images into a dedicated subfolder under `photos/`, for example:
- `photos/sports/photo1.jpg`
- `photos/photo_essay/shot1.jpg`

### Step 2: Update `ALL_PHOTOS` in `index.html`
In the `<script>` section of `index.html`, append the new photos to the `ALL_PHOTOS` array:
```javascript
{ src: 'photos/sports/game_01.jpg', title: 'Tip-Off at Mattamy', info: '1/1000s • f/2.8 • Tri-X 400', book: 'sports' },
```

### Step 3: Activate the Book in `BOOKS`
If this completes an upcoming book, update its entry in `BOOKS`:
```javascript
{ id: 'sports', cover: 'photos/sports/game_01.jpg', title: 'Sports Photos', isUpcoming: false },
```

### Step 4: Test & Deploy
1. Test by opening `index.html` or running `python -m http.server 8080`.
2. Commit and push directly to GitHub:
   ```bash
   git add .
   git commit -m "Add Sports Photos assignment"
   git push origin main
   ```
3. Share the live URL: `https://itsmcmurdoj.github.io/AbigailMorra/`.

---

## ⚡ Git & Deployment Commands (Windows / Universal)
The repository is pre-configured with write access to `https://github.com/itsmcmurdoj/AbigailMorra.git`.

Whenever you complete a task for Abigail:
```bash
git status
git add .
git commit -m "Update portfolio: <describe what was changed>"
git push origin main
```
*Note for Windows*: Commands can be executed in PowerShell, Command Prompt, or Git Bash. If the token ever needs updating, run `setup_github_token.bat` or update `git remote set-url origin`.

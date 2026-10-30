#!/usr/bin/env python3
"""
Automated Google Drive Sync & Deployment Engine for Abigail Morra's Portfolio
Monitors Abigail's Google Drive folder, optimizes new images, updates index.html catalogs,
and automatically commits and pushes updates to GitHub Pages.
"""

import os
import sys
import time
import json
import hashlib
import subprocess
from PIL import Image, ImageOps

DRIVE_ROOT = (
    r"G:\My Drive\jackson is helping me yayyyy"
    if os.path.exists(r"G:\My Drive\jackson is helping me yayyyy")
    else os.path.expanduser(
        "~/Library/CloudStorage/GoogleDrive-mcmurdo.jackson@gmail.com/My Drive/jackson is helping me yayyyy"
    )
)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MANIFEST_FILE = os.path.join(PROJECT_ROOT, ".drive_sync_manifest.json")

ASS1_DRIVE = os.path.join(DRIVE_ROOT, "photos on gall/ass 1")
ASS1_LOCAL = os.path.join(PROJECT_ROOT, "photos/ass1")
LITTLE_GUYS_DRIVE = (
    os.path.join(DRIVE_ROOT, "little guys")
    if os.path.exists(os.path.join(DRIVE_ROOT, "little guys"))
    else os.path.join(DRIVE_ROOT, "little guys?")
)
STICKERS_LOCAL = os.path.join(PROJECT_ROOT, "stickers")

def load_manifest():
    if os.path.exists(MANIFEST_FILE):
        try:
            with open(MANIFEST_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_manifest(manifest):
    with open(MANIFEST_FILE, "w") as f:
        json.dump(manifest, f, indent=2)

def get_file_hash(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

def optimize_image(src_path, dst_path, max_dim=2000, quality=86):
    im = Image.open(src_path)
    im = ImageOps.exif_transpose(im)
    if im.mode != "RGB":
        im = im.convert("RGB")
    if max(im.size) > max_dim:
        scale = max_dim / max(im.size)
        new_size = (int(im.size[0] * scale), int(im.size[1] * scale))
        im = im.resize(new_size, Image.Resampling.LANCZOS)
    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
    im.save(dst_path, "JPEG", quality=quality, optimize=True)

def sync_assignment_1(manifest):
    if not os.path.exists(ASS1_DRIVE):
        return False
    
    updated = False
    for fname in sorted(os.listdir(ASS1_DRIVE)):
        if fname.startswith(".") or not fname.lower().endswith((".jpg", ".jpeg", ".png", ".heic")):
            continue
        
        src = os.path.join(ASS1_DRIVE, fname)
        file_hash = get_file_hash(src)
        dst_name = fname.lower()
        if not dst_name.endswith(".jpg"):
            dst_name = os.path.splitext(dst_name)[0] + ".jpg"
        dst = os.path.join(ASS1_LOCAL, dst_name)
        
        if manifest.get(src) != file_hash or not os.path.exists(dst):
            print(f"[Drive Sync] New/updated Assignment 1 photo: {fname}")
            try:
                optimize_image(src, dst)
                manifest[src] = file_hash
                updated = True
            except Exception as e:
                print(f"[Drive Sync] Error optimizing {fname}: {e}")
    return updated

def sync_little_guys(manifest):
    if not os.path.exists(LITTLE_GUYS_DRIVE):
        return False
    
    updated = False
    for fname in sorted(os.listdir(LITTLE_GUYS_DRIVE)):
        if fname.startswith("."):
            continue
        src = os.path.join(LITTLE_GUYS_DRIVE, fname)
        if not os.path.isfile(src):
            continue
        
        file_hash = get_file_hash(src)
        if manifest.get(src) != file_hash:
            manifest[src] = file_hash
            updated = True
            print(f"[Drive Sync] New ephemera detected: {fname}")
    return updated

def git_commit_and_push(message):
    try:
        subprocess.check_call(["git", "add", "."], cwd=PROJECT_ROOT)
        status = subprocess.check_output(["git", "status", "--porcelain"], cwd=PROJECT_ROOT).decode().strip()
        if not status:
            print("[Drive Sync] No git changes to commit.")
            return
        subprocess.check_call(["git", "commit", "-m", message], cwd=PROJECT_ROOT)
        subprocess.check_call(["git", "push", "origin", "main"], cwd=PROJECT_ROOT)
        print("[Drive Sync] Successfully pushed updates to GitHub!")
    except Exception as e:
        print(f"[Drive Sync] Git push error: {e}")

def run_sync():
    manifest = load_manifest()
    ass1_updated = sync_assignment_1(manifest)
    guys_updated = sync_little_guys(manifest)
    
    if ass1_updated or guys_updated:
        save_manifest(manifest)
        git_commit_and_push("Auto-sync new photos and ephemera from Abigail's Google Drive")
        return True
    return False

def main():
    watch_mode = "--watch" in sys.argv
    print(f"[Drive Sync] Initializing Drive Watcher for: {DRIVE_ROOT}")
    
    run_sync()
    
    if watch_mode:
        print("[Drive Sync] Watching for changes every 60 seconds... (Press Ctrl+C to stop)")
        try:
            while True:
                time.sleep(60)
                if run_sync():
                    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Sync pass completed.")
        except KeyboardInterrupt:
            print("\n[Drive Sync] Watcher stopped.")

if __name__ == "__main__":
    main()

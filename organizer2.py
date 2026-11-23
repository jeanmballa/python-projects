import os
import shutil
import sys

if len(sys.argv) < 2:
    print("Usage: python organizer2.py /path/to/folder")
    sys.exit()

folder = sys.argv[1]

types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Docs": [".txt", ".pdf", ".docx", ".xlsx", ".pptx"],
    "Music": [".mp3", ".wav", ".m4a"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Archives": [".zip", ".rar", ".7z"],
    "Apps": [".apk"],
}

count = 0
for filename in os.listdir(folder):
    path = os.path.join(folder, filename)
    if not os.path.isfile(path):
        continue
    ext = os.path.splitext(filename)[1].lower()
    for category, extensions in types.items():
        if ext in extensions:
            dest = os.path.join(folder, category)
            os.makedirs(dest, exist_ok=True)
            shutil.move(path, os.path.join(dest, filename))
            count += 1
            break

print("Done. Organized", count, "files.")

import os
import shutil

folder = os.path.expanduser("~/projects/messy")

types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Docs": [".txt", ".pdf", ".docx"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv"],
}

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
            print("Moved", filename, "to", category)
            break

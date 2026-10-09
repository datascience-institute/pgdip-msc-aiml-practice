"""Build one download zip per lesson folder.

Each lesson folder gets <Lesson-folder>.zip containing every file in that folder
(notebook and datasets, subfolders included) under a single top-level folder of the
same name, so the notebook's relative data paths still work once it is unzipped.
Re-run after any change to a lesson's files, and commit the zips with it.

    python3 scripts/build_lesson_zips.py
"""
import os
import zipfile
from glob import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

for lesson in sorted(glob(os.path.join(ROOT, 'M*', 'L*', ''))):
    lesson = lesson.rstrip(os.sep)
    name = os.path.basename(lesson)
    target = os.path.join(lesson, name + '.zip')
    files = []
    for dirpath, dirnames, filenames in os.walk(lesson):
        dirnames[:] = sorted(d for d in dirnames if not d.startswith('.'))
        for f in sorted(filenames):
            path = os.path.join(dirpath, f)
            if f.startswith('.') or path == target:
                continue
            files.append(os.path.relpath(path, lesson))
    with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as zf:
        for rel in files:
            # Fixed timestamp, so an unchanged lesson rebuilds to an identical zip.
            info = zipfile.ZipInfo(f'{name}/{rel}', date_time=(2026, 10, 9, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            with open(os.path.join(lesson, rel), 'rb') as fh:
                zf.writestr(info, fh.read())
    print(f'{os.path.relpath(target, ROOT)}  ({len(files)} files)')

"""Build the download zip for each lesson.

The repo holds only one zip per lesson. The zips are built from a staging folder
outside the repo that has the same module/lesson layout and the loose student files
(the notebook and the datasets it reads):

    <staging>/M03-Mathematics-for-Computer-Science/L03-Matrix-Transpose-and-Inverse/
        M3 L03 Matrix Transpose and Inverse.ipynb
        Housing Prices.csv

Each lesson becomes <repo>/<Module>/<Lesson>/<Lesson>.zip, with every file (subfolders
included) under a single top-level folder of the lesson's name, so the notebook's
relative data paths still work once it is unzipped. Timestamps are fixed, so unchanged
files rebuild to an identical zip.

    python3 scripts/build_lesson_zips.py <staging-folder>
"""
import os
import sys
import zipfile
from glob import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if len(sys.argv) != 2:
    sys.exit(__doc__)
staging = os.path.abspath(sys.argv[1])

for lesson in sorted(glob(os.path.join(staging, 'M*', 'L*', ''))):
    lesson = lesson.rstrip(os.sep)
    module, name = os.path.basename(os.path.dirname(lesson)), os.path.basename(lesson)
    files = []
    for dirpath, dirnames, filenames in os.walk(lesson):
        dirnames[:] = sorted(d for d in dirnames if not d.startswith('.'))
        files += [os.path.relpath(os.path.join(dirpath, f), lesson)
                  for f in sorted(filenames) if not f.startswith('.') and not f.endswith('.zip')]
    out_dir = os.path.join(ROOT, module, name)
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, name + '.zip')
    with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as zf:
        for rel in files:
            info = zipfile.ZipInfo(f'{name}/{rel}', date_time=(2026, 10, 9, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            with open(os.path.join(lesson, rel), 'rb') as fh:
                zf.writestr(info, fh.read())
    print(f'{os.path.relpath(target, ROOT)}  ({len(files)} files)')

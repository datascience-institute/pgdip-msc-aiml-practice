# PG Diploma / MSc in Computer Science (AI and ML): practice files

This repository holds the student practice files for the Data Science Institute's
PG Diploma and MSc in Computer Science (AI and ML). Each lesson has one zip containing
the lesson's Jupyter notebook and the datasets it uses. Students download the zip through
the DSI platform, which links each lesson to its folder here.

## Folder naming

One folder per module, and one folder per lesson inside it, holding only the lesson zip:

```
M03-Mathematics-for-Computer-Science/
  L03-Matrix-Transpose-and-Inverse/
    L03-Matrix-Transpose-and-Inverse.zip
```

Folder names are the module and lesson titles with spaces and " - " turned into single
hyphens, and every character other than letters, digits and hyphens removed. The zip is named
after its lesson folder. Inside it, one folder of the same name holds the notebook and its
data, with their file names exactly as in the source material:

```
L03-Matrix-Transpose-and-Inverse/
  M3 L03 Matrix Transpose and Inverse.ipynb
  Housing Prices.csv
```

## Building the zips

The loose notebooks and datasets are not kept here. Copy them into a staging folder outside
the repo with the same module/lesson layout, then run:

```
python3 scripts/build_lesson_zips.py <staging-folder>
```

It writes `<Lesson>.zip` into each lesson folder. Unchanged files rebuild to an identical zip,
so only lessons whose files changed show up in `git status`.

## Rules

- **One folder per lesson, holding only that lesson's zip.**
- **Student files only in the zip.** The practice notebook and the datasets it reads. No
  decks, PDFs, Word documents, images, answer keys, drafts or old versions.
- **HTML exports go in Sanity, not here.** `*.html` is ignored by `.gitignore`.
- **Notebooks read data with relative paths.** In the zip, a data file sits next to its
  notebook, or in a `datasets/` subfolder if the notebook reads `datasets/<file>`.
- **Datasets under 50 MB each.** Git LFS is not used in this repository.
- **Don't rename or move a lesson folder once it is linked in Sanity.** The platform finds the
  zip from the lesson folder's path, so a rename breaks the download for students.

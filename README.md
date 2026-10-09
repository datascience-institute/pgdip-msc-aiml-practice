# PG Diploma / MSc in Computer Science (AI and ML): practice files

This repository holds the student practice files for the Data Science Institute's
PG Diploma and MSc in Computer Science (AI and ML): the Jupyter notebooks for each
lesson and the datasets they use. Students download these files through the DSI
platform, where each lesson links to its folder here.

## Folder naming

One folder per module, and one folder per lesson inside it:

```
M03-Mathematics-for-Computer-Science/
  L03-Matrix-Transpose-and-Inverse/
    M3 L03 Matrix Transpose and Inverse.ipynb
    Housing Prices.csv
    L03-Matrix-Transpose-and-Inverse.zip
```

Each lesson folder also holds a zip of the whole folder (notebook plus datasets), named after
the folder, so students download one file. Unzipped, it gives a folder with the notebook and
its data side by side, ready to run.

Folder names are the module and lesson titles with spaces and " - " turned into single
hyphens, and every character other than letters, digits and hyphens removed. Notebook and
data file names are kept exactly as they are in the source material.

## Rules

- **One folder per lesson.** A lesson's notebook and its data live together in its folder.
- **Student files only.** Practice notebooks and the datasets they read. No decks, PDFs,
  Word documents, images, answer keys, drafts or old versions.
- **HTML exports go in Sanity, not here.** `*.html` is ignored by `.gitignore`.
- **Notebooks read data with relative paths.** A data file sits next to its notebook, or in
  a `datasets/` subfolder if the notebook reads `datasets/<file>`.
- **Rebuild the lesson zips after any change.** Run `python3 scripts/build_lesson_zips.py`
  and commit the zips with the change, so the download always matches the folder.
- **Datasets under 50 MB each.** Git LFS is not used in this repository.
- **Don't rename or move a lesson folder once it is linked in Sanity.** The platform links to
  each lesson folder by its path, so a rename breaks the link for students.

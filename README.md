# ChBE 413 — Data Science in Chemical Engineering

This repository contains homework and project work for **ChBE 413**.  
It follows workflow using Conda/Mamba environments, Jupyter notebooks, and VS Code.

## Setup Instructions

1. Clone the repo:
   git clone https://github.com/mikkelflores-eng/ChBE_413.git
   cd ChBE_413

2. Create environment:
   conda env create -f environment.yml
   conda activate chbe-413

3. Register Jupyter kernel (first time only):
   python -m ipykernel install --user --name chbe-413 --display-name "Python 3.11 (chbe-413)"

4. Open in VS Code:
   code .
   - Open a notebook under hw/ or project/
   - Select kernel "Python 3.11 (chbe-413)"
   - Run cells

## Repo Structure
ChBE_413/
│── hw/           # Homework assignments
│   └── hw01/
│── project/      # Final project work
│── env/          # Environment configs
│── environment.yml
│── README.md
│── .gitignore

## Notes
- Use relative paths for data (Path.cwd() / 'data/file.csv').
- Large raw datasets are ignored by Git (.gitignore).
- Repo is synced with GitHub for version control and reproducibility.


# ChBE 413 — Data Science for Chem/ChBE (Fall 2025)
**Author:** Mikkel Flores  
**Repo purpose:** Coursework repository for weekly homeworks and the final project, built with a professional workflow (VS Code + Conda/Mamba + GitHub).

## Structure
- `hw/hwNN/` — each homework’s notebook + small local data; PDF exports in `reports/`
- `project/` — final project (`notebooks/`, `src/` helpers, `data/`, `reports/`)
- `env/` — local-only things (ignored by git)
- `.vscode/` — editor recommendations

## Environment
Create once (fast with mamba, safe via conda-forge):
```bash
mamba create -n chbe-413 -c conda-forge python=3.11   numpy pandas matplotlib seaborn scikit-learn tensorflow keras rdkit ipykernel jupyterlab
conda activate chbe-413
python -m ipykernel install --user --name chbe-413 --display-name "Python 3.11 (chbe-413)"
```

Export spec after changes:
```bash
mamba env export -n chbe-413 > environment.yml
```

## Run
1. Open the folder in VS Code.
2. Open a notebook (e.g., `hw/hw01/hw01.ipynb`) and select the `Python 3.11 (chbe-413)` kernel.
3. **Restart & Run All** before export.

## Submission
- Export **HTML → PDF** (most robust). Keep PDFs in `hw/hwNN/reports/`.
- Submit `.ipynb` + PDF to Canvas.

## Notes
This repository is **work in progress** for ChBE 413 (Fall 2025). It is intentionally public/structured to serve as a portfolio.

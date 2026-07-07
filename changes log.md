# Changes Log

## 2026-07-06

- Converted `backend/ml/notebooks/BhramGuard.ipynb` from Google Colab paths to local project paths under `backend/ml/datasets` and `backend/ml/models`.
- Added local dataset download/conversion support for the Hugging Face phishing datasets, including `urls.csv` and `webs.csv`.
- Added direct backend requirements for the local ML notebook and dataset downloader dependencies.
- Split model-development work into separate notebook tracks for text, URL, and web phishing models, each with a baseline training workflow.

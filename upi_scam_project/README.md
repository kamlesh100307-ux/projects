# UPI Scam Detection System — Student Project

**Project title chosen:** UPI Scam Detection System

## Description
Student-level Flask app + RandomForest model that predicts suspicious UPI transactions using synthetic data.

## Features included
- Synthetic dataset generator (data/generate_dataset.py)
- Model training (train_model.py) -> saves model.pkl
- Flask app (app.py) with HTML/CSS/JS frontend
- Result page shows probability (you chose probability display) and top features
- Demo screenshot included in static/img/screenshot.png (or uses absolute path fallback)

## How to run locally
1. Create venv and install:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Generate dataset:
   ```bash
   python data/generate_dataset.py
   ```

3. Train model:
   ```bash
   python train_model.py
   ```
   This creates `model.pkl`.

4. Run the app:
   ```bash
   python app.py
   ```
   Open http://127.0.0.1:5000

## Notes for interviews
- Explain dataset features: amount, transaction hour, sender bank, account age, txn type, recipient-in-contacts.
- Mention model choice: RandomForest for explainability. Show feature importances.
- Discuss limitations: synthetic labels, privacy considerations, need for real logs and robust monitoring.

## Files
- app.py, train_model.py, data/generate_dataset.py, templates/, static/, model.pkl (created after training)

## Screenshot path used in the demo:
- Absolute fallback: /mnt/data/40208161-59d1-437b-b93f-18c36abb5873.png
- Repo static path: static/img/screenshot.png


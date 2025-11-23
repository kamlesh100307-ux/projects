# app.py
from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)
MODEL_PATH = 'model.pkl'
if not os.path.exists(MODEL_PATH):
    raise RuntimeError('model.pkl not found. Run train_model.py first.')

saved = joblib.load(MODEL_PATH)
model = saved['model']
columns = saved['columns']

# prefer static image if present, otherwise use absolute path from environment
STATIC_SCREEN = os.path.join('static','img','screenshot.png')
FALLBACK_SCREEN = '/mnt/data/40208161-59d1-437b-b93f-18c36abb5873.png'

def preprocess_input(form):
    # Map fields in order matching training columns
    try:
        amount = float(form.get('amount',0))
    except:
        amount = 0.0
    try:
        hour = int(form.get('hour',0))
    except:
        hour = 0
    sender_bank = form.get('sender_bank','OTHER')
    try:
        account_age_days = int(form.get('account_age_days',365))
    except:
        account_age_days = 365
    txn_type = form.get('txn_type','send')
    try:
        recipient_in_contacts = int(form.get('recipient_in_contacts',0))
    except:
        recipient_in_contacts = 0

    # Create a feature vector consistent with training columns (one-hot)
    base = {
        'amount': amount,
        'hour': hour,
        'account_age_days': account_age_days,
        'recipient_in_contacts': recipient_in_contacts
    }
    # add sender_bank_* and txn_type_* columns default 0
    for c in columns:
        if c not in base:
            base[c] = 0

    # set categorical encodings
    bank_col = f'sender_bank_{sender_bank}'
    if bank_col in base:
        base[bank_col] = 1
    type_col = f'txn_type_{txn_type}'
    if type_col in base:
        base[type_col] = 1

    # order according to columns
    x = [base[c] for c in columns]
    return np.array(x).reshape(1,-1)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        features = preprocess_input(request.form)
        prob = float(model.predict_proba(features)[0,1])
        pred = int(model.predict(features)[0])
        importances = sorted(zip(columns, model.feature_importances_), key=lambda x: x[1], reverse=True)[:6]
        # choose screenshot path
        screenshot = STATIC_SCREEN if os.path.exists(STATIC_SCREEN) else FALLBACK_SCREEN
        return render_template('result.html', prob=round(prob,3), pred=pred, top_imp=importances, form=request.form, screenshot_path=screenshot)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

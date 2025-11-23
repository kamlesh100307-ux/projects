# data/generate_dataset.py
import numpy as np
import pandas as pd
import random
random.seed(42)
np.random.seed(42)

def synth_transaction(n=6000):
    rows = []
    sender_banks = ['HDFC','SBI','ICICI','AXIS','OTHER']
    txn_types = ['send','request','qr','collect']
    for i in range(n):
        amount = round(abs(np.random.normal(loc=1500, scale=2500)),2)  # A
        hour = np.random.randint(0,24)  # B
        sender_bank = random.choice(sender_banks)  # C
        account_age_days = max(1, int(abs(np.random.normal(900, 700))))  # J
        txn_type = random.choice(txn_types)  # K
        recipient_in_contacts = np.random.choice([0,1], p=[0.7,0.3])  # F

        # heuristic risk scoring
        risk = 0
        if amount > 10000: risk += 1
        if amount > 50000: risk += 1
        if recipient_in_contacts==0: risk += 1
        if account_age_days < 60: risk += 1
        if hour < 6 or hour > 23: risk += 1
        if sender_bank == 'OTHER': risk += 1
        if txn_type in ['request']: risk += 1

        label = 1 if risk >= 2 else 0

        rows.append({
            'amount': amount,
            'hour': hour,
            'sender_bank': sender_bank,
            'account_age_days': account_age_days,
            'txn_type': txn_type,
            'recipient_in_contacts': recipient_in_contacts,
            'label': label
        })
    df = pd.DataFrame(rows)
    # one-hot encode categorical for model training convenience
    df = pd.get_dummies(df, columns=['sender_bank','txn_type'])
    return df

if __name__ == '__main__':
    df = synth_transaction(8000)
    df.to_csv('data/synthetic_upi_transactions.csv', index=False)
    print('Saved data/synthetic_upi_transactions.csv rows=', len(df))

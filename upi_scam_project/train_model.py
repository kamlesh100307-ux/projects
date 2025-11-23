# train_model.py
import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score
from joblib import dump
import numpy as np

csv_path = 'data/synthetic_upi_transactions.csv'
if not os.path.exists(csv_path):
    print('Dataset not found. Run data/generate_dataset.py first to generate it.')
    raise SystemExit

df = pd.read_csv(csv_path)
if 'label' not in df.columns:
    raise SystemExit('Label column missing')

X = df.drop(columns=['label'])
y = df['label']

# preserve column names
columns = list(X.columns)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

clf = RandomForestClassifier(n_estimators=150, random_state=42, max_depth=10)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
y_prob = clf.predict_proba(X_test)[:,1]

print('Classification Report:')
print(classification_report(y_test, y_pred))
print('ROC-AUC:', roc_auc_score(y_test, y_prob))

dump({'model': clf, 'columns': columns}, 'model.pkl')
print('Saved model.pkl with columns:', columns)

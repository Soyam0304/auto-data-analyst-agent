import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import accuracy_score, mean_squared_error

# Detect if task is classification or regression
def detect_task(df, target):
    if df[target].dtype == 'object' or len(df[target].unique()) < 10:
        return 'classification'
    else:
        return 'regression'

# Train a simple model
def train_model(df, target):
    X = df.drop(columns=[target])
    y = df[target]
    X = pd.get_dummies(X, drop_first=True)
    task = detect_task(df, target)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    if task == 'classification':
        model = LogisticRegression(max_iter=200)
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        score = accuracy_score(y_test, preds)
    else:
        model = LinearRegression()
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        score = mean_squared_error(y_test, preds, squared=False)
    return model, score, task 
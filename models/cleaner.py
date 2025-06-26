import pandas as pd

# Suggest how to handle missing values
def suggest_missing_value_handling(df):
    suggestions = {}
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            if df[col].dtype == 'object':
                suggestions[col] = 'Fill with mode or drop rows.'
            else:
                suggestions[col] = 'Fill with mean/median or drop rows.'
    return suggestions

# Suggest how to handle outliers
def suggest_outlier_handling(df):
    suggestions = {}
    for col in df.select_dtypes(include='number').columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        outliers = ((df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR))).sum()
        if outliers > 0:
            suggestions[col] = 'Remove or cap outliers using IQR.'
    return suggestions

# Generate Python code for cleaning
def generate_cleaning_code(df):
    code_lines = []
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            if df[col].dtype == 'object':
                code_lines.append(f"df['{col}'] = df['{col}'].fillna(df['{col}'].mode()[0])")
            else:
                code_lines.append(f"df['{col}'] = df['{col}'].fillna(df['{col}'].median())")
    return '\n'.join(code_lines) 
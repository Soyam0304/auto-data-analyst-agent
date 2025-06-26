import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Dataset overview: columns, types, missing values
def dataset_overview(df):
    overview = {
        'columns': df.columns.tolist(),
        'dtypes': df.dtypes.astype(str).to_dict(),
        'missing': df.isnull().sum().to_dict(),
        'shape': df.shape
    }
    return overview

# Summary statistics
def summary_stats(df):
    return df.describe(include='all').T

# Plot histograms for all numeric columns
def plot_histograms(df):
    figs = {}
    for col in df.select_dtypes(include='number').columns:
        fig = px.histogram(df, x=col, title=f'Histogram of {col}')
        figs[col] = fig
    return figs

# Correlation heatmap
def plot_corr_heatmap(df):
    corr = df.corr(numeric_only=True)
    fig = px.imshow(corr, text_auto=True, title='Correlation Heatmap')
    return fig

# Boxplots for numeric columns
def plot_boxplots(df):
    figs = {}
    for col in df.select_dtypes(include='number').columns:
        fig = px.box(df, y=col, title=f'Boxplot of {col}')
        figs[col] = fig
    return figs

# Outlier detection using IQR
def detect_outliers(df):
    outliers = {}
    for col in df.select_dtypes(include='number').columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        mask = (df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR))
        outliers[col] = df[mask][col].tolist()
    return outliers 
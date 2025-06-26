import streamlit as st
import pandas as pd
from models import eda, cleaner, modeler, planner
from jinja2 import Template
import tempfile
import os

st.set_page_config(page_title='AutoData Analyst Agent', layout='wide')
st.title('AutoData Analyst Agent')

st.sidebar.header('Upload CSV File')
uploaded_file = st.sidebar.file_uploader('Choose a CSV file', type='csv')

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success('File uploaded!')
    with st.expander('Dataset Overview'):
        overview = eda.dataset_overview(df)
        st.json(overview)
        st.write('Summary Stats:')
        st.dataframe(eda.summary_stats(df))
    with st.expander('Visual EDA'):
        st.write('Histograms:')
        for col, fig in eda.plot_histograms(df).items():
            st.plotly_chart(fig, use_container_width=True)
        st.write('Correlation Heatmap:')
        st.plotly_chart(eda.plot_corr_heatmap(df), use_container_width=True)
        st.write('Boxplots:')
        for col, fig in eda.plot_boxplots(df).items():
            st.plotly_chart(fig, use_container_width=True)
    with st.expander('Outlier Detection'):
        outliers = eda.detect_outliers(df)
        st.json(outliers)
    with st.expander('Data Cleaning Suggestions'):
        st.write('Missing Value Handling:')
        st.json(cleaner.suggest_missing_value_handling(df))
        st.write('Outlier Handling:')
        st.json(cleaner.suggest_outlier_handling(df))
        st.write('Python Cleaning Code:')
        st.code(cleaner.generate_cleaning_code(df), language='python')
    with st.expander('LLM Agent Plan'):
        schema = eda.dataset_overview(df)
        plan = planner.plan_analysis(schema)
        st.write(plan)
    if st.checkbox('Train Model (if target column exists)?'):
        target = st.selectbox('Select target column:', df.columns)
        model, score, task = modeler.train_model(df, target)
        st.write(f'Model type: {task}')
        st.write(f'Score: {score}')
    if st.button('Generate Report'):
        with tempfile.NamedTemporaryFile(delete=False, suffix='.html') as tmp:
            template = Template(open('report_template.html').read())
            html = template.render(
                overview=overview,
                summary=eda.summary_stats(df).to_html(),
                outliers=outliers,
                cleaning=cleaner.suggest_missing_value_handling(df),
                plan=plan
            )
            tmp.write(html.encode('utf-8'))
            st.success('Report generated!')
            st.download_button('Download Report', data=html, file_name='report.html', mime='text/html')
else:
    st.info('Please upload a CSV file to get started.') 
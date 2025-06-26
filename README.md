# AutoData Analyst Agent

This is a simple tool that helps you analyze any CSV dataset automatically. Just upload your data and get:

- Dataset overview (columns, types, missing values)
- Data cleaning suggestions (with Python code)
- Visual EDA (histograms, heatmaps, boxplots, outliers)
- Feature engineering suggestions
- (Optional) Model training (classification/regression)
- Downloadable report (HTML)

## Features
- Easy file upload in sidebar
- Interactive plots (Plotly)
- LLM agent plans and justifies steps
- Cleaning code suggestions
- Simple model training if you want
- Download a report with all results

## How to Run
1. Clone this repo
2. Install requirements: `pip install -r requirements.txt`
3. Add your API key to a `.env` file:
   - `GROQ_API_KEY=your_key` or `OPENAI_API_KEY=your_key`
4. Run: `streamlit run app.py`

## File Structure
- `app.py` - Main Streamlit app
- `eda.py` - EDA functions (overview, plots, outliers)
- `cleaner.py` - Data cleaning suggestions
- `modeler.py` - Model training
- `planner.py` - LLM agent planner
- `report_template.html` - Jinja2 report template
- `README.md` - This file

## Notes
- Works with real-world messy data
- Needs a Groq or OpenAI API key for LLM features
- Code is simple and easy to read (like a student wrote it) 
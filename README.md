# IBM Data Science Capstone: SpaceX Falcon 9 First-Stage Landing Prediction

**Goal:** Predict whether a Falcon 9 first stage will land successfully. Reuse drives launch cost (about $62M for SpaceX vs $165M+ for competitors).

## Notebooks
| # | Notebook | Purpose |
|---|----------|---------|
| 01 | `notebooks/01-spacex-data-collection-api.ipynb` | Collect launch data from the SpaceX REST API |
| 02 | `notebooks/02-webscraping.ipynb` | Scrape Falcon 9 launch tables from Wikipedia |
| 03 | `notebooks/03-data-wrangling.ipynb` | Clean data and create the landing `Class` label |
| 04 | `notebooks/04-eda-sql.ipynb` | EDA with SQL (SQLite) |
| 05 | `notebooks/05-eda-dataviz.ipynb` | EDA with Matplotlib/Seaborn, feature engineering |
| 06 | `notebooks/06-folium-launch-sites.ipynb` | Folium map: sites, outcomes, proximity |
| 07 | `notebooks/07-predictive-analysis.ipynb` | Logistic Regression, SVM, Decision Tree, KNN |

Dash app: `dash/spacex_dash_app.py` (run with `python spacex_dash_app.py`).

## Results
Fill in after running the notebooks: best model, accuracy, confusion matrix, key insights.

## Tools
Python, Pandas, NumPy, SQL/SQLite, Matplotlib, Seaborn, Folium, Plotly Dash, scikit-learn.

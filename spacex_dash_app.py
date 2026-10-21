import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv"
spacex_df = pd.read_csv(URL)
min_p, max_p = spacex_df["Payload Mass (kg)"].min(), spacex_df["Payload Mass (kg)"].max()

app = Dash(__name__)
sites = [{"label": "All Sites", "value": "ALL"}] + [
    {"label": s, "value": s} for s in spacex_df["Launch Site"].unique()]

app.layout = html.Div([
    html.H1("SpaceX Launch Records Dashboard", style={"textAlign": "center"}),
    dcc.Dropdown(id="site-dropdown", options=sites, value="ALL",
                 placeholder="Select a Launch Site", searchable=True),
    html.Br(),
    dcc.Graph(id="success-pie-chart"),
    html.P("Payload range (kg):"),
    dcc.RangeSlider(id="payload-slider", min=0, max=10000, step=1000,
                    marks={i: str(i) for i in range(0, 10001, 2500)}, value=[min_p, max_p]),
    dcc.Graph(id="success-payload-scatter-chart"),
])

@app.callback(Output("success-pie-chart", "figure"), Input("site-dropdown", "value"))
def pie(site):
    if site == "ALL":
        return px.pie(spacex_df, values="class", names="Launch Site", title="Total Successful Launches by Site")
    d = spacex_df[spacex_df["Launch Site"] == site]["class"].value_counts().reset_index()
    d.columns = ["class", "count"]
    return px.pie(d, values="count", names="class", title=f"Success vs Failure for {site}")

@app.callback(Output("success-payload-scatter-chart", "figure"),
              [Input("site-dropdown", "value"), Input("payload-slider", "value")])
def scatter(site, rng):
    d = spacex_df[spacex_df["Payload Mass (kg)"].between(rng[0], rng[1])]
    if site != "ALL":
        d = d[d["Launch Site"] == site]
    return px.scatter(d, x="Payload Mass (kg)", y="class", color="Booster Version Category",
                      title="Payload vs Launch Outcome")

if __name__ == "__main__":
    app.run(debug=True)

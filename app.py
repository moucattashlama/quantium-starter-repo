import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load the cleaned data
df = pd.read_csv("data/cleaned_data.csv")
df['Date'] = pd.to_datetime(df['Date'])  # Ensure Date is datetime

# Initialize the Dash app
app = Dash(__name__)
app.title = "Pink Morsel Visualizer"

# Layout
app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualizer", style={"textAlign": "center", "color": "#d63384"}),

    html.H3("Filter by Region:", style={"textAlign": "center"}),

    dcc.RadioItems(
        id="region-filter",
        options=[
            {"label": "All", "value": "all"},
            {"label": "North", "value": "north"},
            {"label": "East", "value": "east"},
            {"label": "South", "value": "south"},
            {"label": "West", "value": "west"},
        ],
        value="all",
        inline=True,
        style={"textAlign": "center", "marginBottom": "20px"}
    ),

    dcc.Graph(id="sales-chart")
], style={"backgroundColor": "#f8f9fa", "padding": "20px"})

# Callback to update the chart
@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(region):
    if region == "all":
        filtered_df = df.copy()
    else:
        filtered_df = df[df["Region"] == region]

    daily_sales = filtered_df.groupby("Date")["Sales"].sum().reset_index()

    fig = px.line(
        daily_sales,
        x="Date",
        y="Sales",
        title="Daily Sales of Pink Morsels",
        labels={"Sales": "Sales ($)", "Date": "Date"}
    )
    fig.update_layout(
        plot_bgcolor="#ffffff",
        paper_bgcolor="#f8f9fa",
        title_font=dict(size=24, color="#d63384", family="Arial"),
        font=dict(family="Arial", size=14)
    )
    return fig

# Run the app
if __name__ == "__main__":
    app.run(debug=True)

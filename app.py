import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load the cleaned sales data
df = pd.read_csv("data/cleaned_data.csv")

# Ensure date is in datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Group sales by date (all regions combined)
daily_sales = df.groupby('Date')['Sales'].sum().reset_index()

# Create a line chart
fig = px.line(daily_sales, x='Date', y='Sales', title='Total Daily Sales of Pink Morsels')
fig.update_layout(
    xaxis_title='Date',
    yaxis_title='Sales ($)',
    title_x=0.5
)

# Initialize the Dash app
app = dash.Dash(__name__)

# Layout with header and graph
app.layout = html.Div(children=[
    html.H1('Pink Morsel Sales Over Time', style={'textAlign': 'center'}),
    dcc.Graph(figure=fig),
    html.P("Vertical line = price increase on Jan 15, 2021", style={'textAlign': 'center'})
])

# Run app
if __name__ == '__main__':
    app.run(debug=True)         


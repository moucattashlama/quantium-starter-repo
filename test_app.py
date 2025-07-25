from app import app
from dash import html, dcc

def test_layout_has_header():
    layout = app.layout
    found = any(isinstance(child, html.H1) for child in layout.children)
    assert found, "Header (H1) not found in layout"

def test_layout_has_graph():
    layout = app.layout
    found = any(isinstance(child, dcc.Graph) for child in layout.children)
    assert found, "Graph not found in layout"

def test_layout_has_radio():
    layout = app.layout
    found = any(isinstance(child, dcc.RadioItems) for child in layout.children)
    assert found, "RadioItems (region picker) not found in layout"

#!/usr/bin/env python3
"""A Flask app.
"""
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def get_index() -> str:
    """The home page.
    """
    return render_template('0-index.html')


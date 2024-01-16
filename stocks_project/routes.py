from flask import render_template
from stocks_project import app, database
from stocks_project.database import df

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/stocks')
def next_games():
    return render_template('stocks.html', dataframe=df)
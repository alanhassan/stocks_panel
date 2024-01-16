from flask import render_template, url_for
from stocks_project import app, database
from stocks_project.database import df

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/stocks')
def stocks():
    return render_template('stocks.html', dataframe=df)
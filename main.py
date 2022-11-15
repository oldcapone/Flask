from pprint import pprint
from pickle import dump, load
from os.path import exists
import re
from collections import Counter
from json import dump as jdump

from requests import get
from pycbrf import ExchangeRates

from sqlite3 import connect
from flask import Flask, render_template, request
from hh_json import parce
from crud import add_row

app = Flask(__name__)

@app.get('/index')
@app.get('/')
def index():
    return render_template('index.html')

@app.route('/contacts/')
def contact():
    developer_name = 'Игорь Иванов'
    return render_template('contact.html', name=developer_name, creation_date='16.01.2020')

@app.route('/form/')
def form():
    return render_template('form.html')

@app.post('/result/')
def result():
    """
    Вычисление проекта и вывод страницы результатов
    :return: шаблон с результатами
    """
    vac = request.form
    data = parce(**vac)
    dat = {**data, **vac}
    print(dat)
    dat['where'] = 'в названии вакансии' \
        if dat['where'] == 'name' else 'в названии компании' if dat['where'] == 'company' else 'везде'
    add_row(dat)
    return render_template('about.html', res=dat)

if __name__ == "__main__":
    app.run(debug=True)
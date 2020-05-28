from app import app
from flask import render_template
from flask_bootstrap import Bootstrap


bootstrap = Bootstrap(app)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='О Компании')


@app.route('/researches')
def researches():
    return render_template('researches.html', title='Геолого-технологические исследования')


@app.route('/service')
def service():
    return render_template('service.html', title='Телеметрическое сопровождение')


@app.route('/billboard')
def billboard():
    return render_template('billboard.html', title='Доска информации')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html', title='Контакты')
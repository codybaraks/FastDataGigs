from flask import Flask, render_template, redirect, request, sessions, url_for, flash
import mysql.connector as connector
from validation import *

db = connector.connect(host="localhost", user="root", passwd="root", database="waweru")
app = Flask(__name__, template_folder='templates')
app.secret_key = "fsggrsgsrgrg"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/house')
def house():
    return render_template('index.html')


@app.route('/data', methods=['POST', 'GET'])
def data():
    form = ContactForm()
    if form.validate_on_submit():
        if request.method == 'POST':
            name = request.form["name"]
            email = request.form["email"]
            phone = request.form["phone"]
            organization = request.form["organization"]
            title = request.form["title"]
            description = request.form["description"]

            print(name, email, phone, organization, title, description)
            cursor = db.cursor()
            sql = "INSERT INTO `users`(`name`, `email`, `phone`, `organization`, `title`, `description`) VALUES (%s,%s,%s,%s,%s,%s)"
            val = (name, email, phone, organization, title, description)
            cursor.execute(sql, val)
            db.commit()
            flash("saved in database")

    return render_template('formA.html', form=form)


@app.route('/userdata', methods=['POST', 'GET'])
def userdata():
    form = UserForm()
    if form.validate_on_submit():
        if request.method == 'POST':
            name = request.form["name"]
            email = request.form["email"]
            gender = request.form["gender"]
            title = request.form["title"]
            description = request.form["description"]

            print(name, email, gender, title, description)
            cursor = db.cursor()
            sql = "INSERT INTO `userdata`(`name`, `email`, `gender`, `title`, `description`)  VALUES (%s,%s,%s,%s,%s)"
            val = (name, email, gender, title, description)
            cursor.execute(sql, val)
            db.commit()
            flash("saved in database")
    return render_template('Customer_info.html', form=form)


if __name__ == '__main__':
    app.run()

from wsgiref.validate import validator
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField("Cafe Name", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add')
def add_cafe():
    form = FlaskForm()
    if form.validate_on_submit():
        print("True")

    return render_template("add.html", form=form)


@app.route('/cafes')
def cafes():
    pass



if __name__ == '__main__':
    app.run(debug=True)

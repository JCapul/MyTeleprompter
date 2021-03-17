# encoding: utf-8
from flask import Flask, render_template, flash, request
from wtforms import Form, TextAreaField, validators
from flask_misaka import Misaka, markdown

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
Misaka(app)

class ReusableForm(Form):
    text = TextAreaField('Text:', validators=[validators.required()])

    @app.route("/", methods=['GET', 'POST'])
    def main():
        form = ReusableForm(request.form)

        if request.method == 'POST':
            text = request.form['text']
		    
            if form.validate():
                return render_template("prompt.html", text=markdown(text))

        return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run()

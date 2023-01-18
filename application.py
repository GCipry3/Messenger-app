from flask import Flask, render_template, request, redirect, url_for, session
from wtform_fields import *

app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route('/', methods=['GET', 'POST'])
def index():
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data
        return redirect(url_for('index'))

    return render_template('index.html',form = reg_form)


if __name__ == '__main__':
    app.run(debug=True,port=5000)
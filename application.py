from flask import Flask, render_template, request, redirect, url_for, session , flash
from wtform_fields import *
from models import *

# Configure app
app = Flask(__name__)
app.secret_key = 'super secret key'


# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://GCipry3:RsjHGvmh40DM@ep-square-math-535766.eu-central-1.aws.neon.tech/neondb'
db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        # Check username
        user_object = User.query.filter_by(username=username).first()
        if user_object:
            flash('This username is already taken.')
            return redirect(url_for('index'))
        
        # Add user to database
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        
        flash('You have successfully registered.')
        return redirect(url_for('index'))

    return render_template('index.html',form = reg_form)


if __name__ == '__main__':
    app.run(debug=True,port=5000)
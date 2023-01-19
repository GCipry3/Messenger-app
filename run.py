from flask import Flask, render_template, request, redirect, url_for, session , flash
from wtform_fields import *
from models import *
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, current_user, logout_user, login_required

# Configure app
app = Flask(__name__)
app.secret_key = 'super secret key'


# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://GCipry3:RsjHGvmh40DM@ep-square-math-535766.eu-central-1.aws.neon.tech/neondb'
db = SQLAlchemy(app)


# Configure bcrypt
bcrypt = Bcrypt(app)


# Login manager
login_manager = LoginManager()
login_manager.login_view = 'login'


@app.route('/', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('chat'))

    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        # Hash password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Add user to database
        user = User(username=username, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        flash(f'You have successfully registered.','success')
        return redirect(url_for('login'))

    return render_template('index.html',form = reg_form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        user_object = User.query.filter_by(username=login_form.username.data).first()
        
        if user_object and bcrypt.check_password_hash(user_object.password, login_form.password.data):
            flash('Logged in successfully.', 'success')
            return redirect(url_for('chat'))

        flash('Invalid username or password.', 'danger')
        return redirect(url_for('login'))
    
    return render_template('login.html', form=login_form)



@app.route('/chat', methods=['GET', 'POST'])
def chat():
    return "Chat"

if __name__ == '__main__':
    app.run(debug=True,port=5000)
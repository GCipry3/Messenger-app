from time import localtime, strftime
from flask import Flask, render_template, request, redirect, url_for, session , flash
from wtform_fields import *
from models import *
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from flask_socketio import SocketIO, send, emit, join_room, leave_room


# Configure application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://GCipry3:RsjHGvmh40DM@ep-square-math-535766.eu-central-1.aws.neon.tech/neondb'
app.config['SECRET_KEY'] = 'super secret key' 

# Configure socketio
socketio = SocketIO(app)
ROOMS = ["global", "games", "coding", "random"]

# Configure bcrypt
bcrypt = Bcrypt(app)

# Configure database
db = SQLAlchemy(app)

# Configure login manager
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('chat'))

    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        # Hash password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Add user to database
        user = User(username=username, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        flash(f'You have successfully registered.','success')
        return redirect(url_for('login'))

    return render_template('index.html',form = form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('chat'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        check_password = bcrypt.check_password_hash(user.password, form.password.data)
        
        if user and check_password:
            flash('Logged in successfully.', 'success')
            login_user(user)
            return redirect(url_for('chat'))

        flash('Invalid username or password.', 'danger')
        return redirect(url_for('login'))
    
    return render_template('login.html', form=form)



@app.route('/chat', methods=['GET', 'POST'])
@login_required
def chat():
    return render_template('chat.html',username=current_user.username, 
                           rooms=ROOMS)


@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))


@socketio.on('message')
def message(data):
    print(f"\n\n{data}\n\n")
    send({
            'msg':data['msg'],
            'username':data['username'],
            'time_stamp':strftime('%b-%d %I:%M%p', localtime()),
        }, 
        room=data['room']
    )


@socketio.on('join')
def join(data):
    join_room(data['room'])
    send(
        {'msg':data['username'] + " has joined the " + data['room'] + " room."},
        room=data['room']
    )
    
@socketio.on('leave')
def leave(data):
    leave_room(data['room'])
    send(
        {'msg':data['username'] + " has left the " + data['room'] + " room."},
        room=data['room']
    )
    


if __name__ == '__main__':
    socketio.run(app=app, debug=True,port=5001)
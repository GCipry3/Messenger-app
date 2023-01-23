
# Messenger-App

The project is a __web-based__ blog application built using the Flask web framework and Flask-SQLAlchemy extension. 

The __backend__ of the application is powered by Flask and Flask-SQLAlchemy, which handle the server-side logic and database interactions respectively. 

Additionally, the application uses __Socket.io__ to handle __real-time communication between users__. ,
and it connects to a postgresql database from __neon.tech__ .

The __frontend__ of the application is built using HTML, CSS, and Bootstrap, which provide the layout and styling for the website. 

![Chat](https://github.com/GCipry3/Messenger-app/blob/main/docs/Chat.png)




## Documentation

The application is a website that helps people talk to each other in different chat rooms. 
To use it, people need to make an account and log in. It works by using two special tools called Flask and Flask-SQLAlchemy, which help the website run smoothly and manage the information it gets from users. 
It also uses a tool called Socket.io to make sure the chats happen in real-time. 
Lastly, it connects to a database from neon.tech to save user information.

![Chats](https://github.com/GCipry3/Messenger-app/blob/main/docs/Chats.png)


## Run Locally

Clone the project

```bash
  git clone git@github.com:GCipry3/Messenger-app.git
```

Go to the project directory

```bash
  cd Messenger-app
```

Install dependencies

* Install python3 , python3 virtual environment module and pip
```bash
  sudo apt install python3 python3-venv python3-pip python3-dev libpq-dev
```

* Create the virtual environment
```bash
  python3 -m venv .venv
```

* Activate the virtual environment to separate all the necessary dependencies from the computer
```bash
  source .venv/bin/activate
```

* Install the dependencies into the venv
```bash
  pip install -r requirements.txt
```

Start the server

```bash
  export FLASK_APP=run  
```

```bash
  flask run
```

Open the application

* Access the localhost on port 5000 through your browser
```http
  http://localhost:5000/
```



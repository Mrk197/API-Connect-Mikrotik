from flask import Flask
from flask import render_template
from flask import request, redirect, url_for
from routes.auth import routes_auth
from routes.users_github import users_github
from routes.get_data import get_data
from routes.set_config import set_config
from dotenv import load_dotenv
from routes.sendPing import send_ping
from routes.reparar_router import reparar_router

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


app.register_blueprint(routes_auth, url_prefix="/api")
app.register_blueprint(users_github, url_prefix="/api")
app.register_blueprint(get_data, url_prefix="/api")
app.register_blueprint(set_config, url_prefix="/api")
app.register_blueprint(send_ping, url_prefix="/api")
app.register_blueprint(reparar_router, url_prefix="/api")


if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True, port="4000", host="0.0.0.0") #servidor local

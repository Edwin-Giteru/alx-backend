from flask import Flask, request, render_template, g
from flask_babel import Babel

class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user():
    if request.args.get('login_as'):
        login_id = int(request.args.get('login_as'))
        if login_id in users:
            return users.get(login_id)
    return None

@app.before_request
def before_request():
    g.user = get_user()

def get_locale():
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale  
    return request.accept_languages.best_match(app.config["LANGUAGES"])

babel.init_app(app, locale_selector=get_locale)
@app.route("/")
def index():
    return render_template("3-index.html")

if __name__ == "__main__":
    app.run(debug=True)

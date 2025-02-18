from flask import Flask, request, render_template
from flask_babel import Babel

class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

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

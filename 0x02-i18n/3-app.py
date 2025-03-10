#!/usr/bin/env python3
from flask import Flask, request, render_template
from flask_babel import Babel, _

class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

babel.init_app(app, locale_selector=lambda: request.accept_languages.best_match(app.config["LANGUAGES"]))

@app.route("/")
def home():
    return render_template("3-index.html", home_title=("home_title"),home_header=('home_header') )

if __name__ == "__main__":
    app.run(debug=True)
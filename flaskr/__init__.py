import requests
from api_key import api_key
import json
from flask import Flask, render_template
import os#
from weather_data import weather_data



with open(r"C:\Users\akbar\Weather App\Weather-App\flaskr\sample.json", "r") as openfile:
    json_object = json.load(openfile)


def create_app(test_config=None):
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path,"flaskr.sqlite"),
    )

    if test_config is None:
        app.config.from_pyfile("config.py",silent=True)

    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/main")
    def main():
        data = weather_data()
        return render_template("index.html", data=data)
    
    
    return app
    

create_app().run(debug=True)



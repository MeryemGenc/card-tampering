from flask import Flask

app = Flask(__name__)

app.config["FLASK_ENV"] = app.config.get("FLASK_ENV", "development")

if app.config["FLASK_ENV"] == "production":
    app.config.from_object("config.DevelopmentConfig")
elif app.config["FLASK_ENV"] == "testing":
    app.config.from_object("config.TestingConfig")
else:
    app.config.from_object("config.ProductionConfig")

from app import views

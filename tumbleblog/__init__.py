from flask import Flask
from flask.ext.mongoengine import MongoEngine


app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "tumble_blog", 'HOST': '10.1.0.7'}
app.config["SECRET_KEY"] = "Loo2caiy7L"


db = MongoEngine(app)


def register_blueprints(app):
    # Prevents circular imports
    from tumbleblog.admin import admin
    from tumbleblog.views import posts
    app.register_blueprint(posts)
    app.register_blueprint(admin)


register_blueprints(app)


if __name__ == '__main__':
    app.run()

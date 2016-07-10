from flask import Flask
from flask.ext.mongoengine import MongoEngine


app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "tumble_blog", 'HOST': 'mongo1.webterrorist.net'}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"


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

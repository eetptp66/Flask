from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
migrate = Migrate()
def create_app():
    
    app = Flask(__name__)
    
    app.config.from_pyfile('config.py')
    
    #ORM
    from . import models
    db.init_app(app)
    migrate.init_app(app, db)
    
    #BP
    from . import blue
    from . import view_blue
    app.register_blueprint(blue.bp)
    app.register_blueprint(view_blue.bp)
    
    return app

if __name__ == '__main__':
    create_app().run(debug=True)
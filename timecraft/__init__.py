#import flask - from the package import class
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
app=Flask(__name__)

#create a function that creates a web application
def create_app():
    app.debug=True
    app.secret_key='NeedBetterSecret321'

    #set the app configuration data 
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///timecraft.sqlite'

    #initialize db with flask app
    db.init_app(app)

    bootstrap = Bootstrap(app)
    
    #importing modules here to avoid circular references, register blueprints of routes
    from . import views
    app.register_blueprint(views.bp)
    # from . import admin
    # app.register_blueprint(admin.bp)
   
    return app
from flask import Flask
from app.routes.saham import routes_saham

def configuration(app: Flask):
    app.register_blueprint(routes_saham)
import os

from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(

        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/pokemon/<int:post_id>)
def show_post(https://pokeapi.co/api/v2/pokemon/post_id/#%3Croot%3E.forms[0].name):
    return 'The pokemon with id ' % post_id % ' is %d' 

        @app.route('/pokemon/<String:post_name>)
def show_post(https://pokeapi.co/api/v2/pokemon/post_name/#%3Croot%3E.id):
    return post_name % ' has id %d'

    return app

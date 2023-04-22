from flask import Flask
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor


from config import Config
from app.extensions import db, ckeditor


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # ckeditor = CKEditor(app)    
       

    Bootstrap(app)

    # Initialize Flask extensions here

    db.init_app(app)	
    ckeditor.init_app(app) 
    # Register blueprints here
    from app.main import  bp as main_bp
    app.register_blueprint(main_bp)

    from app.equivalentes import bp as equivalentes_bp
    app.register_blueprint(equivalentes_bp, url_prefix="/equivalentes")

    from app.recetas import bp as recetas_bp
    app.register_blueprint(recetas_bp, url_prefix="/recetas")	
    # from app.questions import bp as questions_bp
    # app.register_blueprint(questions_bp, url_prefix='/questions')



    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app


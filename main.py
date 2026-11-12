import yaml
from flask import Flask
from app.my_project.auth.domain.models import db
from app.my_project.auth.route.routes import api_bp

def create_app():
    app = Flask(__name__)

    # Завантаження налаштувань БД
    with open('app/config/app.yml', 'r') as f:
        config = yaml.safe_load(f)

    db_conf = config['database']
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"mysql+pymysql://{db_conf['user']}:{db_conf['password']}@"
        f"{db_conf['host']}:{db_conf['port']}/{db_conf['name']}"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    app.register_blueprint(api_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
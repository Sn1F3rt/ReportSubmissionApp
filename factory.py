from quart import Quart
from quart_wtf import CSRFProtect


csrf = CSRFProtect()


def create_app():
    app = Quart(__name__)
    app.config.from_pyfile("config.py")

    global csrf
    csrf.init_app(app)

    from blueprints.meta import meta_bp

    app.register_blueprint(meta_bp)

    return app

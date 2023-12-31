import os

from flask import Flask, render_template
from flaskr.blueprint import home, mask_rcnn, condinst, cascade_mask_rcnn, ms_rcnn, solo


def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    """
    註冊服務
    """
    register_extensions(app)
    register_blueprint(app)
    return app


def register_extensions(app: Flask):
    """
    加载扩展
    :param app:
    :return:
    """


def register_blueprint(app: Flask):
    """
    加载蓝图
    :param app:
    :return:
    """
    app.register_blueprint(home.bp)
    app.register_blueprint(mask_rcnn.bp, url_prefix='/maskrcnn')
    app.register_blueprint(condinst.bp, url_prefix='/condinst')
    app.register_blueprint(cascade_mask_rcnn.bp, url_prefix='/cascade_mask_rcnn')
    app.register_blueprint(ms_rcnn.bp, url_prefix='/ms_rcnn')
    app.register_blueprint(solo.bp, url_prefix='/solo')
    app.add_url_rule('/', endpoint='home')



from flask import Blueprint, render_template
import logging
catalog_blueprint = Blueprint('catalog_blueprint', __name__)

#logging.basicConfig(filename="basic.log", level=logging.INFO)

@catalog_blueprint.route('/')
def profile_page():
    """
    Выводит стартовую страничку
    :return: 'index.html'
    """
    logging.info("Главная страница запрошена")
    return render_template('index.html')
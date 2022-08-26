from flask import Blueprint, render_template

posts_blueprint = Blueprint('posts_blueprint', __name__)

import logging

@posts_blueprint.route('/post/', methods=["GET", "POST"])
def page_post_form():
    """
    Выводит страничку с найденными постами по ключевому слову
    :return:
    """
    logging.info("Cтраничка поиска постов запрошена")
    return render_template('post_form.html')
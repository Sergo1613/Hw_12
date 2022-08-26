import os

import logging

from flask import Flask, send_from_directory, request, render_template

# from functions import ...
from functions import load_from_json, save_to_file, check_load_pic, check_extention, find_posts
from loader.views import posts_blueprint
from main.views import catalog_blueprint

logging.basicConfig(filename="basic.log", level=logging.INFO)

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

# Регистрируем первый блюпринт
app.register_blueprint(catalog_blueprint)
app.register_blueprint(posts_blueprint)


@app.route("/search")
def page_tag():
    """
    Страница найденных постов
    :return:
    """
    logging.info("Страница найденных постов запрошена")
    return find_posts()


@app.route("/upload", methods=["POST"])
def page_post_upload():
    """
    Загружает новый пост с фото на страницу и в файл posts.json
    :return: Страницу с новым постом
    """
    picture = request.files.get("picture")
    if not check_load_pic(picture):
        return "<p><a href='/' class='link'>Файл не выбран. Назад</a></p>"
    else:
        filename = picture.filename
        if not check_extention(filename):
            return "<p><a href='/' class='link'>Не верный тип файла. Назад</a></p>"
        else:
            picture.save(f"./uploads/images/{filename}")
            task = request.form['content']
            _path = os.path.join('uploads', 'images', filename)
            dict_post = {'pic': _path, 'content': task}
            current_json_file = load_from_json()
            if not current_json_file:
                return "<p><a href='/' class='link'>Файл не открывается. Назад </a></p>"
            current_json_file.append(dict_post)
            save_to_file(current_json_file)
            logging.info("Страница с загруженным постом запрошена")
            return render_template('post_uploaded.html', task=task, filename=filename)


@app.route("/uploads/<path:path>")
def static_dir(path):
    """
    открывает доступ к директории uploads
    :param path:
    :return:
    """
    logging.info("Выгрузка фото запрошена")
    return send_from_directory("uploads", path)


if __name__ == '__main__':
    app.run()
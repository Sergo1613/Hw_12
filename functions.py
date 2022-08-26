import json

from flask import request, render_template

POST_PATH = "posts.json"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'JPG'}


def load_from_json() -> list:
    """
    Загружает из файла словарь, если ошибка выводит False
    :return:
    """
    try:
        with open(POST_PATH, encoding='utf-8') as file:
            posts = json.load(file)

    except:
        return False

    return posts


def save_to_file(new_json: list):
    """
    Сохраняет в файл обновленный лист со словарями постов.
    :param new_json:
    :return:
    """
    with open(POST_PATH, 'w', encoding='utf-8') as file:
        json.dump(new_json, file, ensure_ascii=False)


def check_extention(file_name: str) -> bool:
    """
    Проверяет расширение файла картинки, перед записью на сервер
    :param file_name:
    :return:
    """
    extension = file_name.split(".")[-1]
    if extension in ALLOWED_EXTENSIONS:
        return True
    else:
        return False


def check_load_pic(pic) -> bool:
    """
    Проверяет наличие картинки в переменной
    :param pic:
    :return:
    """
    if pic:
        return True
    else:
        return False


def find_posts():
    """
    Ищет посты по ключевому слову
    :return: страничку с постами post_list.html
    """
    s = request.args.get("s").lower()
    posts = load_from_json()
    posts_found = []
    if not posts:
        return "<p><a href='/' class='link'>Файл не открывается. Назад</a></p>"

    for post in posts:
        if s in post["content"].lower():
            posts_found.append(post)

    return render_template('post_list.html', post=posts_found, s=s)
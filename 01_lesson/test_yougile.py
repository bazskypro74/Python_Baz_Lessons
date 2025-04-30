from yougileapi import Yougile_Api
api = Yougile_Api("https://ru.yougile.com/api-v2")

log_user = "*"
pass_user = "*"
id_projects_user = "*"
token_user = "*"


def test_company_list_positiv():
    login_user = log_user
    password_user = pass_user
    name_user_company = ""
    comp = api.get_company_list(login_user, password_user, name_user_company)
    ids = comp[1]
    print(f'Подставить id: {ids}  для получения key компании')
    assert ids[0] == ids[-36]


def test_token_list_negativ():  # statusCode = 400, Нет id компании в БД
    login_user = log_user
    password_user = pass_user
    companyID = '0aad5fe0-efd2-40c0-8120-858250206ebe'
    key = api.get_token_company(login_user, password_user, companyID)
    print(key)
    assert key[1] == 200


def test_id_project_positiv():
    token = token_user
    title = "Окно"
    users = {}
    result = api.create_project_company(title, users, token)
    stroka = f'Подставь в test_update_projects для удаления проекта, id: {
        result["id"]}'
    print(stroka)
    assert len(result["id"][-1]) == len(result["id"][32])


def test_id_project_negativ():  # Не верный тип объекта в users

    token = token_user
    title = "Окно"
    users = {0}
    result = api.create_project_company(title, users, token)
    stroka = f'Подставь в id_projects_user для удаления проекта, id: {
        result["id"]}'
    print(stroka)
    assert len(result["id"][-1]) == len(result["id"][32])


def test_update_projects_positiv():
    token = token_user
    title = "Окно"
    users = {}
    id_projects = id_projects_user
    deleted = True
    result = api.update_projects_company(
        deleted, title, users, id_projects, token)
    if deleted is True:
        stroka = f'Удален проект с id: {result["id"]}'
        print(stroka)
    else:
        stroka = f'Изменен проект с id: {result["id"]}'
        print(stroka)
    assert len(result["id"][-1]) == len(result["id"][32])


def test_update_projects_negativ():  # title проекта пустая строка
    token = token_user
    title = ""
    users = {}
    id_projects = id_projects_user
    deleted = True
    result = api.update_projects_company(
        deleted, title, users, id_projects, token)
    if deleted is True:
        stroka = f'Удален проект с id: {result["id"]}'
        print(stroka)
    else:
        stroka = f'Изменен проект с id: {result["id"]}'
        print(stroka)
    assert len(result["id"][-1]) == len(result["id"][32])


def test_get_projects_id_positive():
    token = token_user
    id_projects = id_projects_user
    result = api.get_projects_id(id_projects, token)
    id = result["id"]
    title = result["title"]
    print(f'id={id}')
    print(f'title={title}')
    assert id == id_projects


def test_get_projects_id_negative():  # Лишний пробел в конце id_projects
    token = token_user
    id_projects = id_projects_user+" "
    result = api.get_projects_id(id_projects, token)
    id = result["id"]
    print(id)
    assert id == id_projects

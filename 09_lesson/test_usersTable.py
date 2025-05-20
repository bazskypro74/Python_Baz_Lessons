from UsersTable import UsersTable

db = UsersTable("postgresql://bazskypro:258369zaq@localhost:5432/postgres")


def test_insert_user():
    user_id = "5123"
    user_email = "xswcde@gmail.com"
    subject_id = "6"

    db.insert_user(user_id, user_email, subject_id)
    result = db.get_Table(user_id)
    print(result)
    new_id = result[0]
    new_email = result[1]
    new_subject = result[2]
    print(new_id, new_email, new_subject)
    assert new_email == user_email
    assert new_id == int(user_id)
    assert new_subject == int(subject_id)
    db.deleted_user(new_id)


def test_update_users():
    user_id = "5123"
    user_email = "xswcde@gmail.com"
    subject_id = "6"
    db.insert_user(user_id, user_email, subject_id)
    new_user_email = "zaqxsw@gmail.ru"
    db.update_users(user_id, new_user_email)
    result = db.get_Table(user_id)
    print(result)
    new_id = result[0]
    new_email = result[1]
    new_subject = result[2]
    print(new_id, new_email, new_subject)
    assert new_email == new_user_email
    assert new_id == int(user_id)
    assert new_subject == int(subject_id)
    db.deleted_user(new_id)


def test_delete_user():
    user_id = "5123"
    user_email = "xswcde@gmail.com"
    subject_id = "6"
    db.insert_user(user_id, user_email, subject_id)
    result = db.get_Table(user_id)
    new_id = result[0]
    db.deleted_user(new_id)
    result = db.get_Table(user_id)
    print(result)
    # new_id = result[0]
    # assert new_email == new_email
    assert result == str("Студент удален")

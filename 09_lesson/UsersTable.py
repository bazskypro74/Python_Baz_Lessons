from sqlalchemy import create_engine
from sqlalchemy.sql import text


class UsersTable:

    __scripts = {
        "insert users": text(
            "INSERT INTO users ("
            "\"user_id\", \"user_email\", \"subject_id\")"
            "VALUES (:user_id, :user_email, :subject_id)"),
        "update user_email": text(
            "UPDATE users SET user_email=:new_user_email "
            "WHERE user_id =:new_user_id"),
        "deleted User": text(
            "DELETE FROM users WHERE user_id =:to_delete"),
        "get table": text(
            "SELECT * FROM users WHERE user_id =:user_id")
        }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)
        self.connection = self.__db.connect()

    def insert_user(self, user_id, user_email, subject_id):

        self.connection.execute(self.__scripts["insert users"], {
            "user_id": user_id,
            "user_email": user_email,
            "subject_id": subject_id
            })
        self.connection.commit()

    def get_Table(self, user_id):
        result = self.connection.execute(self.__scripts["get table"], {
            "user_id": user_id
            })
        fetched = result.fetchall()
        if not fetched:
            return "Студент удален"  # или любое другое сообщение
        else:
            return fetched[0]

    def update_users(self, user_id, new_user_email):
        result = self.connection.execute(self.__scripts["update user_email"], {
            "new_user_id": user_id,
            "new_user_email": new_user_email})
        print(result)
        self.connection.commit()

    def deleted_user(self, new_id):
        self.connection.execute(self.__scripts["deleted User"], {
            "to_delete": new_id
            })
        self.connection.commit()

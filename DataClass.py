import sqlite3
class Database:
    def __init__(self, path_to_db='test_2.db'):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple=None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = tuple()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()

        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users(
        id INT NOT NULL, 
        num_app varchar(255),
        name varchar(255),
        address varchar(255),
        phone varchar(255),
        topic varchar(255),
        application varchar(255),
        PRIMARY KEY (id)
        );
        """
        return self.execute(sql)


    def add_app(self, id, num_app: str, topic: str, name: str, address: str, phone: str, application: str):
        sql = "INSERT INTO Users(id, num_app, topic, name, address, phone, application) VALUES  (?, ?, ?, ?, ?, ?, ?)"
        parameters = (id, num_app, topic, name, address, phone, application)
        self.execute(sql, parameters=parameters, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f'{item} = ?' for item in parameters
        ])
        return sql, tuple(parameters.values())

    def  select_all_users(self):
        sql = "SELECT * FROM Users"
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def update_phone_number(self, phone, id):
        sql = 'UPDATE Users SET phone=? WHERE id=?'
        return self.execute(sql, parameters=(phone, id), commit=True)

    def delete_all_users(self):
        self.execute("DELETE FROM Users WHERE TRUE")

def logger(statement):
   print(f"""
___________________________
EXECUTING
{statement}
___________________________
""")
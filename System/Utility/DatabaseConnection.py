import sqlite3

class DatabaseConnection:
    _instance = None
    _conn = None
    _cursor = None

    def __new__(cls, *args, **kwargs):
        basepath = "D:\\OneDrive - Asia Pacific University\\Degree Year 3\\Sem 2\\Final Year Project\\Deepfake Detection System\\Database\\"
        database_name = "deepfake_system_db"
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._conn = sqlite3.connect(basepath + database_name)
            cls._cursor = cls._conn.cursor()
        return cls._instance

    def get_connection(self):
        return self._conn
    
    def get_cursor(self):
        return self._cursor
    
    def execute_query(self, query, data_tuple = ()):
        error_msg = ""

        try:
            # Execute the query with the user data
            self._cursor.execute(query, data_tuple)

        except sqlite3.Error as error:
            error_msg = error
        finally:
            self._conn.commit()
        
        print(error_msg)
        return [error_msg, self._cursor]
    

    
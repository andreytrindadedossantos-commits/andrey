import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create(self, table, columns, values):
        placeholders = ', '.join(['?' for _ in values])
        query = f'INSERT INTO {table} ({columns}) VALUES ({placeholders})'
        self.cursor.execute(query, values)
        self.connection.commit()

    def read(self, table, columns='*', condition=None):
        query = f'SELECT {columns} FROM {table}'
        if condition:
            query += f' WHERE {condition}'
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def update(self, table, column_values, condition):
        set_clause = ', '.join([f'{column} = ?' for column in column_values.keys()])
        query = f'UPDATE {table} SET {set_clause} WHERE {condition}'
        self.cursor.execute(query, list(column_values.values()))
        self.connection.commit()

    def delete(self, table, condition):
        query = f'DELETE FROM {table} WHERE {condition}'
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()
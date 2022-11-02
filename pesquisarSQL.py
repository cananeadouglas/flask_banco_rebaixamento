import sqlite3

conn = sqlite3.connect('employee.db')
cursor = conn.cursor()

# lendo os dados
cursor.execute("""
SELECT * FROM Employees;
""")

for linha in cursor.fetchall():
    print(linha)

conn.close()
import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

cur.execute('INSERT INTO Tracks (title, plays) VALUES (?,?)',
    ('Gotas de Lluvia', 7))
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?,?)',
    ('Como La Flor', 20))
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?,?)',
    ('Si Una Vez', 15))
cur.execute('DELETE FROM Tracks WHERE plays <1')

cur.execute('SELECT title, plays FROM Tracks')
for row in cur:
    print(row)


conn.commit()

conn.close()

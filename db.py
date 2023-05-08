import sqlite3 as sqlite
import os

benjalin_directory= os.path.expanduser('~')+"/benjalin/"
if not os.path.exists(benjalin_directory):
    os.makedirs(benjalin_directory, exist_ok=True)

con = sqlite.connect(benjalin_directory+"benjalin.db")
cur = con.cursor()


cur = con.execute("CREATE TABLE IF NOT EXISTS virtue_scores(id integer primary key, date text, virtue text, note text, score integer)")
con.commit()

def save_score(date, score, virtue, note):
    print(date, score, virtue, note, 'aerokastra')
    sql = "INSERT INTO VIRTUE_SCORES(date, virtue, note, score) VALUES(?, ?, ?, ?)"
    cur = con.cursor()
    cur.execute(sql, (date, virtue, note, score))
    con.commit()


def average(virtue):
    print('retrieving average score for', virtue)
    sql = "select avg(score) from virtue_scores where virtue=?"
    cur = con.cursor()
    cur.execute(sql, (virtue,))
    return cur.fetchone()[0]

def journals_by_virtue(virtue):
    print('retrieving dates', virtue)
    sql = "select date from virtue_scores where virtue=?"
    cur = con.cursor()
    cur.execute(sql, (virtue,))
    records = cur.fetchall()
    result = []
    for row in records:
        result.append(row[0])
    return result

def journal(virtue, date):
    print('retrieving journal', virtue, date)
    sql = "select note from virtue_scores where virtue=? and date=?"
    cur = con.cursor()
    cur.execute(sql, (virtue, date))
    return cur.fetchone()[0]

import  sqlite3
import  datetime

def db_is_created():
    conn = sqlite3.connect('devides.db')
    c = conn.cursor()
    try:
        c.execute('SELECT * FROM main.davices')
        conn.close()
        return True
    except:
        return False

def db_created():
    try:
        conn = sqlite3.connect('devides.db')
        c = conn.cursor()
        #"ID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        c.execute('''CREATE TABLE IF NOT EXISTS  "davices" (               
               "IP"	TEXT NOT NULL UNIQUE,
               "DATE"	INTEGER
               );''')
        conn.commit()
        conn.close()
        return True
    except:
        return False

def db_delete(ip):
    try:
        conn = sqlite3.connect('devides.db')
        c = conn.cursor()
        c.execute(f'DELETE FROM main.davices WHERE IP = ?',ip)
        conn.commit()
        conn.close()
        return True
    except:
        return False

def db_delete_all():
    try:
        conn = sqlite3.connect('devides.db')
        c = conn.cursor()
        c.execute('''DROP TABLE IF EXISTS main.davices''')
        conn.commit()
        conn.close()
        return True
    except:
        return False
    pass

def db_update(ip):
    try:
        date = datetime.datetime.now()
        push=(ip,date,ip)
        conn = sqlite3.connect('devides.db')
        c = conn.cursor()
        c.execute('''
        UPDATE main.davices
SET IP=?,
    DATE=?    
WHERE
     IP= ?''',push)
        conn.commit()
        conn.close()
        return True
    except:
        return False
    pass
def db_add_devices(devices):
    date = datetime.datetime.now()
    push_devices=[]
    for device in devices:
        push_devices.append((device,date))
    try:
        conn = sqlite3.connect('devides.db')
        c = conn.cursor()
        c.executemany('''INSERT INTO  main.davices VALUES(?,?)''',push_devices)
        conn.commit()
        conn.close()
        return True
    except:
        return False
    pass

def db_add_device(device):
    date=datetime.datetime.now()
    try:
        push=(device,date)
        conn = sqlite3.connect('devides.db')
        c = conn.cursor()
        c.execute('INSERT INTO  main.davices VALUES(?,?)',push)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        return False
    pass

def db_select_all():
    try:
        conn = sqlite3.connect('devides.db')
        c = conn.cursor()
        devices =list(c.execute('SELECT * FROM main.davices '))
        conn.commit()
        conn.close()
        return devices
    except:
        return False



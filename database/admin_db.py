import sqlite3 as sq

async def db_start():
    global db, cur
    db = sq.connect('tg.db')
    cur = db.cursor()
    
    cur.execute("CREATE TABLE IF NOT EXISTS accounts "
                "(id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "tg_id INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS items"
                "(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, photo TEXT, price INTEGER)")
    db.commit()

# ==============================================================================

async def cmd_start_db(user_id):
    user = cur.execute("SELECT * FROM accounts WHERE tg_id == {key}".format(key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO accounts (tg_id) VALUES ({key})".format(key=user_id))
        db.commit()
        
async def select_all():
    user = cur.execute("SELECT tg_id FROM accounts").fetchall()
    return user

# ==============================================================================
# Добавление товара

async def add_item_db(info):
    cur.execute("INSERT INTO items (name, description, photo, price) VALUES (?, ?, ?, ?)", (info['name'], info['desc'], info['photo'], info['price']))
    db.commit()

# ==============================================================================
# Добавление товара

def get_all_items():
    items = cur.execute("SELECT * FROM items").fetchall()
    return items

async def get_one_item(id):
    item = cur.execute("SELECT * FROM items WHERE id == {key}".format(key=int(id))).fetchone()
    return item

async def edit_name(id, name):
    cur.execute("UPDATE items SET name = '{key}' WHERE id == {key2}".format(key=name, key2=int(id)))
    db.commit()
    
async def edit_desc(id, desc):
    cur.execute("UPDATE items SET description = '{key}' WHERE id == {key2}".format(key=desc, key2=int(id)))
    db.commit()
    
async def edit_price(id, price):
    cur.execute("UPDATE items SET price = '{key}' WHERE id == {key2}".format(key=price, key2=int(id)))
    db.commit()
    
async def edit_photo(id, photo):
    cur.execute("UPDATE items SET photo = '{key}' WHERE id == {key2}".format(key=photo, key2=int(id)))
    db.commit()
    
async def delete_item(id):
    cur.execute("DELETE FROM items WHERE id = {key}".format(key=int(id))).fetchone()
    db.commit()
# info['name']
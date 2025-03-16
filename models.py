import sqlite3
import click
from flask import current_app, g
import os

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    # Read schema.sql file
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
    
    # Add initial products if they don't exist
    product_count = db.execute('SELECT COUNT(*) FROM product').fetchone()[0]
    if product_count == 0:
        db.execute('INSERT INTO product (name, description, price) VALUES (?, ?, ?)',
                  ('Laptop', 'High-performance laptop with the latest specs', 800))
        db.execute('INSERT INTO product (name, description, price) VALUES (?, ?, ?)',
                  ('Mobile Phone', 'Latest smartphone with advanced camera features', 500))
        db.execute('INSERT INTO product (name, description, price) VALUES (?, ?, ?)',
                  ('Keyboard', 'Mechanical keyboard with RGB lighting', 100)),
        db.commit()
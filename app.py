# from flask import Flask, render_template, request, redirect, url_for, flash, session, g
# import sqlite3
# import os
# from werkzeug.security import generate_password_hash, check_password_hash
# from models import init_db, get_db, close_db

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'dev'
# app.config['DATABASE'] = os.path.join(app.instance_path, 'shop.db')

# # Ensure the instance folder exists
# try:
#     os.makedirs(app.instance_path)
# except OSError:
#     pass

# @app.teardown_appcontext
# def close_db_at_end_of_request(e=None):
#     close_db(e)

# # Replace before_first_request with this function
# def initialize_database():
#     with app.app_context():
#         init_db()

# # Initialize database when the app is created
# initialize_database()

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/register', methods=('GET', 'POST'))
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         db = get_db()
#         error = None

#         if not username:
#             error = 'Username is required.'
#         elif not password:
#             error = 'Password is required.'
#         elif db.execute(
#             'SELECT id FROM user WHERE username = ?', (username,)
#         ).fetchone() is not None:
#             error = f"User {username} is already registered."

#         if error is None:
#             db.execute(
#                 'INSERT INTO user (username, password, balance) VALUES (?, ?, ?)',
#                 (username, generate_password_hash(password), 1000)
#             )
#             db.commit()
#             flash('Registration successful! You can now log in.')
#             return redirect(url_for('login'))

#         flash(error)

#     return render_template('register.html')

# @app.route('/login', methods=('GET', 'POST'))
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         db = get_db()
#         error = None
#         user = db.execute(
#             'SELECT * FROM user WHERE username = ?', (username,)
#         ).fetchone()

#         if user is None:
#             error = 'Incorrect username.'
#         elif not check_password_hash(user['password'], password):
#             error = 'Incorrect password.'

#         if error is None:
#             session.clear()
#             session['user_id'] = user['id']
#             return redirect(url_for('shop'))

#         flash(error)

#     return render_template('login.html')

# @app.before_request
# def load_logged_in_user():
#     user_id = session.get('user_id')

#     if user_id is None:
#         g.user = None
#     else:
#         g.user = get_db().execute(
#             'SELECT * FROM user WHERE id = ?', (user_id,)
#         ).fetchone()

# @app.route('/logout')
# def logout():
#     session.clear()
#     return redirect(url_for('index'))

# @app.route('/shop')
# def shop():
#     if g.user is None:
#         return redirect(url_for('login'))
    
#     db = get_db()
#     products = db.execute('SELECT * FROM product').fetchall()
#     return render_template('shop.html', products=products)

# @app.route('/profile')
# def profile():
#     if g.user is None:
#         return redirect(url_for('login'))
    
#     db = get_db()
#     orders = db.execute(
#         'SELECT o.id, o.date, p.name, p.price FROM orders o JOIN product p ON o.product_id = p.id WHERE o.user_id = ?',
#         (g.user['id'],)
#     ).fetchall()
    
#     return render_template('profile.html', user=g.user, orders=orders)

# @app.route('/buy/<int:product_id>', methods=['POST'])
# def buy_product(product_id):
#     if g.user is None:
#         return redirect(url_for('login'))
    
#     db = get_db()
#     product = db.execute('SELECT * FROM product WHERE id = ?', (product_id,)).fetchone()
    
#     if product is None:
#         flash('Product not found!')
#         return redirect(url_for('shop'))
    
#     if g.user['balance'] < product['price']:
#         flash('Insufficient balance!')
#         return redirect(url_for('shop'))
    
#     # Update user balance
#     new_balance = g.user['balance'] - product['price']
#     db.execute('UPDATE user SET balance = ? WHERE id = ?', (new_balance, g.user['id']))
    
#     # Create order
#     db.execute(
#         'INSERT INTO orders (user_id, product_id, date) VALUES (?, ?, datetime("now"))',
#         (g.user['id'], product_id)
#     )
#     db.commit()
    
#     flash(f'Successfully purchased {product["name"]}!')
#     return redirect(url_for('profile'))

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for, flash, session, g
import sqlite3
import os
from werkzeug.security import generate_password_hash, check_password_hash
from models import init_db, get_db, close_db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
app.config['DATABASE'] = os.path.join(app.instance_path, 'shop.db')

# Ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

@app.teardown_appcontext
def close_db_at_end_of_request(e=None):
    close_db(e)

# Replace before_first_request with this function
def initialize_database():
    with app.app_context():
        init_db()

# Initialize database when the app is created
initialize_database()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = f"User {username} is already registered."

        if error is None:
            db.execute(
                'INSERT INTO user (username, password, balance) VALUES (?, ?, ?)',
                (username, generate_password_hash(password), 1000)
            )
            db.commit()
            flash('Registration successful! You can now log in.')
            return redirect(url_for('login'))

        flash(error)

    return render_template('register.html')

@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('shop'))

        flash(error)

    return render_template('login.html')

@app.before_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/shop')
def shop():
    if g.user is None:
        return redirect(url_for('login'))
    
    db = get_db()
    products = db.execute('SELECT * FROM product').fetchall()
    return render_template('shop.html', products=products)

@app.route('/profile')
def profile():
    if g.user is None:
        return redirect(url_for('login'))
    
    db = get_db()
    orders = db.execute(
        'SELECT o.id, o.date, p.name, p.price FROM orders o JOIN product p ON o.product_id = p.id WHERE o.user_id = ?',
        (g.user['id'],)
    ).fetchall()
    
    return render_template('profile.html', user=g.user, orders=orders)

@app.route('/add_balance', methods=['GET', 'POST'])
def add_balance():
    if g.user is None:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        try:
            amount = int(request.form['amount'])
            if amount <= 0:
                flash('Please enter a positive amount.')
                return redirect(url_for('add_balance'))
            
            db = get_db()
            new_balance = g.user['balance'] + amount
            db.execute('UPDATE user SET balance = ? WHERE id = ?', (new_balance, g.user['id']))
            db.commit()
            
            flash(f'Successfully added ₹{amount} to your balance!')
            return redirect(url_for('profile'))
        except ValueError:
            flash('Please enter a valid amount.')
    
    return render_template('add_balance.html')

@app.route('/buy/<int:product_id>', methods=['POST'])
def buy_product(product_id):
    if g.user is None:
        return redirect(url_for('login'))
    
    db = get_db()
    product = db.execute('SELECT * FROM product WHERE id = ?', (product_id,)).fetchone()
    
    if product is None:
        flash('Product not found!')
        return redirect(url_for('shop'))
    
    if g.user['balance'] < product['price']:
        flash('Insufficient balance!')
        return redirect(url_for('shop'))
    
    # Update user balance
    new_balance = g.user['balance'] - product['price']
    db.execute('UPDATE user SET balance = ? WHERE id = ?', (new_balance, g.user['id']))
    
    # Create order
    db.execute(
        'INSERT INTO orders (user_id, product_id, date) VALUES (?, ?, datetime("now"))',
        (g.user['id'], product_id)
    )
    db.commit()
    
    flash(f'Successfully purchased {product["name"]}!')
    return redirect(url_for('profile'))

if __name__ == '__main__':
    app.run(debug=True)
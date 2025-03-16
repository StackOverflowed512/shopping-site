# Shopping Site with Flask

A simple e-commerce application built with Flask and SQLite that allows users to register, manage their balance, and purchase items.

## Features

- User authentication (register, login, logout)
- Virtual currency system (default 1000₹ for new users)
- Product catalog (Laptop, Mobile Phone, Keyboard)
- Purchase functionality
- Balance management (view and add balance)
- Order history

## Project Structure

```
shopping_site/
│
├── app.py              # Main Flask application
├── models.py           # Database models
├── schema.sql          # SQL schema for database initialization
├── static/             # Static files
│   └── style.css       # CSS styling
├── templates/          # HTML templates
│   ├── base.html       # Base template with common elements
│   ├── index.html      # Homepage
│   ├── login.html      # Login page
│   ├── register.html   # Registration page
│   ├── shop.html       # Shop page with products
│   ├── profile.html    # User profile page
│   └── add_balance.html # Add balance page
└── instance/           # SQLite database location (created automatically)
    └── shop.db         # SQLite database
```

## Installation and Setup

1. Clone the repository or download the source code:
   ```
   git clone https://github.com/yourusername/shopping-site.git
   cd shopping-site
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   ```

   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

3. Install the required packages:
   ```
   pip install flask
   ```

4. Initialize the database:
   This happens automatically when you run the application for the first time.

5. Run the application:
   ```
   python app.py
   ```
   or
   ```
   flask run
   ```

6. Access the application in your web browser:
   ```
   http://127.0.0.1:5000
   ```

## Usage Guide

1. **Register a new account**
   - Click on "Register" in the navigation bar
   - Enter a username and password
   - New accounts start with 1000₹ in balance

2. **Log in to your account**
   - Click on "Log In" in the navigation bar
   - Enter your username and password

3. **View available products**
   - Click on "Shop" in the navigation bar
   - Browse the available products

4. **Purchase products**
   - Click the "Buy Now" button on any product
   - The product will be purchased if you have sufficient balance
   - Your balance will be automatically updated

5. **Add balance to your account**
   - Click on "Add Balance" in the navigation bar
   - Enter the amount you want to add
   - Click "Add Balance" to confirm

6. **View your profile and purchase history**
   - Click on "Profile" in the navigation bar
   - View your current balance and purchase history

7. **Log out**
   - Click on "Log Out" in the navigation bar

## Products

The application comes with three pre-defined products:

1. **Laptop**
   - Price: 800₹
   - Description: High-performance laptop with the latest specs

2. **Mobile Phone**
   - Price: 500₹
   - Description: Latest smartphone with advanced camera features

3. **Keyboard**
   - Price: 100₹
   - Description: Mechanical keyboard with RGB lighting

## Technology Stack

- **Backend**: Flask (Python)
- **Database**: SQLite
- **Frontend**: HTML, CSS
- **Authentication**: Flask session management with password hashing

## Security Features

- Password hashing using Werkzeug's security module
- Form validation for user inputs
- Protection against SQL injection via SQLite's parameterized queries
- Session management for user authentication

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
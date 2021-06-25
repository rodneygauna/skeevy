'''
    File name: main.py
    Author: Rodney Gauna
    Date created: 2021-06-24

    Python Version: 3.9.5
    Flask Version: 2.0.1
    Werkzeug Version: 2.0.1
    Flask Login Version: 0.5.0
    Flask SQLAlchemy Version: 2.5.1
    Jinja2 Version: 3.0.1
    SQLAlchemy Version: 1.4.19
'''

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------
from website import create_app

# ------------------------------------------------------------------------------
# Global Variables
# ------------------------------------------------------------------------------
app = create_app()

# ------------------------------------------------------------------------------
# Executes the code for the application
# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)   # Enabling debug mode so the app auto-updates changes

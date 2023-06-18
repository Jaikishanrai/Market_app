# app = Flask(__name__) ------> refers to local python file that we are working with
# @app.route('/')------> know as decorator. It says what url i am going to navigate and display you some HTML code
"""
To run the project follow the given commands:-
1) open the project directory in cmd
2) type set FLASK_APP=market.py + enter
3) type flask run + enter
4) you will get a local host URL
5) open the url in browser
6) you can open debugger mode ON in cmd by typing set FLASK_DEBUG=1 + enter
7) type flask run
8) by doing this you don't need to reload your page everytime you make any change
9) By after creating final project debugger mode should be off otherwise it will show errors of your program to end user of the app.
"""
# @app.route('/about/<username>')---> allowed the route to receive the string(username) that we want after the about page.
# create a templates directory in the project folder and create a html file named home.html
# from bootstrap.com --> starter template copy and paste the code in html file
# we use bootstrap for styling our page
"""
1) Website templates are pre-designed layouts that allow you to arrange content onto a web page to quickly create a well-designed website.
2) Flask is supported by inbuilt template support named Jinja2.
3) This Web template engine is a fast, expressive, extensible templating engine.
4) Jinja2 extensively helps to write Python code within the HTML file.
5) To declare the variable using Jinja Template we use {{variable_name}} within the HTML file. As a result, the variable will be displayed on the Website.
6) jinja template allows us to access the information that comes from the route
"""
# jinja is a special web templating syntax that we are able to access through html b/c it is specially designed for python web frameworks

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template('market.html', items=items)



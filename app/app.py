"""A simple flask web app"""
from flask import Flask, render_template
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()

@app.route("/calculator", methods=['GET'])
def calculator_get():
    return CalculatorController.get()

@app.route("/calculator", methods=['POST'])
def calculator_post():
    return CalculatorController.post()

@app.route("/article1.html")
def article1():
    return render_template("article1.html")

@app.route("/article2.html")
def article2():
    return render_template("article2.html")

@app.route("/article3.html")
def article3():
    return render_template("article3.html")

@app.route("/article4.html")
def article4():
    return render_template("article4.html")

@app.route("/past.html")
def past():
    return render_template("past.html")

@app.route("/future.html")
def future():
    return render_template("future.html")

@app.route("/calctable.html")
def calctable():
    return render_template("calctable.html")

classes = 'table table-striped table-bordered table-hover'

@app.route("/")
def show_tables():
    data = pd.read_csv('csv/calcresults.csv')
    return render_template('view.html',tables=[data.to_html(classes=classes)], titles = ['na', 'Calculator History'])


if __name__ == "__main__":
    app.run(debug=True)


# @app.route('/calctable.html')
# def table():
#     filename = "C:\\Users\\kenda\\PycharmProjects\\Validationhw\\validationnhw\\csv\\calcresults.csv"
#
#     # to read the csv file using the pandas library
#     data = pandas.read_csv(filename, header=0)
#
#     myData = data.values
#     return render_template('calctable.html', myData=myData)

# @app.route('/')
# def index():
#     users = User.query
#     return render_template('bootstrap_table.html', title='Bootstrap Table',
#                            users=users)

# df = pd.read_csv('sample_data.csv')
# df.to_csv('sample_data.csv', index=None)
#
#
# # route to html page - "table"
# @app.route('/calctable.html')
# def future():
#     # converting csv to html
#     data = pd.read_csv('restable.csv')
#     return render_template('calctable.html', tables=[data.to_html()], titles=[''])


# # route to html page - "table"
# @app.route('/')
# @app.route('/table')
# def table():
#     # converting csv to html
#     data = pd.read_csv('sample_data.csv')
#     return render_template('table.html', tables=[data.to_html()], titles=[''])
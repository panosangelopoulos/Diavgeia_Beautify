from flask import Flask,render_template,request
from core import *


app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def main_page():
    TableSubject = []
    TableIssueDate = []
    TableAda = []
    TabledocumentUrl = []
    TabledecisionTypeLabel =[]
    x = 99
    if request.method == 'POST':
        url = request.form['get_my_url']
        final_result(url, TableAda, TableIssueDate, TabledocumentUrl, TabledecisionTypeLabel, TableSubject)
    global TabledocumentUrl, TableAda, TabledocumentUrl, TabledecisionTypeLabel, TableIssueDate, TableSubject, x, url
    return render_template('get_url.html')


@app.route('/data')
def index():
    return render_template('index.html', TableAda = TableAda ,
                           TabledecisionTypeLabel = TabledecisionTypeLabel,
                           TabledocumentUrl= TabledocumentUrl,
                           TableIssueDate = TableIssueDate,
                           TableSubject= TableSubject,
                           x = x, url= url)

if __name__ == '__main__':
    app.run(debug='TRUE')

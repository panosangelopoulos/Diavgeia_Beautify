from flask import Flask, render_template, request,flash
import urllib, json, re
import urllib.request


app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route('/', methods=['GET', 'POST'])
def main_page():
    global TableAda, TabledocumentUrl, TabledocumentUrl, TabledecisionTypeLabel, TableIssueDate, TableSubject, url, lengthofdata
    TableSubject = []
    TableIssueDate = []
    TableAda = []
    TabledocumentUrl = []
    TabledecisionTypeLabel = []
    lengthofdata = None
    error = None
    if request.method == 'POST':
            url = request.form['get_my_url']
            if re.compile("^https://diavgeia.gov.gr").match(url):
                print ("Correct URL")
                response = urllib.request.urlopen(url)
                data = json.loads(response.read().decode('utf-8'))
                lengthofdata = len(data["decisionResultList"])
                for i in range(len(data["decisionResultList"])):
                    TableAda.append(data["decisionResultList"][i]["ada"])
                    TableSubject.append(data["decisionResultList"][i]["subject"])
                    TableIssueDate.append(data["decisionResultList"][i]["issueDate"])
                    TabledocumentUrl.append(data["decisionResultList"][i]["documentUrl"])
                    TabledecisionTypeLabel.append(data["decisionResultList"][i]["decisionTypeLabel"])
                flash('Great news! You put the correct url, now please click on "Move to results" button.')
                error = False
                #parser.feed("<p><FONT COLOR='red'>Enter your last name:</FONT></p>")
            else:
                flash('Wrong URL, please try again')
                error = True
    return render_template('get_url.html', error=error)


@app.route('/data')
def index():
    return render_template('index.html', TableAda=TableAda,
                           TabledecisionTypeLabel=TabledecisionTypeLabel,
                           TabledocumentUrl=TabledocumentUrl,
                           TableIssueDate=TableIssueDate,
                           TableSubject=TableSubject,
                           lengthofdata=lengthofdata, url=url)


if __name__ == '__main__':
    app.run(debug='TRUE')

import urllib, json
import urllib.request

from Read_json_data import *


def final_result(url, TableAda, TableIssueDate, TabledocumentUrl, TabledecisionTypeLabel, TableSubject):
        print("I'm starting final")
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode('utf-8'))
        print(url)
        for i in range(len(data["decisionResultList"])):
            TableAda.append(data["decisionResultList"][i]["ada"])
            TableSubject.append(data["decisionResultList"][i]["subject"])
            TableIssueDate.append(data["decisionResultList"][i]["issueDate"])
            TabledocumentUrl.append(data["decisionResultList"][i]["documentUrl"])
            TabledecisionTypeLabel.append(data["decisionResultList"][i]["decisionTypeLabel"])
        x = i
        global x
        print(x)
        return TableAda, TableIssueDate, TabledocumentUrl, TabledecisionTypeLabel, TableSubject, x
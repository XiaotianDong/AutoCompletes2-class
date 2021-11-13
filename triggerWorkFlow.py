import requests, demjson, sys
IssueId = sys.argv[1]
Token = sys.argv[2]

Answer = {}
data =demjson.decode(requests.get(f"https://api.github.com/repos/XiaotianDong/AutoCompletes2-class/issues/{IssueId}").text) 
labels = [label['name'] for label in data['labels']]
types = {"FirstLogin":"GetTheFuckingCompetitionQuestion","SecondLogin":"Finish_theFucking_CompetitionAndCourse"}
type = ""
AllCompetitionFinished = False

if "FirstLogin" in labels:
    type = types["FirstLogin"]
elif "SecondLogin" in labels:
    type = types["SecondLogin"]
else:
    exit()
    
body = data['body'].split("\r\n")

if type == "GetTheFuckingCompetitionQuestion":
    Answer += ""
else:
    Resp_data = demjson.decode(requests.get(data['comments_url']))
    id = Resp_data[0]['body']
    id = id[id.index("Id:")+3:]
    if not id:
        AllCompetitionFinished = True
    Answer[id]=Resp_data[1]['body']

requests.post(f"https://api.github.com/repos/XiaotianDong/AutoCompletes2-class/actions/workflows/{type}/dispatches", headers={"Accept":"application/vnd.github.v3+json"}, json={
    "ref": "ref",
    "inputs":{
      "teacherAccount": body[0],
      "teacherPassword": body[1],
      "studentTargetPassword": body[2],
      "IssueId": IssueId,
      "Answer": Answer,
      "AllCompetitionFinished": "fuck"
    }
})

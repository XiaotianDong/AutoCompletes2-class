import requests, demjson, time
from selenium import webdriver
from selenium.webdriver.common.by import By
#import lxml

# Initalize Browser by headless mode
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--log-level=3")
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(20)
driver.get(r"https://2-class.com")

class User:
    def __init__(self, reqtoken, cookies) -> None:
        self.reqtoken = reqtoken
        self.cookies = cookies

class Teacher(User):
    def __init__(self, reqtoken, cookies, gradeId, className, classId, gradeName) -> None:
        super().__init__(reqtoken, cookies)
        self.className = className
        self.classId = classId
        self.gradeId = gradeId
        self.gradeName = gradeName


def login(userName, password, isTeacher=False)-> User:
    #Reinitialize Browser
    driver.delete_all_cookies()
    driver.refresh()
    cookies = {}
    driver.find_element(By.CSS_SELECTOR, "#app > div > div.home-container > div > div > main > div.white-bg-panel > div.login_home > div > div.padding-panel.btn-panel > div > button").click()
    while (not driver.execute_script("return document.querySelector('body > div:nth-child(15) > div > div.ant-modal-wrap > div > div.ant-modal-content')")):time.sleep(0.1)
    for i in driver.get_cookies():
        cookies[i['name']]=i['value']
    reqtoken = driver.execute_script("return window.__DATA__.reqtoken")
    payload = {
        "account": userName,
        "checkCode": "",
        "codeKey": "",
        "nvcVal": "%7B%22a%22%3A%22FFFF0N00000000008182%22%2C%22c%22%3A%22FFFF0N00000000008182%3Anvc_activity%3A1636517155035%3A0.7520663882351899%22%2C%22d%22%3A%22nvc_activity%22%2C%22j%22%3A%7B%22test%22%3A1%7D%2C%22h%22%3A%7B%7D%2C%22b%22%3A%22216!LLDIFdyBFwZ5GLIfkbsPCR3fvLdIJXqOMSkgJWZN%2BABNN5yCcO%2FPa5fbw1m9Ia0mi80iIzztY8IydjbJ%2BvI6e%2BU35g9ZQltxm6aMPSsFtcVFkZ%2BAQPMtlE80fxNB2qY%2FW6Fr8RU485mb4S8A312sxsGXgDPB9tsKutBbeL71sCTtnsR68tgzqGbAbuVZ%2BE627QGeNjS6DboP758GjPJYTKuesPZQWWdR4NHDrSWhyOzkkSiDIFjsfpUE%2Fpl7PV8OIBgtOnd37Mg%2FS%2BCXYv3KIs6wZIKAgyN7Fhq0SWdygAAInd3xw1CMbGUU6Jdv0JqpNeprb7pxFhoMmLjFz8Jrcbpi5qiEunLN6rQKVXoEhV8zmrrRBgNwbI6ifIJ8aTrev2UCZltV5XEnWV9ev%2FDvYUB0BRxWcErJD4mtwRpCNZLXbB%2FrZX578xEUipXN6TU5AG%2Fe%2B2Wi0zaDUZFDJ1J%2Bpclh5GlP0UoHBqRKkfSP3M6Tav0eLnXWV9PEsfUeznqsVPk6iS2sn92fIbeSDZI4V3ZEIpPACqJGhStduSypnYKtlkyeuXj%2FV3ZEIpPACqJGhbREimyBn32ALRELUQj8HbRRUpn3dcxc%2FHLONBDbwQCoaV6KDnSU86%2FyP9wLsbSXYLSDASXu16aCacMIrEcklJtwfWS9D%2FoaGKYNkjyrtbEXR%2FYDUMZOCMze2jNZ%2Bylzm2IMJFHiZa3GNrLzJQOP44nLJeyZgNdZnIGceet3T0ckWe%2F%2BYRJW79x3JhAP3JuAsP%2BXpxH21IgyC0URWCa0mOV2RSHOXr%2FBuyuOreMSNb0msZgMrI6L8gN%2BDJKnXfWo7juFWlj2EpBms5pBkoBfwWNdxps2l8U%2FXelTqu2%2FvsDTiqFJ7tSATSZ%2BkqgFgEJd%2BfaLNNsPEMJgBPYmYtqFuz2JJszXTqWryeLqvvsvmwK76R%2FqN3pVi2Vzs%2Fa0Kgdxb7O8dF6KZcDcayRp5DlLzmqVB7igsjyTAbnJb79hI1VYN7Q0hskaU88YMivINPVQ%2B81Q679V2kxO5PF1URW2o%2F%2FWjXxzokXWPHglMbwB8s79DYbAbECFS%2BGSXKDc8FNa0v1DQ41UiRbnYZOHasWvWVZsk2PQUAxrVfiia4DNvLOO1CBkXRFiVmJOB%2FwQ3BV52RljLq1g5Z2H%2Bm73%2FB1VbK94ZFrkG0C8id8t60Dl46pS0GZ76gb%3D%22%2C%22e%22%3A%22fA68dwnt5xSY-ISFf2ALDiXjTCDHluZNCbqmsr93MU02ufvery5t6e1OxIGoUHpc7a0IbkE_0FA-F5WgiEpV7aeWlyQyxr1LL83v6PCoc3YbWdFNpRGiSow97HJFmhSolqL2iP8Yg3b6GvpNCl1IVD5CbHA_K4aHo6z8QdDUQ9dbuRaeT7yGuHrKEK1fVWWjYizM9JlKkpiqJYbEB2zQGA%22%7D",
        "password": password,
        "reqtoken": reqtoken
    }
    result = demjson.decode(requests.post("https://2-class.com/api/user/login", cookies=cookies, json=payload).text)
    print(f"登陆到:{userName}")
    print(result)
    if not result['data']['result']:
        print(f"登陆失败\nErrorMesssage:{result['data']['errorMsg']}")
        raise RuntimeError(f"登陆失败\nErrorMesssage:{result['data']['errorMsg']}")
    driver.refresh()
    if isTeacher:
        data = driver.execute_script("return window.__DATA__.userInfo.department.gradeClassList[0]")
        return Teacher(reqtoken, cookies, data["gradeId"], data["className"], data["classId"], data["gradeName"])
    return User(reqtoken, cookies)


def CompetitionCommit(user, question) -> bool:
    payload = {
        "list":[{"questionContent":question.answer,"questionId":int(question.id)} for i in range(20)],
        "reqtoken": user.reqtoken,
        "time": 0
    }
    responseData = demjson.decode(requests.post("https://2-class.com/api/quiz/commit",cookies=user.cookies,json=payload).text)
    if not responseData['data']:
        raise RuntimeError(f"竞赛答题失败,ErrorMessage:{responseData['errorMsg']}")
    return True



def CommitCourse(user, course)->bool:
    payload={
        "courseId": course['id'],
        "exam": "course",
        "examCommitReqDataList":[{"answer": course['answer'][answerIndex], "examId": answerIndex+1} for answerIndex in range(len(course['answer']))],
        "reqtoken": user.reqtoken
    }
    data = demjson.decode(requests.post("https://2-class.com/api/exam/commit", cookies=user.cookies, json=payload).text)
    if not data['result']:raise RuntimeError(f"课程提交失败，ErrorMessage:{data['errorMsg']}")


def getCourseAnswer(courseId, user)->list:
    responseData = demjson.decode(requests.get(f"https://2-class.com/api/exam/getTestPaperList?courseId={courseId}", cookies=user.cookies).text)['data']
    if not responseData['result']:raise RuntimeError(f"无法获取课程答案, ErrorMessage:{responseData['errorMsg']}, CourseId: {courseId}")
    return [i['answer'] for i in responseData['testPaperList']]


def getCoursesList(TeacherUser)->list:
    responseData = demjson.decode(requests.get(f"https://2-class.com/api/course/getHomepageCourseList?grade={TeacherUser.gradeName}&pageSize=2&pageNo=1 ").text)
    if not responseData['data']:raise RuntimeError(f"无法获取课程,Errormessage:{responseData['errorMsg']}")
    return [course["id"] for course in responseData['data']['list']]


def resetStudentPassword(TeacherUser:Teacher, password:str) -> bool:
    payload = {
        "classId": TeacherUser.classId,
        "gradeId": TeacherUser.gradeId,
        "password": password,
        "reqtoken": TeacherUser.reqtoken,
        "role": "student"
        }
    responseData = demjson.decode(requests.post("https://2-class.com/api/user/updateTheSamePassword", cookies=TeacherUser.cookies, json=payload).text)
    if not responseData['data']:raise RuntimeError(f"学生密码重置失败，ErrorMessage:{responseData['errorMessage']}")
    return True


def getAllStudentInfo(TeacherUser)->list:
    print(requests.get(f"https://2-class.com/api/user/student/getStudentList?pageNo=1&pageSize=1&gradeId={TeacherUser.gradeId}&classId={TeacherUser.classId}&gradeName={TeacherUser.gradeName}&className={TeacherUser.className}").text)
    responseData = demjson.decode(requests.get(f"https://2-class.com/api/user/student/getStudentList?pageNo=1&pageSize=1&gradeId={TeacherUser.gradeId}&classId={TeacherUser.classId}&gradeName={TeacherUser.gradeName}&className={TeacherUser.className}").text)
    if not responseData['data']:
        raise RuntimeError(f"无法获取学生信息， ErrorMessage:{responseData['data']['errorMsg']}")
    studentTotalNum = responseData['data']["total"]
    responseData = demjson.decode(requests.get(f"https://2-class.com/api/user/student/getStudentList?pageNo=1&pageSize={studentTotalNum}&gradeId={TeacherUser.gradeId}&classId={TeacherUser.classId}&gradeName={TeacherUser.gradeName}&className={TeacherUser.className}").text)['data']["list"]
    return [{"account": student["account"], "realName": student["realName"]} for student in responseData]


def getCompetitionQuestion(User, grade, type)->dict:
    responseData = demjson.decode(requests.get(f"https://2-class.com/api/quiz/getQuestionList?gradeType={grade}", cookies=User.cookies).text)
    if not responseData['data']:raise RuntimeError(f"无法获取竞赛题目,ErrorMessage:{responseData['errorMsg']}")
    for question in responseData['data']['list']:
        if question['answerType'] == type:
            return {
                "questionId": question["id"],
                "questionTitle": question["questionTitle"],
                "questionContent": question["questionContent"]
            }
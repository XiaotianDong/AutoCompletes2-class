import Qingjiao2_class_APi, sys, demjson
# sys.argv[1] 教师账户
# sys.argv[2] 教师密码
# sys.argv[3] 学生重置目标密码

# Teacher Login
try:
    teacherAccount = Qingjiao2_class_APi(sys.argv[1],sys.argv[2], True)
except RuntimeError as e:
    print(f"Error! {str(e)} when login as teacher {sys.argv[1]} with password {sys.argv[2]}")
    exit()

#Reset Student's Password
Qingjiao2_class_APi.resetStudentPassword(teacherAccount, sys.argv[3])
question = {}

for student in Qingjiao2_class_APi.getAllStudentInfo(teacherAccount):
    studentAccount = Qingjiao2_class_APi.login(student['account'], sys.argv[3])
    try:
        question += demjson.decode(Qingjiao2_class_APi.getCompetitionQuestion(studentAccount, teacherAccount.gradeName, "单选题"))
    except RuntimeError as e:
        print(f"Error! {str(e)} when Get competition Question with Student Account {student['realName']}")
    else:
        open("QuestionToDisplay.txt",'w').write(f"Question Title: {question['questionTitle']}\nAnswer: {question['questionContent']}\nQuestionId:{question['questionId']}")

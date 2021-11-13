import Qingjiao2_class_APi, sys, demjson
# sys.argv[1] 由上一GitHubAction Steps获取的题目答案
# sys.argv[2] 教师账户
# sys.argv[3] 教师密码
# sys.argv[4] 学生重置目标密码
answer = sys.argv[1]
CourseAnswer = {}

question = demjson.decode(sys.argv[1])

try:
    teacherAccount = Qingjiao2_class_APi(sys.argv[2],sys.argv[3], True)
except RuntimeError as e:
    print(f"Error! {str(e)} when login as teacher {sys.argv[2]} with password {sys.argv[3]}")
    exit()


for student in Qingjiao2_class_APi.getAllStudentInfo(teacherAccount):
    print(f"Login Student {student['realName']}")
    studentAccount = Qingjiao2_class_APi.login(student['account'], sys.argv[4])

    print("提交禁毒竞赛...")
    if len(sys.argv < 4):
        try:
            Qingjiao2_class_APi.CompetitionCommit(studentAccount, {"id": question['id'], "answer": answer})
        except RuntimeError as e:
            print(f"Error! {str(e)} when Commit Competition")
        else:
            print(f"Student {student['realName']} 's Competition has successfully finished")
    
    print("获取课程...")

    for courseId in Qingjiao2_class_APi.getCoursesList(teacherAccount):
        if courseId not in CourseAnswer.keys():
            try:
                print("获取课程答案")
                CourseAnswer[courseId] = Qingjiao2_class_APi.getCourseAnswer(courseId, studentAccount)
            except RuntimeError as e:
                print(f"Error! {str(e)} when Get course Answer")
        try:
            Qingjiao2_class_APi.CommitCourse(studentAccount, {"id":courseId,"answer":CourseAnswer[courseId]})
        except RuntimeError as e:
            print(f"Error! {str(e)} when Commit Course")
        else:
            print(f"Student {student['realName']} 's Course {courseId} has successfully finished")

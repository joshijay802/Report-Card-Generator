import mysql.connector


mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='reportgenerator'
    )

mycursor=mydb.cursor()



def RegisterStudent(StudentData):
    
    sql="Insert into student_details values"+str(tuple(StudentData))
    mycursor.execute(sql)
    mydb.commit()

def RegisterTeacher(TeacherData):
    
    sql="Insert into teacher_details values"+str(tuple(TeacherData))
    mycursor.execute(sql)
    mydb.commit()

def checkTeacherLogin(username,password):
    sql="Select Password from teacher_details where Username = "+"'"+username+"'"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    if password==result[0][0]:
        return True
    return False
    
def checkStudentLogin(enroll,password):
    sql="Select Password from student_details where Enrollment_No  = "+"'"+enroll+"'"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    if password==result[0][0]:
        return True
    return False





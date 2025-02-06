from tkinter import messagebox
import pandas as pd 
import os

def getFilename(file_name):
    global filename
    filename=str(file_name)

def read_file():
    global df
    try:
        df = pd.read_excel(filename)
    except:
        messagebox.showerror("Error!","Please select an excel file!")

def getTotalStudents():
    global total_students
    total_students=len(df.iloc[:,0])   
    return total_students     

def SingleStudentData(i):
    try:
        Enrollment_No = df.iloc[:,0][i]
        FirstName=df.iloc[:,1][i]
        LastName=df.iloc[:,2][i]
        Sub1=df.iloc[:,3][i]
        Sub2=df.iloc[:,4][i]
        Sub3=df.iloc[:,5][i]
        Sub4=df.iloc[:,6][i]
        StudentData = [Enrollment_No,FirstName,LastName,Sub1,Sub2,Sub3,Sub4]
        return StudentData
    except:
        messagebox.showerror("Error!","Format of the data in the file may be invalid!")


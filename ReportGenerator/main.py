from ReportGenerator.data_extractor import SingleStudentData,read_file,getTotalStudents
from ReportGenerator.Report_card import generatePDF

def generateReport():
    read_file()
    for i in range(getTotalStudents()):
        StudentData = SingleStudentData(i)
        generatePDF(StudentData)
    

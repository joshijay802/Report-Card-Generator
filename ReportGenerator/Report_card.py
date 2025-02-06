from fpdf import FPDF

def generatePDF(StudentData):

    def calculatePercentage():
        per=(StudentData[3]+StudentData[4]+StudentData[5]+StudentData[6])/4
        if(per>=90):
            grade="O"
        elif(per>=80 and per<90):
            grade="A"
        elif(per>=70 and per<80):
            grade="B"
        elif(per>=60 and per<70):
            grade="C"
        elif(per>=50 and per<60):
            grade="D"
        elif(per>=40 and per<50):
            grade="E"
        elif(per<40):
            grade="F"
        result = [per,grade]
        return result
    result = calculatePercentage()
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)

    pdf.cell(190, 10, 'ITMBU',0,1,'C')
    pdf.cell(190, 10, 'School Of Computer Science and Engineering',0,1,'C')
    pdf.cell(190, 10, '______________________________________________________________',0,1,'C')

    pdf.set_font('Arial',size=10)
    pdf.cell(40, 10, 'Enrollment number ',0,0,'C')
    pdf.cell(5, 10, ': ',0,0,'C')
    pdf.cell(100,10,StudentData[0],0,1)
    pdf.cell(40, 10, 'Name ',0,0,'C')
    pdf.cell(5, 10, ': ',0,0,'C')
    pdf.cell(100,10,StudentData[1]+' '+StudentData[2],0,1)
    pdf.cell(40, 10, 'Semester ',0,0,'C')
    pdf.cell(5, 10, ': ',0,0,'C')
    pdf.cell(100,10,'III',0,1)
    pdf.cell(40, 10, 'Degree ',0,0,'C')
    pdf.cell(5, 10, ': ',0,0,'C')
    pdf.cell(100,10,'B.tech',0,1)
    pdf.cell(40, 10, 'School ',0,0,'C')
    pdf.cell(5, 10, ': ',0,0,'C')
    pdf.cell(100,10,'School of Computer Science Engineering and Technology',0,1)

    pdf.cell(190,20,' ',0,1)

    pdf.set_font('Arial', 'B', 14)

    pdf.cell(5,15,' ',0,0)
    pdf.cell(45,15,'Course Code',1,0,'C')
    pdf.cell(75,15,'Course Name',1,0,'C')
    pdf.cell(30,15,'Obtained',1,0,'C')
    pdf.cell(30,15,'Total Marks',1,1,'C')

    pdf.set_font('Arial',size=12)
    pdf.cell(5,15,' ',0,0)
    pdf.cell(45,15,'C221X02',1,0,'C')
    pdf.cell(75,15,'Object-Oriented programming in Java',1,0,'C')
    pdf.cell(30,15,str(StudentData[3]),1,0,'C')
    pdf.cell(30,15,'100',1,1,'C')

    pdf.cell(5,15,' ',0,0)
    pdf.cell(45,15,'C221X50',1,0,'C')
    pdf.cell(75,15,'System Software',1,0,'C')
    pdf.cell(30,15,str(StudentData[4]),1,0,'C')
    pdf.cell(30,15,'100',1,1,'C')

    pdf.cell(5,15,' ',0,0)
    pdf.cell(45,15,'C221X12',1,0,'C')
    pdf.cell(75,15,'Computer Architecture',1,0,'C')
    pdf.cell(30,15,str(StudentData[5]),1,0,'C')
    pdf.cell(30,15,'100',1,1,'C')

    pdf.cell(5,15,' ',0,0)
    pdf.cell(45,15,'C221X02',1,0,'C')
    pdf.cell(75,15,'Database Management Systems',1,0,'C')
    pdf.cell(30,15,str(StudentData[6]),1,0,'C')
    pdf.cell(30,15,'100',1,1,'C')

    pdf.cell(190,10,' ',0,1)

    pdf.set_font('Arial', 'B', 14)
    pdf.cell(45,15,' ',0,0)
    pdf.cell(100,15,'SEMESTER PERFORMANCE',1,1,'C')
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(45,10,' ',0,0)
    pdf.cell(50,10,'Average',1,0,'C')
    pdf.cell(50,10,'Grade',1,1,'C')
    pdf.set_font('Arial',size=12)
    pdf.cell(45,10,' ',0,0)
    pdf.cell(50,10,str(result[0]),1,0,'C')
    pdf.cell(50,10,str(result[1]),1,1,'C')

    pdf.cell(190,20,' ',0,1)

    pdf.cell(95,5,'21.01.2022',0,1,'C')
    pdf.cell(95,5,'_______________',0,0,'C')
    pdf.cell(95,5,'_______________',0,1,'C')
    pdf.cell(95,10,'Date',0,0,'C')
    pdf.cell(95,10,'Signature',0,1,'C')


    pdf.output(f'GeneratedPDF\ {StudentData[0]}_{StudentData[1]}_{StudentData[2]}.pdf','F')


from tkinter import *
from tkinter import messagebox
from database_connection import *
# from LoginPage import TeacherLoginform
def TeacherRegistrationForm():
    root=Tk()
    root.title("Teacher's Form")
    def center_screen():
        window_height = 600
        window_width = 600
        global screen_height, screen_width, x_cordinate, y_cordinate

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
            # Coordinates of the upper left corner of the window to make the window appear in the center
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    center_screen()



    Heading=Label(root,text="Teacher's Registration", font=('Arial',17),bg='orange',fg='white')
    Heading.place(x=0,y=10, width=600, height=50)

    uname=Label(root,text="Username : ")
    uname_data=Entry(root)
    uname.place(x=130 ,y=100 )
    uname_data.place(x=250 ,y=100 ,width=200)

    fname=Label(root,text="First Name : ")
    fname_data=Entry(root)
    fname.place(x=130 ,y=130 )
    fname_data.place(x=250 ,y=130 ,width=200)
    #-------------------------------------------------
    #email, branch, password
    lname=Label(root,text="Last Name : ")
    lname_data=Entry(root)
    lname.place(x=130 ,y=160 )
    lname_data.place(x=250 ,y=160 ,width=200)

    email=Label(root,text="Email ID : ")
    email_data=Entry(root)
    email.place(x=130 ,y=190 )
    email_data.place(x=250 ,y=190 ,width=200)

    branch=Label(root,text="Branch : ")
    branch_data=Entry(root)
    branch.place(x=130 ,y=220 )
    branch_data.place(x=250 ,y=220 ,width=200)

    contact=Label(root,text="Contact number : ")
    contact_data=Entry(root)
    contact.place(x=130 ,y=250 )
    contact_data.place(x=250 ,y=250 ,width=200)

    sem=Label(root,text="Department : ")
    sem_data=Entry(root)
    sem.place(x=130 ,y=280 )
    sem_data.place(x=250 ,y=280 ,width=200)

    school=Label(root,text="School : ")
    school_data=Entry(root)
    school.place(x=130 ,y=310 )
    school_data.place(x=250 ,y=310 ,width=200)

    password=Label(root,text="Password : ")
    password_data=Entry(root,show='*')
    password.place(x=130 ,y=340 )
    password_data.place(x=250 ,y=340 ,width=200)


    def clearVal():
        uname_data.delete(0,END)
        uname_data.insert(0, "")
        
        fname_data.delete(0,END)
        fname_data.insert(0, "")

        lname_data.delete(0,END)
        lname_data.insert(0, "")

        email_data.delete(0,END)
        email_data.insert(0, "")

        branch_data.delete(0,END)
        branch_data.insert(0, "")
        
        contact_data.delete(0,END)
        contact_data.insert(0, "")

        sem_data.delete(0,END)
        sem_data.insert(0, "")

        school_data.delete(0,END)
        school_data.insert(0, "")

        password_data.delete(0,END)
        password_data.insert(0, "")

    
    def submitDetails():
        teacher_details=[uname_data.get(),fname_data.get(),lname_data.get(),email_data.get(),
                        branch_data.get(),contact_data.get(),sem_data.get(),
                        school_data.get(),password_data.get()]
        
        try:
            RegisterTeacher(teacher_details)
            clearVal()
            root.destroy()
            # TeacherLoginform()
        except:
            messagebox.showerror("Error!","An error occured while submitting the data!")


    submit=Button(root,text="Submit", font=('Arial',15),bg='orange',command=submitDetails)
    submit.place(x=250 , y= 500)


    root.mainloop()

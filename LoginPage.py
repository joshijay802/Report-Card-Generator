from tkinter import *
from tkinter import messagebox
from database_connection import checkStudentLogin,checkTeacherLogin
from TeacherHome import TeacherHome
from Student_form import StudentRegistrationForm
from Teacher_form import TeacherRegistrationForm

# defining login function
def Teacherlogin():
    # getting form data
    uname = username.get()
    pwd = password.get()
    # applying empty validation
    if uname == '' or pwd == '':
        # Throw an error
        messagebox.showerror("Error!","A field cannot be empty!")
        
    else:
        try:
            if checkTeacherLogin(uname, pwd):
                message.set("Login success")
                login_screen.destroy()
                TeacherHome()

            else:
                # Throw an error
                messagebox.showerror("Error!","Wrong password!")
        except:
            messagebox.showerror("Error!","Incorrect Username!")

def StudentRegister():
    login_screen.destroy()
    StudentRegistrationForm()

def TeacherRegister():
    login_screen.destroy()
    TeacherRegistrationForm()


def Studentlogin():
    # getting form data
    enroll = enrollment_no.get()
    pwd = password.get()
    # applying empty validation
    if enroll == '' or pwd == '':
        # Throw an error
        messagebox.showerror("Error!","A field cannot be empty!")
        
    else:
        try:
            if checkStudentLogin(enroll,pwd):
                message.set("Login success")
            else:
                # Throw an error
                messagebox.showerror("Error!","Wrong password!")
        except:
            messagebox.showerror("Error!","Incorrect username!")



# defining destroy function
def Destroy_window():
    login_screen.destroy()


# defining loginform function


def TeacherLoginform():
    global login_screen
    login_screen = Tk()
    # Setting title of screen
    login_screen.title("Login Form")
    # setting height and width of screen
    def center_screen():
        window_height = 300
        window_width = 300
        global screen_height, screen_width, x_cordinate, y_cordinate

        screen_width = login_screen.winfo_screenwidth()
        screen_height = login_screen.winfo_screenheight()
            # Coordinates of the upper left corner of the window to make the window appear in the center
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        login_screen.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    center_screen()
    login_screen.resizable(False, False)
    # declaring variable
    global message
    global username
    global password
    username = StringVar()
    password = StringVar()
    message = StringVar()
    # Creating layout of login form
    Label(login_screen, width="300", text="Please enter details below",
          bg="orange", fg="white").pack()
    # Username Label
    Label(login_screen, text="Username * ").place(x=20, y=40)
    # Username textbox
    Entry(login_screen, textvariable=username).place(x=90, y=42)
    # Password Label
    Label(login_screen, text="Password * ").place(x=20, y=80)
    # Password textbox
    Entry(login_screen, textvariable=password, show="*").place(x=90, y=82)
    # Label for displaying login status[success/failed]
    Label(login_screen, text="", textvariable=message).place(x=95, y=100)
    # Login button
    Button(login_screen, text="Login", width=10, height=1,bg="orange", command=Teacherlogin).place(x=50, y=130)

    Label(login_screen, text="OR").place(x=150, y=135)

    Button(login_screen, text="Register", width=10, height=1,bg="orange", command=TeacherRegister).place(x=190, y=130)

    login_screen.mainloop()


def StudentLoginform():
    global login_screen
    login_screen = Tk()
    # Setting title of screen
    login_screen.title("Login Form")
    # setting height and width of screen
    def center_screen():
        window_height = 300
        window_width = 300
        global screen_height, screen_width, x_cordinate, y_cordinate

        screen_width = login_screen.winfo_screenwidth()
        screen_height = login_screen.winfo_screenheight()
            # Coordinates of the upper left corner of the window to make the window appear in the center
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        login_screen.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    center_screen()
    login_screen.resizable(False, False)
    # declaring variable
    global message
    global enrollment_no
    global password
    enrollment_no = StringVar()
    password = StringVar()
    message = StringVar()
    # Creating layout of login form
    Label(login_screen, width="300", text="Please enter details below",
          bg="orange", fg="white").pack()
    # Username Label
    Label(login_screen, text="Enrollment No * ").place(x=20, y=40)
    # Username textbox
    Entry(login_screen, textvariable=enrollment_no).place(x=115, y=42)
    # Password Label
    Label(login_screen, text="Password * ").place(x=20, y=80)
    # Password textbox
    Entry(login_screen, textvariable=password, show="*").place(x=115, y=82)
    # Label for displaying login status[success/failed]
    Label(login_screen, text="", textvariable=message).place(x=95, y=100)
    # Login button
    Button(login_screen, text="Login", width=10, height=1,bg="orange", command=Studentlogin).place(x=50, y=130)

    Label(login_screen, text="OR").place(x=150, y=135)

    Button(login_screen, text="Register", width=10, height=1,bg="orange", command=StudentRegister).place(x=190, y=130)

    login_screen.mainloop()


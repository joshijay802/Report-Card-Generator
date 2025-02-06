from tkinter import *
from tkinter import messagebox
from LoginPage import StudentLoginform,TeacherLoginform


def StartScreen():
    global main_screen
    main_screen = Tk()
    # Setting title of screen
    main_screen.title("Login Form")
    # setting height and width of screen
    def center_screen():
        window_height = 300
        window_width = 300
        global screen_height, screen_width, x_cordinate, y_cordinate

        screen_width = main_screen.winfo_screenwidth()
        screen_height = main_screen.winfo_screenheight()
            # Coordinates of the upper left corner of the window to make the window appear in the center
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        main_screen.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    center_screen()
    main_screen.resizable(False, False)

    Label(main_screen, width="300", text="Enter as a",
          bg="orange", fg="white").pack()

    def Destroy_window():
        main_screen.destroy()
    def callTeacherLogin():
        Destroy_window()
        TeacherLoginform()
    def callStudentLogin():
        Destroy_window()
        StudentLoginform()
    Button(main_screen, text="Teacher", width=10, height=1,bg="orange",command=callTeacherLogin).place(x=60, y=110)
    Button(main_screen, text="Student", width=10, height=1,bg="orange",command=callStudentLogin).place(x=160, y=110)
    main_screen.mainloop()

StartScreen()
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
from ReportGenerator.data_extractor import getFilename
from ReportGenerator.main import generateReport

def TeacherHome():
    global login_screen
    login_screen = Tk()
    # Setting title of screen
    login_screen.title("Home")
    # To open the screen in the center
    def center_screen():
        window_height = 400
        window_width = 400
        global screen_height, screen_width, x_cordinate, y_cordinate

        screen_width = login_screen.winfo_screenwidth()
        screen_height = login_screen.winfo_screenheight()
            # Coordinates of the upper left corner of the window to make the window appear in the center
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        login_screen.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    center_screen()

    # setting height and width of screen
    
    login_screen.resizable(False, False)
    
    # Creating layout of login form
    Label(login_screen, width="300", text="Teacher Admin Pannel",
          bg="orange", fg="white").pack()

    def select_file():
        global selected_file
        filetypes = (
            ('Excel files', '*.xlsx'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)
        selected_file = filename
        file_input.set(selected_file)

    def sendData():
        try:
            if file_input=="":
                messagebox.showerror("Error!","Please select a file!")
            else:
                getFilename(file_input.get())
                generateReport()
                file_input.set("")
                Label(login_screen, text="Report Card Generated").place(x=130, y=240)
        except:
            messagebox.showerror("Please try again!","An error occured while generating reports")

    file_input = StringVar()

    Label(login_screen, text="Select a file:").place(x=160, y=100)

    Entry(login_screen,textvariable=file_input).place(x=50, y=140,width=230)
    
    Button(login_screen, text="Open a file", width=10, height=1,bg="orange",command=select_file).place(x=285, y=140)

    Button(login_screen, text="Generate Report", width=20, height=1,bg="orange",command=sendData).place(x=120, y=180)
    login_screen.mainloop()

    
# TeacherHome()
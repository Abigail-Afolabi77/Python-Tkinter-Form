# import tkinter as tk
# window = tk.Tk()
# window.title("DATA ENTRY")
# window.mainloop()

# CREATING FRAME
# import tkinter as tk
# window = tk.Tk()
# window.title("DATA ENTRY")
# frame = tk.Frame(window)
# frame.pack()
# window.mainloop()

# LABELING A FRAME
# import tkinter as tk
# window = tk.Tk()
# window.title("DATA ENTRY")
# frame = tk.Frame(window)
# frame.pack()
# user_info = tk.LabelFrame(frame,
#                           text="USER'S INFORMATION")
# user_info.grid(row= 0, column= 0)
#
# window.mainloop()

# ADDING WIDGET INSIDE A FRAME
import tkinter as tk
# window = tk.Tk()
# window.title("DATA ENTRY")
# frame = tk.Frame(window)
# frame.pack()
# user_info = tk.LabelFrame(frame,
#                           text="USER'S INFORMATION")
# user_info.grid(row= 0, column= 0)
#
# firstname = tk.Label(user_info, text= "First Name")
# firstname.grid(row= 0, column= 0)
#
# firstname_entry = tk.Entry(user_info)
# firstname_entry.grid(row=1, column= 0)
#
# lastname = tk.Label(user_info, text= "Last Name")
# lastname.grid(row= 0, column= 1)
#
# lastname_entry = tk.Entry(user_info)
# lastname_entry.grid(row=1, column= 1)

# window.mainloop()

# COMBO BOX
# from tkinter import ttk
# window = tk.Tk()
# window.title("DATA ENTRY")
# frame = tk.Frame(window)
# frame.pack()
# user_info = tk.LabelFrame(frame,
#                           text="USER'S INFORMATION")
# user_info.grid(row= 0, column= 0)
#
# firstname = tk.Label(user_info, text= "First Name")
# firstname.grid(row= 0, column= 0)
#
# firstname_entry = tk.Entry(user_info)
# firstname_entry.grid(row=1, column= 0)
#
# lastname = tk.Label(user_info, text= "Last Name")
# lastname.grid(row= 0, column= 1)
#
# lastname_entry = tk.Entry(user_info)
# lastname_entry.grid(row=1, column= 1)
#
# title = tk.Label(user_info, text = "TITLE")
# title.grid(row= 0, column= 2)
# title_combobox = ttk.Combobox(user_info,
#                               values= ['','Mr','Mrs','Miss'])
# title_combobox.grid(row= 1, column= 2)
#
# window.mainloop()

# SPIN BOX
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
window = tk.Tk()
window.title("DATA ENTRY")
frame = tk.Frame(window)
frame.pack()

def enter_data():
    accept = accept_var.get()
    if accept == 'Accepted':

        fn = firstname_entry.get()
        ln = lastname_entry.get()

        # validating entry record
        if fn and ln:
            titles = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()

            # COURSES INFO
            numcourse = numcourses_spinbox.get()
            numsemester = numsemester_spinbox.get()

            # to be able to retrieve information from a checkbutton,
            # we will bind the checkbox to a variable
            registerInfo = register.get

            print(fn, ' ', ln, ' ', registerInfo)
            print('-'*40)
        else:
                tk.messagebox.showwarning(title= "Error",
                                          message="Firstname and Lastname are required")
    else:
            tk.messagebox.showwarning(title="Error",
                                      message="Terms and condition required")


user_info = tk.LabelFrame(frame,
                          text="USER'S INFORMATION")
user_info.grid(row= 0, column= 0)

firstname = tk.Label(user_info, text= "First Name")
firstname.grid(row= 0, column= 0)

firstname_entry = tk.Entry(user_info)
firstname_entry.grid(row=1, column= 0)

lastname = tk.Label(user_info, text= "Last Name")
lastname.grid(row= 0, column= 1)

lastname_entry = tk.Entry(user_info)
lastname_entry.grid(row=1, column= 1)

title = tk.Label(user_info, text = "TITLE")
title.grid(row= 0, column= 2)
title_combobox = ttk.Combobox(user_info,
                              values= ['','Mr','Mrs','Miss'])
title_combobox.grid(row= 1, column= 2)

age_label = tk.Label(user_info, text = "YEAR")
age_spinbox = tk.Spinbox(user_info, from_ = 1998, to= 2023)
age_label.grid(row= 2, column=0)
age_spinbox.grid(row= 3, column=0)

nationality_label = tk.Label(user_info,text= "NATIONANLITY")
nationality_combobox = ttk.Combobox(user_info,
                                   value= [' ' 'Nigerian', 'Ghanian','American'])
nationality_label.grid(row= 2, column= 1)
nationality_combobox.grid(row= 3, column = 1)

# ADDING SECOND FRAME
course_frame = tk.LabelFrame(frame,
                        text= "COURSES " 
                        "INFORMATION")
course_frame.grid(row= 1, column= 0,
                  sticky= "news", padx= 10,
                  pady= 5)

# WORKING WITH CHECK BUTTON
reg_label = tk.Label(course_frame,
                     text= "REGISTERATION")
reg_label.grid(row= 0, column=0)

register = tk.StringVar(value= "NOT REGISTERED")
reg_check = tk.Checkbutton(course_frame,
                           text= "Currently Registered",
                           variable= register,
                           onvalue= "Registered",
                           offvalue= "NOT REGISTERED")
reg_check.grid(row= 1, column= 0)
# COURSES COMPLETED
numcourses_label= tk.Label(course_frame,
                           text= '# Completed Courses')
numcourses_spinbox = tk.Spinbox(course_frame, from_= 0, to= "infinity")
numcourses_label.grid(row= 0, column= 1)
numcourses_spinbox.grid(row=1, column= 1)

# SEMESTER
numsemester_label = tk.Label(course_frame,
                             text = '# Semester')
numsemester_spinbox = \
    tk.Spinbox(course_frame, from_= 0, to= "infinity")
numsemester_label.grid(row= 0, column=2)
numsemester_spinbox.grid(row=1, column= 2)

# TERM
terms_frame = tk.LabelFrame(frame, text="TERMS AND CONDITION")
terms_frame.grid(row=2, column= 0,
                 sticky= "news", padx= 10, pady=5)

accept_var = tk.StringVar(value= "Not Accepted")
terms_check = tk.Checkbutton(terms_frame,
                             text= "I agree with the Terms and Condition",
                             variable = accept_var,
                             onvalue= "Accepted",
                             offvalue= "Not Accepted")
terms_check.grid(row=0, column= 0)

button= tk.Button(frame,text= "Enter data", command=enter_data)
button.grid(row= 3, column= 0, sticky= "news",
            padx= 10, pady=5)
for widget in user_info.winfo_children():
    widget.grid_configure(padx= 10, pady= 5)
for widget in course_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

window.mainloop()

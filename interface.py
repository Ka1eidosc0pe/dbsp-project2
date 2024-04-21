import tkinter as tk
from tkinter import messagebox
from explain import connect_to_database, explain_query, reset_values

# This is just a placeholder, will actually call the login function provided by JH, wherever this is called. We're just handing him the variables for login.
# def attemptLogin(success):
#     if (success):
#         print("Login successful!")
#         return True
#     else:
#         print("Login unsuccessful")
#         return False

# this is the function that will get executed when the login button is filled, we're not doing any validation checking as of yet. Needed? Get group advice.
def clickLogin():
    global connectObj

    host = host_entry.get()
    port = port_entry.get()
    db = db_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    #loginVar = True # this is only temporary, get rid of when using actual login process

    loginTuple = connect_to_database(host, port, db, username, password)
    loginSuccess = loginTuple[0]
    connectObj = loginTuple[1]

    if (loginSuccess):
        login_window.destroy()
        create_main_screen()
    else:
        messagebox.showerror("Login Failed", "Please check credentials and try again!")


def create_login_screen():
    global login_window, host_entry, port_entry, db_entry, username_entry, password_entry
    
    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry('520x300')

    tk.Label(login_window, text = "Host: ").grid(row = 0, column = 0)
    host_entry = tk.Entry(login_window)
    host_entry.grid(row = 0, column = 1)

    tk.Label(login_window, text = "Port: ").grid(row = 1, column = 0)
    port_entry = tk.Entry(login_window)
    port_entry.grid(row = 1, column = 1)

    tk.Label(login_window, text = "Database: ").grid(row = 2, column = 0)
    db_entry = tk.Entry(login_window)
    db_entry.grid(row = 2, column = 1)

    tk.Label(login_window, text = "Username: ").grid(row = 3, column = 0)
    username_entry = tk.Entry(login_window)
    username_entry.grid(row = 3, column = 1)

    tk.Label(login_window, text = "Password: ").grid(row = 4, column = 0)
    password_entry = tk.Entry(login_window, show = "*")
    password_entry.grid(row = 4, column = 1)

    login_button = tk.Button(login_window, text = "Login", command = clickLogin)
    login_button.grid(row = 5, column = 1)

    login_window.mainloop()


def create_main_screen():
    global main_window, query_text, qep_display, cost_display, explanation_display

    main_window = tk.Tk()
    main_window.title("Group 21 - Magic Cost Estimator")
    main_window.geometry("1200x1400")

    canvas = tk.Canvas(main_window)
    scrollbar = tk.Scrollbar(main_window, orient = "vertical", command = canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion = canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window = scrollable_frame, anchor = "nw")
    canvas.configure(yscrollcommand = scrollbar.set)

    tk.Label(scrollable_frame, text = "Query").pack()
    query_text = tk.Text(scrollable_frame, height = 20, width = 150, highlightbackground = "black", highlightcolor = "blue")
    query_text.pack(padx = 10, pady = 5, expand = True)

    calculate_button = tk.Button(scrollable_frame, text = "Calculate", command = clickCalculate)
    calculate_button.pack(pady = 15)

    tk.Label(scrollable_frame, text = "QEP Tree").pack()
    qep_display = tk.Text(scrollable_frame, height = 20, width = 150, highlightbackground = "black")
    qep_display.pack(pady = 10)
    qep_display.config(state = "disabled")

    tk.Label(scrollable_frame, text = "Cost").pack(pady = 5)
    cost_display = tk.Text(scrollable_frame, height = 20, width = 150, highlightbackground = "black")
    cost_display.pack(pady = 10)
    cost_display.config(state = "disabled")

    tk.Label(scrollable_frame, text = "Explanation").pack(pady = 5)
    explanation_display = tk.Text(scrollable_frame, height = 20, width = 150, highlightbackground = "black")
    explanation_display.pack(pady = 15)
    explanation_display.config(state = "disabled")

    reset_button = tk.Button(scrollable_frame, text = "Reset", command = clickReset)
    reset_button.pack()

    canvas.pack(side = "left", fill = "both", expand = True)
    scrollbar.pack(side = "right", fill = "y")

    main_window.mainloop()


def clickCalculate():

    # enable the text fields so that they can be populated
    qep_display.config(state = "normal")
    cost_display.config(state = "normal")
    explanation_display.config(state = "normal")

    query = query_text.get("1.0", "end-1c")

    explainOutputArray = explain_query(connectObj, query)

    #qep = getQEP(query)
    #cost = getEstimatedCost(query)
    #explanation = getCostExplanation(query)

    qep = explainOutputArray[0]
    cost = explainOutputArray[1]
    explanation = explainOutputArray[2]

    qep_display.delete("1.0", tk.END)
    qep_display.insert(tk.END, qep)

    cost_display.delete("1.0", tk.END)
    cost_display.insert(tk.END, cost)

    explanation_display.delete("1.0", tk.END)
    explanation_display.insert(tk.END, explanation)

    # disable text fields so cannot be edited after population
    qep_display.config(state = "disabled")
    cost_display.config(state = "disabled")
    explanation_display.config(state = "disabled")


def clickReset():

    # Reset node numbers in explain module
    reset_values()

    # enable the text fields so that they can be cleared
    qep_display.config(state = "normal")
    cost_display.config(state = "normal")
    explanation_display.config(state = "normal")

    query_text.delete("1.0", tk.END)

    qep_display.delete("1.0", tk.END)
    # qep_display.insert(tk.END, "Loading...")

    cost_display.delete("1.0", tk.END)
    # cost_display.insert(tk.END, "Loading...")

    explanation_display.delete("1.0", tk.END)
    # explanation_display.insert(tk.END, "Loading...")

    # disable text fields so cannot be edited after clearing
    qep_display.config(state = "disabled")
    cost_display.config(state = "disabled")
    explanation_display.config(state = "disabled")


# this is just a placeholder function for testing, in reality, a call to explain.py will be made which will provide the real value
def getQEP(query):
    print(query)
    return "test"

# this is just a placeholder for testing, in reality, a call to explain.py will be made which will provide the real value
def getEstimatedCost(query):
    print(query)
    return "3000"

# this is just a placeholder for testing, in reality, a call to explain.py will be made which will provide the real value
def getCostExplanation(query):
    print(query)
    return "some explanation"

# function call to kick off the entire flow
# create_login_screen()
import tkinter as tk
from tkinter import messagebox

# This is just a placeholder, will actually call the login function provided by JH, wherever this is called. We're just handing him the variables for login.
def attemptLogin(success):
    if (success):
        print("Login successful!")
        return True
    else:
        print("Login unsuccessful")
        return False

# this is the function that will get executed when the login button is filled, we're not doing any validation checking as of yet. Needed? Get group advice.
def clickLogin():
    host = host_entry.get()
    port = port_entry.get()
    db = db_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    loginVar = True # this is only temporary, get rid of when using actual login process

    if (attemptLogin(loginVar)):
        login_window.destroy()
        create_main_screen()
    else:
        messagebox.showerror("Login Failed", "Please check credentials and try again!")


def create_login_screen():
    global login_window, host_entry, port_entry, db_entry, username_entry, password_entry
    
    login_window = tk.Tk()
    login_window.title("Login")

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
    password_entry = tk.Entry(login_window)
    password_entry.grid(row = 4, column = 1)

    login_button = tk.Button(login_window, text = "Login", command = clickLogin)
    login_button.grid(row = 5, column = 1)

    login_window.mainloop()


def create_main_screen():
    global main_window, query_text, qep_display, cost_display, explanation_display

    main_window = tk.Tk()
    main_window.title("Main Screen")

    query_text = tk.Text(main_window, height = 5, width = 50)
    query_text.pack()

    calculate_button = tk.Button(main_window, text = "Calculate", command = clickCalculate)
    calculate_button.pack()

    qep_display = tk.Text(main_window, height = 5, width = 50)
    qep_display.pack()

    cost_display = tk.Text(main_window, height = 5, width = 50)
    cost_display.pack()

    explanation_display = tk.Text(main_window, height = 5, width = 50)
    explanation_display.pack()

    reset_button = tk.Button(main_window, text = "Reset", command = clickReset)
    reset_button.pack()

    main_window.mainloop()


def clickCalculate():
    query = query_text.get("1.0", "end-1c")

    qep = getQEP(query)
    cost = getEstimatedCost(query)
    explanation = getCostExplanation(query)

    qep_display.delete("1.0", tk.END)
    qep_display.insert(tk.END, qep)

    cost_display.delete("1.0", tk.END)
    cost_display.insert(tk.END, cost)

    explanation_display.delete("1.0", tk.END)
    explanation_display.insert(tk.END, explanation)


def clickReset():
    query_text.delete("1.0", tk.END)

    qep_display.delete("1.0", tk.END)
    qep_display.insert(tk.END, "Loading...")

    cost_display.delete("1.0", tk.END)
    cost_display.insert(tk.END, "Loading...")

    explanation_display.delete("1.0", tk.END)
    explanation_display.insert(tk.END, "Loading...")


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
create_login_screen()
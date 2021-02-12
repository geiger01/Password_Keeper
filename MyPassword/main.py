from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


def save():
    web_text=web_input.get()
    email_text=email_input.get()
    pass_text=password_input.get()
    new_data={web_text:{
        "email":email_text,
        "password": pass_text

    }
}

    if len(pass_text)==0 or len(web_text)==0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        
    else:
        try:
            with open("data.json", "r") as data_file:     
                data=json.load(data_file)

        except FileNotFoundError:
            with open('data.json', "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)

            with open("data.json","w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:  
            password_input.delete(0,END)
            web_input.delete(0,END)

def generate():
    password_input.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(6, 8)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    password_input.insert(0,password)
    pyperclip.copy(password)

def search():
    web_text= web_input.get()
    try:        
        with open("data.json") as data_file:
            data=json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    
    else:
        
        if web_text in data:
            email = data[web_text]["email"]
            password = data[web_text]["password"]
            messagebox.showinfo(title=web_text, message=f"Email: {email}\nPassword: {password}")
        else:   
            messagebox.showinfo(title="Error", message=f"No details for {web_text}")




    


window=Tk()
window.title("Mypass")
window.config(padx=50, pady=50)

web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label= Label(text="Password:")
password_label.grid(column=0, row=3)

add_button=Button(text="Add", width=14, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button=Button(text="Search", width=17, command=search)
search_button.grid(column=2, row=1, columnspan=2)

gen_pass=Button(text="Generate Password", width=14, command=generate)
gen_pass.grid(column=2, row=3)

web_input = Entry(width=17)
web_input.grid(column=1, row=1)
web_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "Something@gmail.com")

password_input = Entry(width=17)
password_input.grid(column=1, row=3)

canvas = Canvas(width=200, height= 200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

window.mainloop()

import json
import tkinter
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_numbers + password_letters + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")
    password_text.insert(0, f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_click():
    if len(password_text.get()) != 0 and len(mail_text.get()) != 0 and len(website_text.get()) != 0:
        is_ok = messagebox.askokcancel(title=website_text.get(),
                                       message=f"Your password: {password_text.get()}\n and mail: {mail_text.get()}")
        new_data = {
            website_text.get(): {
                "email": mail_text.get(),
                "password": password_text.get()
            }
        }
        if is_ok:
            try:
                with open("accounts.json", mode="r") as data_file1:
                    # read old data
                    data = json.load(data_file1)
            except FileNotFoundError:
                with open("accounts.json", "w") as data_file1:
                    json.dump(new_data, data_file1, indent=4)
            else:
                # update old data
                data.update(new_data)
                with open("accounts.json", mode="w") as data_file2:
                    json.dump(data, data_file2, indent=4)
            finally:
                website_text.delete(0, 'end')
                password_text.delete(0, 'end')
    else:
        messagebox.showinfo(message="Please Enter VALID mail, password and website name.")

# ---------------------------Search Password---------------------------#
def search_password():
    try:
        with open("accounts.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(message="Developer Error, Contact me @meMail")
    else:
        try:
            messagebox.showinfo(message=f"MailId:  {data[website_text.get().title()]['email']}\n Password:  {data[website_text.get().title()]['password']}")
        except KeyError:
            messagebox.showinfo(message="No such Account Found, GoAhead create one.")




# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = tkinter.Canvas(width=200, height=200)
lock_image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)

mail_label = tkinter.Label(text="Email/Username:")
mail_label.grid(row=2, column=0)

password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)

website_text = tkinter.Entry(width=21)
website_text.grid(row=1, column=1, sticky="EW")
website_text.focus()

mail_text = tkinter.Entry(width=35)
mail_text.grid(row=2, column=1, columnspan=2, sticky="EW")
mail_text.insert(0, "jalayadav@gmail.com")

password_text = tkinter.Entry(width=21)
password_text.grid(row=3, column=1, sticky="EW")

search_button = tkinter.Button(text="Search", command=search_password)
search_button.grid(row=1,column=2, sticky="EW")

generate_password = tkinter.Button(text="Generate Password", command=gen_password)
generate_password.grid(row=3, column=2, sticky="EW")

add_button = tkinter.Button(text="ADD", width=36, command=add_click)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()

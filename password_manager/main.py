
from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():
    pass_input.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for n in range(randint(8, 10))]
    password_list += [choice(symbols) for n in range(randint(2, 4))]
    password_list += [choice(numbers) for n in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    pass_input.insert(END, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = user_input.get()
    pw = pass_input.get()
    new_data = {
        website:{
            "email":email,
            "password":pw,
        }
    }

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n"
                                                  f"Email: {email}\nPassword: {pw}\n"
                                                  f"Is it okay to save?")
    if is_ok:
        if len(website) == 0 or len(email) == 0 or len(pw) == 0:
            messagebox.showerror(title="Opps", message="Please don't leave any fields empty!")
        else:

            try:
                with open("data.json", "r") as fp:
                    # reading data
                    data = json.load(fp)

            except FileNotFoundError:
                with open("data.json", "w") as fp:
                    # create new file
                    json.dump(new_data, fp, indent=4)
            else:
                # updating data
                data.update(new_data)
                with open("data.json", "w") as fp:
                    # saving updated data
                    json.dump(data ,fp ,indent=4)
            finally:
                website_input.delete(0,END)
                pass_input.delete(0,END)


def find_password():
    input = website_input.get()
    try:
        with open("data.json", "r") as fp:
            seach_data = json.load(fp)
            website = seach_data[website_input.get()]
            messagebox.showinfo(title=website_input.get(), message=f"Email: {website['email']}\n"
                                                                   f"Password: {website['password']}")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data file Found")
    except KeyError:
        messagebox.showerror(title="Error", message=f"No detail for {input} exist")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50,padx=50)


canvas = Canvas(width=200, height=200)
img = PhotoImage(file = "logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(column=1, row=0)

website_label= Label(text="Website:")
website_label.grid(column=0,row=1)
website_input = Entry(width=20)
website_input.grid(column=1,row=1)
website_input.focus()

user_label= Label(text="Email/Username:")
user_label.grid(column=0,row=2)
user_input = Entry(width=38)
user_input.grid(column=1,row=2,columnspan=2)
user_input.insert(0,"your_email@email.com")

pass_label= Label(text="Password:")
pass_label.grid(column=0,row=3)
pass_input = Entry(width=20)
pass_input.grid(column=1,row=3)

generate_button = Button(text="Generate Password", command=generate_password, width= 14)
generate_button.grid(column=2,row=3)

add_button =Button(text= "Add",width=35, command=save)
add_button.grid(column=1,row=4,columnspan=2)

search_button= Button(text ="search", width=14,command=find_password)
search_button.grid(column=2,row=1)

window.mainloop()
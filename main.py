import tkinter as tk
from PIL import Image, ImageTk
import json


def rgb(r, g ,b):
    tuple = (r, g, b)
    return "#%02x%02x%02x" % tuple


class App(tk.Tk):


    position_list = [[0.1, 0.1]]  # user tab positions
    step_x = 0.15
    step_y = 0.4
    ind = 0  # total number of users
    user_amt_row = 0  # how many users in 1 row
    button_color = rgb(0, 126, 100)


    def __init__(self):
        tk.Tk.__init__(self)

        self.title("Notebook")
        self.geometry("1366x786")

        self.label = tk.Label(self)
        self.imgg = Image.open(r"images\backgroundas.png")
        self.label.img = ImageTk.PhotoImage(self.imgg)
        self.label['image'] = self.label.img
        self.label.place(relwidth=1, relheight=1, relx=0, rely=0)


        self.laukelis_add = tk.Frame(self, bg=rgb(49, 164, 125))
        self.laukelis_add.place(

            relwidth=0.1464,
            relheight=0.395,
            relx=self.position_list[0][0],
            rely=self.position_list[0][1]
        )

        self.add_button = tk.Button(self.laukelis_add, command=self.new_user,
        bg="blue"
        )

        self.add_button.place(relx=0.5, rely=0.5, anchor="center")
        self.load_users()

    # coordinates of widgets
    @classmethod
    def coords(cls):
        cls.user_amt_row += 1

        if cls.user_amt_row == 6:
            cls.position_list[cls.ind][0] = 0.1
            cls.position_list.append([cls.position_list[cls.ind][0], cls.position_list[cls.ind][1] + cls.step_y])
            cls.user_amt_row = 0
        else:
            cls.position_list.append([cls.position_list[cls.ind][0] + cls.step_x, cls.position_list[cls.ind][1]])
        cls.ind += 1


    def new_user(self):

        self.coords()
        self.laukelis_add.place_forget()

        self.laukelis_add.place(
        relwidth=0.1464,
        relheight=0.395,
        relx=self.position_list[self.ind][0],
        rely=self.position_list[self.ind][1]
        )

        self.user = User_frame()
        self.user.place(
        relx=self.position_list[self.ind - 1][0],
        rely=self.position_list[self.ind - 1][1],
        relwidth=0.1464,
        relheight=0.395
    )

    def load_users(self):
        self.data = Json_writer.read_json(self, "data.json")
        for _ in range(len(self.data["users"])):
            self.new_user()





class Json_writer:

    def write_json(self, data, filename):
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)


    def read_json(self, filename):
        with open(filename) as f:
            self.data = json.load(f)
            return self.data


    def add_user(self, filename, json_element):
        self.data = Json_writer.read_json(self, filename)
        self.data["users"].append(json_element)
        Json_writer.write_json(self, self.data, filename)


    def delete_user(self, filename, index):
        self.data = Json_writer.read_json(self, filename)
        del self.data["users"][index]
        Json_writer.write_json(self, self.data, filename)




# Keeping track of frames
class User_frame(tk.Frame):

    counter = 0
    widgets = []

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        User_frame.counter += 1
        self.widgets.append(self)
        #class variables
        self.dist = 0.05
        self.dist_xent = 0.4

        self["bg"] = rgb(49, 164, 125)

        label_color = rgb(49, 164, 125)
        self.vardas = tk.Label(self, text="Vardas:", bg=label_color)  # data[i]["vardas"]
        self.vardas.place(relx=self.dist, rely=0.2)
        self.pavarde = tk.Label(self, text="Pavardė:", bg=label_color)
        self.pavarde.place(relx=self.dist, rely=0.3)
        self.adresas = tk.Label(self, text="Adresas:", bg=label_color)
        self.adresas.place(relx=self.dist, rely=0.4)
        self.email = tk.Label(self, text="El. paštas:", bg=label_color)
        self.email.place(relx=self.dist, rely=0.5)
        self.numeris = tk.Label(self, text="Tel. nr.:", bg=label_color)
        self.numeris.place(relx=self.dist, rely=0.6)

        entry_color = rgb(0, 190, 151)
        self.ent_vardas = tk.Entry(self, state="normal", bg=entry_color)  # data[i]["vardas"]
        self.ent_vardas.place(relx=self.dist_xent, rely=0.2)
        self.ent_pavarde = tk.Entry(self, state="normal", bg=entry_color)
        self.ent_pavarde.place(relx=self.dist_xent, rely=0.3)
        self.ent_adresas = tk.Entry(self, state="normal", bg=entry_color)
        self.ent_adresas.place(relx=self.dist_xent, rely=0.4)
        self.ent_email = tk.Entry(self, state="normal", bg=entry_color)
        self.ent_email.place(relx=self.dist_xent, rely=0.5)
        self.ent_numeris = tk.Entry(self, state="normal", bg=entry_color)
        self.ent_numeris.place(relx=self.dist_xent, rely=0.6)

        self.b_edit = tk.Button(self, text="edit", command=self.edit_b_command,
        bg=App.button_color)
        self.b_edit_img = Image.open(r"images\edit-mazas.ico")
        self.b_edit.img = ImageTk.PhotoImage(self.b_edit_img)
        self.b_edit.config(image=self.b_edit.img)
        self.b_edit.place(relx=0.5)

        self.b_del = tk.Button(self, text="delete", command=self.delete_widget,
        bg=App.button_color)
        self.b_del_img = Image.open(r"images\Delete-mazas.ico")
        self.b_del.img = ImageTk.PhotoImage(self.b_del_img)
        self.b_del.config(image=self.b_del.img)
        self.b_del.place(relx=0.75)

        self.b_ok = tk.Button(self, text="OK", command=self.b_ok_command,
        bg=App.button_color)
        self.b_ok_img = Image.open(r"images\OK-mazas.ico")
        self.b_ok.img = ImageTk.PhotoImage(self.b_ok_img)
        self.b_ok.config(image=self.b_ok.img)



    def deactivate(self):
        self.ent_vardas["state"] = "disabled"
        self.ent_pavarde["state"] = "disabled"
        self.ent_adresas["state"] = "disabled"
        self.ent_email["state"] = "disabled"
        self.ent_numeris["state"] = "disabled"


    def activate(self):
        self.ent_vardas["state"] = "normal"
        self.ent_pavarde["state"] = "normal"
        self.ent_adresas["state"] = "normal"
        self.ent_email["state"] = "normal"
        self.ent_numeris["state"] = "normal"


    def edit_b_command(self):
        self.b_edit.place_forget()
        self.b_ok.place(relx=0.5)
        self.activate()


    def b_ok_command(self):
        self.b_ok.place_forget()
        self.b_edit.place(relx=0.5)


        self.temp_dict = {

            "vardas": self.ent_vardas.get(),
            "pavarde": self.ent_pavarde.get(),
            "adresas": self.ent_adresas.get(),
            "el_pastas" : self.ent_email.get(),
            "tel_nr": self.ent_numeris.get()
        }


        Json_writer.add_user(self, "data.json", self.temp_dict)
        self.deactivate()


    def delete_widget(self):

        self.place_forget()
        Json_writer.delete_user(self, "data.json", 0)


if __name__ == "__main__":
    root = App()
    root.mainloop()

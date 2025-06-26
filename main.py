import tkinter as tk
from PIL import Image, ImageTk
import json


def rgb(r, g, b):
    return "#%02x%02x%02x" % (r, g, b)


class JsonWriter:
    @staticmethod
    def write_json(data, filename):
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def read_json(filename):
        with open(filename) as f:
            return json.load(f)

    @staticmethod
    def add_user(filename, json_element):
        data = JsonWriter.read_json(filename)
        data["users"].append(json_element)
        JsonWriter.write_json(data, filename)

    @staticmethod
    def delete_user(filename, index):
        data = JsonWriter.read_json(filename)
        del data["users"][index]
        JsonWriter.write_json(data, filename)


class ContactFrame(tk.Frame):
    def __init__(self, master, user_data=None, on_delete=None, on_update=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.on_delete = on_delete
        self.on_update = on_update
        self.user_data = user_data or {
            "first_name": "",
            "last_name": "",
            "address": "",
            "email": "",
            "phone_number": ""
        }
        self["bg"] = rgb(49, 164, 125)
        label_color = rgb(49, 164, 125)
        entry_color = rgb(0, 190, 151)
        self.dist = 0.05
        self.dist_xent = 0.4
        # Labels
        self.first_name = tk.Label(self, text="First Name:", bg=label_color)
        self.first_name.place(relx=self.dist, rely=0.2)
        self.last_name = tk.Label(self, text="Last Name:", bg=label_color)
        self.last_name.place(relx=self.dist, rely=0.3)
        self.address = tk.Label(self, text="Address:", bg=label_color)
        self.address.place(relx=self.dist, rely=0.4)
        self.email = tk.Label(self, text="Email:", bg=label_color)
        self.email.place(relx=self.dist, rely=0.5)
        self.phone_number = tk.Label(self, text="Phone Nr:", bg=label_color)
        self.phone_number.place(relx=self.dist, rely=0.6)
        # Entries
        self.ent_first_name = tk.Entry(self, state="disabled", bg=entry_color)
        self.ent_first_name.place(relx=self.dist_xent, rely=0.2)
        self.ent_last_name = tk.Entry(self, state="disabled", bg=entry_color)
        self.ent_last_name.place(relx=self.dist_xent, rely=0.3)
        self.ent_address = tk.Entry(self, state="disabled", bg=entry_color)
        self.ent_address.place(relx=self.dist_xent, rely=0.4)
        self.ent_email = tk.Entry(self, state="disabled", bg=entry_color)
        self.ent_email.place(relx=self.dist_xent, rely=0.5)
        self.ent_phone_number = tk.Entry(self, state="disabled", bg=entry_color)
        self.ent_phone_number.place(relx=self.dist_xent, rely=0.6)
        # Fill entries if data is provided
        self.set_fields(self.user_data)
        # Buttons
        self.b_edit = tk.Button(self, command=self.edit_b_command, bg=App.button_color)
        self.b_edit_img = Image.open(r"images/edit-contact.ico")
        self.b_edit.img = ImageTk.PhotoImage(self.b_edit_img)
        self.b_edit.config(image=self.b_edit.img)
        self.b_edit.place(relx=0.5)
        self.b_del = tk.Button(self, command=self.delete_widget, bg=App.button_color)
        self.b_del_img = Image.open(r"images/delete-contact.ico")
        self.b_del.img = ImageTk.PhotoImage(self.b_del_img)
        self.b_del.config(image=self.b_del.img)
        self.b_del.place(relx=0.75)
        self.b_ok = tk.Button(self, command=self.b_ok_command, bg=App.button_color)
        self.b_ok_img = Image.open(r"images/ok-contact.ico")
        self.b_ok.img = ImageTk.PhotoImage(self.b_ok_img)
        self.b_ok.config(image=self.b_ok.img)
        # self.b_ok is not placed initially

    def set_fields(self, data):
        self.ent_first_name.config(state="normal")
        self.ent_last_name.config(state="normal")
        self.ent_address.config(state="normal")
        self.ent_email.config(state="normal")
        self.ent_phone_number.config(state="normal")
        self.ent_first_name.delete(0, tk.END)
        self.ent_first_name.insert(0, data.get("first_name", ""))
        self.ent_last_name.delete(0, tk.END)
        self.ent_last_name.insert(0, data.get("last_name", ""))
        self.ent_address.delete(0, tk.END)
        self.ent_address.insert(0, data.get("address", ""))
        self.ent_email.delete(0, tk.END)
        self.ent_email.insert(0, data.get("email", ""))
        self.ent_phone_number.delete(0, tk.END)
        self.ent_phone_number.insert(0, data.get("phone_number", ""))
        self.ent_first_name.config(state="disabled")
        self.ent_last_name.config(state="disabled")
        self.ent_address.config(state="disabled")
        self.ent_email.config(state="disabled")
        self.ent_phone_number.config(state="disabled")

    def activate(self):
        self.ent_first_name["state"] = "normal"
        self.ent_last_name["state"] = "normal"
        self.ent_address["state"] = "normal"
        self.ent_email["state"] = "normal"
        self.ent_phone_number["state"] = "normal"

    def deactivate(self):
        self.ent_first_name["state"] = "disabled"
        self.ent_last_name["state"] = "disabled"
        self.ent_address["state"] = "disabled"
        self.ent_email["state"] = "disabled"
        self.ent_phone_number["state"] = "disabled"

    def edit_b_command(self):
        self.b_edit.place_forget()
        self.b_ok.place(relx=0.5)
        self.activate()

    def b_ok_command(self):
        self.b_ok.place_forget()
        self.b_edit.place(relx=0.5)
        self.deactivate()
        # Update user data
        self.user_data = {
            "first_name": self.ent_first_name.get(),
            "last_name": self.ent_last_name.get(),
            "address": self.ent_address.get(),
            "email": self.ent_email.get(),
            "phone_number": self.ent_phone_number.get()
        }
        if self.on_update:
            self.on_update(self)

    def delete_widget(self):
        if self.on_delete:
            self.on_delete(self)


class App(tk.Tk):
    button_color = rgb(0, 126, 100)
    step_x = 0.15
    step_y = 0.4
    max_per_row = 6

    def __init__(self):
        super().__init__()
        self.title("Notebook")
        self.geometry("1366x786")
        # Background
        self.label = tk.Label(self)
        self.imgg = Image.open(r"images/background.png")
        self.label.img = ImageTk.PhotoImage(self.imgg)
        self.label['image'] = self.label.img
        self.label.place(relwidth=1, relheight=1, relx=0, rely=0)
        # User frames
        self.user_frames = []
        # Add button frame
        self.add_frame = tk.Frame(self, bg=rgb(49, 164, 125))
        self.add_button = tk.Button(self.add_frame, command=self.add_user, bg=App.button_color)
        self.add_img = Image.open(r"images/add-contact.ico")
        self.add_button.img = ImageTk.PhotoImage(self.add_img)
        self.add_button.config(image=self.add_button.img)
        self.add_button.place(relx=0.5, rely=0.5, anchor="center")
        # Load users from file
        self.data_file = "data.json"
        self.load_users()

    def get_position(self, idx):
        row = idx // self.max_per_row
        col = idx % self.max_per_row
        relx = 0.1 + col * self.step_x
        rely = 0.1 + row * self.step_y
        return relx, rely

    def render_widgets(self):
        # Remove all user frames and add_frame from UI
        for frame in self.user_frames:
            frame.place_forget()
        self.add_frame.place_forget()
        # Place user frames
        for idx, frame in enumerate(self.user_frames):
            relx, rely = self.get_position(idx)
            frame.place(relx=relx, rely=rely, relwidth=0.1464, relheight=0.395)
        # Place add button after last user (always visible)
        relx, rely = self.get_position(len(self.user_frames))
        self.add_frame.place(relx=relx, rely=rely, relwidth=0.1464, relheight=0.395)

    def load_users(self):
        # Remove any existing user frames from UI and memory
        for frame in self.user_frames:
            frame.place_forget()
            frame.destroy()
        self.user_frames.clear()
        try:
            data = JsonWriter.read_json(self.data_file)
            users = data.get("users", [])
        except Exception:
            users = []
        for user_data in users:
            frame = ContactFrame(self, user_data=user_data, on_delete=self.delete_user, on_update=self.update_user)
            self.user_frames.append(frame)
        self.render_widgets()

    def add_user(self):
        # Add a new user with empty fields
        new_user = {
            "first_name": "",
            "last_name": "",
            "address": "",
            "email": "",
            "phone_number": ""
        }
        frame = ContactFrame(self, user_data=new_user, on_delete=self.delete_user, on_update=self.update_user)
        self.user_frames.append(frame)
        self.render_widgets()
        # Ensure the new frame is visible and editable
        frame.edit_b_command()

    def delete_user(self, frame):
        if frame in self.user_frames:
            self.user_frames.remove(frame)
            frame.place_forget()
            frame.destroy()
            self.save_all_users()
            self.render_widgets()
        else:
            # Defensive: ignore if frame is not in list
            pass

    def update_user(self, frame):
        # Save all users when one is updated
        self.save_all_users()

    def save_all_users(self):
        users = [frame.user_data for frame in self.user_frames]
        data = {"users": users}
        JsonWriter.write_json(data, self.data_file)


if __name__ == "__main__":
    root = App()
    root.mainloop()

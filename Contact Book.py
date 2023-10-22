import tkinter as tk

# Function to add a contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    contact_list.insert(tk.END, f"{name}: {phone}")
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

# Function to delete a contact
def delete_contact():
    selected_contact = contact_list.get(tk.ACTIVE)
    contact_list.delete(tk.ACTIVE)

# Function to search for a contact
def search_contact():
    search_term = search_entry.get()
    for i in range(contact_list.size()):
        if search_term in contact_list.get(i):
            contact_list.selection_clear(0, tk.END)
            contact_list.select_set(i)

# Function to edit a contact
def edit_contact():
    selected_contact = contact_list.get(tk.ACTIVE)
    name, phone = selected_contact.split(": ")
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    name_entry.insert(0, name)
    phone_entry.insert(0, phone)
    delete_contact()

# Create the main window
root = tk.Tk()
root.title("Contact Book")

# Create entry fields for name and phone number
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

phone_label = tk.Label(root, text="Phone:")
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

# Create buttons for add, delete, search, and edit
add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.pack()

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.pack()

search_button = tk.Button(root, text="Search Contact", command=search_contact)
search_button.pack()

edit_button = tk.Button(root, text="Edit Contact", command=edit_contact)
edit_button.pack()

# Create a listbox to display contacts
contact_list = tk.Listbox(root)
contact_list.pack()

# Entry field for searching contacts
search_label = tk.Label(root, text="Search:")
search_label.pack()
search_entry = tk.Entry(root)
search_entry.pack()

# Start the GUI application
root.mainloop()
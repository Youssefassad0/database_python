import pyodbc
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from table import open_table_creation_window  # Import the function from table.py

class DeleteDB:
    def __init__(self, root, show_frame, main_menu_frame):
        self.frame = ctk.CTkFrame(root, fg_color="#2b2b2b")  # Dark gray background
        self.show_frame = show_frame
        self.main_menu_frame = main_menu_frame
        
        # Ensure the frame occupies the full window
        self.frame.grid(row=0, column=0, sticky='nsew')

        # Create and configure widgets
        self.create_widgets()

    def create_widgets(self):
        # Database name entry
        self.entry_label = ctk.CTkLabel(self.frame, text="Database Name:", text_color="white", fg_color="#2b2b2b")
        self.entry_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        self.entry_database = ctk.CTkEntry(self.frame, placeholder_text="Enter database name")
        self.entry_database.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

        # Info label
        self.info_label = ctk.CTkLabel(self.frame, text="", text_color="white", fg_color="#2b2b2b")
        self.info_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='w')

        self.delete_button = ctk.CTkButton(self.frame, text="Delete Database", command=self.confirm_delete_db)
        self.delete_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

        # Back button
        self.back_button = ctk.CTkButton(self.frame, text="Back to Menu", command=self.back_to_menu)
        self.back_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

        # Configure grid columns and rows to resize properly
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_rowconfigure(2, weight=1)

    def back_to_menu(self):
        self.show_frame(self.main_menu_frame)

    def validate_entry(self):
        return self.entry_database.get().strip() != ""

    def confirm_delete_db(self):
        if not self.validate_entry():
            self.info_label.configure(text="Please enter a database name", text_color="red")
            return

        database_name = self.entry_database.get()
        # Show confirmation dialog
        if messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete the database '{database_name}'? This action cannot be undone."):
            self.delete_db()

    def delete_db(self):
        database_name = self.entry_database.get()
        connection = None
        try:
            connection = pyodbc.connect(
                'DRIVER={SQL Server};'
                'Server=localhost;'
                'Database=master;'
                'Trusted_Connection=True;'
            )
            connection.autocommit = True
            cursor = connection.cursor()
            cursor.execute(f'DROP DATABASE {database_name}')
            self.info_label.configure(text="Database deleted", text_color="green")

        except pyodbc.Error as ex:
            print('Connection failed:', ex)
            self.info_label.configure(text="database don't exists", text_color="red")

        finally:
            if connection:
                connection.close()
                print("Connection closed")

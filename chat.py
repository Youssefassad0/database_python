import pyodbc
import customtkinter as ctk
import tkinter
from table import open_table_creation_window  # Import the function from table.py

class DatabaseManagement:
    def __init__(self, root, show_frame, main_menu_frame):
        self.frame = ctk.CTkFrame(root, fg_color="#2b2b2b")  # Dark gray background
        self.show_frame = show_frame
        self.main_menu_frame = main_menu_frame

        # Ensure the frame occupies the full window
        self.frame.grid(row=0, column=0, sticky='nsew')

        # Create and pack the database entry
        self.entry_database = ctk.CTkEntry(self.frame, placeholder_text="Enter database name", fg_color="#3b3b3b", text_color="white")
        self.entry_database.pack(pady=20, padx=20)

        # Create a label for displaying connection status
        self.info_label = ctk.CTkLabel(self.frame, text="", text_color="white")
        self.info_label.place(relx=0.1, rely=0.9)  # Adjusted the position

        # Buttons
        self.create_button = ctk.CTkButton(self.frame, text="Create Database", command=self.create_db, fg_color="#1f6aa5", hover_color="#144d78")
        self.create_button.pack(pady=10)

        self.connect_button = ctk.CTkButton(self.frame, text="Connect to Database", command=self.connect_db, fg_color="#1f6aa5", hover_color="#144d78")
        self.connect_button.pack(pady=10)

        # Back Button to return to the main menu
        self.back_button = ctk.CTkButton(
            self.frame, text="Back to Menu", command=self.back_to_menu, corner_radius=32,
            fg_color="#c850c0", hover_color="#4158d0"
        )
        self.back_button.pack(pady=1)

    def back_to_menu(self):
        self.show_frame(self.main_menu_frame)

    def validate_entry(self):
        return self.entry_database.get().strip() != ""

    def create_db(self):
        if not self.validate_entry():
            self.info_label.configure(text="Please enter a database name", text_color="red")
            return

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
            cursor.execute(f'CREATE DATABASE {database_name}')
            self.info_label.configure(text="Database created", text_color="green")

        except pyodbc.Error as ex:
            print('Connection failed:', ex)
            self.info_label.configure(text="Creation Failed", text_color="red")

        finally:
            if connection:
                connection.close()
                print("Connection closed")

    def connect_db(self):
        if not self.validate_entry():
            self.info_label.configure(text="Please enter a database name", text_color="red")
            return

        database_name = self.entry_database.get()
        connection = None
        try:
            connection = pyodbc.connect(
                'DRIVER={SQL Server};'
                'Server=localhost;'
                f'Database={database_name};'
                'Trusted_Connection=True;'
            )
            self.info_label.configure(text="Connection successful", text_color="green")

            # Open the table creation window
            open_table_creation_window(connection)

        except pyodbc.Error as ex:
            print('Connection failed:', ex)
            self.info_label.configure(text="Connection Failed", text_color="red")

        finally:
            if connection:
                connection.close()
                print("Connection closed")

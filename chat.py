import pyodbc
import customtkinter as ctk

class DatabaseManagement:
    def __init__(self, root):
        self.frame = ctk.CTkFrame(root)
        
        # Create and pack the database entry
        self.entry_database = ctk.CTkEntry(self.frame, placeholder_text="Enter database name")
        self.entry_database.pack(pady=20, padx=20)
        
        # Create a label for displaying connection status
        self.info_label = ctk.CTkLabel(self.frame, text="", text_color="black")
        self.info_label.place(relx=0.1, rely=0.9)  # Adjusted the position
        
        # Buttons
        self.create_button = ctk.CTkButton(self.frame, text="Create Database", command=self.create_db, fg_color="black")
        self.create_button.pack(pady=10)
        
        self.connect_button = ctk.CTkButton(self.frame, text="Connect to Database", command=self.connect_db, fg_color="green")
        self.connect_button.pack(pady=10)

        # Back Button to return to the main menu
        self.back_button = ctk.CTkButton(self.frame, text="Back to Menu", command=lambda: self.frame.tkraise())
        self.back_button.pack(pady=10)

    def validate_entry(self):
        return self.entry_database.get().strip() != ""

    def create_db(self):
        if not self.validate_entry():
            self.info_label.configure(text="Please enter a database name", text_color="red")
            return
        
        try:
            database_name = self.entry_database.get()  # Use the entry widget to get the database name
            # Connect to the database
            connection = pyodbc.connect(
                'DRIVER={SQL Server};'
                'Server=localhost;'  # Replace with the full server name if necessary
                f'Database=master;'
                'Trusted_Connection=True;'
            )
            connection.autocommit = True
            connection.execute(f'CREATE DATABASE {database_name}')
            self.info_label.configure(text="Database created", text_color="green")
        
        except pyodbc.Error as ex:
            print('Connection failed:', ex)
            self.info_label.configure(text="Creation Failed", text_color="red")
        
        finally:
            try:
                connection.close()
                print("Connection closed")
            except NameError:
                pass

    def connect_db(self):
        if not self.validate_entry():
            self.info_label.configure(text="Please enter a database name", text_color="red")
            return
        
        try:
            database_name = self.entry_database.get()  # Use the entry widget to get the database name
            # Connect to the database
            connection = pyodbc.connect(
                'DRIVER={SQL Server};'
                'Server=localhost;'  # Replace with the full server name if necessary
                f'Database={database_name};'
                'Trusted_Connection=True;'
            )
            self.info_label.configure(text="Connection successful", text_color="green")
        
        except pyodbc.Error as ex:
            print('Connection failed:', ex)
            self.info_label.configure(text="Connection Failed", text_color="red")
        
        finally:
            try:
                connection.close()
                print("Connection closed")
            except NameError:
                pass

import pyodbc
import customtkinter

# Configure appearance and theme
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")

# Initialize the app
app = customtkinter.CTk()
app.geometry("300x300")
app.title("Database Manager")

# Create and pack the database entry
entry_database = customtkinter.CTkEntry(app, placeholder_text="Enter database name")
entry_database.pack(pady=20, padx=20)

# Create a label for displaying connection status
info_label = customtkinter.CTkLabel(app, text="", text_color="black")
info_label.place(relx=0.1, rely=0.9)  # Adjusted the position

def validate_entry():
    """Check if the database name entry is empty."""
    return entry_database.get().strip() != ""

def create_db():
    if not validate_entry():
        info_label.configure(text="Please enter a database name", text_color="red")
        return
    
    try:
        database_name = entry_database.get()  # Use the entry widget to get the database name
        # Connect to the database
        connection = pyodbc.connect(
            'DRIVER={SQL Server};'
            'Server=localhost;'  # Replace with the full server name if necessary
            f'Database=master;'
            'Trusted_Connection=True;'
        )
        connection.autocommit=True
        connection.execute(f'create database {database_name}')
        info_label.configure(text="Database created", text_color="green")
    
    except pyodbc.Error as ex:
        print('Connection failed:', ex)
        info_label.configure(text="Creation Failed", text_color="red")
    
    finally:
        # Close the connection if it was opened
        try:
            connection.close()
            print("Connection closed")
        except NameError:
            pass  # Handle the case where the connection wasn't established

# Create a button for creating a database
create_button = customtkinter.CTkButton(app, text="Create Database", command=create_db, fg_color="black")
create_button.pack(pady=10)

def connect_db():
    if not validate_entry():
        info_label.configure(text="Please enter a database name", text_color="red")
        return
    
    try:
        database_name = entry_database.get()  # Use the entry widget to get the database name
        # Connect to the database
        connection = pyodbc.connect(
            'DRIVER={SQL Server};'
            'Server=localhost;'  # Replace with the full server name if necessary
            f'Database={database_name};'
            'Trusted_Connection=True;'
        )
        info_label.configure(text="Connection successful", text_color="green")
    
    except pyodbc.Error as ex:
        print('Connection failed:', ex)
        info_label.configure(text="Connection Failed", text_color="red")
    
    finally:
        # Close the connection if it was opened
        try:
            connection.close()
            print("Connection closed")
        except NameError:
            pass  # Handle the case where the connection wasn't established

# Create a button for connecting to the database
connect_button = customtkinter.CTkButton(app, text="Connect to Database", command=connect_db, fg_color="green")
connect_button.pack(pady=10)

# Start the app
app.mainloop()

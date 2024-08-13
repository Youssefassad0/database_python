import customtkinter as ctk
import tkinter
import pyodbc

# Set appearance and theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Create the main application window
app = ctk.CTk()
app.geometry("500x500")
app.title("CREATE TABLE")

# Input fields for table name and column names
entry_table_name = ctk.CTkEntry(app, placeholder_text="TABLE NAME", width=250)
entry_table_name.place(relx=0.25, rely=0.05)

entry_column1 = ctk.CTkEntry(app, placeholder_text="COLUMN1", width=190)
entry_column1.place(relx=0.1, rely=0.2)

entry_column2 = ctk.CTkEntry(app, placeholder_text="COLUMN2", width=190)
entry_column2.place(relx=0.1, rely=0.3)

entry_column3 = ctk.CTkEntry(app, placeholder_text="COLUMN3", width=190)
entry_column3.place(relx=0.1, rely=0.4)

# Function to open a new window
def open_new_window():
    new_window = ctk.CTkToplevel(app)  # Use CTkToplevel for a new window
    new_window.geometry("400x400")
    new_window.title("New Window")

    # You can add widgets to this new window here
    new_label = ctk.CTkLabel(new_window, text="This is the new window!")
    new_label.pack(pady=20)

# Function to create the table
def create():
    try:
        # Establish connection to the SQL Server
        connection = pyodbc.connect(
            'DRIVER={SQL SERVER}; Server=localhost; Database=assad_youssef; Trusted_Connection=True'
        )
        connection.autocommit = True
        
        # Construct the SQL statement
        sql_stmt = f"""
        CREATE TABLE {entry_table_name.get()} (
            {entry_column1.get()} {radio_var_col1.get()},
            {entry_column2.get()} {radio_var_col2.get()},
            {entry_column3.get()} {radio_var_col3.get()}
        )"""
        
        # Execute the SQL statement
        connection.execute(sql_stmt)
        info_label.configure(text="Table created successfully!")

        # Open the new window after table creation
        open_new_window()

    except pyodbc.Error as ex:
        print("Connection Failed: ", ex)
        info_label.configure(text="Connection Failed")

# Button to trigger table creation
create_button = ctk.CTkButton(app, text="CREATE", command=create)
create_button.place(relx=0.1, rely=0.5)

# Radio buttons for column 1 data type
radio_var_col1 = tkinter.StringVar(value="")
col1_rd_varchar50 = ctk.CTkRadioButton(app, text="varchar(50)", variable=radio_var_col1, value="varchar(50)")
col1_rd_varchar50.place(relx=0.5, rely=0.21)

col1_rd_int = ctk.CTkRadioButton(app, text="integer", variable=radio_var_col1, value="integer")
col1_rd_int.place(relx=0.7, rely=0.21)

# Radio buttons for column 2 data type
radio_var_col2 = tkinter.StringVar(value="")
col2_rd_varchar50 = ctk.CTkRadioButton(app, text="varchar(50)", variable=radio_var_col2, value="varchar(50)")
col2_rd_varchar50.place(relx=0.5, rely=0.31)

col2_rd_int = ctk.CTkRadioButton(app, text="integer", variable=radio_var_col2, value="integer")
col2_rd_int.place(relx=0.7, rely=0.31)

# Radio buttons for column 3 data type
radio_var_col3 = tkinter.StringVar(value="")
col3_rd_varchar50 = ctk.CTkRadioButton(app, text="varchar(50)", variable=radio_var_col3, value="varchar(50)")
col3_rd_varchar50.place(relx=0.5, rely=0.41)

col3_rd_int = ctk.CTkRadioButton(app, text="integer", variable=radio_var_col3, value="integer")
col3_rd_int.place(relx=0.7, rely=0.41)

# Label to display information about table creation status
info_label = ctk.CTkLabel(app, text="", text_color="white")
info_label.place(relx=0.1, rely=0.6)

# Start the application loop
app.mainloop()

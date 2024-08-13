import pyodbc
import customtkinter as ctk
import tkinter

def open_table_creation_window(connection):
    # Create a new top-level window for table creation
    new_window = ctk.CTkToplevel()
    new_window.geometry("500x500")
    new_window.title("Create Table")

    # Input fields for table name and column names
    entry_table_name = ctk.CTkEntry(new_window, placeholder_text="TABLE NAME", width=250)
    entry_table_name.place(relx=0.25, rely=0.05)

    entry_column1 = ctk.CTkEntry(new_window, placeholder_text="COLUMN1", width=190)
    entry_column1.place(relx=0.1, rely=0.2)

    entry_column2 = ctk.CTkEntry(new_window, placeholder_text="COLUMN2", width=190)
    entry_column2.place(relx=0.1, rely=0.3)

    entry_column3 = ctk.CTkEntry(new_window, placeholder_text="COLUMN3", width=190)
    entry_column3.place(relx=0.1, rely=0.4)

    # Radio buttons for column data types
    radio_var_col1 = tkinter.StringVar(value="")
    col1_rd_varchar50 = ctk.CTkRadioButton(new_window, text="varchar(50)", variable=radio_var_col1, value="varchar(50)")
    col1_rd_varchar50.place(relx=0.5, rely=0.21)

    col1_rd_int = ctk.CTkRadioButton(new_window, text="integer", variable=radio_var_col1, value="integer")
    col1_rd_int.place(relx=0.7, rely=0.21)

    radio_var_col2 = tkinter.StringVar(value="")
    col2_rd_varchar50 = ctk.CTkRadioButton(new_window, text="varchar(50)", variable=radio_var_col2, value="varchar(50)")
    col2_rd_varchar50.place(relx=0.5, rely=0.31)

    col2_rd_int = ctk.CTkRadioButton(new_window, text="integer", variable=radio_var_col2, value="integer")
    col2_rd_int.place(relx=0.7, rely=0.31)

    radio_var_col3 = tkinter.StringVar(value="")
    col3_rd_varchar50 = ctk.CTkRadioButton(new_window, text="varchar(50)", variable=radio_var_col3, value="varchar(50)")
    col3_rd_varchar50.place(relx=0.5, rely=0.41)

    col3_rd_int = ctk.CTkRadioButton(new_window, text="integer", variable=radio_var_col3, value="integer")
    col3_rd_int.place(relx=0.7, rely=0.41)

    # Label to display information about table creation status
    info_label = ctk.CTkLabel(new_window, text="", text_color="white")
    info_label.place(relx=0.1, rely=0.6)

    # Function to create the table
    def create():
        try:
            # Construct the SQL statement
            sql_stmt = f"""
            CREATE TABLE {entry_table_name.get()} (
                {entry_column1.get()} {radio_var_col1.get()},
                {entry_column2.get()} {radio_var_col2.get()},
                {entry_column3.get()} {radio_var_col3.get()}
            )"""

            # Execute the SQL statement
            cursor = connection.cursor()
            cursor.execute(sql_stmt)
            connection.commit()
            info_label.configure(text="Table created successfully!")

        except pyodbc.Error as ex:
            print("Creation Failed: ", ex)
            info_label.configure(text="Creation Failed")

    # Button to trigger table creation
    create_button = ctk.CTkButton(new_window, text="CREATE", command=create)
    create_button.place(relx=0.1, rely=0.5)

    new_window.mainloop()

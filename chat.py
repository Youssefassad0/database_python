import pyodbc
import customtkinter
customtkinter.set_appearance_mode("light") 
# light black system
customtkinter.set_default_color_theme("green")
app=customtkinter.CTk()
app.geometry("300x300")
app.title("Database Manager")
entry_database = customtkinter.CTkEntry(app, placeholder_text="Enter database name")
entry_database.pack(pady=20, padx=20)

def create_db():
    pass
create_button = customtkinter.CTkButton(app, text="Create Database", command=create_db, fg_color="black")
create_button.pack(pady=10)

def connect_db() :
    try:
        database_name = input('Enter a database name to create :')
        # Connexion à la base de données master
        connection = pyodbc.connect(
        'DRIVER={SQL Server};'
        'Server=localhost;'  # Remplacez par le nom complet de votre serveur si nécessaire
        f'Database={entry_database.get()};'
        'Trusted_Connection=True;'
    )
        info_label.configure(text="Connection with success")
        print("Database checked and created if it didn't exist")
 
    except pyodbc.Error as ex:
        print('Connection failed:', ex)

    finally:
        # Fermer la connexion si elle est ouverte
        if 'connection' in locals():
            connection.close()
            print("Connection closed")

connect_button = customtkinter.CTkButton(app, text="Connect to Database", command=connect_db, fg_color="green")
connect_button.pack(pady=10)

info_label = customtkinter.CTkLabel(app,"")
info_label.place(relx=0.1,rely=0.4)

app.mainloop()


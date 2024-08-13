import customtkinter as ctk

# Configure appearance and theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# Initialize the app
app = ctk.CTk()
app.geometry("500x250")
app.title("Rentway - SQLServer")

# Function for button actions
def fleet_management():
    print("Fleet Management button clicked")

def rent_a_car():
    print("Rent a Car button clicked")

def system_manager():
    print("System Manager button clicked")

def change_display_language():
    print("Change Display Language button clicked")

def change_user():
    print("Change User button clicked")

def exit_app():
    app.quit()

# Create and place buttons
button_fleet_management = ctk.CTkButton(app, text="database Management", command=fleet_management)
button_fleet_management.grid(row=0, column=0, padx=10, pady=10)

button_rent_a_car = ctk.CTkButton(app, text="Rent a Car", command=rent_a_car)
button_rent_a_car.grid(row=0, column=1, padx=10, pady=10)

button_system_manager = ctk.CTkButton(app, text="System Manager", command=system_manager)
button_system_manager.grid(row=0, column=2, padx=10, pady=10)

button_change_display_language = ctk.CTkButton(app, text="Change Display Language", command=change_display_language)
button_change_display_language.grid(row=1, column=0, padx=10, pady=10)

button_change_user = ctk.CTkButton(app, text="Change User", command=change_user)
button_change_user.grid(row=1, column=1, padx=10, pady=10)

button_exit = ctk.CTkButton(app, text="Exit", command=exit_app)
button_exit.grid(row=1, column=2, padx=10, pady=10)

# Start the app
app.mainloop()

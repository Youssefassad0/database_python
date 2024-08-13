import customtkinter as ctk
from chat import DatabaseManagement  # Import the Fleet Management (Database Management) module

# Configure appearance and theme
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

# Initialize the app
app = ctk.CTk()
app.geometry("500x300")
app.title("EuropCar - SQLServer")

def show_frame(frame):
    frame.tkraise()

# Create frames
main_menu_frame = ctk.CTkFrame(app)
fleet_management_frame = DatabaseManagement(app).frame  # Create the Fleet Management frame from the imported module

# Add frames to the grid
for frame in (main_menu_frame, fleet_management_frame):
    frame.grid(row=0, column=0, sticky='nsew')

# Main Menu Frame with Buttons
button_fleet_management = ctk.CTkButton(main_menu_frame, text="Fleet Management", command=lambda: show_frame(fleet_management_frame))
button_fleet_management.grid(row=0, column=0, padx=10, pady=30)

button_rent_a_car = ctk.CTkButton(main_menu_frame, text="Rent a Car", command=lambda: print("Rent a Car button clicked"))
button_rent_a_car.grid(row=0, column=1, padx=10, pady=10)

button_system_manager = ctk.CTkButton(main_menu_frame, text="System Manager", command=lambda: print("System Manager button clicked"))
button_system_manager.grid(row=0, column=2, padx=10, pady=10)

button_change_display_language = ctk.CTkButton(main_menu_frame, text="Change Display Language", command=lambda: print("Change Display Language button clicked"))
button_change_display_language.grid(row=1, column=0, padx=10, pady=10)

button_change_user = ctk.CTkButton(main_menu_frame, text="Change User", command=lambda: print("Change User button clicked"))
button_change_user.grid(row=1, column=1, padx=10, pady=10)

button_exit = ctk.CTkButton(main_menu_frame, text="Exit", command=app.quit)
button_exit.grid(row=1, column=2, padx=10, pady=10)

# Start by showing the main menu frame
show_frame(main_menu_frame)

# Start the app
app.mainloop()

# Main application
import customtkinter as ctk
from chat import DatabaseManagement

# Configure appearance and theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Initialize the app
app = ctk.CTk()
app.geometry("500x300")
app.title("EuropCar - SQLServer")

# Ensure the window grid expands with the content
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)


def show_frame(frame):
    frame.tkraise()


# Create frames
main_menu_frame = ctk.CTkFrame(app, fg_color="#2b2b2b")  # Dark gray background
database_management_frame = DatabaseManagement(app, show_frame, main_menu_frame).frame

# Ensure frames fill the window
main_menu_frame.grid(row=0, column=0, sticky="nsew")
database_management_frame.grid(row=0, column=0, sticky="nsew")

# Main Menu Frame with Buttons
button_fleet_management = ctk.CTkButton(
    main_menu_frame,
    text="database Management",
    command=lambda: show_frame(database_management_frame),
    fg_color="#1f6aa5",
    hover_color="#144d78",
)
button_fleet_management.grid(row=0, column=0, padx=10, pady=30)

button_rent_a_car = ctk.CTkButton(
    main_menu_frame,
    text="Rent a Car",
    command=lambda: print("Rent a Car button clicked"),
    fg_color="#1f6aa5",
    hover_color="#144d78",
)
button_rent_a_car.grid(row=0, column=1, padx=10, pady=10)

button_system_manager = ctk.CTkButton(
    main_menu_frame,
    text="System Manager",
    command=lambda: print("System Manager button clicked"),
    fg_color="#1f6aa5",
    hover_color="#144d78",
)
button_system_manager.grid(row=0, column=2, padx=10, pady=10)

button_change_display_language = ctk.CTkButton(
    main_menu_frame,
    text="Change Display Language",
    command=lambda: print("Change Display Language button clicked"),
    fg_color="#1f6aa5",
    hover_color="#144d78",
)
button_change_display_language.grid(row=1, column=0, padx=10, pady=10)

button_change_user = ctk.CTkButton(
    main_menu_frame,
    text="Change User",
    command=lambda: print("Change User button clicked"),
    fg_color="#1f6aa5",
    hover_color="#144d78",
)
button_change_user.grid(row=1, column=1, padx=10, pady=10)

button_exit = ctk.CTkButton(
    main_menu_frame,
    text="Exit",
    command=app.quit,
    fg_color="#c850c0",
    hover_color="#4158d0",
)
button_exit.grid(row=1, column=2, padx=10, pady=10)

# Start by showing the main menu frame
show_frame(main_menu_frame)

# Start the app
app.mainloop()

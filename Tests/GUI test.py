from guizero import App, Box, PushButton, Text
import time

# Sample data for connected slaves
connected_slaves = ["Slave 1", "Slave 2", "Slave 3"]
slave_details = {
    "Slave 1": {"time": 1, "voltage": 4, "current": 7},
    "Slave 2": {"time": 2, "voltage": 5, "current": 8},
    "Slave 3": {"time": 3, "voltage": 6, "current": 9},
}

# Function to simulate changing values
def update_slave_details():
    for slave in slave_details:
        slave_details[slave]["time"] += 1
        slave_details[slave]["voltage"] += 1
        slave_details[slave]["current"] += 1

# Function to switch to the view mode
def view_mode():
    clear_widgets()
    Text(app_box, text="Connected Slaves:", size=20, color="navy", font="Arial", grid=[0,0], width=30, height=2)
    update_display()
    create_home_button()

def update_display():
    global row
    row = 1
    for slave in connected_slaves:
        Text(app_box, text=slave, size=16, color="darkgreen", font="Arial", grid=[0, row], width=30, height=2)
        details = slave_details[slave]
        Text(app_box, text=f"Time: {details['time']}s, Voltage: {details['voltage']}V, Current: {details['current']}A", size=14, color="black", font="Arial", grid=[0, row+1], width=30, height=2)
        row += 3  # Move to the next row for the next slave
    app.after(1000, update_display)  # Schedule update_display to run again in 1000 milliseconds (1 second)

# Function to switch to the select mode
def select_mode():
    clear_widgets()
    Text(app_box, text="Select a Slave:", size=20, color="darkred", font="Arial", grid=[0,0], width=30, height=2)
    for i, slave in enumerate(connected_slaves):
        button = PushButton(app_box, text=slave, command=lambda s=slave: slave_clicked(s), grid=[0, i+1], width=20, height=2)
    create_home_button()

# Function to handle slave button clicks
def slave_clicked(slave):
    print(f"Slave clicked: {slave}")

# Function to clear all widgets
def clear_widgets():
    for widget in app_box.children:
        widget.destroy()

# Function to create the home button
def create_home_button():
    PushButton(app_box, text="Home", command=show_choice_screen, grid=[0, len(connected_slaves)*3 + 1], width=10, height=2)

# Function to show the choice screen
def show_choice_screen():
    clear_widgets()
    Text(app_box, text="Choose an Option:", size=24, color="purple", font="Arial", grid=[0,0], width=30, height=3)
    PushButton(app_box, text="View", command=view_mode, grid=[0,1], width=20, height=2)
    PushButton(app_box, text="Select", command=select_mode, grid=[0,2], width=20, height=2)

# Create the main application window
app = App("Slave Manager", width=500, height=400, bg="white")

# Create a box to hold widgets
app_box = Box(app, layout="grid")

# Show the choice screen initially
show_choice_screen()

# Run the app
app.display()

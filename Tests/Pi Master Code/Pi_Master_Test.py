from smbus import SMBus
import time

# I2C addresses of the slave devices
slave_addresses = {
    '1': 0x8,
    '2': 0x9
}

bus = SMBus(1)

# Mapping between character and color names
color_map = {
    'R': 'Red',
    'G': 'Green',
    'B': 'Blue',
    'O': 'Off'
}

def send_command_with_space(device_address, command):
    # Create a list of two bytes: a space followed by the actual command
    message = [ord(' '), ord(command)]
    bus.write_i2c_block_data(device_address, 0, message)

def request_data(device_address):
    try:
        data = bus.read_byte(device_address)  # Read only one byte
        return chr(data)
    except Exception as e:
        print("Error: ", e)
        return None

def change_color(slave_id, color):
    device_address = slave_addresses.get(slave_id)
    if not device_address:
        print(f"Invalid slave ID: {slave_id}")
        return

    color_code = {v.lower(): k for k, v in color_map.items()}  # Reverse map for input
    if color in color_code:
        command = color_code[color]
        send_command_with_space(device_address, command)  # Sending the command with a leading space
        print(f"Sent command to set LED on slave {slave_id} to {color.capitalize()}")
    else:
        print("Invalid color. Valid options are: red, green, blue, off.")

def get_color(slave_id):
    device_address = slave_addresses.get(slave_id)
    if not device_address:
        print(f"Invalid slave ID: {slave_id}")
        return

    response = request_data(device_address)  # Request the current color from the specified slave
    if response:
        color_name = color_map.get(response, "Unknown")
        print(f"Current color on slave {slave_id}: {color_name}")
    else:
        print(f"No response from slave {slave_id}")

try:
    while True:
        # Main menu
        print("\nWhat do you want to do?")
        print("1. Change the color of a slave")
        print("2. Get the current color of a slave")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # Change color option
            slave_id = input("Enter the slave ID (1 or 2): ").strip()
            color = input("Enter the color (red, green, blue, off): ").strip().lower()
            change_color(slave_id, color)
        
        elif choice == '2':
            # Get current color option
            slave_id = input("Enter the slave ID (1 or 2): ").strip()
            get_color(slave_id)

        elif choice == '3':
            # Exit option
            print('Exiting...')
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

        time.sleep(1)  # Wait before showing the menu again

except Exception as e:
    print("Error: ", e)

finally:
    bus.close()

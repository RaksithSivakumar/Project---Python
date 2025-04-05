import pyautogui
import time

# Set the delay between clicks (in seconds)
delay = 1.0

# Set the number of clicks (use None for infinite clicks)
num_clicks = 10

# Define the click function
def auto_clicker():
    for i in range(num_clicks):
        pyautogui.click()  # Perform a click
        time.sleep(delay)  # Wait for the specified delay
    print("Auto-clicking completed!")

# Run the auto-clicker
auto_clicker()

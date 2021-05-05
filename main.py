from hueman import Lamp


def console_input(lamp):
    print("Please enter command")
    while True:
        inp = input().split(" ")
        if "switch" in inp:
            lamp.toggle_active()
            print("Lamp activated/deactivated")
        elif "colorloop" in inp:
            lamp.toggle_colorloop()
            print("Colorloop toggled")
        elif "brightness" in inp:
            lamp.set_brightness(int(inp[1]))
            print("Brightness set to " + inp[1])
        elif "color" in inp:
            if len(inp) == 2:
                lamp.set_color_by_name(inp[1])
            else:
                lamp.set_color_by_rgb(int(inp[1]), int(inp[2]), int(inp[3]))
            print("Color changed")
        elif "devices" in inp:
            print(lamp.get_input_devices())
        elif "music" in inp:
            print("Brightness by audio started for " + inp[2] + " seconds")
            lamp.brightness_by_audio(int(inp[1]), int(inp[2]))
            print("Brightness by audio finished")
        elif "exit" in inp:
            print("Exiting...")
            break
        else:
            print("Command not recognized")


myLamp = Lamp(1, "192.168.178.43")
console_input(myLamp)

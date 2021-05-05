# HUEmane
With HUEman, you can give your Philips Hue lights some life.  
This project is based on the [phue library](https://github.com/studioimaginaire/phue).

## Requirements
First you have to install the Python libraries in the requirements.txt:
```batch
pip install sounddevice
pip install numpy
pip install phue
pip install webcolors
```
Furthermore you have to install the rgb to xy convertor, that you can find [here](https://github.com/benknight/hue-python-rgb-converter). Special thanks to @benknight for this converter.

## Usage
First you have to initialize a new lamp object in main.py like this:
```python
myLamp = Lamp(ID_OF_YOUR_LAMP, IP_OF_YOUR_BRIDGE)
```
In my case it would be:
```python
myLamp = Lamp(1, "192.168.178.43")
```

Now you can call the function console_input(myLamp) with the lamp object as the parameter.  
Then you can control your lamp over the console with following commands:
- **switch** : toggles active state
- **colorloop** : toggles colorloop
- **brightness INT** : set brightness to given integer (0 - 255)
- **color STRING** : set color to given color string
- **color INT INT INT** : set color to given rgb code
- **music INT INT** : changes brightness corresponding to volume of current input device (first parameter: device ID, you can get all device ID's by typing devices in console; second parameter: duration in seconds)
- **exit** : exits program


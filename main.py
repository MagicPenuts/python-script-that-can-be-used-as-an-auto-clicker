import pyautogui
import time

# Set the number of seconds to wait between clicks
delay = 1

# Set the number of times to click
num_clicks = 10

# Set the coordinates to click at
x = 100
y = 100

# Click the specified number of times at the given coordinates
for i in range(num_clicks):
    pyautogui.click(x, y)
    time.sleep(delay)
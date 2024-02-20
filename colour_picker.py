import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle  # Import the ThemedStyle class
import pyperclip

rgb_value=f"(0,0,0)"

def update_colour(_):
    # Get slider values
    red_value = int(red_slider.get())
    green_value = int(green_slider.get())
    blue_value = int(blue_slider.get())

    # Update colour label
    colour_label.config(bg=f'#{red_value:02X}{green_value:02X}{blue_value:02X}')

    # Update RGB values labels
    red_label.config(text=f"Red: {red_value}")
    green_label.config(text=f"Green: {green_value}")
    blue_label.config(text=f"Blue: {blue_value}")

    # Update RGB values label for clipboard copy
    rgb_value = f"({red_value}, {green_value}, {blue_value})"
    rgb_label.config(text=rgb_value)

    # Copy RGB value to clipboard
    pyperclip.copy(rgb_value)

def copy_rgb_to_clipboard(red, green, blue):
    # Copy RGB value to clipboard
    rgb_value = f"({red}, {green}, {blue})"
    pyperclip.copy(rgb_value)

# Create main window
window = tk.Tk()
window.title("Color Creator")

# Create a themed style
style = ThemedStyle(window)
style.set_theme("radiance")  # Change the theme (you can try different themes)

window.geometry("500x300")  # Set initial size
window.resizable(False, False)  # Make window not resizable

# Display current colour
colour_label = tk.Label(window, text="Color", width=20, height=3)
colour_label.pack(pady=10)

# Create sliders for red, green, and blue components & Display RGB values labels

red_label = tk.Label(window, text="Red: 0")
red_label.pack(pady=5)
red_slider = ttk.Scale(window, from_=0, to=255, length=300, orient=tk.HORIZONTAL, command=update_colour)
red_slider.pack(pady=5)

green_label = tk.Label(window, text="Green: 0")
green_label.pack(pady=5)
green_slider = ttk.Scale(window, from_=0, to=255, length=300, orient=tk.HORIZONTAL, command=update_colour)
green_slider.pack(pady=5)

blue_label = tk.Label(window, text="Blue: 0")
blue_label.pack(pady=5)
blue_slider = ttk.Scale(window, from_=0, to=255, length=300, orient=tk.HORIZONTAL, command=update_colour)
blue_slider.pack(pady=5)

# Display RGB values as a clickable button
rgb_label = tk.Button(window, text="Copy RGB Value", command=lambda: copy_rgb_to_clipboard(int(red_slider.get()),int(green_slider.get()),int(blue_slider.get())))
rgb_label.pack(side=tk.RIGHT, padx=10)

# Call update_color to initialize the colour label
update_colour(None)

# Run the GUI
window.mainloop()
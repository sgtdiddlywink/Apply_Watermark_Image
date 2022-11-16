# Import Statements
from tkinter import *
from PIL import Image

# Set transparency for watermark image. The lower the number the more transparent.
TRANSPARENCY = 45


# Function for applying the watermark button.
def apply_watermark():
    # Grabs the relative locations of the images from the entry boxes.
    im1 = upload_entry_box.get()
    im2 = watermark_entry_box.get()
    # Opens the two images using the relative locations.
    # Important Note: The watermark image and upload image need to specified by their relative location to the main.py.
    uploaded_img = Image.open(fp=im1)
    watermark_img = Image.open(fp=im2)
    # Quick way to roughly center the watermark in the image. This can be removed and the watermark will be applied
    # in the upper left hand corner instead.
    center_loc = tuple(map(lambda p: round(p / 3), uploaded_img.size))
    print(center_loc)
    # Creates a new watermark if the mode is incorrect.
    if watermark_img.mode != "RGBA":
        alpha = Image.new("L", watermark_img.size, 255)
        watermark_img.putalpha(alpha)
    # Changes watermark's transparency and pastes it to the uploaded image.
    paste_mask = watermark_img.split()[3].point(lambda i: i * TRANSPARENCY / 100)
    uploaded_img.paste(im=watermark_img, box=center_loc, mask=paste_mask)
    # Displays the image at the end.
    uploaded_img.show()


# Opens Tk Window.
window = Tk()
window.title("Add Watermark to Image")
window.minsize(width=500, height=100)
window.config(padx=20, pady=0)

# Uploaded Image Label.
label_1 = "Image to apply watermark to (Provide route to image): "
uploaded_img_label = Label(text=label_1, font=("Arial", 12, "bold"))
uploaded_img_label.grid(column=0, row=0)
uploaded_img_label.config(padx=5, pady=5)

# Uploaded Watermark Label.
label_2 = "Watermark Image (Provide route to image): "
watermark_img_label = Label(text=label_2, font=("Arial", 12, "bold"))
watermark_img_label.grid(column=0, row=1)
watermark_img_label.config(padx=5, pady=5)

# Apply Button
apply_button = Button(text="Apply Watermark", command=apply_watermark)
apply_button.grid(column=0, row=2, columnspan=2)

# Important Note: The watermark image and upload image need to specified by their relative location to the main.py.
# Add Upload Entry Box.
upload_entry_box = Entry(width=50)
upload_entry_box.grid(column=1, row=0)

# Important Note: The watermark image and upload image need to specified by their relative location to the main.py.
# Add Watermark Entry Box.
watermark_entry_box = Entry(width=50)
watermark_entry_box.grid(column=1, row=1)

# Keeps window open.
window.mainloop()



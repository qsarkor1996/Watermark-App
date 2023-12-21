import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk


def upload_image():
    global img, img_label, img_tk
    file_path = filedialog.askopenfilename()  # allows to ask upload file
    if file_path:
        img = Image.open(file_path)
        img.thumbnail((500, 500))  # size of image
        img_tk = ImageTk.PhotoImage(img)
        if img_label is None:
            img_label = tk.Label(app, image=img_tk)
            img_label.grid(row=1, column=1, columnspan=3)
        else:
            img_label.config(image=img_tk)
            img_label.image = img_tk  # Keeping reference


def add_watermark():
    global img, img_label, img_tk
    if img:
        # Load a font and specify the size
        font = ImageFont.truetype("arial.ttf", 40)  # font of the text

        # Define the text and its color
        text = "Watermark"
        fill_color = "red"  # Color

        # Create a new image to draw rotated text
        text_img = Image.new('RGBA', (500, 500), (255, 255, 255, 0))
        text_draw = ImageDraw.Draw(text_img)
        text_draw.text((0, 0), text, font=font, fill=fill_color)

        # Rotate the text image
        rotated_text_img = text_img.rotate(45, expand=1)

        # Paste the rotated text image onto the main image
        img.paste(rotated_text_img, (100, 20), rotated_text_img)

        # Convert for Tkinter and update label
        img_tk = ImageTk.PhotoImage(img)
        img_label.config(image=img_tk)
        img_label.image = img_tk


def save_image():
    global img
    if img:
        file_path = filedialog.asksaveasfilename(defaultextension=".png")
        if file_path:
            img.save(file_path)


app = tk.Tk()
app.title("Watermark APP")
img = None
img_label = None

upload_btn = tk.Button(app, text="Upload Image", command=upload_image)
upload_btn.grid(row=2, column=1)

watermark_btn = tk.Button(app, text="Watermarking", command=add_watermark)
watermark_btn.grid(row=2, column=2)

save_btn = tk.Button(app, text="Save the image", command=save_image)
save_btn.grid(row=2, column=3)

app.mainloop()

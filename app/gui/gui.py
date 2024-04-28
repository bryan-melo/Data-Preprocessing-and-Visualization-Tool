from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

ASSETS_PATH = Path(r"/Users/bryanmelo/Documents/GitHub/cs122/app/gui/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1280x800")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 800,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1280.0,
    55.0,
    fill="#141414",
    outline="")

canvas.create_rectangle(
    265.0,
    55.0,
    1280.0,
    800.0,
    fill="#282828",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    94.0,
    40.0,
    image=image_image_1
)

canvas.create_rectangle(
    0.0,
    55.0,
    85.0,
    800.0,
    fill="#141414",
    outline="")

canvas.create_rectangle(
    85.0,
    55.0,
    315.0,
    800.0,
    fill="#141414",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=0.0,
    y=55.0,
    width=85.0,
    height=40.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=0.0,
    y=95.0,
    width=85.0,
    height=40.0
)

canvas.create_text(
    178.0,
    19.0,
    anchor="nw",
    text="  Preprocess and visualize data",
    fill="#3C3C3C",
    font=("KaiseiTokumin Regular", 12 * -1)
)

canvas.create_text(
    107.0,
    68.0,
    anchor="nw",
    text="EXPLORER",
    fill="#BBBBBB",
    font=("KaiseiTokumin Regular", 10 * -1)
)

canvas.create_text(
    286.0,
    61.0,
    anchor="nw",
    text="...",
    fill="#BBBBBB",
    font=("KaiseiTokumin Regular", 12 * -1)
)
window.resizable(False, False)
window.mainloop()

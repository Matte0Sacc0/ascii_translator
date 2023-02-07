import tkinter as tk
import ascii_func as af

has_to_reset = False


def _create_image(color):
    image = tk.PhotoImage(width=250, height=1)
    for x in range(250):
        image.put(color, (x, 0))
    return image

# Funzione per elaborare il testo inserito


def process_text(*args):
    response_text = af.translateInput(input_value.get())
    if response_text.startswith("ERROR:"):
        response.config(
            text=response_text[response_text.index(":") + 2:], image=no_border)
    else:
        response.config(text=response_text, image=ok_border)
    has_to_reset = True


def reset_in():
    input_value.delete(0, tk.END)


def reset_out(*args):
    response.config(text=" ", image=neutral_border)
    if has_to_reset:
        reset_in()


def reset_all(*args):
    reset_in()
    reset_out()


# Crea la finestra principale
root = tk.Tk()
root.iconbitmap(r'.\\resources\\ascii.ico')
root.wm_iconphoto(False, tk.PhotoImage(file='.\\resources\\ascii.png'))
root.title("ASCII to Char converter")
root.configure(bg="white")
root.geometry("300x150")
root.maxsize(300, 150)
root.attributes("-fullscreen", False)
root.resizable(False, False)

# Crea la label per il titolo della textbox
input_label = tk.Label(
    root, text="Insert char or ASCII value:", font=("Helvetica", 12))
input_label.configure(bg="white")
input_label.pack(side="top", anchor="c", pady=6)

# Crea la textbox
input_value = tk.Entry(root, font=("Helvetica", 11), justify="center",
                       highlightcolor="blue", highlightthickness=1, width=30)
input_value.pack(side="top", anchor="c", pady=6)
input_value.focus()
input_value.bind("<Return>", process_text)
input_value.bind("<FocusIn>", reset_out)
input_value.bind("<Double-Button-1>", reset_all)

# Crea immagini per il bordo inferiore della risposta
neutral_border = _create_image("#808080")
ok_border = _create_image("#00FF00")
no_border = _create_image("#FF0000")

# Crea la label per la risposta
response = tk.Label(root, text=" ", font=("Helvetica", 11),
                    width=250, height=20, image=neutral_border, compound="bottom")
response.configure(bg="white")
response.pack(side="top", anchor="c", pady=6)

# Crea il pulsante per elaborare il testo
button = tk.Button(root, text="Convert", command=process_text)
button.pack(side="top", anchor="c", pady=6)
button.bind("<Return>", process_text)

# Avvia la GUI
root.mainloop()

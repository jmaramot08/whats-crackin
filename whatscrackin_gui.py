import tkinter as tk
import webbrowser
from PIL import Image, ImageTk

from whatscrackin_data import retrieve_data


def callback(url):
    webbrowser.open_new(url)

def display_data():
    sorted_dict = retrieve_data()
    num = 0
    for key, value in sorted_dict.items():
        exec('Label%d=tk.Label(canvas,text="%s",font=16,cursor="hand2",bg="white")\nLabel%d.pack()' % (num,
                f'{key}: {value} mentions', num))
        exec('Label%d.bind("<Button-1>", lambda e: callback("https://www.google.com/search?q=%s"))' % (num, f'{key}'))
        num += 1

def reset():
    labels = canvas.pack_slaves()
    for l in labels:
        l.destroy()

root = tk.Tk()

root.title("What's Crackin'?!")

# set window size
root.geometry("400x700")
root.configure(bg='white')

# set window icon
p1 = tk.PhotoImage(file='wsb.png')
root.iconphoto(False, p1)

# labels
header = tk.Label(root, text="What's Crackin'?!", font=("Calibri", 36))
header.configure(bg='white')
header.pack(pady=(20,0))

logo = Image.open('wsb.jpg')
logo_image = ImageTk.PhotoImage(logo.resize((300,228), Image.ANTIALIAS))
logo_button = tk.Label(root, image=logo_image, cursor="hand2")
logo_button.image = logo_image
logo_button.configure(bg='white')
logo_button.pack(pady=(20,20))
logo_button.bind("<Button-1>", lambda e: callback('https://www.reddit.com/r/wallstreetbets/'))

# buttons
button_frame = tk.Frame(root)
button_frame.configure(bg='white')
button_frame.pack(pady=(0,20))

start_button = tk.Button(button_frame, text="See What's Crackin'?!", command=display_data)
start_button.pack(side='left', padx=5)

reset_button = tk.Button(button_frame, text="Reset", command=reset)
reset_button.pack(side='left', padx=5)

# canvas to output retrieved data
canvas = tk.Canvas(root)
canvas.configure(bg='white', highlightthickness=0)
canvas.pack()

root.mainloop()
import tkinter as tk
import webbrowser

from whatscrackin_data import retrieve_data


def callback(url):
    webbrowser.open_new(url)

def display_data():
    sorted_dict = retrieve_data()
    num = 0
    for key, value in sorted_dict.items():
        exec('Label%d=tk.Label(canvas,text="%s",font=16)\nLabel%d.pack()' % (num,
                f'{key}: {value} mentions', num))
        num += 1

def reset():
    labels = canvas.pack_slaves()
    for l in labels:
        l.destroy()

root = tk.Tk()

root.title("What's Crackin'?!")

# sets window size
root.geometry("400x600")

# set window icon
p1 = tk.PhotoImage(file='wsb.png')
root.iconphoto(False, p1)

# labels
header = tk.Label(root, text="What's Crackin'?!", font=("Calibri", 36))
header.pack(pady=(50,0))

sub_header = tk.Label(root, text="r/wallstreetbets", font=("Calibri", 20))
sub_header.pack(pady=(0,20))

# buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=(20,20))

start_button = tk.Button(button_frame, text="See What's Crackin'?!", command=display_data)
start_button.pack(side='left', padx=5)

reset_button = tk.Button(button_frame, text="Reset", command=reset)
reset_button.pack(side='left', padx=5)

# canvas to output retrieved data
canvas = tk.Canvas(root)
canvas.pack()

root.mainloop()
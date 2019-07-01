import tkinter as tk
import matplotlib.animation as ani
import mpl_toolkits.mplot3d.axes3d as p3
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
def sys_exit():
    root.destroy()
def toggle(event):
    global tog
    if tog == True:
        t_btn.config(image = off)
        tog = False
    else:
        t_btn.config(image = on)
        tog = True
def caca(root):
    fig = plt.figure()
    frame = tk.Frame(root, width=300, height=800)
    frame.place(x=240, y = 150, height =546, width=642)
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().pack(side='top', fill='both')
    ax = p3.Axes3D(fig)
    def gen(n):


        a1 = 30

        a = 15
        for t in np.linspace(-5 * np.pi, 5 * np.pi, 200):
            yield np.array([a1 * np.sin(a) * t * np.cos(t), a1 * np.sin(a) * t * np.sin(t), a1 * np.cos(a) * t])

    def update(num, data, line):
        line.set_data(data[:2, :num])
        line.set_3d_properties(data[2, :num])

    N = 200
    data = np.array(list(gen(N))).T
    line, = ax.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1], label='conica de papus')

    # Setting the axes properties
    ax.set_xlim3d([-400.0, 400.0])
    ax.set_xlabel('X')

    ax.set_ylim3d([-400.0, 400.0])
    ax.set_ylabel('Y')

    ax.set_zlim3d([-400.0, 400.0])
    ax.set_zlabel('Z')

    ani = animation.FuncAnimation(fig, update, N, fargs=(data, line), interval=1000 / N, blit=False, repeat=False)

    ax.legend()
    #plt.show()
    canvas._tkcanvas.pack(side='top', fill='both', expand=1)
    tk.mainloop()
    
if __name__ == "__main__":
    tog = False
    root = tk.Tk()
    root.wm_title("Física Interactiva")
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)
    root.geometry("900x900")
    hipopoda_button1 = tk.Button(master=root , text="Posición")
    hipopoda_button1.pack()
    hipopoda_button1.place(x = 20, y = 130,height = 40, width = 200)
    hipopoda_button2 = tk.Button(master=root , text="Velocidad")
    hipopoda_button2.pack()
    hipopoda_button2.place(x = 20, y = 190,height = 40, width = 200)
    hipopoda_button = tk.Button(master=root , text="Velocidad Media")
    hipopoda_button.pack()
    hipopoda_button.place(x = 20, y = 250,height = 40, width = 200)
    hipopoda_button = tk.Button(master=root , text="Aceleración")
    hipopoda_button.pack()
    hipopoda_button.place(x = 20, y = 310,height = 40, width = 200)
    hipopoda_button = tk.Button(master=root , text="Aceleración Media")
    hipopoda_button.pack()
    hipopoda_button.place(x = 20, y = 370,height = 40, width = 200)
    hipopoda_button = tk.Button(master=root , text="Curvatura")
    hipopoda_button.pack()
    hipopoda_button.place(x = 20, y = 430,height = 40, width = 200)
    hipopoda_button = tk.Button(master=root , text="Radio de Curvatura")
    hipopoda_button.pack()
    hipopoda_button.place(x = 20, y = 490,height = 40, width = 200)
    hipopoda_button = tk.Button(master=root , text="Torsión")
    hipopoda_button.pack()
    hipopoda_button.place(x = 20, y = 550,height = 40, width = 200)
    hipopoda_button = tk.Button(master=root , text="Radio de Torsión")
    hipopoda_button.pack()
    hipopoda_button.place(x = 20, y = 610,height = 40, width = 200)
    hipopoda_button = tk.Button(master=root , text="Longitud de Arco")
    hipopoda_button.pack()
    hipopoda_button.place(x = 20, y = 670,height = 40, width = 200)
    hipopoda_button = tk.Button(master=root , text="Atrás", command = sys_exit)
    hipopoda_button.pack()
    hipopoda_button.place(x = 20, y = 10,height = 40, width = 200)
    titulo_label = tk.Label(master = root, text = "papus",font = ("letter case",50) )
    titulo_label.place(x = 290, y = 70 , height = 371 , width = 111)
    titulo_label.pack()
    label = tk.Label(master = root, text = "b", font = ("letter case",12))
    label.place(x= 440, y = 810, height = 21, width = 21)
    label.pack
    label = tk.Label(master = root, text = "c", font = ("letter case",12))
    label.place(x= 560, y = 810, height = 21, width = 21)
    label.pack
    label = tk.Label(master = root, text = "d", font = ("letter case",12))
    label.place(x= 680, y = 810, height = 21, width = 21)
    label.pack
    label = tk.Label(master = root, text = "a", font = ("letter case",12))
    label.place(x= 320, y = 810, height = 21, width = 21)
    label.pack
    entry = tk.Entry(master = root)
    entry.place(x=340, y = 810, height = 30, width = 75)
    entry.pack
    entry = tk.Entry(master = root)
    entry.place(x=460, y = 810, height = 30, width = 75)
    entry.pack
    entry = tk.Entry(master = root)
    entry.place(x=580, y = 810, height = 30, width = 75)
    entry.pack
    entry = tk.Entry(master = root)
    entry.place(x=700, y = 810, height = 30, width = 75)
    entry.pack
    on = tk.PhotoImage(file="on.gif")
    off = tk.PhotoImage(file="off.gif")
    t_btn = tk.Label(width=12, image = off)
    t_btn.bind('<Button-1>', toggle)
    t_btn.pack
    t_btn.place(x=840, y = 10, height = 15, width = 27)
    labelk = tk.Label(master = root , text = "Animación")
    labelk.place(x=820, y = 30)
    caca(root)
        
        

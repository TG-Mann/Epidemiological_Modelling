import sys

import customtkinter as ctk
from matplotlib.figure import Figure
from Solvers import odeInt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

ctk.set_appearance_mode("dark")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Epidemiological Modelling")
        self.geometry("1500x800")
        self.background_Colour = "#474645"
        self.Secondary_Colour = "#193b89"
        self.font = "Small Fonts"  # Courier MS Serif  Small Fonts

        # removes titlebar
        self.overrideredirect(True)

        # configure grid layout (4x4)
        self.grid_columnconfigure((1,2,3,4,5,6,7,8,9,10), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame
        self.sidebar_frame = ctk.CTkFrame(self, width=120, corner_radius=10, fg_color=self.background_Colour)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, columnspan = 1,sticky="nsew", padx=10, pady=10)
        self.sidebar_frame.grid_rowconfigure(5, weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Modelling", font=ctk.CTkFont(self.font, size=30, weight="bold")  )
        self.logo_label.grid(row=0, column=0, padx=20, pady=20, columnspan = 1, sticky="nsew")

        # create Main frame
        self.sidebar_frame2 = ctk.CTkFrame(self, width=120, corner_radius=10, fg_color=self.background_Colour)
        self.sidebar_frame2.grid(row=0, column=1, rowspan=4, columnspan=10, sticky="nsew", padx=20, pady=20)
        self.sidebar_frame2.grid_rowconfigure(4, weight=1)

        self.sidebar_button_1 = ctk.CTkButton(self.sidebar_frame, border_color=self.Secondary_Colour, text = "Models", font= (self.font, 20),
                                              border_width=5, height = 60, fg_color=self.background_Colour)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=20,  columnspan = 2, sticky="nsew")

        self.sidebar_button_2 = ctk.CTkButton(self.sidebar_frame, border_color=self.Secondary_Colour, text = "Details", font= (self.font, 20),
                                              border_width=5, height = 60, fg_color=self.background_Colour)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.sidebar_button_3 = ctk.CTkButton(self.sidebar_frame, border_color=self.Secondary_Colour, text = "Parameters", font= (self.font, 20),
                                              border_width=5,height = 60, fg_color=self.background_Colour)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.sidebar_button_4 = ctk.CTkButton(self.sidebar_frame, border_color=self.Secondary_Colour, text = "Simulate", font= (self.font, 20),
                                              border_width=5, height = 60, fg_color=self.background_Colour, command=self.setupChart)
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.sidebar_button_5 = ctk.CTkButton(self.sidebar_frame, border_color=self.Secondary_Colour, text = "Exit", font= (self.font, 20),
                                              border_width=5, height = 60, fg_color=self.background_Colour, command=sys.exit)
        self.sidebar_button_5.grid(row=5, column=0, padx=20, pady=20, columnspan=2, sticky = "s" )

        #self.setupChart()

    def setupChart(self):

        fig_1 = Figure(figsize=(5, 5), facecolor= self.background_Colour, alpha = 0.9)
        ax_1 = fig_1.add_subplot()
        ax_1.set_facecolor(self.background_Colour)
        ax_1.set_alpha(0.9)
        #ax_1.fill_between(x=[1,2,3,4,5,6,7], y1=[1,2,3,4,5,6,7])
        S,I,R,ts = odeInt()
        ax_1.plot(ts, S)
        ax_1.plot(ts, I)
        ax_1.plot(ts, R)
        ax_1.grid(visible = True)
        canvas = FigureCanvasTkAgg(figure=fig_1, master=self.sidebar_frame2)
        canvas.draw()
        canvas.get_tk_widget().place(x=10, y=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()
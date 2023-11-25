import sys

import customtkinter as ctk

from Solvers import odeInt

ctk.set_appearance_mode("dark")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Epidemiological Modelling")
        self.geometry("1500x800")
        self.background_Colour = "#474645"
        self.Secondary_Colour = "#193b89"

        #removes titlebar
        self.overrideredirect(True)

        # configure grid layout (4x4)
        self.grid_columnconfigure((1,2,3,4,5,6,7,8,9,10), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame
        self.sidebar_frame = ctk.CTkFrame(self, width=120, corner_radius=10, fg_color=self.background_Colour)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, columnspan = 1,sticky="nsew", padx=10, pady=10)
        self.sidebar_frame.grid_rowconfigure(5, weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Modelling", font=ctk.CTkFont(size=30, weight="bold") )
        self.logo_label.grid(row=0, column=0, padx=20, pady=20, columnspan = 1, sticky="nsew")

        self.sidebar_button_1 = ctk.CTkButton(self.sidebar_frame, border_color=self.Secondary_Colour, text = "Models", border_width=2, fg_color=self.background_Colour, command= odeInt)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=20,  columnspan = 2, sticky="nsew")

        self.sidebar_button_2 = ctk.CTkButton(self.sidebar_frame, border_color=self.Secondary_Colour, text = "Details", border_width=2, fg_color=self.background_Colour)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.sidebar_button_3 = ctk.CTkButton(self.sidebar_frame, border_color=self.Secondary_Colour, text = "Parameters", border_width=2, fg_color=self.background_Colour)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.sidebar_button_4 = ctk.CTkButton(self.sidebar_frame, border_color=self.Secondary_Colour, text = "Simulate",border_width=2, fg_color=self.background_Colour)
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.sidebar_button_4 = ctk.CTkButton(self.sidebar_frame, border_color=self.Secondary_Colour, text = "Exit",border_width=2, fg_color=self.background_Colour, command=sys.exit)
        self.sidebar_button_4.grid(row=5, column=0, padx=20, pady=20, columnspan=2, sticky = "s" )

        # create Main frame
        self.sidebar_frame2 = ctk.CTkFrame(self, width=120, corner_radius=10, fg_color=self.background_Colour)
        self.sidebar_frame2.grid(row=0, column=1, rowspan=4, columnspan=10, sticky="nsew", padx=20, pady=20)
        self.sidebar_frame2.grid_rowconfigure(4, weight=1)





if __name__ == "__main__":
    app = App()
    app.mainloop()
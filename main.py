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
        self.width = 1500
        self.height = 800
        # ui parameters
        self.background_colour = "#474645"
        self.secondary_colour = "#193b89"
        self.font = "Small Fonts"
        self.button_height = 65
        self.button_font_size = 20
        self.button_border_width = 5
        self.button_padx = 20
        self.button_pady = 20
        self.menu_present = False

        # removes titlebar
        self.overrideredirect(True)

        # configure grid layout (4x4)
        self.grid_columnconfigure((1,2,3,4,5,6,7,8,9,10), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure(( 1 ), weight=0)

        # create sidebar frame
        self.sidebar_frame = ctk.CTkFrame(self, width=100, corner_radius=10, fg_color=self.background_colour)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, columnspan = 1,sticky="nsew", padx=10, pady=10)
        self.sidebar_frame.grid_rowconfigure(5, weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Modelling", font=ctk.CTkFont(self.font, size=30, weight="bold")  )
        self.logo_label.grid(row=0, column=0, padx=20, pady=20, columnspan = 1, sticky="nsew")

        # create Main frame
        self.sidebar_frame2 = ctk.CTkFrame(self, width=1000, corner_radius=10, fg_color=self.background_colour)
        self.sidebar_frame2.grid(row=0, column=2, rowspan=4, columnspan=10, sticky="nsew", padx=10, pady=20)
        self.sidebar_frame2.grid_rowconfigure(4, weight=1)

        self.sidebar_button_1 = ctk.CTkButton(self.sidebar_frame, border_color=self.secondary_colour, text = "Models", font= (self.font, self.button_font_size),
                                              border_width=self.button_border_width, height = self.button_height, fg_color=self.background_colour, command = self.model_menu)
        self.sidebar_button_1.grid(row=1, column=0, padx=self.button_padx, pady=self.button_pady,  columnspan = 2, sticky="nsew")

        self.sidebar_button_2 = ctk.CTkButton(self.sidebar_frame, border_color=self.secondary_colour, text = "Details", font= (self.font, self.button_font_size),
                                              border_width=self.button_border_width, height = self.button_height, fg_color=self.background_colour, command = self.detail_menu)
        self.sidebar_button_2.grid(row=2, column=0, padx=self.button_padx, pady=self.button_pady, columnspan=2, sticky="nsew")

        self.sidebar_button_3 = ctk.CTkButton(self.sidebar_frame, border_color=self.secondary_colour, text = "Parameters", font= (self.font, self.button_font_size),
                                              border_width=self.button_border_width,height = self.button_height, fg_color=self.background_colour, command = self.parameters_menu)
        self.sidebar_button_3.grid(row=3, column=0, padx=self.button_padx, pady=self.button_pady, columnspan=2, sticky="nsew")

        self.sidebar_button_4 = ctk.CTkButton(self.sidebar_frame, border_color=self.secondary_colour, text = "Simulate", font= (self.font, self.button_font_size),
                                              border_width=self.button_border_width, height = self.button_height, fg_color=self.background_colour, command=self.setup_chart)
        self.sidebar_button_4.grid(row=5, column=0, padx=self.button_padx, pady=self.button_pady, columnspan=2, sticky="nsew")

        self.sidebar_button_5 = ctk.CTkButton(self.sidebar_frame, border_color=self.secondary_colour, text="Back", font=(self.font, self.button_font_size),
                                              border_width=self.button_border_width, height=self.button_height, fg_color=self.background_colour, command=self.remove_model_menu)
        self.sidebar_button_5.grid(row=4, column=0, padx=self.button_padx, pady=self.button_pady, columnspan=2,
                                   sticky="nsew")

        self.sidebar_button_6 = ctk.CTkButton(self.sidebar_frame, border_color=self.secondary_colour, text = "Exit", font= (self.font, self.button_font_size),
                                              border_width=self.button_border_width, height = self.button_height, fg_color=self.background_colour, command=sys.exit)
        self.sidebar_button_6.grid(row=6, column=0, padx=self.button_padx, pady=self.button_pady, columnspan=2, sticky = "s" )

    def setup_chart(self):

        print(self.model_slider.get())

        fig = Figure(figsize=(6, 7), facecolor= self.background_colour, alpha = 0.9)
        ax = fig.add_subplot()
        ax.set_facecolor(self.background_colour)
        ax.set_alpha(0.9)

        s,i,r,ts = odeInt()
        ax.plot(ts, s)
        ax.plot(ts, i)
        ax.plot(ts, r)

        ax.grid(visible = True)
        canvas = FigureCanvasTkAgg(figure=fig, master=self.sidebar_frame2)
        canvas.draw()
        canvas.get_tk_widget().place(x=10, y=10)

    def model_menu(self):

        self.remove_model_menu()

        self.menu_present = True
        self.sidebar_frame3 = ctk.CTkFrame(self, width=120, corner_radius=10, fg_color=self.background_colour)
        self.sidebar_frame3.grid(row=0, column=1, rowspan=4, columnspan=1, sticky="nsew", padx=10, pady=20)
        self.sidebar_frame3.grid_rowconfigure((1,2,3,4,5,6,7,8), weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar_frame3, text="Models", font=ctk.CTkFont(self.font, size=30, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=20, columnspan=1, sticky="nsew")

        # code for number of charts ui
        self.choice_frame = ctk.CTkFrame(master=self.sidebar_frame3)
        self.choice_frame.grid(row=1, column=0, padx=10, pady=10)
        self.logo_label = ctk.CTkLabel(self.choice_frame, text="Number of Graphs", font=ctk.CTkFont(self.font, size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=5, pady=5, columnspan=1, sticky="nsew")
        self.segemented_button = ctk.CTkSegmentedButton(self.choice_frame, values=["One", "Two", "Three", "Four"], height=50, width = 100)
        self.segemented_button.grid(row=1, column=0, padx=5, pady=5, columnspan=1)

        self.button_padding = 10

        #code for selecting a model
        self.choice_frame = ctk.CTkFrame(master=self.sidebar_frame3)
        self.choice_frame.grid(row=2, column=0, padx=5, pady=5)
        self.logo_label = ctk.CTkLabel(self.choice_frame, text="Types of Model", font=ctk.CTkFont(self.font, size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=15, pady=15, columnspan=1, sticky="nsew")
        self.checkbox_sir = ctk.CTkCheckBox(master=self.choice_frame, text=" SIR", onvalue="on", offvalue="off")
        self.checkbox_sir.grid(row=1, column=0, padx=self.button_padding, pady=self.button_padding, columnspan=1, sticky="nsew")
        self.checkbox_seir = ctk.CTkCheckBox(master=self.choice_frame, text=" SEIR", onvalue="on", offvalue="off")
        self.checkbox_seir.grid(row=2, column=0, padx=self.button_padding, pady=self.button_padding, columnspan=1, sticky="nsew")
        self.checkbox_sit = ctk.CTkCheckBox(master=self.choice_frame, text=" SIT", onvalue="on", offvalue="off")
        self.checkbox_sit.grid(row=3, column=0, padx=self.button_padding, pady=self.button_padding, columnspan=1, sticky="nsew")
        self.checkbox_seqijr = ctk.CTkCheckBox(master=self.choice_frame, text=" SEQIJR", onvalue="on", offvalue="off")
        self.checkbox_seqijr.grid(row=4, column=0, padx=self.button_padding, pady=self.button_padding, columnspan=1, sticky="nsew")
        self.checkbox_sis = ctk.CTkCheckBox(master=self.choice_frame, text=" SIS", onvalue="on", offvalue="off")
        self.checkbox_sis.grid(row=5, column=0, padx=self.button_padding, pady=self.button_padding, columnspan=1, sticky="nsew")
        self.checkbox_sird = ctk.CTkCheckBox(master=self.choice_frame, text=" SIRD", onvalue="on", offvalue="off")
        self.checkbox_sird.grid(row=6, column=0, padx=self.button_padding, pady=self.button_padding, columnspan=1, sticky="nsew")
        self.checkbox_MSIR = ctk.CTkCheckBox(master=self.choice_frame, text=" MSIR", onvalue="on", offvalue="off")
        self.checkbox_MSIR.grid(row=7, column=0, padx=self.button_padding, pady=self.button_padding, columnspan=1, sticky="nsew")

        self.sidebar_button_6 = ctk.CTkButton(self.sidebar_frame3, border_color=self.secondary_colour, text="Confirm",font=(self.font, self.button_font_size),border_width=self.button_border_width, height=self.button_height,fg_color=self.background_colour)
        self.sidebar_button_6.grid(row=3, column=0, padx=self.button_padx, pady=self.button_pady, columnspan=1, sticky="s")



    def detail_menu(self):

        self.remove_model_menu()

        self.menu_present = True
        self.sidebar_frame3 = ctk.CTkFrame(self, width=120, corner_radius=10, fg_color=self.background_colour)
        self.sidebar_frame3.grid(row=0, column=1, rowspan=4, columnspan=1, sticky="nsew", padx=10, pady=20)
        self.sidebar_frame3.grid_rowconfigure(5, weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar_frame3, text="Details",
                                       font=ctk.CTkFont(self.font, size=30, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=20, columnspan=1, sticky="nsew")

    def parameters_menu(self):

        self.remove_model_menu()

        self.menu_present = True
        self.sidebar_frame3 = ctk.CTkFrame(self, width=120, corner_radius=10, fg_color=self.background_colour)
        self.sidebar_frame3.grid(row=0, column=1, rowspan=4, columnspan=1, sticky="nsew", padx=10, pady=20)
        self.sidebar_frame3.grid_rowconfigure(5, weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar_frame3, text="Parameters",
                                       font=ctk.CTkFont(self.font, size=30, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=20, columnspan=1, sticky="nsew")

    def remove_model_menu(self):

        if (self.menu_present):
            self.sidebar_frame3.grid_remove()

if __name__ == "__main__":
    app = App()
    app.mainloop()
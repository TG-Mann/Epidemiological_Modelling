import sys

import customtkinter as ctk
from matplotlib.figure import Figure
from Solvers import solver
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

ctk.set_appearance_mode("dark")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Epidemiological Modelling")
        self.geometry("1500x800")
        self.width = 1500
        self.height = 800

        # UI Parameters
        self.background_colour = "#474645"
        self.secondary_colour = "#193b89"
        self.un_active_button = "#282b2c"
        self.font = "MS Serif"
        self.button_height = 55
        self.button_font_size = 20
        self.button_border_width = 5
        self.button_padx = 20
        self.button_pady = 20
        self.menu_present = False

        self.num_of_charts = 0

        # Model Menu Parameters
        self.types_of_chart = []
        self.checkbox_values = []

        # Detail Menu Parameters
        self.types_of_detail = []
        self.checkbox_birthrates_value = []
        self.checkbox_maternal_immunity_value = []
        self.checkbox_deaths_value = []
        self.checkbox_treatment_value = []
        self.checkbox_seasonal_forcing_value = []

        # Parameter Menu Variables
        self.slider_value_time = []
        self.slider_value_susceptible = []
        self.slider_value_infected = []
        self.slider_value_recovered = []
        self.slider_value_exposed = []
        self.slider_value_transmission = []
        self.slider_value_recovery = []
        self.slider_value_exposure = []
        self.slider_value_birthrates = []
        self.slider_value_maternal_immunity_loss = []
        self.slider_value_death_rate = []
        self.slider_value_seasonal_forcing_severity = []
        self.slider_value_num_in_treatment = []
        self.slider_value_reduced_infect_treatment = []
        self.slider_value_selected_treatment = []
        self.slider_value_quarantined = []
        self.slider_value_isolated = []

        # removes titlebar
        self.overrideredirect(True)

        # configure grid layout (4x4)
        self.grid_columnconfigure((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((1), weight=0)

        # create main sidebar frame
        self.sidebar_frame = ctk.CTkFrame(self, width=100, corner_radius=10, fg_color=self.background_colour)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, columnspan=1, sticky="nsew", padx=10, pady=10)
        self.sidebar_frame.grid_rowconfigure(5, weight=1)
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Modelling", font=ctk.CTkFont(self.font, size=30,
                                                                                              weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=20, columnspan=1, sticky="nsew")

        # create Main frame
        self.sidebar_frame2 = ctk.CTkFrame(self, width=1000, corner_radius=10, fg_color=self.background_colour)
        self.sidebar_frame2.grid(row=0, column=2, rowspan=4, columnspan=10, sticky="nsew", padx=10, pady=20)
        self.sidebar_frame2.grid_rowconfigure(4, weight=1)

        # buttons for main sidebar frame
        self.sidebar_button_1 = ctk.CTkButton(self.sidebar_frame, border_color=self.secondary_colour, text="Models",
                                              font=(self.font, self.button_font_size),
                                              border_width=self.button_border_width, height=self.button_height,
                                              fg_color=self.background_colour, command=self.model_menu)
        self.sidebar_button_1.grid(row=2, column=0, padx=self.button_padx, pady=self.button_pady, columnspan=2,
                                   sticky="nsew")

        self.sidebar_button_2 = ctk.CTkButton(self.sidebar_frame, border_color=self.un_active_button, text="Details",
                                              font=(self.font, self.button_font_size),
                                              border_width=self.button_border_width, height=self.button_height,
                                              fg_color=self.background_colour, command=self.detail_menu, state="disabled")
        self.sidebar_button_2.grid(row=3, column=0, padx=self.button_padx, pady=self.button_pady, columnspan=2,
                                   sticky="nsew")

        self.sidebar_button_3 = ctk.CTkButton(self.sidebar_frame, border_color=self.un_active_button, text="Parameters",
                                              font=(self.font, self.button_font_size),
                                              border_width=self.button_border_width, height=self.button_height,
                                              fg_color=self.background_colour, command=self.parameters_menu, state="disabled")
        self.sidebar_button_3.grid(row=4, column=0, padx=self.button_padx, pady=self.button_pady, columnspan=2,
                                   sticky="nsew")

        self.sidebar_button_4 = ctk.CTkButton(self.sidebar_frame, border_color=self.un_active_button, text="Simulate",
                                              font=(self.font, self.button_font_size),
                                              border_width=self.button_border_width, height=self.button_height,
                                              fg_color=self.background_colour, command=self.setup_chart, state="disabled")
        self.sidebar_button_4.grid(row=5, column=0, padx=self.button_padx, pady=self.button_pady, columnspan=2,
                                   sticky="nsew")

        self.sidebar_button_5 = ctk.CTkButton(self.sidebar_frame, border_color=self.secondary_colour, text="Back",
                                              font=(self.font, self.button_font_size),
                                              border_width=self.button_border_width, height=self.button_height,
                                              fg_color=self.background_colour, command=self.remove_model_menu)
        self.sidebar_button_5.grid(row=6, column=0, padx=self.button_padx, pady=self.button_pady, columnspan=2,
                                   sticky="nsew")

        self.sidebar_button_6 = ctk.CTkButton(self.sidebar_frame, border_color=self.secondary_colour, text="Exit",
                                              font=(self.font, self.button_font_size),
                                              border_width=self.button_border_width, height=self.button_height,
                                              fg_color=self.background_colour, command=sys.exit)
        self.sidebar_button_6.grid(row=7, column=0, padx=self.button_padx, pady=self.button_pady, columnspan=2,
                                   sticky="nsew")

        # Choice of num of charts frame
        self.choice_frame = ctk.CTkFrame(master=self.sidebar_frame, fg_color=self.background_colour)
        self.choice_frame.grid(row=1, column=0, padx=5, pady=5)
        self.logo_label = ctk.CTkLabel(self.choice_frame, text="Number of Graphs", font=ctk.CTkFont(self.font, size=20,
                                                                                                    weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=5, pady=5, columnspan=1, sticky="nsew")

        self.segmented_button = ctk.CTkSegmentedButton(self.choice_frame, values=["One", "Two", "Three", "Four"],
                                                       height=40, width=100, selected_color=self.secondary_colour,
                                                       font=(self.font, self.button_font_size - 6), command=self.set_buttons)
        self.segmented_button.grid(row=1, column=0, padx=5, pady=5, columnspan=1)
        self.segmented_button.set("One")


    def set_buttons(self, value):
        self.sidebar_button_2.configure(border_color=self.un_active_button, state="disabled")
        self.sidebar_button_3.configure(border_color=self.un_active_button, state="disabled")
        self.sidebar_button_4.configure(border_color=self.un_active_button, state="disabled")

    def setup_chart(self):

        fig = Figure(figsize=(7, 7), facecolor=self.background_colour, alpha=0.9)
        ax = fig.add_subplot()
        ax.set_facecolor(self.background_colour)
        ax.set_alpha(0.9)
        plot_values = []
        y = 0
        for x in self.checkbox_values:

            if x.get() == "SIR":

                num_of_s = self.slider_value_susceptible[y].get()
                num_of_i = self.slider_value_infected[y].get()
                num_of_r = self.slider_value_recovered[y].get()
                num_of_beta = self.slider_value_transmission[y].get()
                num_of_gamma = self.slider_value_recovery[y].get()

                s, i, r, ts = solver(x.get(), [num_of_s, num_of_i, num_of_r, num_of_beta, num_of_gamma])
                plot_values.append([s, i, r, ts])
                ax.plot(ts, s)
                ax.plot(ts, i)
                ax.plot(ts, r)

            if x.get() == "SIS":

                s, i, ts = solver(x.get(), [])
                ax.plot(ts, s)
                ax.plot(ts, i)

            if x.get() == "SEIR":
                s, e, i, r, ts = solver(x.get(), [])
                ax.plot(ts, s)
                ax.plot(ts, e)
                ax.plot(ts, i)
                ax.plot(ts, r)

            y += 1




        ax.grid(visible=True)
        canvas = FigureCanvasTkAgg(figure=fig, master=self.sidebar_frame2)
        canvas.draw()
        canvas.get_tk_widget().place(x=10, y=10)

    def number_of_charts(self):
        # finding number of charts
        if (self.segmented_button.get()) == "Two":
            return 2
        if (self.segmented_button.get()) == "Three":
            return 3
        if (self.segmented_button.get()) == "Four":
            return 4
        else:
            return 1

    def model_menu(self):

        self.sidebar_button_2.configure(border_color=self.secondary_colour, state= "normal")

        self.remove_model_menu()
        self.menu_present = True

        self.sidebar_frame3 = ctk.CTkFrame(self, width=120, corner_radius=10, fg_color=self.background_colour)
        self.sidebar_frame3.grid(row=0, column=1, rowspan=4, columnspan=1, sticky="ns", padx=10, pady=20)
        self.sidebar_frame3.grid_rowconfigure((1, 2, 3, 4, 5, 6, 7, 8), weight=0)

        self.logo_label = ctk.CTkLabel(self.sidebar_frame3, text="Models",
                                       font=ctk.CTkFont(self.font, size=30, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=20, columnspan=1, sticky="nsew")

        self.button_padding = 10

        self.types_of_chart = []
        self.checkbox_values = []

        self.text_size = 16
        self.radio_button_height = 16
        self.title_size = 20
        self.title_padding = 5
        self.frame_padding = 2

        # creates a number of selection option per chart
        i = 0
        while i < self.number_of_charts():
            # code for selecting a model
            self.types_of_chart.append(ctk.CTkFrame(master=self.sidebar_frame3))
            self.types_of_chart[i].grid(row=i + 1, column=0, padx=self.frame_padding, pady=self.frame_padding,
                                        sticky="ew")
            self.logo_label = ctk.CTkLabel(self.types_of_chart[i], text="Model " + str(i + 1),
                                           font=ctk.CTkFont(self.font, size=self.title_size, weight="bold"))
            self.logo_label.grid(row=0, column=0, padx=self.title_padding, pady=self.title_padding, columnspan=1,
                                 sticky="nsew")

            self.checkbox_values.append(ctk.StringVar(value="SIR"))
            self.checkbox_sir = ctk.CTkRadioButton(master=self.types_of_chart[i], text="SIR", value="SIR",
                                                   variable=self.checkbox_values[i],
                                                   radiobutton_width=self.radio_button_height,
                                                   radiobutton_height=self.radio_button_height,
                                                   width=25, fg_color=self.secondary_colour,
                                                   font=ctk.CTkFont(self.font, size=self.text_size, weight="bold"))
            self.checkbox_sir.grid(row=1, column=0, padx=self.button_padding, pady=self.button_padding, columnspan=1,
                                   sticky="nsew")

            self.checkbox_seqijr = ctk.CTkRadioButton(master=self.types_of_chart[i], text="SEIR", value="SEIR",
                                                      variable=self.checkbox_values[i],
                                                      radiobutton_width=self.radio_button_height,
                                                      radiobutton_height=self.radio_button_height,
                                                      width=25, fg_color=self.secondary_colour,
                                                      font=ctk.CTkFont(self.font, size=self.text_size, weight="bold"))
            self.checkbox_seqijr.grid(row=2, column=0, padx=self.button_padding, pady=self.button_padding, columnspan=1,
                                      sticky="nsew")

            self.checkbox_sird = ctk.CTkRadioButton(master=self.types_of_chart[i], text="SI(S)", value="SIS",
                                                    variable=self.checkbox_values[i],
                                                    radiobutton_width=self.radio_button_height,
                                                    radiobutton_height=self.radio_button_height,
                                                    width=25, fg_color=self.secondary_colour,
                                                    font=ctk.CTkFont(self.font, size=self.text_size, weight="bold"))
            self.checkbox_sird.grid(row=3, column=0, padx=self.button_padding, pady=self.button_padding, columnspan=1,
                                    sticky="nsew")

            i += 1

    def detail_menu(self):

        self.remove_model_menu()
        self.menu_present = True

        self.sidebar_button_3.configure(border_color=self.secondary_colour, state= "normal")

        if self.number_of_charts() == 4 or self.number_of_charts() == 3:
            self.sidebar_frame3 = ctk.CTkScrollableFrame(self, width=180, corner_radius=10, fg_color=self.background_colour)
            self.sidebar_frame3.grid(row=0, column=1, rowspan=4, columnspan=1, sticky="nsew", padx=10, pady=20)
            self.sidebar_frame3.grid_rowconfigure((1, 2, 3, 4, 5, 6, 7, 8), weight=1)
        else:
            self.sidebar_frame3 = ctk.CTkFrame(self, width=120, corner_radius=10, fg_color=self.background_colour)
            self.sidebar_frame3.grid(row=0, column=1, rowspan=4, columnspan=1, sticky="ns", padx=10, pady=20)
            self.sidebar_frame3.grid_rowconfigure((1, 2, 3, 4, 5, 6, 7, 8), weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar_frame3, text="Models",
                                       font=ctk.CTkFont(self.font, size=30, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=20, columnspan=1, sticky="nsew")

        self.button_padding = 10

        self.types_of_detail = []
        self.checkbox_birthrates_value = []
        self.checkbox_treatment_value = []
        self.checkbox_maternal_immunity_value = []
        self.checkbox_deaths_value = []
        self.checkbox_seasonal_forcing_value = []

        # creates a number of selection option per chart
        i = 0
        while i < self.number_of_charts():

            # code for selecting a model
            if self.number_of_charts() == 4 or self.number_of_charts() == 3:
                self.types_of_detail.append(ctk.CTkFrame(master=self.sidebar_frame3))
                self.types_of_detail[i].grid(row=i + 1, column=0, padx=0, pady=5, sticky="ew")
            else:
                self.types_of_detail.append(ctk.CTkFrame(master=self.sidebar_frame3))
                self.types_of_detail[i].grid(row=i + 1, column=0, padx=5, pady=5, sticky="ew")

            if len(self.checkbox_values) != 0:
                self.logo_label = ctk.CTkLabel(self.types_of_detail[i], text="Model " + str(i + 1) + " (" + str(self.checkbox_values[i].get()) + ")",
                                              font=ctk.CTkFont(self.font, size=20, weight="bold"))
                self.logo_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky="nsew")
            else:
                self.logo_label = ctk.CTkLabel(self.types_of_detail[i], text="Model " + str(i + 1),
                                                font=ctk.CTkFont(self.font, size=20, weight="bold"))
                self.logo_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky="nsew")

            self.checkbox_birthrates_value.append(ctk.StringVar(value="No"))
            self.checkbox_birthrates = ctk.CTkCheckBox(master=self.types_of_detail[i], text="Add Birth Rates",
                                                              onvalue="Birth Rates", offvalue="No",
                                                              variable=self.checkbox_birthrates_value[i],
                                                              width=25, fg_color=self.secondary_colour,
                                                              font=ctk.CTkFont(self.font, size=12, weight="bold"))
            self.checkbox_birthrates.grid(row=1, column=0, padx=self.button_padding, pady=self.button_padding,
                                              columnspan=1, sticky="nsew")

            self.checkbox_treatment_value.append(ctk.StringVar(value="No"))
            self.checkbox_quarantine = ctk.CTkRadioButton(master=self.types_of_detail[i],
                                                                     text="Quarantine",
                                                                     value="Quarantine",
                                                                     variable=self.checkbox_treatment_value[i],
                                                                     width=25, fg_color=self.secondary_colour,
                                                                     font=ctk.CTkFont(self.font, size=12,
                                                                                      weight="bold"))
            self.checkbox_quarantine.grid(row=2, column=0, padx=self.button_padding,
                                                     pady=self.button_padding, columnspan=1, sticky="nsew")

            self.checkbox_treatment_value.append(ctk.StringVar(value="No"))
            self.checkbox_treatment_model = ctk.CTkRadioButton(master=self.types_of_detail[i],
                                                            text="Treatment Model",
                                                            value="Treatment Model",
                                                            variable=self.checkbox_treatment_value[i],
                                                            width=25, fg_color=self.secondary_colour,
                                                            font=ctk.CTkFont(self.font, size=12,
                                                                             weight="bold"))
            self.checkbox_treatment_model.grid(row=3, column=0, padx=self.button_padding,
                                               pady=self.button_padding, columnspan=1, sticky="nsew")

            self.checkbox_maternal_immunity_value.append(ctk.StringVar(value="No"))
            self.checkbox_maternal_immunity = ctk.CTkCheckBox(master=self.types_of_detail[i],
                                                       text="Maternal Immunity",
                                                       onvalue="Maternal Immunity", offvalue="No",
                                                       variable=self.checkbox_maternal_immunity_value[i],
                                                       width=25, fg_color=self.secondary_colour,
                                                       font=ctk.CTkFont(self.font, size=12,
                                                                        weight="bold"))
            self.checkbox_maternal_immunity.grid(row=4, column=0, padx=self.button_padding,
                                          pady=self.button_padding, columnspan=1, sticky="nsew")

            self.checkbox_deaths_value.append(ctk.StringVar(value="No"))
            self.checkbox_deaths = ctk.CTkCheckBox(master=self.types_of_detail[i],
                                                              text="Deaths from Disease Rate",
                                                              onvalue="Deaths", offvalue="No",
                                                              variable=self.checkbox_deaths_value[i],
                                                              width=25, fg_color=self.secondary_colour,
                                                              font=ctk.CTkFont(self.font, size=12,
                                                                               weight="bold"))
            self.checkbox_deaths.grid(row=5, column=0, padx=self.button_padding,
                                                 pady=self.button_padding, columnspan=1, sticky="nsew")

            self.checkbox_seasonal_forcing_value.append(ctk.StringVar(value="No"))
            self.checkbox_seasonal_forcing = ctk.CTkCheckBox(master=self.types_of_detail[i],
                                                   text="Seasonal Forcing",
                                                   onvalue="Seasonal Forcing", offvalue="No",
                                                   variable=self.checkbox_seasonal_forcing_value[i],
                                                   width=25, fg_color=self.secondary_colour,
                                                   font=ctk.CTkFont(self.font, size=12,
                                                                    weight="bold"))
            self.checkbox_seasonal_forcing.grid(row=6, column=0, padx=self.button_padding,
                                      pady=self.button_padding, columnspan=1, sticky="nsew")




            i += 1

    def parameters_menu(self):

        self.remove_model_menu()
        self.menu_present = True

        self.sidebar_button_4.configure(border_color=self.secondary_colour, state= "normal")

        self.sidebar_frame3 = ctk.CTkScrollableFrame(self, width=220, corner_radius=10, fg_color=self.background_colour)
        self.sidebar_frame3.grid(row=0, column=1, rowspan=4, columnspan=1, sticky="nsew", padx=10, pady=20)
        self.sidebar_frame3.grid_rowconfigure((1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar_frame3, text="Parameters",
                                       font=ctk.CTkFont(self.font, size=30, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=20, columnspan=1, sticky="nsew")

        self.button_padding = 10

        self.types_of_detail = []
        self.slider_value_time = []
        self.slider_value_susceptible = []
        self.slider_value_infected = []
        self.slider_value_recovered = []
        self.slider_value_exposed = []
        self.slider_value_transmission = []
        self.slider_value_recovery = []
        self.slider_value_exposure = []
        self.slider_value_birthrates = []
        self.slider_value_maternal_immunity_loss = []
        self.slider_value_death_rate = []
        self.slider_value_seasonal_forcing_severity = []
        self.slider_value_num_in_treatment = []
        self.slider_value_reduced_infect_treatment = []
        self.slider_value_selected_treatment = []
        self.slider_value_quarantined = []
        self.slider_value_isolated = []


        # creates a number of selection option per chart
        i = 0
        while i < self.number_of_charts():

            # code for selecting a model
            if self.number_of_charts() == 5 or self.number_of_charts() == 6 or self.number_of_charts() == 7:
                self.types_of_detail.append(ctk.CTkScrollableFrame(master=self.sidebar_frame3))
                self.types_of_detail[i].grid(row=i + 1, column=0, padx=5, pady=5, sticky="ew")
            else:
                self.types_of_detail.append(ctk.CTkFrame(master=self.sidebar_frame3))
                self.types_of_detail[i].grid(row=i + 1, column=0, padx=0, pady=5, sticky="ew")

            if len(self.checkbox_values) != 0:
                self.logo_label = ctk.CTkLabel(self.types_of_detail[i], text="Model " + str(i + 1) + " (" + str(
                    self.checkbox_values[i].get()) + ")",
                    font=ctk.CTkFont(self.font, size=20, weight="bold"))
                self.logo_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky="nsew")
            else:
                self.logo_label = ctk.CTkLabel(self.types_of_detail[i], text="Model " + str(i + 1),
                                               font=ctk.CTkFont(self.font, size=20, weight="bold"))
                self.logo_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky="nsew")

            self.number_of_sliders = 0

            if (self.checkbox_values[i].get() == "SIR" or self.checkbox_values[i].get() == "SIS"
                    or self.checkbox_values[i].get() == "SEIR"):

                # label and slider for time
                self.create_slider(self.slider_value_time, "Time", i, 50, 1, 1000)

                # label and slider for susceptible
                self.create_slider(self.slider_value_susceptible, "Number of Susceptible", i,  1500, 1, 2000)

                # label and slider for Infected
                self.create_slider(self.slider_value_infected, "Number of Infected", i, 1, 1, 1000)

                # label and slider for Recovered
                if self.checkbox_values[i].get() == "SIR" or self.checkbox_values[i].get() == "SEIR":

                    self.create_slider(self.slider_value_recovered, "Number of Recovered", i, 0, 0, 1000)
                else:
                    self.slider_value_recovered.append("No")

                # label and slider for Exposed
                if self.checkbox_values[i].get() == "SEIR":

                    # label and slider for Exposed
                    self.create_slider(self.slider_value_exposed, "Number of Exposed", i, 50, 1, 1000)

                    # label and slider for Exposure
                    self.create_slider(self.slider_value_exposure, "Exposure Rate", i, 50, 1, 1000)

                else:
                    self.slider_value_exposed.append("No")
                    self.slider_value_exposure.append("No")


                # label and slider for transmission rate
                self.create_slider(self.slider_value_transmission, "Transmission Rate (Beta)", i, 0.0005, 0.0005, 1)

                # label and slider for recovery rate
                self.create_slider(self.slider_value_recovery, "Recovery Rate (Gamma)", i, 0.1, 0.1, 10)

                if self.checkbox_birthrates_value[i].get() == "Birth Rates":
                    self.create_slider(self.slider_value_birthrates, "Birth rate", i, 50, 1, 1000)
                else:
                    self.slider_value_birthrates.append("No")

                if self.checkbox_maternal_immunity_value[i].get() == "Maternal Immunity":
                    self.create_slider(self.slider_value_maternal_immunity_loss, "Rate of Maternal Immunity Loss", i, 50, 1, 1000)
                else:
                    self.slider_value_maternal_immunity_loss.append("No")

                if self.checkbox_deaths_value[i].get() == "Deaths":
                    self.create_slider(self.slider_value_death_rate, "Rate of Deaths from Disease", i, 50, 1, 1000)
                else:
                    self.slider_value_death_rate.append("No")

                if self.checkbox_seasonal_forcing_value[i].get() == "Seasonal Forcing":
                    self.create_slider(self.slider_value_seasonal_forcing_severity, "Seasonal Forcing Severity", i, 50, 1, 1000)
                else:
                    self.slider_value_seasonal_forcing_severity.append("No")

                if self.checkbox_treatment_value[i].get() == "Treatment Model":
                    self.number_of_sliders += 1
                    self.label = ctk.CTkLabel(self.types_of_detail[i], text="Treatment Model Parameters", font=ctk.CTkFont(self.font, size=14, weight="bold"))
                    self.label.grid(row=self.number_of_sliders, column=0, rowspan=1, columnspan=2, sticky="nsew", padx=5, pady=5)

                    self.create_slider(self.slider_value_num_in_treatment, "Number in Treatment", i, 50, 1, 1000)
                    self.create_slider(self.slider_value_reduced_infect_treatment, "Reduced Infectivity from Treatment", i, 50, 1, 1000)
                    self.create_slider(self.slider_value_selected_treatment, "Fraction selected for Treatment", i, 50, 1, 1000)

                if self.checkbox_treatment_value[i].get() == "Quarantine":
                    self.number_of_sliders += 1
                    self.label = ctk.CTkLabel(self.types_of_detail[i], text="Quarantine Parameters", font=ctk.CTkFont(self.font, size=14, weight="bold"))
                    self.label.grid(row=self.number_of_sliders, column=0, rowspan=1, columnspan=2, sticky="nsew", padx=5, pady=5)

                    self.create_slider(self.slider_value_quarantined, "Number in Quarantine", i, 50, 1, 1000)
                    self.create_slider(self.slider_value_isolated, "Number isolated", i, 50, 1, 1000)
            i += 1


    def create_slider(self, array, text, i, start_value, bottom, top):

        # label and slider for parameters menu
        self.number_of_sliders += 1
        self.container = ctk.CTkFrame(self.types_of_detail[i], border_color=self.background_colour, border_width=2)
        self.container.grid(row=self.number_of_sliders, column=0, rowspan=1, columnspan=2, sticky="nsew",padx=5, pady=5)

        self.label = ctk.CTkLabel(self.container, text=text, font=ctk.CTkFont(self.font, size=12, weight="bold"))
        self.label.grid(row=0, column=0, padx=3, pady=3, columnspan=2, sticky="nsew")
        self.number_of_sliders += 1
        array.append(ctk.DoubleVar(value=start_value))

        self.slider = ctk.CTkSlider(self.container, from_=bottom, to=top, variable=array[i])
        self.slider.grid(row=1, column=0, padx=5, pady=5, columnspan=2,
                                  sticky="nsew")

    def remove_model_menu(self):

        if (self.menu_present):
            self.sidebar_frame3.grid_remove()


if __name__ == "__main__":
    app = App()
    app.mainloop()

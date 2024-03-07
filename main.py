import sys
import customtkinter as ctk
from matplotlib.figure import Figure
from Solvers import solver
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # configure window
        ctk.set_appearance_mode("dark")
        self.geometry("1500x800")
        self.width = 1500
        self.height = 800

        # UI Parameters
        self.background_colour = "#474645"
        self.secondary_colour = "#193b89"
        self.un_active_colour = "#282b2c"
        self.font = "MS Serif"
        self.button_height = 55
        self.button_font_size = 20
        self.button_border_width = 5
        self.button_padx = 20
        self.button_pady = 20
        self.menu_present = False

        # num of charts picked by user
        self.num_of_charts = 0

        # Model Menu Parameters
        self.types_of_chart = []
        self.checkbox_values = []

        # Plot Colour
        self.susceptible_colour = ['#009900', '#00FF00', '#66FF66', '#CCFFCC']
        self.infected_colour = ['#994C00', '#FF8000', '#FFB266', '#FFE5CC']
        self.recovered_colour = ['#009999', '#00FFFF', '#66FFFF', '#CCFFFF']
        self.exposed_colour = ['#99004C', '#FF007F', '#FF66B2', '#FFCCE5']
        self.death_colour = ['#990000', '#FF0000', '#FF6666', '#FFCCC']
        self.treatment_colour = ['#000099', '#0000FF', '#6666FF', '#CCCCFF']
        self.vaccinated_colour = ['#999900', '#FFFF00', '#FFFF66', '#FFFFCC']
        self.isolated_colour = ['#F5BDA1', '#EE8D5C', '#CC5316', '#983D10']

        # Detail Menu Parameters
        self.types_of_detail = []
        self.checkbox_birthrates_value = []
        self.checkbox_vaccination_value = []
        self.checkbox_deaths_value = []
        self.checkbox_treatment_value = []
        self.checkbox_seasonal_forcing_value = []
        self.checkbox_isolation_value = []

        # Parameter Menu Variables
        self.slider_value_susceptible = []
        self.slider_value_susceptible2 = []
        self.slider_value_susceptible3 = []
        self.slider_value_susceptible4 = []

        self.slider_value_infected = []
        self.slider_value_infected2 = []
        self.slider_value_infected3 = []
        self.slider_value_infected4 = []

        self.slider_value_recovered = []
        self.slider_value_recovered2 = []
        self.slider_value_recovered3 = []
        self.slider_value_recovered4 = []

        self.slider_value_exposed = []
        self.slider_value_exposed2 = []
        self.slider_value_exposed3 = []
        self.slider_value_exposed4 = []

        self.slider_value_transmission = []
        self.slider_value_transmission2 = []
        self.slider_value_transmission3 = []
        self.slider_value_transmission4 = []

        self.slider_value_recovery = []
        self.slider_value_recovery2 = []
        self.slider_value_recovery3 = []
        self.slider_value_recovery4 = []

        self.slider_value_exposure = []
        self.slider_value_exposure2 = []
        self.slider_value_exposure3 = []
        self.slider_value_exposure4 = []

        self.slider_value_birthrates = []
        self.slider_value_birthrates2 = []
        self.slider_value_birthrates3 = []
        self.slider_value_birthrates4 = []

        self.slider_value_vaccination = []
        self.slider_value_vaccination2 = []
        self.slider_value_vaccination3 = []
        self.slider_value_vaccination4 = []

        self.slider_value_death_rate = []
        self.slider_value_death_rate2 = []
        self.slider_value_death_rate3 = []
        self.slider_value_death_rate4 = []

        self.slider_value_seasonal_forcing_severity = []
        self.slider_value_seasonal_forcing_severity2 = []
        self.slider_value_seasonal_forcing_severity3 = []
        self.slider_value_seasonal_forcing_severity4 = []

        self.slider_value_length_of_treatment = []
        self.slider_value_length_of_treatment2 = []
        self.slider_value_length_of_treatment3 = []
        self.slider_value_length_of_treatment4 = []

        self.slider_value_reduced_infect_treatment = []
        self.slider_value_reduced_infect_treatment2 = []
        self.slider_value_reduced_infect_treatment3 = []
        self.slider_value_reduced_infect_treatment4 = []

        self.slider_value_selected_treatment = []
        self.slider_value_selected_treatment2 = []
        self.slider_value_selected_treatment3 = []
        self.slider_value_selected_treatment4 = []

        self.slider_value_quarantined = []
        self.slider_value_quarantined2 = []
        self.slider_value_quarantined3 = []
        self.slider_value_quarantined4 = []

        self.slider_value_isolated = []
        self.slider_value_isolated2 = []
        self.slider_value_isolated3 = []
        self.slider_value_isolated4 = []

        self.slider_value_removal_to_j = []
        self.slider_value_removal_to_j2 = []
        self.slider_value_removal_to_j3 = []
        self.slider_value_removal_to_j4 = []

        self.slider_value_reduced_infect_isolation = []
        self.slider_value_reduced_infect_isolation2 = []
        self.slider_value_reduced_infect_isolation3 = []
        self.slider_value_reduced_infect_isolation4 = []

        self.simulate_menu_present = False

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
        self.sidebar_frame2.grid(row=0, column=3, rowspan=4, columnspan=10, sticky="nsew", padx=10, pady=20)
        self.sidebar_frame2.grid_rowconfigure(4, weight=1)

        # for line menu
        self.checkbox_s = []
        self.checkbox_i = []
        self.checkbox_r = []
        self.checkbox_e = []
        self.checkbox_j = []
        self.checkbox_v = []
        self.checkbox_t = []
        self.checkbox_d = []

        # buttons for main sidebar frame
        self.sidebar_button_1 = ctk.CTkButton(self.sidebar_frame, border_color=self.secondary_colour, text="Models",
                                              font=(self.font, self.button_font_size),
                                              border_width=self.button_border_width, height=self.button_height,
                                              fg_color=self.background_colour, command=self.model_menu)
        self.sidebar_button_1.grid(row=2, column=0, padx=self.button_padx, pady=self.button_pady, columnspan=2,
                                   sticky="nsew")

        self.sidebar_button_2 = ctk.CTkButton(self.sidebar_frame, border_color=self.un_active_colour, text="Details",
                                              font=(self.font, self.button_font_size),
                                              border_width=self.button_border_width, height=self.button_height,
                                              fg_color=self.background_colour, command=self.detail_menu,
                                              state="disabled")
        self.sidebar_button_2.grid(row=3, column=0, padx=self.button_padx, pady=self.button_pady, columnspan=2,
                                   sticky="nsew")

        self.sidebar_button_3 = ctk.CTkButton(self.sidebar_frame, border_color=self.un_active_colour, text="Parameters",
                                              font=(self.font, self.button_font_size),
                                              border_width=self.button_border_width, height=self.button_height,
                                              fg_color=self.background_colour, command=self.parameters_menu,
                                              state="disabled")
        self.sidebar_button_3.grid(row=4, column=0, padx=self.button_padx, pady=self.button_pady, columnspan=2,
                                   sticky="nsew")

        self.sidebar_button_4 = ctk.CTkButton(self.sidebar_frame, border_color=self.un_active_colour, text="Simulate",
                                              font=(self.font, self.button_font_size),
                                              border_width=self.button_border_width, height=self.button_height,
                                              fg_color=self.background_colour, command=self.setup_chart,
                                              state="disabled")
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
                                                       font=(self.font, self.button_font_size - 6),
                                                       command=self.set_buttons)
        self.segmented_button.grid(row=1, column=0, padx=5, pady=5, columnspan=1)
        self.segmented_button.set("One")

        self.charts_displayed = []

    def set_parameters_menu(self):

        self.types_of_detail = []

        self.slider_value_susceptible = []
        self.slider_value_susceptible2 = []
        self.slider_value_susceptible3 = []
        self.slider_value_susceptible4 = []

        self.slider_value_infected = []
        self.slider_value_infected2 = []
        self.slider_value_infected3 = []
        self.slider_value_infected4 = []

        self.slider_value_recovered = []
        self.slider_value_recovered2 = []
        self.slider_value_recovered3 = []
        self.slider_value_recovered4 = []

        self.slider_value_exposed = []
        self.slider_value_exposed2 = []
        self.slider_value_exposed3 = []
        self.slider_value_exposed4 = []

        self.slider_value_transmission = []
        self.slider_value_transmission2 = []
        self.slider_value_transmission3 = []
        self.slider_value_transmission4 = []

        self.slider_value_recovery = []
        self.slider_value_recovery2 = []
        self.slider_value_recovery3 = []
        self.slider_value_recovery4 = []

        self.slider_value_exposure = []
        self.slider_value_exposure2 = []
        self.slider_value_exposure3 = []
        self.slider_value_exposure4 = []

        self.slider_value_birthrates = []
        self.slider_value_birthrates2 = []
        self.slider_value_birthrates3 = []
        self.slider_value_birthrates4 = []

        self.slider_value_vaccination = []
        self.slider_value_vaccination2 = []
        self.slider_value_vaccination3 = []
        self.slider_value_vaccination4 = []

        self.slider_value_death_rate = []
        self.slider_value_death_rate2 = []
        self.slider_value_death_rate3 = []
        self.slider_value_death_rate4 = []

        self.slider_value_seasonal_forcing_severity = []
        self.slider_value_seasonal_forcing_severity2 = []
        self.slider_value_seasonal_forcing_severity3 = []
        self.slider_value_seasonal_forcing_severity4 = []

        self.slider_value_length_of_treatment = []
        self.slider_value_length_of_treatment2 = []
        self.slider_value_length_of_treatment3 = []
        self.slider_value_length_of_treatment4 = []

        self.slider_value_reduced_infect_treatment = []
        self.slider_value_reduced_infect_treatment2 = []
        self.slider_value_reduced_infect_treatment3 = []
        self.slider_value_reduced_infect_treatment4 = []

        self.slider_value_selected_treatment = []
        self.slider_value_selected_treatment2 = []
        self.slider_value_selected_treatment3 = []
        self.slider_value_selected_treatment4 = []

        self.slider_value_quarantined = []
        self.slider_value_quarantined2 = []
        self.slider_value_quarantined3 = []
        self.slider_value_quarantined4 = []

        self.slider_value_isolated = []
        self.slider_value_isolated2 = []
        self.slider_value_isolated3 = []
        self.slider_value_isolated4 = []

        self.slider_value_removal_to_j = []
        self.slider_value_removal_to_j2 = []
        self.slider_value_removal_to_j3 = []
        self.slider_value_removal_to_j4 = []

        self.slider_value_reduced_infect_isolation = []
        self.slider_value_reduced_infect_isolation2 = []
        self.slider_value_reduced_infect_isolation3 = []
        self.slider_value_reduced_infect_isolation4 = []

    def set_buttons(self, value):
        self.sidebar_button_2.configure(border_color=self.un_active_colour, state="disabled")
        self.sidebar_button_3.configure(border_color=self.un_active_colour, state="disabled")
        self.sidebar_button_4.configure(border_color=self.un_active_colour, state="disabled")

    def setup_chart(self):

        fig = Figure(figsize=(7.8, 7.8), facecolor=self.background_colour, alpha=0.9)
        ax = fig.add_subplot()
        ax.set_facecolor(self.background_colour)
        ax.set_alpha(0.9)
        y = 0

        for x in self.checkbox_values:

            num_of_s = self.find_susceptible(y)
            num_of_i = self.find_infected(y)

            num_of_beta = self.find_beta(y)
            num_of_gamma = self.find_gamma(y)

            num_of_j = self.find_isolated_number(y)
            num_of_birth = self.find_birth_rate(y)
            num_of_deaths = self.find_death_rate(y)
            num_of_vac = self.find_vaccination_rate(y)
            num_in_treat = self.find_treatment_rate(y)
            red_in_infect = self.find_infect_reduction(y)
            rem_of_treat = self.find_treatment_removal(y)
            seasonal_forcing = self.find_amplitude(y)
            reduced_infect_q = self.find_reduced_rate(y)
            removal_rate_q = self.find_removal_rate(y)

            if x.get() == "SIS":
                s, i, d, v, t, j, ts = solver(x.get(), {"susceptible": num_of_s, "infected": num_of_i,
                                                        "beta": num_of_beta, "gamma": num_of_gamma,
                                                        "births": num_of_birth, "deaths_from_disease": num_of_deaths,
                                                        "vaccinated": num_of_vac, "num in treatment": num_in_treat,
                                                        "reduction infect": red_in_infect,
                                                        "removal from treatment": rem_of_treat,
                                                        "seasonal forcing": seasonal_forcing,
                                                        "Reduced interaction q": reduced_infect_q,
                                                        "removal rate q": removal_rate_q, "isolated": num_of_j})

                self.charts_displayed = [s, "", i, "", d, v, t, j, ts, ax, y]
                self.display_charts(s, "", i, "", d, v, t, j, ts, ax, y)

            if x.get() == "SIR":
                num_of_r = self.find_recovered(y)

                s, i, r, d, v, t, j, ts = solver(x.get(), {"susceptible": num_of_s, "infected": num_of_i,
                                                           "recovered": num_of_r, "beta": num_of_beta,
                                                           "gamma": num_of_gamma, "births": num_of_birth,
                                                           "deaths_from_disease": num_of_deaths,
                                                           "vaccinated": num_of_vac, "num in treatment": num_in_treat,
                                                           "reduction infect": red_in_infect,
                                                           "removal from treatment": rem_of_treat,
                                                           "seasonal forcing": seasonal_forcing,
                                                           "Reduced interaction q": reduced_infect_q,
                                                           "removal rate q": removal_rate_q, "isolated": num_of_j})

                self.charts_displayed = [s, "", i, r, d, v, t, j, ts, ax, y]
                self.display_charts(s, "", i, r, d, v, t, j, ts, ax, y)

            if x.get() == "SEIR":
                num_of_e = self.find_exposed(y)
                num_of_r = self.find_recovered(y)
                num_of_exposure = self.find_exposure(y)

                s, e, i, r, d, v, t, j, ts = solver(x.get(), {"susceptible": num_of_s, "exposed": num_of_e,
                                                              "infected": num_of_i, "recovered": num_of_r,
                                                              "beta": num_of_beta, "gamma": num_of_gamma,
                                                              "exposure": num_of_exposure, "births": num_of_birth,
                                                              "deaths_from_disease": num_of_deaths,
                                                              "vaccinated": num_of_vac,
                                                              "num in treatment": num_in_treat,
                                                              "reduction infect": red_in_infect,
                                                              "removal from treatment": rem_of_treat,
                                                              "seasonal forcing": seasonal_forcing,
                                                              "isolated": num_of_j,
                                                              "Reduced interaction q": reduced_infect_q,
                                                              "removal rate q": removal_rate_q})

                self.charts_displayed = [s, e, i, r, d, v, t, j, ts, ax, y]
                self.display_charts(s, e, i, r, d, v, t, j, ts, ax, y)

            y += 1

        ax.grid(visible=True)
        canvas = FigureCanvasTkAgg(figure=fig, master=self.sidebar_frame2)
        canvas.draw()
        canvas.get_tk_widget().place(x=10, y=10)

    # this is the one to edit when line menu complete
    def display_charts(self, s, e, i, r, d, v, t, j, ts, ax, y):

        if not self.simulate_menu_present:
            self.simulate_menu()

        if self.checkbox_s[y].get() == 1:
            ax.plot(ts, s, color=self.susceptible_colour[y])

        if self.checkbox_i[y].get() == 1:
            ax.plot(ts, i, color=self.infected_colour[y])

        if self.checkbox_values[y].get() == "SIR" or self.checkbox_values[y].get() == "SEIR":
            if self.checkbox_r[y].get() == 1:
                ax.plot(ts, r, color=self.recovered_colour[y])
        if self.checkbox_values[y].get() == "SEIR":
            if self.checkbox_e[y].get() == 1:
                ax.plot(ts, e, color=self.exposed_colour[y])
        if self.checkbox_deaths_value[y].get() == "Deaths":
            if self.checkbox_d[y].get() == 1:
                ax.plot(ts, d, color=self.death_colour[y])
        if self.checkbox_vaccination_value[y].get() == "Vaccinations":
            if self.checkbox_v[y].get() == 1:
                ax.plot(ts, v, color=self.vaccinated_colour[y])

        if self.checkbox_treatment_value[y].get() == "Treatment Model":
            if self.checkbox_t[y].get() == 1:
                ax.plot(ts, t, color=self.treatment_colour[y])
        if self.checkbox_isolation_value[y].get() == "Isolated":
            if self.checkbox_j[y].get() == 1:
                ax.plot(ts, j, color=self.isolated_colour[y])

    def find_exposure(self, y):

        if y == 0:
            return self.slider_value_exposure[0].get()
        if y == 1:
            return self.slider_value_exposure2[0].get()
        if y == 2:
            return self.slider_value_exposure3[0].get()
        if y == 3:
            return self.slider_value_exposure4[0].get()

    def find_susceptible(self, y):

        if y == 0:
            return self.slider_value_susceptible[0].get()
        if y == 1:
            return self.slider_value_susceptible2[0].get()
        if y == 2:
            return self.slider_value_susceptible3[0].get()
        if y == 3:
            return self.slider_value_susceptible4[0].get()

    def find_recovered(self, y):

        if y == 0:
            return self.slider_value_recovered[0].get()
        if y == 1:
            return self.slider_value_recovered2[0].get()
        if y == 2:
            return self.slider_value_recovered3[0].get()
        if y == 3:
            return self.slider_value_recovered4[0].get()

    def find_exposed(self, y):

        if y == 0:
            return self.slider_value_exposed[0].get()
        if y == 1:
            return self.slider_value_exposed2[0].get()
        if y == 2:
            return self.slider_value_exposed3[0].get()
        if y == 3:
            return self.slider_value_exposed4[0].get()

    def find_infected(self, y):

        if y == 0:
            return self.slider_value_infected[0].get()
        if y == 1:
            return self.slider_value_infected2[0].get()
        if y == 2:
            return self.slider_value_infected3[0].get()
        if y == 3:
            return self.slider_value_infected4[0].get()

    def find_beta(self, y):

        if y == 0:
            return self.slider_value_transmission[0].get()
        if y == 1:
            return self.slider_value_transmission2[0].get()
        if y == 2:
            return self.slider_value_transmission3[0].get()
        if y == 3:
            return self.slider_value_transmission4[0].get()

    def find_gamma(self, y):

        if y == 0:
            return self.slider_value_recovery[0].get()
        if y == 1:
            return self.slider_value_recovery2[0].get()
        if y == 2:
            return self.slider_value_recovery3[0].get()
        if y == 3:
            return self.slider_value_recovery4[0].get()


    def find_death_rate(self, y):

        if self.checkbox_deaths_value[y].get() == "Deaths":
            if y == 0:
                return self.slider_value_death_rate[0].get()
            if y == 1:
                return self.slider_value_death_rate2[0].get()
            if y == 2:
                return self.slider_value_death_rate3[0].get()
            if y == 3:
                return self.slider_value_death_rate4[0].get()
        else:
            return 0

    def find_amplitude(self, y):

        if self.checkbox_seasonal_forcing_value[y].get() == "Seasonal Forcing":
            if y == 0:
                return self.slider_value_seasonal_forcing_severity[0].get()
            if y == 1:
                return self.slider_value_seasonal_forcing_severity2[0].get()
            if y == 2:
                return self.slider_value_seasonal_forcing_severity3[0].get()
            if y == 3:
                return self.slider_value_seasonal_forcing_severity4[0].get()
        else:
            return 0

    def find_vaccination_rate(self, y):

        if self.checkbox_vaccination_value[y].get() == "Vaccinations":
            if y == 0:
                return self.slider_value_vaccination[0].get()
            if y == 1:
                return self.slider_value_vaccination2[0].get()
            if y == 2:
                return self.slider_value_vaccination3[0].get()
            if y == 3:
                return self.slider_value_vaccination4[0].get()
        else:
            return 0

    def find_isolated_number(self, y):

        if self.checkbox_isolation_value[y].get() == "Isolated":
            if y == 0:
                return self.slider_value_isolated[0].get()
            if y == 1:
                return self.slider_value_isolated2[0].get()
            if y == 2:
                return self.slider_value_isolated3[0].get()
            if y == 3:
                return self.slider_value_isolated4[0].get()
        else:
            return 0

    def find_removal_rate(self, y):

        if self.checkbox_isolation_value[y].get() == "Isolated":
            if y == 0:
                return self.slider_value_removal_to_j[0].get()
            if y == 1:
                return self.slider_value_removal_to_j2[0].get()
            if y == 2:
                return self.slider_value_removal_to_j3[0].get()
            if y == 3:
                return self.slider_value_removal_to_j4[0].get()
        else:
            return 0

    def find_reduced_rate(self, y):

        if self.checkbox_isolation_value[y].get() == "Isolated":
            if y == 0:
                return self.slider_value_reduced_infect_isolation[0].get()
            if y == 1:
                return self.slider_value_reduced_infect_isolation2[0].get()
            if y == 2:
                return self.slider_value_reduced_infect_isolation3[0].get()
            if y == 3:
                return self.slider_value_reduced_infect_isolation4[0].get()
        else:
            return 0

    def find_treatment_rate(self, y):

        if self.checkbox_treatment_value[y].get() == "Treatment Model":
            if y == 0:
                return self.slider_value_selected_treatment[0].get()
            if y == 1:
                return self.slider_value_selected_treatment2[0].get()
            if y == 2:
                return self.slider_value_selected_treatment3[0].get()
            if y == 3:
                return self.slider_value_selected_treatment4[0].get()
        else:
            return 0

    def find_treatment_removal(self, y):

        if self.checkbox_treatment_value[y].get() == "Treatment Model":
            if y == 0:
                return self.slider_value_length_of_treatment[0].get()
            if y == 1:
                return self.slider_value_length_of_treatment2[0].get()
            if y == 2:
                return self.slider_value_length_of_treatment3[0].get()
            if y == 3:
                return self.slider_value_length_of_treatment4[0].get()
        else:
            return 0

    def find_infect_reduction(self, y):

        if self.checkbox_treatment_value[y].get() == "Treatment Model":
            if y == 0:
                return self.slider_value_reduced_infect_treatment[0].get()
            if y == 1:
                return self.slider_value_reduced_infect_treatment2[0].get()
            if y == 2:
                return self.slider_value_reduced_infect_treatment3[0].get()
            if y == 3:
                return self.slider_value_reduced_infect_treatment4[0].get()
        else:
            return 0

    def find_birth_rate(self, y):

        if self.checkbox_birthrates_value[y].get() == "Birth Rates":
            if y == 0:
                return self.slider_value_birthrates[0].get()
            if y == 1:
                return self.slider_value_birthrates2[0].get()
            if y == 2:
                return self.slider_value_birthrates3[0].get()
            if y == 3:
                return self.slider_value_birthrates4[0].get()
        else:
            return 0

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

        self.simulate_menu_present = False
        self.sidebar_button_2.configure(border_color=self.secondary_colour, state="normal")
        self.sidebar_button_3.configure(border_color=self.un_active_colour, state="disabled")
        self.sidebar_button_4.configure(border_color=self.un_active_colour, state="disabled")

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

        self.simulate_menu_present = False
        self.remove_model_menu()
        self.menu_present = True

        self.sidebar_button_3.configure(border_color=self.secondary_colour, state="normal")
        self.sidebar_button_4.configure(border_color=self.un_active_colour, state="disabled")

        if self.number_of_charts() == 4 or self.number_of_charts() == 3:
            self.sidebar_frame3 = ctk.CTkScrollableFrame(self, width=180, corner_radius=10,
                                                         fg_color=self.background_colour)
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
        self.checkbox_vaccination_value = []
        self.checkbox_deaths_value = []
        self.checkbox_seasonal_forcing_value = []
        self.checkbox_isolation_value = []

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
                self.logo_label = ctk.CTkLabel(self.types_of_detail[i], text=str(i + 1) + ": ("
                                                                             + str(self.checkbox_values[i].get()) + ")",
                                               font=ctk.CTkFont(self.font, size=20, weight="bold"))
                self.logo_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky="nsew")
            else:
                self.logo_label = ctk.CTkLabel(self.types_of_detail[i], text="Model " + str(i + 1),
                                               font=ctk.CTkFont(self.font, size=20, weight="bold"))
                self.logo_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky="nsew")

            self.checkbox_birthrates_value.append(ctk.StringVar(value="No"))
            self.checkbox_birthrates = ctk.CTkCheckBox(master=self.types_of_detail[i], text="Add Birth Rates",
                                                       onvalue="Birth Rates", offvalue="No",
                                                       variable=self.checkbox_birthrates_value[i], width=25,
                                                       fg_color=self.secondary_colour,
                                                       font=ctk.CTkFont(self.font, size=12, weight="bold"))
            self.checkbox_birthrates.grid(row=1, column=0, padx=self.button_padding, pady=self.button_padding,
                                          columnspan=1, sticky="nsew")

            self.checkbox_treatment_value.append(ctk.StringVar(value="No"))

            self.checkbox_treatment_value.append(ctk.StringVar(value="No"))
            self.checkbox_treatment_model = ctk.CTkCheckBox(master=self.types_of_detail[i], text="Treatment Model",
                                                            onvalue="Treatment Model", offvalue="No",
                                                            variable=self.checkbox_treatment_value[i], width=25,
                                                            fg_color=self.secondary_colour,
                                                            font=ctk.CTkFont(self.font, size=12, weight="bold"))
            self.checkbox_treatment_model.grid(row=3, column=0, padx=self.button_padding,
                                               pady=self.button_padding, columnspan=1, sticky="nsew")

            self.checkbox_vaccination_value.append(ctk.StringVar(value="No"))
            self.checkbox_vaccination = ctk.CTkCheckBox(master=self.types_of_detail[i], text="Vaccination",
                                                        onvalue="Vaccinations", offvalue="No",
                                                        variable=self.checkbox_vaccination_value[i],
                                                        width=25, fg_color=self.secondary_colour,
                                                        font=ctk.CTkFont(self.font, size=12, weight="bold"))
            self.checkbox_vaccination.grid(row=4, column=0, padx=self.button_padding, pady=self.button_padding,
                                           columnspan=1, sticky="nsew")

            self.checkbox_deaths_value.append(ctk.StringVar(value="No"))
            self.checkbox_deaths = ctk.CTkCheckBox(master=self.types_of_detail[i], text="Deaths from Disease Rate",
                                                   onvalue="Deaths", offvalue="No",
                                                   variable=self.checkbox_deaths_value[i], width=25,
                                                   fg_color=self.secondary_colour,
                                                   font=ctk.CTkFont(self.font, size=12, weight="bold"))
            self.checkbox_deaths.grid(row=5, column=0, padx=self.button_padding, pady=self.button_padding, columnspan=1,
                                      sticky="nsew")

            self.checkbox_seasonal_forcing_value.append(ctk.StringVar(value="No"))
            self.checkbox_seasonal_forcing = ctk.CTkCheckBox(master=self.types_of_detail[i], text="Seasonal Forcing",
                                                             onvalue="Seasonal Forcing", offvalue="No",
                                                             variable=self.checkbox_seasonal_forcing_value[i],
                                                             width=25, fg_color=self.secondary_colour,
                                                             font=ctk.CTkFont(self.font, size=12, weight="bold"))
            self.checkbox_seasonal_forcing.grid(row=6, column=0, padx=self.button_padding, pady=self.button_padding,
                                                columnspan=1, sticky="nsew")

            # need to change the names here
            self.checkbox_isolation_value.append(ctk.StringVar(value="No"))
            self.checkbox_quarantine = ctk.CTkCheckBox(master=self.types_of_detail[i], text="Isolated",
                                                       onvalue="Isolated", offvalue="No",
                                                       variable=self.checkbox_isolation_value[i],
                                                       width=25, fg_color=self.secondary_colour,
                                                       font=ctk.CTkFont(self.font, size=12, weight="bold"))
            self.checkbox_quarantine.grid(row=7, column=0, padx=self.button_padding, pady=self.button_padding,
                                          columnspan=1, sticky="nsew")

            i += 1

    def parameters_menu(self):

        self.remove_model_menu()
        self.menu_present = True

        self.sidebar_button_4.configure(border_color=self.secondary_colour, state="normal")

        self.sidebar_frame3 = ctk.CTkScrollableFrame(self, width=220, corner_radius=10, fg_color=self.background_colour)
        self.sidebar_frame3.grid(row=0, column=1, rowspan=4, columnspan=1, sticky="nsew", padx=10, pady=20)
        self.sidebar_frame3.grid_rowconfigure((1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar_frame3, text="Parameters",
                                       font=ctk.CTkFont(self.font, size=30, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=20, columnspan=1, sticky="nsew")

        self.button_padding = 10

        self.set_parameters_menu()

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
                self.logo_label = ctk.CTkLabel(self.types_of_detail[i], text=str(i + 1) + ": (" + str(
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

                if i == 0:
                    # label and slider for susceptible
                    self.create_slider(self.slider_value_susceptible, "Number of Susceptible", 0, 1500, 500, 4000)
                    # label and slider for Infected
                    self.create_slider(self.slider_value_infected, "Number of Infected", 0, 1, 1, 1000)
                if i == 1:
                    # label and slider for susceptible
                    self.create_slider(self.slider_value_susceptible2, "Number of Susceptible", 1, 1500, 500, 4000)
                    # label and slider for Infected
                    self.create_slider(self.slider_value_infected2, "Number of Infected", 1, 1, 1, 1000)
                if i == 2:
                    # label and slider for susceptible
                    self.create_slider(self.slider_value_susceptible3, "Number of Susceptible", 2, 1500, 500, 4000)
                    # label and slider for Infected
                    self.create_slider(self.slider_value_infected3, "Number of Infected", 2, 1, 1, 1000)
                if i == 3:
                    # label and slider for susceptible
                    self.create_slider(self.slider_value_susceptible4, "Number of Susceptible", 3, 1500, 500, 4000)
                    # label and slider for Infected
                    self.create_slider(self.slider_value_infected4, "Number of Infected", 3, 1, 1, 1000)

                # label and slider for Recovered
                if self.checkbox_values[i].get() == "SIR" or self.checkbox_values[i].get() == "SEIR":
                    if i == 0:
                        self.create_slider(self.slider_value_recovered, "Number of Recovered", 0, 0, 0, 1000)
                    if i == 1:
                        self.create_slider(self.slider_value_recovered2, "Number of Recovered", 1, 0, 0, 1000)
                    if i == 2:
                        self.create_slider(self.slider_value_recovered3, "Number of Recovered", 2, 0, 0, 1000)
                    if i == 3:
                        self.create_slider(self.slider_value_recovered4, "Number of Recovered", 3, 0, 0, 1000)

                # label and slider for Exposed
                if self.checkbox_values[i].get() == "SEIR":
                    # label and slider for Exposed
                    if i == 0:
                        self.create_slider(self.slider_value_exposed, "Number of Exposed", 0, 1, 1, 100)
                        self.create_slider(self.slider_value_exposure, "Exposure Rate", 0, 50, 1, 100)
                    if i == 1:
                        self.create_slider(self.slider_value_exposed2, "Number of Exposed", 1, 1, 1, 100)
                        self.create_slider(self.slider_value_exposure2, "Exposure Rate", 1, 50, 1, 100)
                    if i == 2:
                        self.create_slider(self.slider_value_exposed3, "Number of Exposed", 2, 1, 1, 100)
                        self.create_slider(self.slider_value_exposure3, "Exposure Rate", 2, 50, 1, 100)
                    if i == 3:
                        self.create_slider(self.slider_value_exposed4, "Number of Exposed", 3, 1, 1, 100)
                        self.create_slider(self.slider_value_exposure4, "Exposure Rate", 3, 50, 1, 100)

                if i == 0:
                    self.create_slider(self.slider_value_transmission, "Transmission Rate (Beta)", 0, 0.0005, 0.00001, 0.001)
                if i == 1:
                    self.create_slider(self.slider_value_transmission2, "Transmission Rate (Beta)", 1, 0.0005, 0.00001,
                                       0.001)
                if i == 2:
                    self.create_slider(self.slider_value_transmission3, "Transmission Rate (Beta)", 2, 0.0005, 0.00001,
                                       0.001)
                if i == 3:
                    self.create_slider(self.slider_value_transmission4, "Transmission Rate (Beta)", 3, 0.0005, 0.00001,
                                       0.001)

                if (self.checkbox_values[i].get() == "SIR" or self.checkbox_values[i].get() == "SIS"
                        or self.checkbox_values[i].get() == "SEIR"):
                    if i == 0:
                        self.create_slider(self.slider_value_recovery, "Recovery Rate (Gamma)", 0, 0.1, 0.01, 1)
                    if i == 1:
                        self.create_slider(self.slider_value_recovery2, "Recovery Rate (Gamma)", 1, 0.1, 0.01, 1)
                    if i == 2:
                        self.create_slider(self.slider_value_recovery3, "Recovery Rate (Gamma)", 2, 0.1, 0.01, 1)
                    if i == 3:
                        self.create_slider(self.slider_value_recovery4, "Recovery Rate (Gamma)", 3, 0.1, 0.01, 1)

                if self.checkbox_birthrates_value[i].get() == "Birth Rates":
                    if i == 0:
                        self.create_slider(self.slider_value_birthrates, "Birth / Death rate", 0, 0.05, 0, 0.1)
                    if i == 1:
                        self.create_slider(self.slider_value_birthrates2, "Birth / Death rate", 1, 0.05, 0, 0.1)
                    if i == 2:
                        self.create_slider(self.slider_value_birthrates3, "Birth / Death rate", 2, 0.05, 0, 0.1)
                    if i == 3:
                        self.create_slider(self.slider_value_birthrates4, "Birth / Death rate", 2, 0.05, 0, 0.1)

                if self.checkbox_vaccination_value[i].get() == "Vaccinations":
                    if i == 0:
                        self.create_slider(self.slider_value_vaccination, "Number of Vaccinations", 0,
                                           0.001, 0.01, 0.1)
                    if i == 1:
                        self.create_slider(self.slider_value_vaccination2, "Number of Vaccinations", 1,
                                           0.001, 0.01, 0.1)
                    if i == 2:
                        self.create_slider(self.slider_value_vaccination3, "Number of Vaccinations", 2,
                                           0.001, 0.01, 0.1)
                    if i == 3:
                        self.create_slider(self.slider_value_vaccination4, "Number of Vaccinations", 3,
                                           0.001, 0.01, 0.1)

                if self.checkbox_deaths_value[i].get() == "Deaths":
                    if i == 0:
                        self.create_slider(self.slider_value_death_rate, "Rate of Deaths from Disease", 0, 0.2, 0, 1)
                    if i == 1:
                        self.create_slider(self.slider_value_death_rate2, "Rate of Deaths from Disease", 1, 0.2, 0, 1)
                    if i == 2:
                        self.create_slider(self.slider_value_death_rate3, "Rate of Deaths from Disease", 2, 0.2, 0, 1)
                    if i == 3:
                        self.create_slider(self.slider_value_death_rate4, "Rate of Deaths from Disease", 3, 0.2, 0, 1)


                if self.checkbox_seasonal_forcing_value[i].get() == "Seasonal Forcing":
                    if i == 0:
                        self.create_slider(self.slider_value_seasonal_forcing_severity, "Seasonal Forcing Severity", 0,
                                       0.5, 0, 1)
                    if i == 1:
                        self.create_slider(self.slider_value_seasonal_forcing_severity2, "Seasonal Forcing Severity", 1,
                                       0.5, 0, 1)
                    if i == 2:
                        self.create_slider(self.slider_value_seasonal_forcing_severity3, "Seasonal Forcing Severity", 2,
                                       0.5, 0, 1)
                    if i == 3:
                        self.create_slider(self.slider_value_seasonal_forcing_severity4, "Seasonal Forcing Severity", 3,
                                       0.5, 0, 1)


                if self.checkbox_treatment_value[i].get() == "Treatment Model":

                    if i == 0:
                        self.number_of_sliders += 1
                        self.label = ctk.CTkLabel(self.types_of_detail[i], text="Treatment Model Parameters",
                                                  font=ctk.CTkFont(self.font, size=14, weight="bold"))
                        self.label.grid(row=self.number_of_sliders, column=0, rowspan=1, columnspan=2, sticky="nsew",
                                        padx=5, pady=5)

                        self.create_slider(self.slider_value_length_of_treatment, "Rate of Removal treatment", 0, 0.5, 0, 1)
                        self.create_slider(self.slider_value_reduced_infect_treatment, "Reduced Infectivity from Treatment", 0, 1, 0, 10)
                        self.create_slider(self.slider_value_selected_treatment, "Fraction selected for Treatment", 0, 0.25, 0, 0.5)

                    if i == 1:
                        self.number_of_sliders += 1
                        self.label = ctk.CTkLabel(self.types_of_detail[i], text="Treatment Model Parameters",
                                                  font=ctk.CTkFont(self.font, size=14, weight="bold"))
                        self.label.grid(row=self.number_of_sliders, column=0, rowspan=1, columnspan=2, sticky="nsew",
                                        padx=5, pady=5)

                        self.create_slider(self.slider_value_length_of_treatment2, "Rate of Removal treatment", 1, 0.5,
                                           0, 1)
                        self.create_slider(self.slider_value_reduced_infect_treatment2,
                                           "Reduced Infectivity from Treatment", 1, 1, 0, 10)
                        self.create_slider(self.slider_value_selected_treatment2, "Fraction selected for Treatment", 1,
                                           0.25, 0, 0.5)

                    if i == 2:
                        self.number_of_sliders += 1
                        self.label = ctk.CTkLabel(self.types_of_detail[i], text="Treatment Model Parameters",
                                                  font=ctk.CTkFont(self.font, size=14, weight="bold"))
                        self.label.grid(row=self.number_of_sliders, column=0, rowspan=1, columnspan=2, sticky="nsew",
                                        padx=5, pady=5)

                        self.create_slider(self.slider_value_length_of_treatment3, "Rate of Removal treatment", 2, 0.5,
                                           0, 1)
                        self.create_slider(self.slider_value_reduced_infect_treatment3,
                                           "Reduced Infectivity from Treatment", 2, 1, 0, 10)
                        self.create_slider(self.slider_value_selected_treatment3, "Fraction selected for Treatment", 2,
                                           0.25, 0, 0.5)

                    if i == 3:
                        self.number_of_sliders += 1
                        self.label = ctk.CTkLabel(self.types_of_detail[i], text="Treatment Model Parameters",
                                                  font=ctk.CTkFont(self.font, size=14, weight="bold"))
                        self.label.grid(row=self.number_of_sliders, column=0, rowspan=1, columnspan=2, sticky="nsew",
                                        padx=5, pady=5)

                        self.create_slider(self.slider_value_length_of_treatment4, "Rate of Removal treatment", 3, 0.5,
                                           0, 1)
                        self.create_slider(self.slider_value_reduced_infect_treatment4,
                                           "Reduced Infectivity from Treatment", 3, 1, 0, 10)
                        self.create_slider(self.slider_value_selected_treatment4, "Fraction selected for Treatment", 3,
                                           0.25, 0, 0.5)

                # need to change name here
                if self.checkbox_isolation_value[i].get() == "Isolated":
                    if i == 0:
                        self.number_of_sliders += 1
                        self.label = ctk.CTkLabel(self.types_of_detail[i], text="Isolation Parameters",
                                                  font=ctk.CTkFont(self.font, size=14, weight="bold"))
                        self.label.grid(row=self.number_of_sliders, column=0, rowspan=1, columnspan=2, sticky="nsew",
                                        padx=5, pady=5)

                        self.create_slider(self.slider_value_removal_to_j, "Rate of Removal to quarantine", 0, 0.05, 0, 1)
                        self.create_slider(self.slider_value_reduced_infect_isolation,
                                           "Reduced Infectivity from Quarantine",
                                           0, 0.5, 0, 1)
                        self.create_slider(self.slider_value_isolated, "Number isolated",
                                           0, 0, 0, 100)

                    if i == 1:
                        self.number_of_sliders += 1
                        self.label = ctk.CTkLabel(self.types_of_detail[i], text="Isolation Parameters",
                                                  font=ctk.CTkFont(self.font, size=14, weight="bold"))
                        self.label.grid(row=self.number_of_sliders, column=0, rowspan=1, columnspan=2, sticky="nsew",
                                        padx=5, pady=5)

                        self.create_slider(self.slider_value_removal_to_j2, "Rate of Removal to quarantine", 1, 0.05, 0, 1)
                        self.create_slider(self.slider_value_reduced_infect_isolation2,
                                           "Reduced Infectivity from Quarantine",
                                           1, 0.5, 0, 1)
                        self.create_slider(self.slider_value_isolated2, "Number isolated",
                                           1, 0, 0, 100)

                    if i == 2:
                        self.number_of_sliders += 1
                        self.label = ctk.CTkLabel(self.types_of_detail[i], text="Isolation Parameters",
                                                  font=ctk.CTkFont(self.font, size=14, weight="bold"))
                        self.label.grid(row=self.number_of_sliders, column=0, rowspan=1, columnspan=2, sticky="nsew",
                                        padx=5, pady=5)

                        self.create_slider(self.slider_value_removal_to_j3, "Rate of Removal to quarantine", 2, 0.05, 0, 1)
                        self.create_slider(self.slider_value_reduced_infect_isolation3,
                                           "Reduced Infectivity from Quarantine",
                                           2, 0.5, 0, 1)
                        self.create_slider(self.slider_value_isolated3, "Number isolated",
                                           2, 0, 0, 100)
                    if i == 3:
                        self.number_of_sliders += 1
                        self.label = ctk.CTkLabel(self.types_of_detail[i], text="Isolation Parameters",
                                                  font=ctk.CTkFont(self.font, size=14, weight="bold"))
                        self.label.grid(row=self.number_of_sliders, column=0, rowspan=1, columnspan=2, sticky="nsew",
                                        padx=5, pady=5)

                        self.create_slider(self.slider_value_removal_to_j4, "Rate of Removal to quarantine", 3, 0.05, 0, 1)
                        self.create_slider(self.slider_value_reduced_infect_isolation4,
                                           "Reduced Infectivity from Quarantine",
                                           3, 0.5, 0, 1)
                        self.create_slider(self.slider_value_isolated4, "Number isolated",
                                           3, 0, 0, 100)

            i += 1

    def simulate_menu(self):

        self.types_of_line = []

        self.simulate_menu_present = True
        self.sidebar_frame2.configure(width=850)
        self.sidebar_frame4 = ctk.CTkScrollableFrame(self, width=125, corner_radius=10, fg_color=self.background_colour)
        self.sidebar_frame4.grid(row=0, column=100, rowspan=4, columnspan=1, sticky="ns", padx=10, pady=20)
        self.sidebar_frame4.grid_rowconfigure((1, 2, 3, 4), weight=0)

        self.logo_label = ctk.CTkLabel(self.sidebar_frame4, text="Lines",
                                       font=ctk.CTkFont(self.font, size=30, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=20, columnspan=1, sticky="nsew")

        self.checkbox_s = []
        self.checkbox_e = []
        self.checkbox_i = []
        self.checkbox_r = []
        self.checkbox_j = []
        self.checkbox_v = []
        self.checkbox_t = []
        self.checkbox_d = []

        i = 0
        while i < self.number_of_charts():

            if self.number_of_charts() == 4 or self.number_of_charts() == 3:
                self.types_of_line.append(ctk.CTkFrame(master=self.sidebar_frame4))
                self.types_of_line[i].grid(row=i + 1, column=0, padx=0, pady=5, sticky="w")
            else:
                self.types_of_line.append(ctk.CTkFrame(master=self.sidebar_frame4))
                self.types_of_line[i].grid(row=i + 1, column=0, padx=0, pady=5, sticky="w")

            if len(self.checkbox_values) != 0:
                self.logo_label = ctk.CTkLabel(self.types_of_line[i], text=str(i + 1) + ": ("
                                                                           + str(self.checkbox_values[i].get()) + ")",
                                               font=ctk.CTkFont(self.font, size=20, weight="bold"))
                self.logo_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky="nsew")
            else:
                self.logo_label = ctk.CTkLabel(self.types_of_line[i], text="Model " + str(i + 1),
                                               font=ctk.CTkFont(self.font, size=20, weight="bold"))
                self.logo_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky="nsew")

            self.number_of_sliders = 1

            if (self.checkbox_values[i].get() == "SIR" or self.checkbox_values[i].get() == "SIS"
                    or self.checkbox_values[i].get() == "SEIR"):

                # label and slider for susceptible

                self.checkbox_s.append(
                    ctk.CTkCheckBox(self.types_of_line[i], text="Susceptible", fg_color=self.susceptible_colour[i],
                                    command=self.resimulate_lines, font=ctk.CTkFont(self.font, size=14, weight="bold")))
                self.checkbox_s[i].select()
                self.checkbox_s[i].grid(row=self.number_of_sliders, column=0, padx=10, pady=10, columnspan=2,
                                        sticky="nsew")
                self.number_of_sliders += 1

                self.checkbox_i.append(
                    ctk.CTkCheckBox(self.types_of_line[i], text="Infected", fg_color=self.infected_colour[i],
                                    command=self.resimulate_lines, font=ctk.CTkFont(self.font, size=14, weight="bold")))
                self.checkbox_i[i].select()
                self.checkbox_i[i].grid(row=self.number_of_sliders, column=0, padx=10, pady=10, columnspan=2,
                                        sticky="nsew")
                self.number_of_sliders += 1

                if (self.checkbox_values[i].get() == "SIR" or self.checkbox_values[i].get() == "SEIR"):

                    self.checkbox_r.append(
                        ctk.CTkCheckBox(self.types_of_line[i], text="Recovered", fg_color=self.recovered_colour[i],
                                        command=self.resimulate_lines,
                                        font=ctk.CTkFont(self.font, size=14, weight="bold")))
                    self.checkbox_r[i].select()
                    self.checkbox_r[i].grid(row=self.number_of_sliders, column=0, padx=10, pady=10, columnspan=2,
                                            sticky="nsew")
                    self.number_of_sliders += 1

                else:  # this is the bug!!!!!!!!!!!!!
                    self.checkbox_r.append(0)

                if (self.checkbox_values[i].get() == "SEIR"):

                    self.checkbox_e.append(
                        ctk.CTkCheckBox(self.types_of_line[i], text="Exposed", fg_color=self.exposed_colour[i],
                                        command=self.resimulate_lines,
                                        font=ctk.CTkFont(self.font, size=14, weight="bold")))
                    self.checkbox_e[i].select()
                    self.checkbox_e[i].grid(row=self.number_of_sliders, column=0, padx=10, pady=10, columnspan=2,
                                            sticky="nsew")
                    self.number_of_sliders += 1

                else:  # this is the bug!!!!!!!!!!!!!
                    self.checkbox_e.append(0)

                if (self.checkbox_deaths_value[i].get() == "Deaths"):

                    self.checkbox_d.append(ctk.CTkCheckBox(self.types_of_line[i], text="Deaths",
                                                           fg_color=self.death_colour[i], command=self.resimulate_lines,
                                                           font=ctk.CTkFont(self.font, size=14, weight="bold")))
                    self.checkbox_d[i].select()
                    self.checkbox_d[i].grid(row=self.number_of_sliders, column=0, padx=10, pady=10, columnspan=2,
                                            sticky="nsew")
                    self.number_of_sliders += 1
                else:  # this is the bug!!!!!!!!!!!!!
                    self.checkbox_d.append(0)

                if (self.checkbox_vaccination_value[i].get() == "Vaccinations"):

                    self.checkbox_v.append(ctk.CTkCheckBox(self.types_of_line[i], text="Vaccinated",
                                                           fg_color=self.vaccinated_colour[i],
                                                           command=self.resimulate_lines,
                                                           font=ctk.CTkFont(self.font, size=14, weight="bold")))

                    self.checkbox_v[i].select()
                    self.checkbox_v[i].grid(row=self.number_of_sliders, column=0, padx=10, pady=10, columnspan=2,
                                            sticky="nsew")
                    self.number_of_sliders += 1
                else:  # this is the bug!!!!!!!!!!!!!
                    self.checkbox_v.append(0)

                if (self.checkbox_treatment_value[i].get() == "Treatment Model"):

                    self.checkbox_t.append(ctk.CTkCheckBox(self.types_of_line[i], text="Treated",
                                                           fg_color=self.treatment_colour[i],
                                                           command=self.resimulate_lines,
                                                           font=ctk.CTkFont(self.font, size=14, weight="bold")))
                    self.checkbox_t[i].select()
                    self.checkbox_t[i].grid(row=self.number_of_sliders, column=0, padx=10, pady=10, columnspan=2,
                                            sticky="nsew")
                    self.number_of_sliders += 1
                else:  # this is the bug!!!!!!!!!!!!!
                    self.checkbox_t.append(0)

                if (self.checkbox_isolation_value[i].get() == "Isolated"):



                    self.checkbox_j.append(ctk.CTkCheckBox(self.types_of_line[i], text="Isolated",
                                                           fg_color=self.isolated_colour[i],
                                                           command=self.resimulate_lines,
                                                           font=ctk.CTkFont(self.font, size=14, weight="bold")))
                    self.checkbox_j[i].select()
                    self.checkbox_j[i].grid(row=self.number_of_sliders, column=0, padx=10, pady=10, columnspan=2,
                                            sticky="nsew")
                    self.number_of_sliders += 1
                else:  # this is the bug!!!!!!!!!!!!!
                    self.checkbox_j.append(0)

                i += 1

    def resimulate(self, num):

        if self.charts_displayed != []:
            self.setup_chart()

    def resimulate_lines(self):

        if self.charts_displayed != []:
            self.setup_chart()

    def create_slider(self, array, text, i, start_value, bottom, top):

        # label and slider for parameters menu
        self.number_of_sliders += 1
        self.container = ctk.CTkFrame(self.types_of_detail[i], border_color=self.background_colour, border_width=2)
        self.container.grid(row=self.number_of_sliders, column=0, rowspan=1, columnspan=2, sticky="nsew", padx=5,
                            pady=5)

        self.label = ctk.CTkLabel(self.container, text=text, font=ctk.CTkFont(self.font, size=12, weight="bold"))
        self.label.grid(row=0, column=0, padx=3, pady=3, columnspan=2, sticky="nsew")
        self.number_of_sliders += 1
        array.append(ctk.DoubleVar(value=start_value))

        self.slider = ctk.CTkSlider(self.container, from_=bottom, to=top, variable=array[0], command=self.resimulate)
        array.append(ctk.DoubleVar(value=start_value))
        self.slider.grid(row=1, column=0, padx=5, pady=5, columnspan=2,
                         sticky="nsew")

    def remove_model_menu(self):

        if self.menu_present:
            self.sidebar_frame3.grid_remove()


if __name__ == "__main__":
    app = App()
    app.mainloop()

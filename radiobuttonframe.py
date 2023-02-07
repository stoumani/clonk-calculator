import customtkinter


class RadioButtonFrame(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="Calculator Types", **kwargs):
        super().__init__(*args, **kwargs)

        self.radio_button_var = customtkinter.StringVar(value="")

        self.radio_button_1 = customtkinter.CTkRadioButton(self, text="Scientific", value="Scientific",
                                                           variable=self.radio_button_var)
        self.radio_button_1.grid(row=1, column=0, padx=10, pady=10)
        self.radio_button_2 = customtkinter.CTkRadioButton(self, text="Graphing", value="Graphing",
                                                           variable=self.radio_button_var)
        self.radio_button_2.grid(row=2, column=0, padx=10, pady=5)
        self.radio_button_3 = customtkinter.CTkRadioButton(self, text="Financial", value="Financial",
                                                           variable=self.radio_button_var)
        self.radio_button_3.grid(row=3, column=0, padx=10, pady=(10, 20))

    def get_value(self):
        """ returns selected value as a string, returns an empty string if nothing selected """
        return self.radio_button_var.get()

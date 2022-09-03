from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934

class MilesToKilometerConverter(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')

    def calculate(self):
        valid_value = self.get_valid_miles()
        result = valid_value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        valid_value = self.get_valid_miles() + change
        self.root.ids.input_miles.text = str(valid_value)
        self.calculate()

    def get_valid_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

MilesToKilometerConverter().run()
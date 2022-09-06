from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name_to_phone = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456"}

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_label.kv')
        return self.root

    def on_start(self):
        for name in self.name_to_phone:
            temp_label = Label(text="{}'s number is {}".format(name, self.name_to_phone[name]))
            self.root.ids.main.add_widget(temp_label)

DynamicLabelsApp().run()
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout


class CalculatorApp(App):

    def build(self):
        self.operations = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None

        main_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        result_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=0.2)
        self.result = TextInput(font_size=120, readonly=True, halign='right', multiline=False)
        result_layout.add_widget(self.result)
        main_layout.add_widget(result_layout)

        button_layout = GridLayout(cols=4, spacing=10, size_hint_y=0.6)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        for button in buttons:
            btn = Button(text=button, pos_hint={'center_x': 0.5, 'center_y': 0.5})
            btn.bind(on_press=self.on_button_press)
            button_layout.add_widget(btn)

        main_layout.add_widget(button_layout)

        return main_layout

    def on_button_press(self, instance):
        current = self.result.text
        button_text = instance.text

        if button_text == 'C':
            self.result.text = ''
        elif button_text == '=':
            try:
                result = str(eval(current))
                self.result.text = result
            except Exception as e:
                self.result.text = 'Error'
        elif button_text in self.operations:
            if self.last_was_operator:
                return
            else:
                new_text = current + button_text
                self.last_button = button_text
                self.result.text = new_text
                self.last_was_operator = True
        else:
            new_text = current + button_text
            self.result.text = new_text
            self.last_button = button_text
            self.last_was_operator = False


if __name__ == '__main__':
    CalculatorApp().run()

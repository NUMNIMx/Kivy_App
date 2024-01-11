import subprocess
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label  # Import Label

class MyApp(App):
    def build(self):
        # Create a label with uppercase text
        label = Label(text='PLEASE SELECT YOUR APP', font_size='20sp', size_hint_y=None, height=44)

        button_hello = Button(text='Open Calculator.py', size_hint=(None, None), size=(200, 40))
        button_hello.bind(on_press=self.open_hello_app)

        button_another = Button(text='Open Paint tool.py', size_hint=(None, None), size=(200, 40))
        button_another.bind(on_press=self.open_another_app)

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(label)  # Add the label to the layout
        layout.add_widget(button_hello)
        layout.add_widget(button_another)

        return layout

    def open_hello_app(self, instance):
        subprocess.Popen(['python', 'calculator.py'])

    def open_another_app(self, instance):
        subprocess.Popen(['python', 'paint_tool.py'])

if __name__ == '__main__':
    MyApp().run()

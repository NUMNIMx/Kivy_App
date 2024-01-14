import subprocess
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label  

class MyApp(App):
    def build(self):
        label = Label(text='PLEASE SELECT YOUR APP', font_size='40sp', height=45)

        button_hello = Button(text='Calculator', size=(20, 40),font_size='30sp')
        button_hello.bind(on_press=self.open_hello_app)

        button_another = Button(text='Paint tool', size=(20, 40),font_size='30sp')
        button_another.bind(on_press=self.open_another_app)

        button_another1 = Button(text='CPS Test', size=(20, 40),font_size='30sp')
        button_another1.bind(on_press=self.open_another1_app)

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(label)
        layout.add_widget(button_hello)
        layout.add_widget(button_another)
        layout.add_widget(button_another1)

        return layout

    def open_hello_app(self, instance):
        subprocess.Popen(['python', 'calculator.py'])

    def open_another_app(self, instance):
        subprocess.Popen(['python', 'paint_tool.py'])

    def open_another1_app(self, instance):
        subprocess.Popen(['python', 'cps.py'])

if __name__ == '__main__':
    MyApp().run()
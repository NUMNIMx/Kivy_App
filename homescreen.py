import subprocess
from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        button = Button(text='Open hello.py')
        button.bind(on_press=self.open_hello_app)
        return button

    def open_hello_app(self, instance):
        # เรียกใช้งาน hello.py ด้วย subprocess
        subprocess.Popen(['python', 'calculator.py'])

if __name__ == '__main__':
    MyApp().run()

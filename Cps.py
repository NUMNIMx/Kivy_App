from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock

class CPSClickTestApp(App):
    def build(self):
        self.click_count = 0
        self.time_elapsed = 0
        self.max_time = 10
        self.layout = BoxLayout(orientation='vertical', spacing=10)

        self.click_label = Label(text='Clicks : 0', font_size='50sp')
        self.layout.add_widget(self.click_label)

        self.timer_label = Label(text='Time : 0s', font_size='50sp')
        self.layout.add_widget(self.timer_label)

        self.result_label = Label(text='Final CPS : ', font_size='50sp')
        self.layout.add_widget(self.result_label)

        self.click_button = Button(text='Click me!', font_size='50sp')
        self.click_button.bind(on_press=self.on_button_click)
        self.layout.add_widget(self.click_button)

        Clock.schedule_interval(self.update_timer, 1)

        Clock.schedule_once(self.finish_test, self.max_time)

        return self.layout

    def on_button_click(self, instance):
        if self.time_elapsed < self.max_time:
            self.click_count += 1
            self.click_label.text = f'Clicks : {self.click_count}'

    def update_timer(self, dt):
        if self.time_elapsed < self.max_time:
            self.time_elapsed += 1
            self.timer_label.text = f'Time : {self.time_elapsed}s'

    def finish_test(self, dt):

        self.click_button.disabled = True
        cps = self.click_count / self.time_elapsed if self.time_elapsed > 0 else 0
        self.result_label.text = f'Final CPS : {cps:.2f}'

    def on_stop(self):

        pass

if __name__ == '__main__':
    CPSClickTestApp().run()
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color, Ellipse


class PaintWidget(Widget):
    def __init__(self, **kwargs):
        super(PaintWidget, self).__init__(**kwargs)
        self.color = (1, 1, 1, 1)  # Initial color of the paintbrush

    def on_touch_down(self, touch):
        with self.canvas:
            Color(*self.color)
            d = 10  # Size of the paintbrush tip
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=2)

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class PaintApp(App):
    def build(self):
        self.paint_widget = PaintWidget()
        color_picker = ColorPicker()
        color_picker.bind(color=self.on_color)

        clear_button = Button(text='Clear', size_hint=(None, None), size=(100, 50))
        clear_button.bind(on_release=self.clear_canvas)

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.paint_widget)
        layout.add_widget(color_picker)
        layout.add_widget(clear_button)

        return layout

    def on_color(self, instance, value):
        self.paint_widget.color = value

    def clear_canvas(self, instance):
        self.paint_widget.canvas.clear()


if __name__ == '__main__':
    PaintApp().run()

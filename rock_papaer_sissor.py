from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import random

class RockPaperScissorsGame(App):
    def build(self):
        self.result_label = Label(text="Choose: Rock, Paper, or Scissors")
        self.player_choice_label = Label(text="Your choice: ")
        self.computer_choice_label = Label(text="Computer's choice: ")
        self.outcome_label = Label(text="Result: ")

        rock_button = Button(text="Rock", on_press=self.play_game)
        paper_button = Button(text="Paper", on_press=self.play_game)
        scissors_button = Button(text="Scissors", on_press=self.play_game)

        layout = BoxLayout(orientation='vertical', spacing=10)
        layout.add_widget(self.result_label)
        layout.add_widget(self.player_choice_label)
        layout.add_widget(self.computer_choice_label)
        layout.add_widget(self.outcome_label)
        layout.add_widget(rock_button)
        layout.add_widget(paper_button)
        layout.add_widget(scissors_button)

        return layout

    def play_game(self, instance):
        choices = ["Rock", "Paper", "Scissors"]
        player_choice = instance.text
        computer_choice = random.choice(choices)

        self.player_choice_label.text = f"Your choice: {player_choice}"
        self.computer_choice_label.text = f"Computer's choice: {computer_choice}"

        if player_choice == computer_choice:
            result = "It's a tie!"
        elif (
            (player_choice == "Rock" and computer_choice == "Scissors") or
            (player_choice == "Paper" and computer_choice == "Rock") or
            (player_choice == "Scissors" and computer_choice == "Paper")
        ):
            result = "You win!"
        else:
            result = "You lose!"

        self.outcome_label.text = f"Result: {result}"

if __name__ == '__main__':
    RockPaperScissorsGame().run()

import tkinter as tk
import random
class Game:
    def __init__(self,root):
        self.user_score = 0
        self.comp_score = 0
        root.title("Rock Paper Scissors")
        root.geometry("500x400")
        root.configure(bg='lightblue')

        tk.Label(root, text="Score:",font=("microsoft himalaya",20), bg ='lightyellow').pack()
        self.score_label = tk.Label(root, text="You:0  Computer:0",font=("microsoft himalaya",20),bg = 'lightyellow')
        self.score_label.pack(pady=10)

        self.result_label = tk.Label(root,text="Choose Rock, Paper, or Scissor",font=("microsoft himalaya",18), bg = 'lightyellow')
        self.result_label.pack(pady=15)

        frame = tk.Frame(root)
        frame.pack(pady=20)
        for choice in ['rock','paper','scissor']:
            button =tk.Button(frame, text=choice.title(),width=15,command=lambda c=choice:self.play_round(c), bg = 'lightyellow')
            button.pack(side=tk.LEFT,padx=10)
        self.play_again_button = tk.Button(root, text="Play Again", width=15,bg = 'lightyellow',
                                        command=self.reset_game, state=tk.DISABLED)
        self.play_again_button.pack(pady=10)

    def play_round(self,user_choice):
        comp_choice = random.choice(['rock','paper','scissor'])
        winner = self.determine_winner(user_choice,comp_choice)
        if winner == 'user':
            self.user_score += 1
            result = "You win this round!"
        elif winner == 'computer':
            self.comp_score += 1
            result = "Computer won this round!"
        else:
            result = "It's a tie!"
        self.score_label.config(text=f"You: {self.user_score}   Computer: {self.comp_score}")
        self.result_label.config(text=f"You chose {user_choice}, computer chose {comp_choice}. {result}")
        self.play_again_button.config(state=tk.NORMAL)

    @staticmethod
    def determine_winner(user, comp):
        if user == comp:
            return 'tie'
        wins = {'rock':'scissor','scissor':'paper','paper':'rock'}
        return 'user' if wins[user] == comp else 'computer'
    def reset_game(self):
        self.user_score = self.comp_score = 0
        self.score_label.config(text="You: 0   Computer: 0")
        self.result_label.config(text="Choose rock, paper, or scissor")
        self.play_again_button.config(state=tk.DISABLED)
        
if __name__ == "__main__":
    root = tk.Tk()
    Game(root)
    root.mainloop()

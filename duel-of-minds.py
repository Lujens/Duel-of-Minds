import tkinter as tk
import random

# Initialize the main application window
root = tk.Tk()
root.title("Duel of Minds: Get Your Facts Straight !")
root.geometry("600x400") # size of the pop-up window

# Define question sets
history_questions = [
    ("True or False: The Great Wall of China was built entirely during the Qin Dynasty.", 
     (False, "The Great Wall of China was not built entirely during the Qin Dynasty. While construction began during the Qin Dynasty (221–206 BC), most of the existing wall was built during the Ming Dynasty (1368–1644 AD).")),
    ("True or False: Julius Caesar was the first Roman Emperor.", 
     (False, "Julius Caesar was not the first Roman Emperor; he was a Roman general and statesman who played a significant role in the transition from the Roman Republic to the Roman Empire. The first Roman Emperor was Augustus, who came to power after Caesar's death.")),
    ("True or False: The Hundred Years' War was fought between England and France.", 
     (True, "The Hundred Years' War was a series of conflicts fought between England and France from 1337 to 1453 over various territorial and dynastic disputes.")),
    ("True or False: The Renaissance began in the 14th century in Italy.", 
     (True, "The Renaissance, a period of cultural, artistic, and intellectual rebirth, began in Italy in the 14th century before spreading to other parts of Europe.")),
    ("True or False: World War II ended in 1945.", 
     (True, "World War II ended in 1945 with the surrender of Japan in September, following the atomic bombings of Hiroshima and Nagasaki and the subsequent unconditional surrender of Japan.")),
    ("True or False: The Industrial Revolution began in Britain during the late 18th century.", 
     (True, "The Industrial Revolution began in Britain in the late 18th century, characterized by the transition to new manufacturing processes and the widespread adoption of machinery.")),
    ("True or False: Nelson Mandela was the first black president of South Africa, elected in 1994.", 
     (True, "Nelson Mandela was indeed the first black president of South Africa, elected in 1994 following the end of apartheid.")),
    ("True or False: The Declaration of Independence was signed in 1776.", 
     (True, "The Declaration of Independence was adopted by the Continental Congress on July 4, 1776, declaring the thirteen American colonies independent from British rule.")),
    ("True or False: The United States entered World War II after the bombing of Pearl Harbor on December 7, 1941.", 
     (True, "The United States entered World War II after the Japanese attack on Pearl Harbor on December 7, 1941.")),
    ("True or False: The Titanic sank in 1912 after hitting an iceberg.", 
     (True, "The Titanic, a British passenger liner, sank on April 15, 1912, after hitting an iceberg during its maiden voyage from Southampton to New York City."))
] 

general_questions = [
    ("True or False: The Pacific Ocean is the largest ocean on Earth.", 
     (True, "The Pacific Ocean is indeed the largest ocean by both surface area and volume.")),
    ("True or False: The Great Wall of China is visible from space.", 
     (False, "Despite the common belief, the Great Wall of China is not visible from space with the unaided eye. Astronauts can see it using specific photography equipment, but it's not visible to the naked eye.")),
    ("True or False: Mount Everest is the tallest mountain in the world.", 
     (True, "Mount Everest is the tallest mountain above sea level, reaching an elevation of 8,848.86 meters (29,031.7 feet).")),
    ("True or False: The capital of Australia is Sydney.", 
     (False, "The capital of Australia is Canberra.")),
    ("True or False: The human body has four lungs.", 
     (False, "The human body typically has two lungs.")),
    ("True or False: he currency of Japan is the yuan.", 
     (False, "The currency of Japan is the yen.")),
    ("True or False: he Amazon Rainforest is primarily located in Africa.", 
     (False, "The Amazon Rainforest is primarily located in South America, spanning across several countries including Brazil, Peru, Colombia, and others.")),
    ("True or False: Water boils at 100 degrees Celsius (212 degrees Fahrenheit).", 
     (True, "Water boils at 100 degrees Celsius (212 degrees Fahrenheit) at sea level under standard atmospheric pressure.")),
    ("True or False: The Statue of Liberty was a gift from France to the United States.", 
     (True, "The Statue of Liberty was a gift from the people of France to the United States, symbolizing freedom and democracy.")),
    ("True or False: The painting Mona Lisa was created by Vincent van Gogh.", 
     (False, 'The painting "Mona Lisa" was created by Leonardo da Vinci, not Vincent van Gogh.'))
]

sports_questions = [
    ("True or False: The Olympic Games were originally held in Rome, Italy.", 
     (False, "The original Olympic Games were held in Olympia, Greece.")),
    ("True or False: Golf was played on the moon by astronaut Alan Shepard during the Apollo 14 mission.", 
     (True, "Alan Shepard famously hit two golf balls on the lunar surface during the Apollo 14 mission.")),
    ("True or False: The Tour de France cycling race was originally started to increase sales for a newspaper.", 
     (True, "The Tour de France was initially organized in 1903 by the newspaper L'Auto to increase its circulation.")),
    ("True or False: The Super Bowl is the most-watched sporting event in the world each year.", 
     (False, "The FIFA World Cup final is generally the most-watched sporting event globally, surpassing the Super Bowl.")),
    ("True or False: The New York Yankees have won more World Series titles than any other team in MLB history.", 
     (True, "The New York Yankees have won 27 World Series titles, the most in MLB history.")),
    ("True or False: In tennis, a 'golden set' is when a player wins a set without losing a single point.", 
     (True, "True or False: A golden set is an extremely rare achievement where a player wins all 24 points of a set.")),
    ("True or False: The National Hockey League (NHL) was founded in the United States.", 
     (False, "The NHL was founded in Montreal, Canada, in 1917.")),
    ("True or False: The term 'grand slam' originates from bridge, a card game, before it was used in sports.", 
     (True, "The term 'grand slam' was used in card games like bridge and whist before it was adopted in sports.")),
    ("True or False: In the NBA, the team with the best regular-season record automatically hosts the first game of the Finals.", 
     (True, "The team with the better regular-season record gets home-court advantage in the NBA Finals.")),
    ("True or False: The term 'hole in one' is exclusive to the sport of golf.", 
     (True, 'A "hole in one" refers specifically to golf when a ball is hit directly from the tee into the cup with one stroke.')),
]

# Entry for player names
player1_label = tk.Label(root, text="Player 1, what's your name? 😊")
player1_label.pack(pady=(10, 5))
player1_name = tk.StringVar()
player2_name = tk.StringVar()
player1_entry = tk.Entry(root, textvariable=player1_name)
player1_entry.pack(pady=(10, 5))
player2_label = tk.Label(root, text="Player 2, don't feel left out. What's yours? 🫡")
player2_label.pack(pady=(10, 5))
player2_entry = tk.Entry(root, textvariable=player2_name)
player2_entry.pack(pady=5)

# Dropdown for selecting topic
topic_choice = tk.StringVar()
topic_choice.set("1")  # Default value
topic_label = tk.Label(root, text="Choose a topic:\n1. History\n2. Sports\n3. General Knowledge")
topic_label.pack(pady=(10, 5))
topic_menu = tk.OptionMenu(root, topic_choice, "1", "2", "3")
topic_menu.pack()

# Status and result display
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, wraplength=550)
result_label.pack(pady=(10, 0))  # Initially hidden

# Button to start the game
start_button = tk.Button(root, text="Let's Get It!", command=lambda: start_game())
start_button.pack(pady=20)

def start_game():
    player1_label.pack_forget()
    player2_label.pack_forget()
    player1_entry.pack_forget()
    player2_entry.pack_forget()
    topic_menu.pack_forget()
    start_button.pack_forget()
    topic_label.pack_forget()

    questions = {
        "1": history_questions,
        "2": sports_questions,
        "3": general_questions
    }.get(topic_choice.get(), history_questions)  # Default to history if something goes wrong

    play_trivia_game(questions)

def play_trivia_game(questions):
    player_scores = {player1_name.get(): 0, player2_name.get(): 0}
    players = [player1_name.get(), player2_name.get()]
    question_count = {player1_name.get(): 0, player2_name.get(): 0}
    questions_asked = [0]  # Use a list for mutable integer
    current_question = [None]  # Mutable container for the current question

    def clear_display():
        """Clears the question and explanation text from the screen before showing final scores."""
        question_info.set("")
        explanation_info.set("")
        answer_entry.delete(0, tk.END)
        answer_entry.pack_forget()
        submit_button.pack_forget()
        next_button.pack_forget()
        current_turn_info.set("")

    def ask_question():
        nonlocal questions
        if questions_asked[0] >= 10:
            clear_display() # Clear the display before displaying the scores.
            result_text.set(f"End of the Duel ! Let's see how you did:\n{players[0]}: {player_scores[players[0]]}\n{players[1]}: {player_scores[players[1]]}")
            next_button.pack_forget()
            return  # End game if both players have answered all their questions

        current_player = players[questions_asked[0] % 2]
        question_num = question_count[current_player] + 1

        # Select and display the current question
        current_question[0] = random.choice(questions)
        question, (correct_answer, explanation) = current_question[0]
        current_turn_info.set(f"{current_player}, here's your {ordinal(question_num)} question:")
        question_info.set(question)

        answer_entry.config(state='normal')
        submit_button.pack(pady=(5, 20))

    def check_answer():
        nonlocal questions_asked
        current_player = players[questions_asked[0] % 2]
        question, (correct_answer, explanation) = current_question[0]
        user_answer = answer_var.get().strip().lower() == str(correct_answer).lower()
        if user_answer:
            player_scores[current_player] += 3  # Increment score by 3 (just like football)
            explanation_info.set("What a genius!🤯 This is Correct! " + explanation)
        else:
            explanation_info.set(f"Nah. Get Your Facts Straight👎🏽. This is Incorrect! The correct answer is: {correct_answer}. {explanation}")

        questions.remove(current_question[0])  # Remove the answered question
        question_count[current_player] += 1  # Increment question count for current player
        questions_asked[0] += 1  # Increment total questions asked
        answer_entry.config(state='disabled')
        submit_button.pack_forget()

    # UI components for the game
    current_turn_info = tk.StringVar()
    tk.Label(root, textvariable=current_turn_info).pack()

    question_info = tk.StringVar()
    tk.Label(root, textvariable=question_info, wraplength=550).pack()

    answer_var = tk.StringVar()
    answer_entry = tk.Entry(root, textvariable=answer_var)
    answer_entry.pack()

    submit_button = tk.Button(root, text="👉🏽Check Your Fact", command=check_answer)

    explanation_info = tk.StringVar()
    tk.Label(root, textvariable=explanation_info, wraplength=550).pack()

    next_button = tk.Button(root, text="🧠 Next Question", command=ask_question)
    next_button.pack(pady=(10, 20))

    ask_question()  # Start the first question

def ordinal(n):
    """Convert an integer into its ordinal representation to properly format question labels."""
    if 10 <= n % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return str(n) + suffix

root.mainloop()


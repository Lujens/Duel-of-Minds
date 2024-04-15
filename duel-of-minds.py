import random

# History questions:
history_questions = [
    ("The Great Wall of China was built entirely during the Qin Dynasty.", 
     (False, "The Great Wall of China was not built entirely during the Qin Dynasty. While construction began during the Qin Dynasty (221–206 BC), most of the existing wall was built during the Ming Dynasty (1368–1644 AD).")),
    ("Julius Caesar was the first Roman Emperor.", 
     (False, "Julius Caesar was not the first Roman Emperor; he was a Roman general and statesman who played a significant role in the transition from the Roman Republic to the Roman Empire. The first Roman Emperor was Augustus, who came to power after Caesar's death.")),
    ("The Hundred Years' War was fought between England and France.", 
     (True, "The Hundred Years' War was a series of conflicts fought between England and France from 1337 to 1453 over various territorial and dynastic disputes.")),
    ("The Renaissance began in the 14th century in Italy.", 
     (True, "The Renaissance, a period of cultural, artistic, and intellectual rebirth, began in Italy in the 14th century before spreading to other parts of Europe.")),
    ("World War II ended in 1945.", 
     (True, "World War II ended in 1945 with the surrender of Japan in September, following the atomic bombings of Hiroshima and Nagasaki and the subsequent unconditional surrender of Japan.")),
    ("The Industrial Revolution began in Britain during the late 18th century.", 
     (True, "The Industrial Revolution began in Britain in the late 18th century, characterized by the transition to new manufacturing processes and the widespread adoption of machinery.")),
    ("Nelson Mandela was the first black president of South Africa, elected in 1994.", 
     (True, "Nelson Mandela was indeed the first black president of South Africa, elected in 1994 following the end of apartheid.")),
    ("The Declaration of Independence was signed in 1776.", 
     (True, "The Declaration of Independence was adopted by the Continental Congress on July 4, 1776, declaring the thirteen American colonies independent from British rule.")),
    ("The United States entered World War II after the bombing of Pearl Harbor on December 7, 1941.", 
     (True, "The United States entered World War II after the Japanese attack on Pearl Harbor on December 7, 1941.")),
    ("The Titanic sank in 1912 after hitting an iceberg.", 
     (True, "The Titanic, a British passenger liner, sank on April 15, 1912, after hitting an iceberg during its maiden voyage from Southampton to New York City."))
]

# General knowledge questions:
general_questions = [
    ("The Pacific Ocean is the largest ocean on Earth.", 
     (True, "The Pacific Ocean is indeed the largest ocean by both surface area and volume.")),
    ("The Great Wall of China is visible from space.", 
     (False, "Despite the common belief, the Great Wall of China is not visible from space with the unaided eye. Astronauts can see it using specific photography equipment, but it's not visible to the naked eye.")),
    ("Mount Everest is the tallest mountain in the world.", 
     (True, "Mount Everest is the tallest mountain above sea level, reaching an elevation of 8,848.86 meters (29,031.7 feet).")),
    ("The capital of Australia is Sydney.", 
     (False, "The capital of Australia is Canberra.")),
    ("The human body has four lungs.", 
     (False, "The human body typically has two lungs.")),
    ("The currency of Japan is the yuan.", 
     (False, "The currency of Japan is the yen.")),
    ("The Amazon Rainforest is primarily located in Africa.", 
     (False, "The Amazon Rainforest is primarily located in South America, spanning across several countries including Brazil, Peru, Colombia, and others.")),
    ("Water boils at 100 degrees Celsius (212 degrees Fahrenheit).", 
     (True, "Water boils at 100 degrees Celsius (212 degrees Fahrenheit) at sea level under standard atmospheric pressure.")),
    ("The Statue of Liberty was a gift from France to the United States.", 
     (True, "The Statue of Liberty was a gift from the people of France to the United States, symbolizing freedom and democracy.")),
    ("The painting Mona Lisa was created by Vincent van Gogh.", 
     (False, 'The painting "Mona Lisa" was created by Leonardo da Vinci, not Vincent van Gogh.'))
]
# Sports Questions:
sports_questions = [
    ("The Olympic Games were originally held in Rome, Italy.", 
     (False, "The original Olympic Games were held in Olympia, Greece.")),
    ("Michael Phelps has won more Olympic gold medals than any other athlete in history.", 
     (True, "Michael Phelps has won a total of 23 Olympic gold medals.")),
    ("In basketball, the term 'slam dunk' was first introduced by the NBA.", 
     (False, "The term 'slam dunk' was popularized in basketball well before the NBA adopted it as a key part of the game.")),
    ("Golf was played on the moon by astronaut Alan Shepard during the Apollo 14 mission.", 
     (True, "Alan Shepard famously hit two golf balls on the lunar surface during the Apollo 14 mission.")),
    ("The FIFA World Cup has always included teams from every continent since its inception.", 
     (False, "The initial World Cups did not have as inclusive a representation of teams from every continent as they do today.")),
    ("Serena Williams has won more Grand Slam singles titles than any other woman in the Open Era.", 
     (True, "Serena Williams has won 23 Grand Slam singles titles, the most by any player in the Open Era.")),
    ("The marathon race distance is exactly the same distance as the original run from the Battle of Marathon to Athens.", 
     (False, "The original marathon distance was approximately 40 kilometers, but the official marathon distance now is 42.195 kilometers (26.219 miles).")),
    ("In cricket, a 'hat-trick' refers to a bowler taking three wickets with consecutive deliveries.", 
     (True, "A hat-trick in cricket is achieved when a bowler takes three wickets with three consecutive balls.")),
    ("The Tour de France cycling race was originally started to increase sales for a newspaper.", 
     (True, "The Tour de France was initially organized in 1903 by the newspaper L'Auto to increase its circulation.")),
    ("The Super Bowl is the most-watched sporting event in the world each year.", 
     (False, "The FIFA World Cup final is generally the most-watched sporting event globally, surpassing the Super Bowl.")),
    ("Lionel Messi has won the FIFA World Player of the Year award more times than Cristiano Ronaldo.", 
     (True, "Both players have won numerous awards, but their totals can vary depending on the specific award in question. Messi has won the Ballon d'Or award more times than Ronaldo.")),
    ("The New York Yankees have won more World Series titles than any other team in MLB history.", 
     (True, "The New York Yankees have won 27 World Series titles, the most in MLB history.")),
    ("In tennis, a 'golden set' is when a player wins a set without losing a single point.", 
     (True, "A golden set is an extremely rare achievement where a player wins all 24 points of a set.")),
    ("The National Hockey League (NHL) was founded in the United States.", 
     (False, "The NHL was founded in Montreal, Canada, in 1917.")),
    ("A regulation soccer match consists of two 45-minute halves with a 15-minute halftime break.", 
     (True, "This is the standard format for regulation soccer matches.")),
    ("The term 'grand slam' originates from bridge, a card game, before it was used in sports.", 
     (True, "The term 'grand slam' was used in card games like bridge and whist before it was adopted in sports.")),
    ("In the NBA, the team with the best regular-season record automatically hosts the first game of the Finals.", 
     (True, "The team with the better regular-season record gets home-court advantage in the NBA Finals.")),
    ("The first Winter Olympic Games were held in Chamonix, France, in 1924.", 
     (True, "The first Winter Olympics took place in Chamonix in 1924.")),
    ("The term 'hole in one' is exclusive to the sport of golf.", 
     (True, 'A "hole in one" refers specifically to golf when a ball is hit directly from the tee into the cup with one stroke.')),
    ("Rugby is older than American football, and American football evolved from rugby.", 
     (True, "Rugby dates back to the 19th century and influenced the development of American football."))
]

#Null Scores
player1_score = 0
player2_socre = 0


# OUTPUT

print("Welcome to Duel of Minds: Get Your Facts Straight")

player_1_name = input("Player 1, What's your name?\n")

player_2_name = input("Player 2, What's your name?\n")

topic = input("Choose a topic:\n 1. History\n 2. Sports\n 3. General Knowledge\n" )

print("Alright.", topic, "Let's Get Started with the Duel of Minds!")


# Game Mechanics and Flow

question_set = player_history_questions if topic_choice == '1' else []

    player1_score = 0
    player2_score = 0
    num_questions = min(5, len(question_set))

    for i in range(num_questions):
        # Each player takes a turn
        for player_name in [player1_name, player2_name]:
            if not question_set:
                break  # No more questions available
            question, (correct_answer, explanation) = random.choice(question_set)
            print(f"\n{player_name}, your question is: {question}")
            player_response = input("True or False? ").strip().lower() == str(correct_answer).lower()
            if player_response:
                print("Correct!")
                if player_name == player1_name:
                    player1_score += 1
                else:
                    player2_score += 1
            else:
                print("Incorrect!")
            print(f"Explanation: {explanation}")  # Display the explanation regardless of the answer
            question_set.remove((question, (correct_answer, explanation)))  # Remove the used question


  
  

  

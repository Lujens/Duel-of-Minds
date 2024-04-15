import random

#history questions:

history_questions = [("The Great Wall of China was built entirely during the Qin Dynasty.", (False, "The Great Wall of China was not built entirely during the Qin Dynasty. While construction began during the Qin Dynasty (221–206 BC), most of the existing wall was built during the Ming Dynasty (1368–1644 AD).")), ("Julius Caesar was the first Roman Emperor.", (False, "Julius Caesar was not the first Roman Emperor; he was a Roman general and statesman who played a significant role in the transition from the Roman Republic to the Roman Empire. The first Roman Emperor was Augustus, who came to power after Caesar's death,")), ("The Hundred Years' War was fought between England and France.", (True, "The Hundred Years' War was a series of conflicts fought between England and France from 1337 to 1453 over various territorial and dynastic disputes.")), ("The Renaissance began in the 14th century in Italy.", (True, "The Renaissance, a period of cultural, artistic, and intellectual rebirth, began in Italy in the 14th century before spreading to other parts of Europe.")), ("World War II ended in 1945.", (True, "World War II ended in 1945 with the surrender of Japan in September, following the atomic bombings of Hiroshima and Nagasaki and the subsequent unconditional surrender of Japan.")), ("The Industrial Revolution began in Britain during the late 18th century.", (True, "The Industrial Revolution began in Britain in the late 18th century, characterized by the transition to new manufacturing processes and the widespread adoption of machinery.")), ("Nelson Mandela was the first black president of South Africa, elected in 1994.", (True, "Nelson Mandela was indeed the first black president of South Africa, elected in 1994 following the end of apartheid.")), ("The Declaration of Independence was signed in 1776.", (True, "The Declaration of Independence was adopted by the Continental Congress on July 4, 1776, declaring the thirteen American colonies independent from British rule.")), ("The United States entered World War II after the bombing of Pearl Harbor on December 7, 1941.", (True, "The United States entered World War II after the Japanese attack on Pearl Harbor on December 7, 1941.")), ("The Titanic sank in 1912 after hitting an iceberg.", (True, "The Titanic, a British passenger liner, sank on April 15, 1912, after hitting an iceberg during its maiden voyage from Southampton to New York City."));
("The Great Depression began in the United States in 1929 after the stock market crash.", (True, "The Great Depression indeed began in the United States in 1929 after the stock market crash of October 1929, also known as Black Tuesday, which led to a severe economic downturn affecting countries worldwide.")), ("The Battle of Stalingrad was a decisive victory for Nazi Germany during World War II.", (False, "The Battle of Stalingrad, fought from 1942 to 1943, resulted in a decisive victory for the Soviet Union, not Nazi Germany. It marked a turning point in the war as it was the first major defeat for the German army on the Eastern Front.")), ("The Maya civilization flourished primarily in present-day Mexico and Central America.", (True, "The Maya civilization indeed flourished primarily in present-day Mexico and Central America, encompassing regions of what are now Guatemala, Belize, Honduras, and El Salvador.")), ("The Magna Carta was signed by King Henry VIII of England in 1215.", (False, "The Magna Carta was signed by King John of England in 1215, not King Henry VIII. It is considered one of the most important documents in the history of constitutional law, as it established the principle that the king was subject to the law.")), ("The Taj Mahal was built as a palace for a Mughal emperor.", (False, "The Taj Mahal was built by the Mughal emperor Shah Jahan as a mausoleum for his wife Mumtaz Mahal, not as a palace. It is regarded as one of the most beautiful buildings in the world and is a UNESCO World Heritage Site.")), ("The Battle of Trafalgar, fought in 1805, marked a decisive victory for Napoleon Bonaparte.", (False, "The Battle of Trafalgar, fought in 1805, was a decisive naval victory for the British Royal Navy under Admiral Horatio Nelson against the combined fleets of France and Spain, not for Napoleon Bonaparte.")), ("The Trail of Tears refers to the forced relocation of Native American tribes, primarily the Cherokee, from their ancestral lands in the southeastern United States to present-day Oklahoma.", (True, "The Trail of Tears indeed refers to the forced relocation of several Native American tribes, including the Cherokee, from their ancestral lands in the southeastern United States to Indian Territory (present-day Oklahoma) following the Indian Removal Act of 1830.")), ("The Cuban Missile Crisis occurred in 1962 and brought the world to the brink of nuclear war between the United States and the Soviet Union.", (True, "The Cuban Missile Crisis indeed occurred in 1962, when the United States discovered that the Soviet Union had placed nuclear missiles in Cuba. It was a tense standoff between the two superpowers, bringing the world to the brink of nuclear war."));
("The Battle of Saratoga, fought during the American Revolutionary War in 1777, is considered a turning point as it convinced France to openly support the American cause against Britain.", (True, "The Battle of Saratoga, fought in 1777, is considered a turning point in the American Revolutionary War as the American victory convinced France to openly support the American cause against Britain by providing military assistance and ultimately entering the war as an ally.")), ("The Renaissance, a period of cultural, artistic, and intellectual revival, began in Italy in the 14th century and later spread to the rest of Europe.", (True, "The Renaissance indeed began in Italy in the 14th century before spreading to the rest of Europe. It was characterized by a renewed interest in classical learning, humanism, and artistic expression."))]

#general knowledge questions:

general_questions = [("The Pacific Ocean is the largest ocean on Earth.", (True, "The Pacific Ocean is indeed the largest ocean by both surface area and volume.")), ("The Great Wall of China is visible from space.", (False, "Despite the common belief, the Great Wall of China is not visible from space with the unaided eye. Astronauts can see it using specific photography equipment, but it's not visible to the naked eye.")), ("Mount Everest is the tallest mountain in the world.", (True, "Mount Everest is the tallest mountain above the sea level, reaching an elevation of 8,848.86 meters (29,031.7 feet).")), ("The capital of Australia is Sydney.", (False, "the capital of Australia is Canberra.")), ("The human body has four lungs.", (False, "the human body tipically has two lungs.")), ("The currency of Japan is the yuan.", (False, "the currency of Japan is the yen.")), ("The Amazon Rainforest is primarily located in Africa.", (False, "the Amazon Rainforest is primarily located in South America, spanning across several countries including Brazil, Peru, Colombia, and others.")), ("Water boils at 100 degrees Celsius (212 degrees Fahrenheit).", (True, "water boils at 100 degrees Celsius (212 degrees Fahrenheit) at sea level under standard atmosphetic pressure.")), ("The Statue of Liberty was a gift from France to the United States.", (True, "the Statue of Liberty was a gift from the people of France to the United States, symbolizing freedom and democracy.")), ("The painting Mona Lisa was created by Vincent van Gogh.", (False, 'the painting "Mona Lisa" was created by Leonardo da Vinci, not Vincent van Gogh."));
("The Great Wall of China is visible from space with the naked eye.", (False, "contrary to popular belief, the Great Wall of China is not visible from space with the naked eye.")), ('Shakespeare invented the name "Jessica."', (True, 'the name "Jessica" first appears in Shakespeare's play "The Merchant of Venice."')), ("The first person to walk on the moon was Neil Armstrong in 1969", (True, "Neil Armstrong became the first person to walk on the moon on July 20, 1969.")), ("Albert Einstein was awarded the Nobel Prize in Physics for his theory of relativity.", (False, Einstein was awarded the Nobel Prize in Physics in 1921 for his explanation of the photoelectric effect, not for his theory of relativity.")), ("The longest river in the world is the Nile.", (False, "while the Nile was traditionally considered the longest, recent studies and measurements suggest that the Amazon River might be sltghtly longer.")), ("Penguins are capable of flying.", (False, "penguins are flightless birds, adapted for life in water.")), ("The internet was originally developed as a means of secure communication for the U.S. military.", (True, "the precursor to the internet, ARPANET, was developed by the U.S. Department of Defense as a means of secure communication.")), ("The largest desert in the world is the Sahara Desert.", (False, "while the Sahara Desert is undoubtedly vast, covering much of North Africa, it is not the largest desert in the world in terms of total area. The largest desert is actually Antarctica. Despite being covered in ice, Antarctica meets the definition of a desert due to its extremely low precipitation levels. It is the driest and windiest continent on Earth, with precipitation levels so low that it qualifies as a desert.")), ("The human body can't distinguish between naturally occurring sugars and added sugars.", (True, "the statement is generally true. From a biochemical standpoint, the body processes naturally occurring sugars found in foods like fruits, vegetables, and dairy products in the same way as added sugars found in processed foods and beverages. Both types of sugars are broken down into glucose and used by the body for energy. However, there are nuances in how these sugars are consumed within the context of whole foods versus processed foods, which can affect factors like satiety, nutrient density, and overall health outcomes."))]

#Sports Questions:

sports_questions = [("The Olympic Games were originally held in Rome, Italy.", (False, "The original Olympic Games were held in Olympia, Greece." )), ("Michael Phelps has won more Olympic gold medals than any other athlete in history.", (True, "Michael Phelps has won a total of 23 Olympic gold medals.")), ("In basketball, the term 'slam dunk' was first introduced by the NBA.", (False,'The term "slam dunk" was popularized in basketball well before the NBA adopted it as a key part of the game.')), ("Golf was played on the moon by astronaut Alan Shepard during the Apollo 14 mission.", (True, "Alan Shepard famously hit two golf balls on the lunar surface during the Apollo 14 mission.")), ("The FIFA World Cup has always included teams from every continent since its inception.", (False, "The initial World Cups did not have as inclusive a representation of teams from every continent as they do today.")), ("Serena Williams has won more Grand Slam singles titles than any other woman in the Open Era.", (True, "Serena Williams has won 23 Grand Slam singles titles, the most by any player in the Open Era.")), ("The marathon race distance is exactly the same distance as the original run from the Battle of Marathon to Athens.", (False, "the original marathon distance was approximately 40 kilometers, but the official marathon distance now is 42.195 kilometers (26.219 miles).")), ("In cricket, a 'hat-trick' refers to a bowler taking three wickets with consecutive deliveries.", (True, "a hat-trick in cricket is achieved when a bowler takes three wickets with three consecutive balls.")), ("The Tour de France cycling race was originally started to increase sales for a newspaper.", (True, "the Tour de France was initially organized in 1903 by the newspaper L'Auto to increase its circulation.")), ("The Super Bowl is the most-watched sporting event in the world each year.", (False, "The FIFA World Cup final is generally the most-watched sporting event globally, surpassing the Super Bowl."));
		   ("Lionel Messi has won the FIFA World Player of the Year award more times than Cristiano Ronaldo.", (True, "Both players have won numerous awards, but their totals can vary depending on the specific award in question. Messi has won the Ballon d'Or award more times than Ronaldo.")), ("The New York Yankees have won more World Series titles than any other team in MLB history.", (True, "The New York Yankees have won 27 World Series titles than any other team in MLB history")), ("In tennis, a 'golden set' is when a player wins a set without losing a single point.", (True, "A golden set is an extremely rare achievement where a player wins all 24 points of a set.")), ("The National Hockey League (NHL) was founded in the United States.", (False, "The NHL was founded in Montreal, Canada, in 1917.")), ("A regulation soccer match consists of two 45-minute halves with a 15-minute halftime break.", (True, "This is the standard format for regulation soccer matches.")), ("The term 'grand slam' originates from bridge, a card game, before it was used in sports.", (True, 'the term "grand slam" was used in card games like bridge and whist before it was adopted in sports.')), ("In the NBA, the team with the best regular-season record automatically hosts the first game of the Finals.", (True, "The team with the better regular-season record gets home-court advantage in the NBA Finals.")), ("The first Winter Olympic Games were held in Chamonix, France, in 1924.", (True, "the first Winter Olympics took place in Charmonix in 1924.")), ("The term 'hole in one' is exclusive to the sport of golf.", (True, 'A "hole in one" refers specifically to golf when a ball is hit directly from the tee into the cup with one storke.")), ("Rugby is older than American football, and American football evolved from rugby.", (True, "Rugby dates back to the 19th century and influenced the development of American football."))]

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


  
  

  

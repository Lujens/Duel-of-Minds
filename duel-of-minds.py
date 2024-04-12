import random

#player one history questions:

player1_hq = ["True or False: The Great Wall of China was built entirely during the Qin Dynasty.","True or False: Julius Caesar was the first Roman Emperor.","True or False: The Hundred Years' War was fought between England and France.", "True or False: The Renaissance began in the 14th century in Italy.","True or False: World War II ended in 1945.", "True or False: The Industrial Revolution began in Britain during the late 18th century.", "True or False: Nelson Mandela was the first black president of South Africa, elected in 1994.", "True or False: The Declaration of Independence was signed in 1776.", "True or False: The United States entered World War II after the bombing of Pearl Harbor on December 7, 1941.", "True or False: The Titanic sank in 1912 after hitting an iceberg."]

#player one history answers:

player1_ha = ["False. The Great Wall of China was not built entirely during the Qin Dynasty. While construction began during the Qin Dynasty (221–206 BC), most of the existing wall was built during the Ming Dynasty (1368-1644 AD).", "False. Julius Caesar was not the first Roman Emperor; he was a Roman general and statesman who played a significant role in the transition from the Roman Republic to the Roman Empire. The first Roman Emperor was Augustus, who came to power after Caesar's death.", "True.  The Hundred Years' War was a series of conflicts fought between England and France from 1337 to 1453 over various territorial and dynastic disputes.", "True. The Renaissance, a period of cultural, artistic, and intellectual rebirth, began in Italy in the 14th century before spreading to other parts of Europe.", "True. World War II ended in 1945 with the surrender of Japan in September, following the atomic bombings of Hiroshima and Nagasaki and the subsequent unconditional surrender of Japan.", "True. The Industrial Revolution began in Britain in the late 18th century, characterized by the transition to new manufacturing processes and the widespread adoption of machinery.", "True. Nelson Mandela was indeed the first black president of South Africa, elected in 1994 following the end of apartheid.", "True. The Declaration of Independence was adopted by the Continental Congress on July 4, 1776, declaring the thirteen American colonies independent from British rule.", "True. The United States entered World War II after the Japanese attack on Pearl Harbor on December 7, 1941.", "True. The Titanic, a British passenger liner, sank on April 15, 1912, after hitting an iceberg during its maiden voyage from Southampton to New York City."]

#player two history questions:

player2_hq = ["True or False: The Great Depression began in the United States in 1929 after the stock market crash.", "True or False: The Battle of Stalingrad was a decisive victory for Nazi Germany during World War II.", "True or False: The Maya civilization flourished primarily in present-day Mexico and Central America.", "True or False: The Magna Carta was signed by King Henry VIII of England in 1215.", "True or False: The Taj Mahal was built as a palace for a Mughal emperor.", "True or False: The Battle of Trafalgar, fought in 1805, marked a decisive victory for Napoleon Bonaparte.", "True or False: The Trail of Tears refers to the forced relocation of Native American tribes, primarily the Cherokee, from their ancestral lands in the southeastern United States to present-day Oklahoma.", "True or False: The Cuban Missile Crisis occurred in 1962 and brought the world to the brink of nuclear war between the United States and the Soviet Union.", "True or False: The Battle of Saratoga, fought during the American Revolutionary War in 1777, is considered a turning point as it convinced France to openly support the American cause against Britain.", "True or False: The Renaissance, a period of cultural, artistic, and intellectual revival, began in Italy in the 14th century and later spread to the rest of Europe."]

#player two history answers:

player2_ha = ["True. The Great Depression indeed began in the United States in 1929 after the stock market crash of October 1929, also known as Black Tuesday, which led to a severe economic downturn affecting countries worldwide.", "False.  The Battle of Stalingrad, fought from 1942 to 1943, resulted in a decisive victory for the Soviet Union, not Nazi Germany. It marked a turning point in the war as it was the first major defeat for the German army on the Eastern Front.", "True. The Maya civilization indeed flourished primarily in present-day Mexico and Central America, encompassing regions of what are now Guatemala, Belize, Honduras, and El Salvador.", "False. The Magna Carta was signed by King John of England in 1215, not King Henry VIII. It is considered one of the most important documents in the history of constitutional law, as it established the principle that the king was subject to the law.", "False. The Taj Mahal was built by the Mughal emperor Shah Jahan as a mausoleum for his wife Mumtaz Mahal, not as a palace. It is regarded as one of the most beautiful buildings in the world and is a UNESCO World Heritage Site.", "False. The Taj Mahal was built by the Mughal emperor Shah Jahan as a mausoleum for his wife Mumtaz Mahal, not as a palace. It is regarded as one of the most beautiful buildings in the world and is a UNESCO World Heritage Site.", "False. The Battle of Trafalgar, fought in 1805, was a decisive naval victory for the British Royal Navy under Admiral Horatio Nelson against the combined fleets of France and Spain, not for Napoleon Bonaparte.", "True. The Trail of Tears indeed refers to the forced relocation of several Native American tribes, including the Cherokee, from their ancestral lands in the southeastern United States to Indian Territory (present-day Oklahoma) following the Indian Removal Act of 1830.", "True. The Cuban Missile Crisis indeed occurred in 1962, when the United States discovered that the Soviet Union had placed nuclear missiles in Cuba. It was a tense standoff between the two superpowers, bringing the world to the brink of nuclear war.", "True.  The Battle of Saratoga, fought in 1777, is considered a turning point in the American Revolutionary War as the American victory convinced France to openly support the American cause against Britain by providing military assistance and ultimately entering the war as an ally.", "True. The Renaissance indeed began in Italy in the 14th century before spreading to the rest of Europe. It was characterized by a renewed interest in classical learning, humanism, and artistic expression."]

#player one general knowledge questions:

player1_gq = ["True or False: The Pacific Ocean is the largest ocean on Earth.", "True or False: The Great Wall of China is visible from space.", "True or False: Mount Everest is the tallest mountain in the world.", "True or False: The capital of Australia is Sydney.", "True or False: The human body has four lungs.", "True or False: The currency of Japan is the yuan.", "True or False: The Amazon Rainforest is primarily located in Africa.", " True or False: Water boils at 100 degrees Celsius (212 degrees Fahrenheit).", "True or False: The Statue of Liberty was a gift from France to the United States.", "True or False: The painting Mona Lisa was created by Vincent van Gogh."]

#player one general knowledge answers:

player1_ga = ["True. The Pacific Ocean is indeed the largest ocean by both surface area and volume.", "False. Despite the common belief, the Great Wall of China is not visible from space with the unaided eye. Astronauts can see it using specific photography equipment, but it's not visible to the naked eye.", "True. Mount Everest is the tallest mountain above sea level, reaching an elevation of 8,848.86 meters (29,031.7 feet).", "False. "]

# Player 2 general knowledge questions:

player2_gq = ["True or False: The Great Wall of China is visible from space with the naked eye.", "True or False: Shakespeare invented the name 'Jessica.'", "True or False: The human body has four lungs.", "True or False: The capital of Australia is Sydney.", "Water boils at 100 degrees Celsius at sea level.", "True or False: The first person to walk on the moon was Neil Armstrong in 1969", "True or False: Albert Einstein was awarded the Nobel Prize in Physics for his theory of relativity.", "True or False: The longest river in the world is the Nile.", "True or False: Penguins are capable of flying.", "True or False: The internet was originally developed as a means of secure communication for the U.S. military."]

#Player 2 general knowledge answers:

player2_ga = ["False. Contrary to popular belief, the Great Wall of China is not visible from space with the naked eye.", "True. The name 'Jessica' first appears in Shakespeare's play 'The Merchant of Venice'.", "False. The human body has two lungs, not four.", "False. The capital of Australia is Canberra, not Sydney.", "True. At sea level, water boils at 100 degrees Celsius (212 degrees Fahrenheit).", "True. Neil Armstrong became the first person to walk on the moon on July 20, 1969.", "False. Einstein was awarded the Nobel Prize in Physics in 1921 for his explanation of the photoelectric effect, not for his theory of relativity.", "False. While the Nile was traditionally considered the longest, recent studies and measurements suggest that the Amazon River might be slightly longer.", "False. Penguins are flightless birds, adapted for life in the water.", "True. The precursor to the internet, ARPANET, was developed by the U.S. Department of Defense as a means of secure communication."]

# Player 1 Sports Questions:

player1_sq = ["True or False: The Olympic Games were originally held in Rome, Italy.", "True or False: Michael Phelps has won more Olympic gold medals than any other athlete in history.", "True or False: In basketball, the term 'slam dunk' was first introduced by the NBA.", "True or False: Golf was played on the moon by astronaut Alan Shepard during the Apollo 14 mission.", "True or False: The FIFA World Cup has always included teams from every continent since its inception.", "True or False: Serena Williams has won more Grand Slam singles titles than any other woman in the Open Era.", "True or False: The marathon race distance is exactly the same distance as the original run from the Battle of Marathon to Athens.", "True or False: In cricket, a 'hat-trick' refers to a bowler taking three wickets with consecutive deliveries.", "True or False: The Tour de France cycling race was originally started to increase sales for a newspaper.", "True or False: The Super Bowl is the most-watched sporting event in the world each year."]

#Player 1 Sports Answers

player1_sa = ["False. The original Olympic Games were held in Olympia, Greece.", "True. Michael Phelps has won a total of 23 Olympic gold medals.", 'False. The term "slam dunk" was popularized in basketball well before the NBA adopted it as a key part of the game.', "True. Alan Shepard famously hit two golf balls on the lunar surface during the Apollo 14 mission.", "False. The initial World Cups did not have as inclusive a representation of teams from every continent as they do today.", "True. Serena Williams has won 23 Grand Slam singles titles, the most by any player in the Open Era.",  "False. The original marathon distance was approximately 40 kilometers, but the official marathon distance now is 42.195 kilometers (26.219 miles).", "True. A hat-trick in cricket is achieved when a bowler takes three wickets with three consecutive balls.", "True. The Tour de France was initially organized in 1903 by the newspaper L'Auto to increase its circulation.", "False. The FIFA World Cup final is generally the most-watched sporting event globally, surpassing the Super Bowl."]

# Player 2 Sports Questions

player2_sq = ["True or False: Lionel Messi has won the FIFA World Player of the Year award more times than Cristiano Ronaldo.", "True or False: The New York Yankees have won more World Series titles than any other team in MLB history.", "True or False: In tennis, a 'golden set' is when a player wins a set without losing a single point.", "True or False: The National Hockey League (NHL) was founded in the United States.", "True or False: A regulation soccer match consists of two 45-minute halves with a 15-minute halftime break.", "True or False: The term 'grand slam' originates from bridge, a card game, before it was used in sports.", "True or False: In the NBA, the team with the best regular-season record automatically hosts the first game of the Finals.", "True or False: The first Winter Olympic Games were held in Chamonix, France, in 1924.", "True or False: The term 'hole in one' is exclusive to the sport of golf.", "True or False: Rugby is older than American football, and American football evolved from rugby."]

# Player 2 Sports Answers

player2_sa = ["True (as of 2024). Both players have won numerous awards, but their totals can vary depending on the specific award in question. Messi has won the Ballon d'Or award more times than Ronaldo.", "True. The New York Yankees have won 27 World Series titles, the most in MLB history.", "True. A golden set is an extremely rare achievement where a player wins all 24 points of a set.", "False. The NHL was founded in Montreal, Canada, in 1917.", "True. This is the standard format for regulation soccer matches.", 'True. The term "grand slam" was used in card games like bridge and whist before it was adopted in sports.', "True. The team with the better regular-season record gets home-court advantage in the NBA Finals.", "True. The first Winter Olympics took place in Chamonix in 1924.", 'True. A "hole in one" refers specifically to golf when a ball is hit directly from the tee into the cup with one stroke.', "True. Rugby dates back to the 19th century and influenced the development of American football."]

#Null Scores
player1_score = 0
player2_socre = 0


# OUTPUT

print("Welcome to Duel of Minds: Get Your Facts Straight")

player_1_name = input("Player 1, What's your name?\n")

player_2_name = input("Player 2, What's your name?\n")

topic = input("Choose a topic:\n 1. History\n 2. Sports\n 3. General Knowledge\n" )

print("Alright.", topic, "Let's Get Started with the Duel of Minds!")

if topic == "1" or topic == "History":
  p1_question = random.choice(player1_hq)

print(player_1_name,", Here is your first question:")
print(p1_question)

player1_input = input()

if p1_question == player1_hq[5]:
	if player1_input == player1_ha[5]: #not defined yet
		player1_score = player1_score + 3
		print("I recognize a genius when I see one ! Bravo.")
		print("The answer is indeed: ", player1_ha[5])
	else:
		print("Nah, that's incorrect.")
		print("The correct answer is: ", player1_ha[5])
  

# Game Mechanics and Flow




  
  

  

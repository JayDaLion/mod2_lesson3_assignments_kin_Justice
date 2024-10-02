"""#lucky draw my code first teachers after
import random

participant = ['Santos', 'Kinard', 'Seyci', 'Xavier', 'Alex', 'doe', 'john',]
drawn_name = []

while participant != 'Alex':
    for name in participant:
        random.choices(name)
        if name != "Alex":
             
            drawn_name.append(name)
            participant.remove(name)
        continue
    if name == "Alex":
            print(f"Hi {name}")
            break"""

"""import random

participant = ['Santos', 'Kinard', 'Seyci', 'Xavier', 'Alex', 'doe', 'john',]
while 'Alex' not in random.choices(participant, k=1):
     pass

print("Hi Alex")"""

"""#random steps
import random

directions = ['North', 'South', 'East' ,'West']

for step in range(10):
    step_direction = random.choice(directions)
    print(f"step {step + 1}: The entity moves 10 steps to the {step_direction}.")"""


"""#dice rolls
import random

while True:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print(f"Dice1: {dice1}, Dice2: {dice2}")
    if dice1== dice2:
        print(f"Both dice landed on {dice1}.")
        break"""


"""#quiz master shufffle
import random
questions = ['Who is mj','What is ac','When will love come','Where are you now that i need u',]
random.shuffle(questions)
for question in questions:
    print(questions)
    break"""

"""#classroom attendence
import random
students_names = ["kinard", "seyci", "xavier", "tyler", "tyson", "philip", "brad", "chad", "timmy", "jimmy", "tommy",]
selected_students = random.sample(students_names, 5)

for name in selected_students:
    print(f"is {name} present?")"""
    
"""#passwords
import random
import string

characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(characters) for _ in range(9) )
print(f"Generated password: {password}")"""

"""#dynamic color gen
import random
num_colors = 10

for _ in range(num_colors):
    red = random.randint(0,255)
    green= random.randint(0,255)
    blue = random.randint(0,255)
    print(f"R: {red}, G: {green}, B; {blue}")"""


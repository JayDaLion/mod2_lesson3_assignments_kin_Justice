"""#marshmellow example
marshmallows = 4
while marshmallows < 5:
    marshmallows += 1
    print("Added a marshmellow! Now there are " + str(marshmallows) + " marshmallows.")"""

"""#down we go
steps = 40

while steps > 0:
    print("descending the stairs, "+ str(steps) + " steps remaing")
    steps -= 1
print("we reached the bottom")"""

"""#The final countdown 
set_time = 40

while set_time > 0:
    set_time -= 1
    print(f"Theres {set_time} seconds left")"""

"""#patient que
patients = 20
while patients > 0:
    patients -= 2
    print(f"There are {patients} patients Left to take care of!!!")"""

"""#Battery charger x efficiency check
battery_percentage = 50
charging=[]
charge_type = ["Bulk", "Absorption", "Float"]

while battery_percentage < 100:
    if battery_percentage < 80:
        print(f"Battery is at {battery_percentage} supplying  {charge_type[0]} charge!!!") 
    elif  battery_percentage >= 80:
            print(f"Battery is at {battery_percentage} supplying a {charge_type[1]} charge!!!")
    battery_percentage += 1
    charging.append(battery_percentage )
    print(f"'Charging' - battery is at {battery_percentage}%")
else:
     print(f"(Fully Charged) - Battery is at {battery_percentage}%")
     print(f"Battery is at {battery_percentage} supplying a {charge_type[2]} charge!!!")"""

"""#smart coffee

coffee_types = [["Plain Black", 28],
                ["Americano", 12],
                ["Latte", 2],
                ["Iced Latte", 7],
                ["Frappe", 10]]

while coffee_types:
     user_choice = input("What type of coffee would you like?: ")
     found = False
     
     for coffee_order in coffee_types:
        coffee, left = coffee_order
        
        if user_choice.lower() == coffee.lower():
            if left > 0:
                print(f"Here is your {user_choice}, enjoy!")
                coffee_order[1] -= 1
                found = True

                if coffee_order[1] == 0:
                    print(f"{coffee} is out, Please choose something else")
            else:
                print(f"Sorry, {coffee} is out, please choose something else")
                found = True
            break
     if not found:
            print("Sorry we dont have that, please choose something else")"""
        

     
     
"""# Smart Coffee Machine

coffee_reservoir = 10
coffee_types = ["espresso", "cappuccino", "latte", "americano", "black"]

while coffee_reservoir > 0:
    if coffee_types:
        current_coffee = coffee_types.pop(0)
        print(f"Dispensing {current_coffee}.")

        coffee_reservoir -= 1
        print(f"coffe types left: {coffee_types}")
    else:
        print("no more locked doors")
        break

print("ALL GONE")"""

"""#ELLLEVATORRR
floor = 5
request_stops = [1, 3, 4]
while floor> 0:
    if floor in request_stops:
        print(f"Stopping at Floor {floor}")
        request_stops.remove(floor)

    floor -= 1 #has to be outside the if statement or it wouldnt run
    print(f"Descending to floor {floor}")"""

"""#traffic light

traffic_lights = ['red', 'yellow', 'green', 'yellow']
green_count = 0

while True:
    for color in traffic_lights:
        print(f"The traffic light is now {color}")
        if color == 'green'.lower():
            green_count += 1
            if green_count == 3:
                print("stop")
                break
    if green_count == 3: #without this it would be an endless loop
        break"""
        
"""#skipping rope?
countdown = 30
landed_numbers = []

while countdown > 0:
    countdown -= 1
    if countdown % 2 == 1:
        continue
    landed_numbers.append(countdown)

print("Numbers landed on:",landed_numbers[::1])"""
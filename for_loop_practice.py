"""#festival planner
#pre research
music_stage = ["A", "B", "C", "D", "E"]
music_artist = ["That Mexican OT", "J.Cole", "Kendrick Lamar", "Lil Tecca", "Lil Wayne"]
vendors = ["Jungle Boys", "Muha Meds", "Aurora", "Jeeter Juice"]
vendor_area = ["1", "2", "3", "4"]

for stage in music_stage:
    for artist in music_artist:
        print(artist + " is on stage " + stage + "!!!")
    break

#post research
music_stage = ["A", "B", "C", "D", "E", ]
music_artist = ["That Mexican OT", "J.Cole", "Kendrick Lamar", "Lil Tecca", "Lil Wayne"]
vendors = ["Jungle Boys", "Muha Meds", "Aurora", "Jeeter Juice"]
vendor_area = ["1", "2", "3", "4"]
for i in range(len(music_stage)):
    stage = music_stage[i]
    artist = music_artist[i]
    print(f"{artist} is on stage {stage}!!!")
for i in range(len(vendor_area)):
    area = vendor_area[i]
    vendor = vendors[i]
    print(f"{vendor} is at booth {area}!!!")

#video version
booth_types = ["Food","Games","Music","Crafts",]
schedule_times = ["10:00 AM","1:00 AM","3:00 PM","5;00 PM",]
items_needed = ["Grill","Tickets","Instruments","Paint",]

for i in range(len(booth_types)):
    booth = booth_types[i] 
    time = schedule_times[i]
    item = items_needed[i]
    print(f"{booth} Booth - Schedule: {time}, item needed: {item}")"""


"""#classroom seats
class_seats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,]
students = ["bre", "ale", "chastity", "alesha", "michelle", "priscilla", "mel", "haley", "unique", "shaniya", "cheyanne", "carol"]
for i in range(len(class_seats)):
    seat = class_seats[i]
    who = students[i]
    print(f"{who} is in seat {seat} ")

#in video version
total_students = 30
rows = 5

students_per_row = total_students // rows

for row in range(1, rows + 1):
    for seat in range(1, students_per_row + 1):
        seat_number = (row - 1) * students_per_row + seat
        print(f"Row {row} - Seat {seat}: student {seat_number}")"""

"""#shopping cart total
item_prices = [2.99, 5.49, 3.25, 1.99, 4.75]

total_cost = 0

for price in item_prices:
    total_cost += price

print(f"the total cost of the shopping cart is: ${total_cost:.2f}")"""

"""#multi table gen
table_size = int(input("Enter the size of the multi table: "))

for row in range(1, table_size + 1):
    for col in range(1, table_size + 1):
        product = row * col
        print(f"{product} \t", end="")
    print()"""

"""#inventory management
inventory = [
    ["Apples", 5],
    ["bananas", 2],
    ["Oranges", 0],
    ["Milk", 1],
    ["Eggs", 12],
]

reorder_thresh = 3

for item in inventory:
    name, quantity = item
    if quantity < reorder_thresh:
        print(f"{name} needs to be reordered.")"""

"""#treasure hunt

caves = [False, False, True, False, False]
for index, cave in enumerate(caves):
    if cave:
        print(f"Treasure found in cave {index + 1}!")
        break
    else:
        print("Treasure is not here!")"""

"""#email clean up
emails = ["user1@example.com","user2@example.com",None,"user3@example.com", None]

valid_emails = []

for email in emails:
    if emails is None:
        continue
    valid_emails.append(email)

print(valid_emails)"""
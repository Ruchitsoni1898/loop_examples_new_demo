#main_num = 14
#user_input = 0
#while user_input != main_num:
 #   user_input = int(input("Guess a number between 0 and 20:"))
  #  user_input = int(user_input)
   # print(type(user_input))
    #print(f"you entered:{user_input}")
    # print(user_input!= main_num)

#print("Finish!!!")
# example 1
# main_num = 15
# user_input = 0
# while True:
    # user_input = int(input("Enter a number between 0 and 10:"))
    # print(f"you entered:{user_input}")
    #if int(user_input)== main_num:
     #   break
    #else:
     #   continue

# print("Finish!!!")

# example 2
# given a country print its capital city if its in the given set of data, else print unknown.
""""capitals = {
    "peru" :"Lima",
    "Philippines" : "Manila",
    "Spain" : "Madrid",
    "India" : "Delhi",
    "Germany" : "Berlin",
}
user_input = "Spain"
capital_city = capitals[user_input]
for country,capital in capitals.items():
    print("Current country :"+ country)
    if user_input.lower() == country.lower():
        print("Current capital:"+ capital)
        break
"""
# Example 3
# given a dictionary with book prices and list of courses, calculate total cost of books
book_prices = {"calculus": 300, "physics": 255, "chemistry": 400, "english": 150, "theater": 100}
my_courses = ["physics", "english", "psychology", "calculus", "history"]
total_cost = 0
for course in my_courses:
    if course not in book_prices.keys():
        continue
    total_cost += book_prices[course]
    total_cost = total_cost + book_prices[course]

print("Total books cost: {}".format(total_cost))



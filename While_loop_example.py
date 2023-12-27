main_num = 10
user_input = 0
while user_input != main_num:
    user_input = int(input("Enter a number between 0 and 10:"))
    user_input = int(user_input)
    print(type(user_input))
    print(f"you entered:{user_input}")
    print(user_input!= main_num)

print("Finish!!!")


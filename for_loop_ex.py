my_list = ["house","car","bike","bicycle"]
for i in my_list:
    print(i)
    print("--------")
fruits = ["Apple","Banana","Orange","Guava"]
for j in fruits:
    print(j)

# example 2
# print out words that are 2 or less characters..
quote = "Be yourself; everyone else is already taken"
words_list = quote.split()
print(words_list)
for i in quote.split():
    if len(i) <=4:
     print(i)
    else:
        pass
# example 3
# print out small words(3 or less characters) into a list and print a list
quote = "Be yourself; everyone else is already taken"
small_words=[]
for i in quote.split():
    if len(i) <= 3:
        small_words.append(1)
    print(small_words)
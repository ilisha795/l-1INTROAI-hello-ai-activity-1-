print("Hello ! I am an AI Bot. What is your name ?: ")

name = input()

print(f"Nice to meet you, {name} !")

print("How are you feeling today ? Good or bad ?: ")
mood = input().lower()

if mood == "good":
    print("I'm glad to hear that !")
elif mood == "bad":
    print("I'm sorry to hear that. I hope things get better soon !")

print(f"It was nice talking to you, {name}. Bye !")
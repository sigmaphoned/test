# Minecraft username generator script
import random
usernames = []
for _ in range(10):
    adjective = ["Mighty", "Sneaky", "Crazy", "Swift", "Fiery", "Daring"]
    noun = ["Dragon", "Warrior", "Shadow", "Wizard", "Ninja", "Hero"]
    username = random.choice(adjective) + random.choice(noun)
    usernames.append(username)
for username in usernames:
    print(username)
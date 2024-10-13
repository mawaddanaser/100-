################### Scope ####################
# difference between local and global scope
enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

########################

# There is no block scope
game_level = 3
enenmies = ["skeleton", "vambires", "alien"]
if game_level < 5:
    new_enemy = enenmies[0]

print(new_enemy)


#########################
# Local Scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()
print(potion_strength)

# Global Scope
player_health = 10


def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()


print(player_health)

# Modifying global scope
enemies = 1


def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1


enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

# Global Constants (all upper case)

PI = 3.14159
URL = ""
TWITTER_HANDLE = ""

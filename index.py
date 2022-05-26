import random


# 0 - камінь
# 1 - Спок
# 2 - папір
# 3 - хамелеон
# 4 - ножиці

def name_to_number(name):
    if name == "камінь":
        return 0
    elif name == "Спок":
        return 1
    elif name == "папір":
        return 2
    elif name == "хамелеон":
        return 3
    elif name == "ножиці":
        return 4


def number_to_name(code):
    if code == 0:
        return "камінь"
    elif code == 1:
        return "Спок"
    elif code == 2:
        return "папір"
    elif code == 3:
        return "хамелеон"
    elif code == 4:
        return "ножиці"

def rpsls(player_choice):

    print("\n")

    print("Гравець обрав " + player_choice)

    player_code = name_to_number(player_choice)

    # хід ПК
    bot_code = random.randrange(0, 5)
    comp_choice = number_to_name(bot_code)
    print("Комп'ютер обрав " + comp_choice)

    diff = (bot_code - player_code) % 5

    if (diff == 1) or (diff == 2):
        print("Комп'ютер виграв!")
    elif (diff == 3) or (diff == 4):
        print("Гравець виграв!")
    else:
        print("Нічия")

rpsls("камінь")
rpsls("Спок")
rpsls("папір")
rpsls("хамелеон")
rpsls("ножиці")

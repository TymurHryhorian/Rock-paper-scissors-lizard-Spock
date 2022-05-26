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

def number_to_name(number):
    if number == 0:
        return "камінь"
    elif number == 1:
        return "Спок"
    elif number == 2:
        return "папір"
    elif number == 3:
        return "хамелеон"
    elif number == 4:
        return "ножиці"
    else:
        print "number_to_name() find unkown number:",number
        
def rpsls(player_choice): 
    """ 
    player_choice: the name of the player choice
    """

    print("\n")
    
    print "Гравець обрав "+player_choice
    
    player_number = name_to_number(player_choice)
    
    # хід ПК
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print ("Computer chooses "+comp_choice)
    
    diff = (comp_number - player_number) % 5
    
    if (diff == 1) or (diff == 2):
        print ("Комп'ютер виграв!")
    elif (diff == 3) or (diff == 4):
        print("Гравець виграв!")
    else:
        print("Нічия")
                         
rpsls("камінь")
rpsls("Спок")
rpsls("папір")
rpsls("хамелеон")
rpsls("ножиці")

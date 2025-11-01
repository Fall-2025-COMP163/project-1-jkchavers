

"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Jaylen Chavers
Date: 10/28/2025

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""
from collections import namedtuple
import os

def create_character(name, character_class):
    character = {"name": name, "class": character_class}

    classStats = calculate_stats(character_class, 1)
    character = {"name": name, "class": character_class,
                 "level": 1, "strength": classStats[0],
                 "magic": classStats[1],
                 "health": classStats[2],
                 "gold": 100,}

    return character

    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
    pass

def calculate_stats(character_class, level):

    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    Design your own formulas! Ideas:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    """
    levelScaling = (level * 3) // 2 #each level up increases starting stats exponentially as additional level ups occur.
    classStats = namedtuple("ClassStats", ["strength", "magic", "health"])
    #base stats scale by 1 point with each level up.
    if character_class == "Mage":
        class_stats = classStats(5 + levelScaling, 15 + levelScaling, 3 + levelScaling)

    elif character_class == "Warrior":
        class_stats = classStats(20 + levelScaling, 5 + levelScaling, 20 + levelScaling)

    elif character_class == "Rogue":
        class_stats = classStats(10 + levelScaling, 15 + levelScaling, 8 + levelScaling)

    elif character_class == "Cleric":
        class_stats = classStats(8 + levelScaling, 20 + levelScaling, 20 + levelScaling)

    elif character_class == "Depraved":
        class_stats = classStats(5 + levelScaling, 5 + levelScaling, 20 + levelScaling)
    else:
        character_class = "Rogue"
        class_stats = classStats(20 + levelScaling, 5 + levelScaling, 20 + levelScaling)

    return class_stats
    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)

    pass

def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    save_data = f"Character Name: [{character["name"]}]\nClass: [{character["class"]}]\nLevel: [{character["level"]}]\nStrength: [{character["strength"]}]\nMagic: [{character["magic"]}]\nHealth: [{character["health"]}]\nGold: [{character["gold"]}]"


    with open(filename, "w") as save_file:
        save_file.writelines(save_data.strip())
        print(save_data.strip())

        if os.path.exists(filename) == True:
            return True
        elif os.path.exists(filename) == False:
            return False







    # TODO: Implement this function

    # Remember to handle file errors gracefully


def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    character = {}
    if os.path.isfile(filename) == True:
        with open(filename, "r") as save_file:
            #initialize empty variables to store values retrieved from save file
            extractedVals = []

            for line in save_file:
                if(line.strip() != ""): #used strip method to fix reading blank lines from save data
                    startIndex = line.find("[")
                    endingIndex = line.find("]")
                    extractedVals.append(line[startIndex + 1:endingIndex])

            character = {"name": extractedVals[0], "class": extractedVals[1],
                         "level": int(extractedVals[2]), "strength": extractedVals[3],
                         "magic": extractedVals[4], "health": extractedVals[5]}
            print(character)
            return character
    elif os.path.isfile(filename) == False:
        return None


    # TODO: Implement this function
    # Remember to handle file not found errors


def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)

    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    print("=== CHARACTER SHEET ===")
    print("Name:",character["name"])
    print("Class:",character["class"])
    print("Level:",character["level"])
    print("Strength:",character["strength"])
    print("Magic:",character["magic"])
    print("Health:",character["health"])
    print("Gold:",character["gold"])
    # TODO: Implement this function
    pass

def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None

    """
    character["level"] += 1
    calculate_stats(character, character["level"])
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    pass

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    char = create_character("Mai", "Flying Swordsman")
    display_character(char)
    save_character(char, "my_character.txt")
    loaded = load_character("my_character.txt")
    print(loaded)
    level_up(char)
    #print("=== CHARACTER LEVEL UP ===")
    #print(display_character(char))
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")

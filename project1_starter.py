

"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Jaylen Chavers
Date: 10/28/2025

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""
from collections import namedtuple


def create_character(name, character_class):
    character = {"name": name, "character_class": character_class}

    classStats = calculate_stats(character_class, 1)
    character = {"name": name, "character_class": character_class,
                 "level": classStats[0], "strength": classStats[1],
                 "dexterity": classStats[2], "magic": classStats[3],
                 "faith": classStats[4], "health": classStats[5]}

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
    classStats = namedtuple("ClassStats", ["level", "strength", "dexterity", "magic", "faith", "health"])

    if character_class == "Wizard":
        class_stats= classStats(1, 5, 15, 20, 2, 5)

    elif character_class == "Flying Swordsman":
        class_stats = classStats(1, 15, 15, 20, 10, 20)

    elif character_class == "Viking":
        class_stats = classStats(1, 5, 10, 10, 5, 25)

    elif character_class == "Cleric":
        class_stats = classStats(1, 5, 5, 15, 15, 2)

    elif character_class == "Depraved":
        class_stats = classStats(1, 15, 15, 5, 1, 5)
    else:
        character_class = "Depraved"
        class_stats = classStats(1, 15, 15, 5, 1, 5)

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
    save_data = f"""
    Character Name: [{character["name"]}]
    Class: [{character["character_class"]}]
    Level: [{character["level"]}]
    Strength: [{character["strength"]}]
    Dexterity: [{character["dexterity"]}]
    Magic: [{character["magic"]}]
    Faith: [{character["faith"]}]
    Health: [{character["health"]}]
    """

    with open(filename, "w") as save_file:
        save_file.writelines(save_data)
        return True




    # TODO: Implement this function

    # Remember to handle file errors gracefully


def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    character = {}
    with open(filename, "r") as save_file:
        #initialize empty variables to store values retreived from save file
        extractedVals = []
        name = ""
        character_class = ""
        classStats = ()
        for line in save_file:
            startIndex = line.find("[")
            endingIndex = line.find("]")
            extractedVals.append(line[startIndex + 1:endingIndex])

        character = {"name": extractedVals[0], "character_class": extractedVals[1],
                     "level": extractedVals[2], "strength": extractedVals[3],
                     "dexterity": extractedVals[4], "magic": extractedVals[5],
                     "faith": extractedVals[6], "health": extractedVals[7]}

        return character


    # TODO: Implement this function
    # Remember to handle file not found errors
    pass

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
    print("Class:",character["character_class"])
    print("Level:",character["level"])
    print("Strength:",character["strength"])
    print("Dexterity:",character["dexterity"])
    print("Magic:",character["magic"])
    print("Faith:",character["faith"])
    print("Health:",character["health"])
    # TODO: Implement this function
    pass

def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    pass

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    char = create_character("Mai", "Mage")
    display_character(char)
    save_character(char, "my_character.txt")
    loaded = load_character("my_character.txt")
    print(loaded)
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")

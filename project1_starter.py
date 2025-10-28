"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Jaylen Chavers
Date: 10/28/2025

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""

def create_character(name, character_class):
    character = {"name": name, "character_class": character_class}

    if character_class == "Wizard":
        character["character_class"] = "Wizard"
        character["level"] = 1
        character["strength"] = 5
        character["dexterity"] = 15
        character["magic"] = 20
        character["faith"] = 2
        character["health"] = 5
    elif character_class == "Flying Swordsman":
        character["character_class"] = "Flying Swordsman"
        character["level"] = 1
        character["strength"] = 15
        character["dexterity"] = 5
        character["magic"] = 5
        character["faith"] = 10
        character["health"] = 20
    elif character_class == "Viking":
        character["character_class"] = "Viking"
        character["level"] = 1
        character["strength"] = 10
        character["dexterity"] = 5
        character["magic"] = 10
        character["faith"] = 5
        character["health"] = 25
    elif character_class == "Cleric":
        character["character_class"] = "Cleric"
        character["level"] = 1
        character["strength"] = 5
        character["dexterity"] = 5
        character["magic"] = 15
        character["faith"] = 15
        character["health"] = 2
    elif character_class == "Depraved":
        character["character_class"] = "Depraved"
        character["level"] = 1
        character["strength"] = 15
        character["dexterity"] = 15
        character["magic"] = 5
        character["faith"] = 1
        character["health"] = 5

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
    # TODO: Implement this function
    # Remember to handle file errors gracefully
    pass

def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
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
    print(create_character("Mael", "Depraved"))
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")

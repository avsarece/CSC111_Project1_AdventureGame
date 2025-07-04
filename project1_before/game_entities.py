"""CSC111 Project 1: Text Adventure Game - Game Entities

Instructions (READ THIS FIRST!)
===============================

This Python module contains the entity classes for Project 1, to be imported and used by
 the `adventure` module.
 Please consult the project handout for instructions and details.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2025 CSC111 Teaching Team
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Item:
    """An item in our text adventure game world.

    Instance Attributes:
        - Instance Attributes:
        - name: the name of the item
        - description: the description script of the item
        - start_positiion: the location id where the item was found
        - target_position: the target location id of the item
        - target_points: the score gained after this item is found

    Representation Invariants:
        - self.start_position > 0
        - self.target_position > 0
        - self.name != ""
    """

    # NOTES:
    # This is just a suggested starter class for Item.
    # You may change these parameters and the data available for each Item object as you see fit.
    # (The current parameters correspond to the example in the handout).
    #
    # The only thing you must NOT change is the name of this class: Item.
    # All item objects in your game MUST be represented as an instance of this class.

    name: str
    description: str
    start_position: int
    target_position: int
    target_points: int


@dataclass
class Location:
    """A location in our text adventure game world.

    Instance Attributes:
        - id_num: integer id for this location
        - description: brief description of this location
        - available_commands: a mapping of available commands at this location to
                                the location executing that command would lead to

    Representation Invariants:
        - self.id_num > 0
        - self.name != ''
        - self.brief_description != ''
        - self.long_description != ''
    """
    name: str
    id_num: int
    available_commands: dict[str, int]
    brief_description: str
    long_description: str
    items: Optional[list[Item]]
    password: Optional[str]
    visited: bool
    door: bool
    is_unlocked: bool

    # This is just a suggested starter class for Location.
    # You may change/add parameters and the data available for each Location object as you see fit.
    #
    # The only thing you must NOT change is the name of this class: Location.
    # All locations in your game MUST be represented as an instance of this class.

    def __init__(self, id_num, name, brief_description, long_description, available_commands, items,
                 password, visited=False, door=False, is_unlocked=False) -> None:
        """Initialize a new location.

        Since it is being initialized, visited, door and is_unlocked features are set to False.
        """

        self.name = name
        self.id_num = id_num
        self.brief_description = brief_description
        self.long_description = long_description
        self.available_commands = available_commands
        self.items = items
        self.password = password
        self.visited = visited
        self.door = door
        self.is_unlocked = is_unlocked


class NPC:
    """A class representing an NPC in the AdventureGame
        Instance Attributes:
            - name: name of the npc
            - location_id: the location this npc is founded in
            - gives_item: the item the npc will give to the player
            - required_item: the item the npc will ask in order to give gives_item
            - message: message npc transfers
            - after_message: message npc transfers after the interaction.

        Representation Invariants:
        - self.name != ''
        - self.location_id > 0

        """
    name: str
    location_id: int
    gives_item: list[str]
    required_item: str | int
    message: str
    after_message: Optional[str]

    def __init__(self, name, location_id, gives_item, required_item, message, after_message):
        self.name = name.lower()
        self.location_id = location_id
        self.gives_item = gives_item
        self.required_item = required_item
        self.message = message
        self.after_message = after_message


# Note: Other entities you may want to add, depending on your game plan:
# - Puzzle class to represent special locations (could inherit from Location class if it seems suitable)
# - Player class
# etc.

if __name__ == "__main__":
    pass
    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (Delete the "#" and space before each line.)
    # IMPORTANT: keep this code indented inside the "if __name__ == '__main__'" block
    import python_ta
    python_ta.check_all(config={
        'max-line-length': 120,
        'disable': ['R1705', 'E9998', 'E9999']
    })

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
        - # TODO Describe any necessary representation invariants
    """
    id_num: int
    description: str
    available_commands: dict[str, int]
    brief_description = str
    long_description = str
    items = Optional[list[Item]]
    visited = bool

    # This is just a suggested starter class for Location.
    # You may change/add parameters and the data available for each Location object as you see fit.
    #
    # The only thing you must NOT change is the name of this class: Location.
    # All locations in your game MUST be represented as an instance of this class.

    def __init__(self, location_id, brief_description, long_description, available_commands, items,
                 visited=False) -> None:
        """Initialize a new location.

        # TODO Add more details here about the initialization if needed
        """

        self.id_num = location_id
        self.brief_description = brief_description
        self.long_description = long_description
        self.available_commands = available_commands
        self.items = items
        self.visited = visited





@dataclass
class Location:
    """A location in our text adventure game world.

    Instance Attributes:
        - id_num: integer id for this location
        - brief_description: brief description of this location
        - long_description: long description of this location
        - available_commands: a mapping of available commands at this location to
                                the location executing that command would lead to
        - items: items available at this current location, or None if the items list is empty
        - visited: Indicates whether this location has already been visited or not


    Representation Invariants:
        - id_num > 0
    """
    id_num: int
    brief_description: str
    long_description: str
    available_commands: dict[str, int]
    items: Optional[list[Item]]
    visited: bool

    # This is just a suggested starter class for Location.
    # You may change/add parameters and the data available for each Location object as you see fit.
    #
    # The only thing you must NOT change is the name of this class: Location.
    # All locations in your game MUST be represented as an instance of this class.

    def __init__(self, location_id, brief_description, long_description, available_commands, items,
                 visited=False) -> None:
        """Initialize a new location.

        # TODO Add more details here about the initialization if needed
        """

        self.id_num = location_id
        self.brief_description = brief_description
        self.long_description = long_description
        self.available_commands = available_commands
        self.items = items
        self.visited = visited


# Note: Other entities you may want to add, depending on your game plan:
# - Puzzle class to represent special locations (could inherit from Location class if it seems suitable)
# - Player class
# etc.

if __name__ == "__main__":
    pass
    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (Delete the "#" and space before each line.)
    # IMPORTANT: keep this code indented inside the "if __name__ == '__main__'" block
    # import python_ta
    # python_ta.check_all(config={
    #     'max-line-length': 120,
    #     'disable': ['R1705', 'E9998', 'E9999']
    # })

"""CSC111 Project 1: Text Adventure Game - Game Manager
"""
from __future__ import annotations
import json
from typing import Optional
import time

from game_entities import Location, Item, NPC
from proj1_event_logger import Event, EventList


# Note: You may add in other import statements here as needed

# Note: You may add helper functions, classes, etc. below as needed


class AdventureGame:
    """A text adventure game class storing all location, item and map data.

    Instance Attributes:
        - current_location_id: location id of the current location
        - ongoing: Whether the game is ongoing or not
        - current_location_items: A dictionary where the current location id is mapped to
        list of Item objects available at this location

    Representation Invariants:
        - self.current_location_id >= 0

    """

    # Private Instance Attributes (do NOT remove these two attributes):
    #   - _locations: a mapping from location id to Location object.
    #                       This represents all the locations in the game.
    #   - _items: a list of Item objects, representing all items in the game.
    #   - _npcs: a mapping from location id to npc object.
    #          This represents all the locations in the game.

    _locations: dict[int, Location]
    _items: list[Item]
    current_location_id: int  # Suggested attribute, can be removed
    ongoing: bool  # Suggested attribute, can be removed
    _npcs: list[NPC]
    inventory: list[str]

    def __init__(self, game_data_file: str, initial_location_id: int) -> None:
        """
        Initialize a new text adventure game, based on the data in the given file, setting starting location of game
        at the given initial location ID.
        (note: you are allowed to modify the format of the file as you see fit)

        Preconditions:
        - game_data_file is the filename of a valid game data JSON file
        """

        # NOTES:
        # You may add parameters/attributes/methods to this class as you see fit.

        # Requirements:
        # 1. Make sure the Location class is used to represent each location.
        # 2. Make sure the Item class is used to represent each item.

        # Suggested helper method (you can remove and load these differently if you wish to do so):
        self._locations, self._items, self._npcs = self._load_game_data(game_data_file)

        # Suggested attributes (you can remove and track these differently if you wish to do so):
        self.current_location_id = initial_location_id  # game begins at this location
        self.ongoing = True  # whether the game is ongoing

        self.inventory = []

    @staticmethod
    def _load_game_data(filename: str) -> tuple[dict[int, Location], list[Item], list[NPC]]:
        """Load locations and items from a JSON file with the given filename and
        return a tuple consisting of (1) a dictionary of locations mapping each game location's ID to a Location object,
        and (2) a list of all Item objects and (3) list of all npc objects"""

        with open(filename, 'r') as f:
            data = json.load(f)  # This loads all the data from the JSON file
        items = []
        # YOUR CODE BELOW
        for item_data in data["items"]:
            item_obj = Item(item_data['name'],
                            item_data['description'],
                            item_data['start_position'],
                            item_data['target_position'],
                            item_data['target_points'])

            items.append(item_obj)

        locations = {}
        for loc_data in data['locations']:  # Go through each element associated with the 'locations' key in the file
            location_items = [item for item in items if item.start_position == loc_data['id']]
            location_obj = Location(loc_data['id'],
                                    loc_data['name'],
                                    loc_data['brief_description'],
                                    loc_data['long_description'],
                                    loc_data['available_commands'],
                                    location_items,
                                    loc_data['password'],
                                    door=loc_data.get('door', False),
                                    is_unlocked=loc_data.get('is_unlocked', False))
            locations[loc_data['id']] = location_obj

        npcs = []
        for npc_data in data["npcs"]:
            npc_obj = NPC(npc_data['name'],
                          npc_data['location_id'],
                          npc_data['gives_item'],
                          npc_data['required_item'],
                          npc_data['message'],
                          npc_data['after_message'])

            npcs.append(npc_obj)

        return locations, items, npcs

    def get_location(self, loc_id: Optional[int] = None) -> Location:
        """Return Location object associated with the provided location ID.
        If no ID is provided, return the Location object associated with the current location.
        """
        # YOUR CODE BELOW
        if loc_id is None:
            loc_id = self.current_location_id
        return self._locations[loc_id]

    def get_npc(self, loc_id: Optional[int] = None) -> Optional[NPC]:
        """Return NPC object associated with the provided location ID.
                If no ID is provided, return the NPC object associated with the current location.
                """
        if loc_id is None:
            loc_id = self.current_location_id

        for npc1 in self._npcs:
            if npc1.location_id == loc_id:
                return npc1
        return None

    def get_inventory_items(self) -> list[str]:
        """Return a list of item names currently in the inventory."""
        return [item.name for item in self._items if item.start_position == -1]

    def




if __name__ == "__main__":

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (Delete the "#" and space before each line.)
    # IMPORTANT: keep this code indented inside the "if __name__ == '__main__'" block
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 120,
        'disable': ['R1705', 'E9998', 'E9999']
    })

    game_log = EventList()  # This is REQUIRED as one of the baseline requirements
    game = AdventureGame('game_data.json', 1)  # load data, setting initial location ID to 1
    menu = ["look", "inventory", "score", "undo", "log", "quit", "unlock"]
    # Regular menu options available at each location
    choice = None

    # Note: You may modify the code below as needed; the following starter code is just a suggestion
    while game.ongoing:
        # Note: If the loop body is getting too long, you should split the body up into helper functions
        # for better organization. Part of your marks will be based on how well-organized your code is.

        location = game.get_location()
        npc = game.get_npc()

        #  Note that the <choice> variable should be the command which led to this event
        # YOUR CODE HERE
        event = Event(location.id_num, location.long_description, None, None, game_log.last)
        game_log.add_event(event, choice)

        # YOUR CODE HERE
        if choice != "look":

            if location.visited:
                print("LOCATION", location.id_num)
                print(location.brief_description)
            else:
                print("LOCATION", location.id_num)
                print(location.long_description)
                location.visited = True
                if npc is not None:
                    print(npc.message)

        # Display possible actions at this location
        if choice != quit:
            print("What to do? Choose from: look, inventory, score, undo, log, quit, unlock")
            print("At this location, you can also:")
            for action in location.available_commands:
                print("-", action)

        # Validate choice
        choice = input("\nEnter action: ").lower().strip()
        while (choice not in location.available_commands and choice not in menu and not choice.startswith("take ")
               and not choice.startswith("use ") and choice != '1' and choice != '2550'):
            print("That was an invalid option; try again.")
            choice = input("\nEnter action: ").lower().strip()

        print("========")
        print("You decided to:", choice)

        if choice in menu:
            # Note: For the "undo" command, remember to manipulate the game_log event list to keep it up-to-date
            if choice == "log":
                game_log.display_events()
            elif choice == "score":
                # Calculate and display score based on items in correct positions
                score = sum(item.target_points for item in location.items
                            if item.start_position == item.target_position)
                print("Current score:", score)

            elif choice == "inventory":
                if game.inventory:
                    print("Your inventory:", game.inventory)
                else:
                    print("Your inventory is empty!")

            elif choice == "look":
                print(location.long_description)

            elif choice == "undo":
                if game_log.first is not None and game_log.last is not None and game_log.last.prev is not None:
                    last_event = game_log.last
                    last_command = last_event.next_command
                    if last_command is not None:
                        if last_command.startswith("take "):
                            item_name = last_command[5:]
                            if item_name in game.inventory:
                                game.inventory.remove(item_name)
                                for item in game._items:
                                    if item.name == item_name:
                                        item.start_position = game.current_location_id
                                        break
                        elif last_command.startswith("use "):
                            item_name = last_command[4:]
                            for item in game._items:
                                if item.name == item_name and item.start_position == -1:
                                    game.inventory.append(item.name)
                                    item.start_position = game.current_location_id
                                    break
                    game.current_location_id = game_log.last.prev.id_num
                    game_log.remove_last_event()

            elif choice == "quit":
                answers = ["yes", "no"]
                print("Would you like to quit?")
                for answer in answers:
                    print("-", answer)

                user_input = input("Enter your choice: ").strip().lower()
                if user_input == "yes":
                    print("Goodbye!")
                    game.ongoing = False

                elif user_input == "no":
                    print("Alright, returning back to the game")

            elif choice == "unlock":
                location = game.get_location()
                if location:
                    if location.door:
                        if location.password:
                            print("this door is locked")
                            user_password = input("\nPlease enter password: ").strip()
                            if user_password == location.password:
                                print("Password is correct!. You may pass")
                                location.is_unlocked = True
                                game.current_location_id = 7
                    else:
                        print("There is no door to be unlocked in this location")

        elif choice.startswith("take "):
            # Handle taking items
            item_name = choice[5:]
            for item in game._items:
                if item.name.lower() == item_name and item.start_position == location.id_num:
                    item.start_position = -1  # -1 represents the inventory
                    game.inventory.append(item.name)
                    print("Taken:", item_name)
                    break
            else:
                print("That item isn't here.")
        elif choice.startswith("use "):
            # Handle using items
            item_name = choice[4:]  # Remove "use " prefix
            for item in game._items:
                if location.id_num == 8 and item.name.lower() == item_name.lower() and item.target_position == 8:
                    print("Successfully used", item.name, "!")
                    item.start_position = location.id_num
                    game.inventory.remove(item.name)
                elif item.name.lower() == item_name.lower() and item.start_position == -1:
                    # Verify item is in inventory
                    if location.id_num == item.target_position:
                        print("Successfully used", item.name, "!")
                        if item.name.lower() == 'key':
                            print(
                                "MESSAGE FROM THE WISE: if you want to achieve virtue, go and look under the statue")
                        item.start_position = location.id_num  # Place item at current location
                        game.inventory.remove(item.name)  # Remove from inventory list
                    else:
                        print("Can't use", item.name, "here.")
                    break

        else:
            if choice in location.available_commands:
                result = location.available_commands[choice]
                game.current_location_id = result

            # ENTER YOUR CODE BELOW to handle other menu commands (remember to use helper functions as appropriate)
            if game.current_location_id == 5 and choice not in location.available_commands:
                approved_answer = 1  # Answer of the Prof's question
                if int(choice) == approved_answer:
                    print(npc.after_message)
                else:
                    print("That's the wrong answer. Try again")

            if game.current_location_id == 4 and choice not in location.available_commands:
                approved_answer = 2550  # Answer of the Genie's question
                if int(choice) == approved_answer:
                    print(npc.after_message)
                    time.sleep(3)
                    game.current_location_id = 7
                else:
                    print("That's the wrong answer. Try again")

        if len(game_log.get_id_log()) >= 30:
            print("Maximum moves reached. GAME OVER")
            game.ongoing = False

        else:
            if all(item.start_position == item.target_position for item in game._items):
                score = sum(item.target_points for item in game._items)
                print("Congratulations! You won. Your total score is:", score)
                game.ongoing = False

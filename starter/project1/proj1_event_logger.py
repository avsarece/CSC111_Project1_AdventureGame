"""CSC111 Project 1: Text Adventure Game - Event Logger

Instructions (READ THIS FIRST!)
===============================

This Python module contains the code for Project 1. Please consult
the project handout for instructions and details.

You can copy/paste your code from the ex1_simulation file into this one, and modify it as needed
to work with your game.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2025 CSC111 Teaching Team
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


# TODO: Copy/paste your ex1_event_logger code below, and modify it if needed to fit your game


@dataclass
class Event:
    """
    A node representing one event in an adventure game.

    Instance Attributes:
    - id_num: Integer id of this event's location
    - description: Long description of this event's location
    - next_command: String command which leads this event to the next event, None if this is the last game event
    - next: Event object representing the next event in the game, or None if this is the last game event
    - prev: Event object representing the previous event in the game, None if this is the first game event
    """

    # NOTES:
    # This is proj1_event_logger (separate from the ex1 file). In this file, you may add new attributes/methods,
    # or modify the names or types of provided attributes/methods, as needed for your game.
    # If you want to create a special type of Event for your game that requires a different
    # set of attributes, you can create new classes using inheritance, as well.

    id_num: int
    description: str
    next_command: Optional[str] = None
    next: Optional[Event] = None
    prev: Optional[Event] = None


class EventList:
    """
    A linked list of game events.

    Instance Attributes:
        - # TODO add descriptions of instance attributes here

    Representation Invariants:
        - # TODO add any appropriate representation invariants, if needed
    """
    first: Optional[Event]
    last: Optional[Event]

    def __init__(self) -> None:
        """Initialize a new empty event list."""

        self.first = None
        self.last = None

    def display_events(self) -> None:
        """Display all events in chronological order."""
        curr = self.first
        while curr:
            print(f"Location: {curr.id_num}, Command: {curr.next_command}")
            curr = curr.next

    def is_empty(self) -> bool:
        """Return whether this event list is empty."""

        return self.display_events() is None

    def add_event(self, event: Event, command: str = None) -> None:
        """Add the given new event to the end of this event list.
        The given command is the command which was used to reach this new event, or None if this is the first
        event in the game.
         >>> eventlist = EventList()
        >>> event1 = Event(1, 'a')
        >>> event2 = Event(2, 'b')
        >>> event3 = Event(3, 'c')
        >>> eventlist.add_event(event1, 'walk')
        >>> eventlist.add_event(event2, 'run')
        >>> eventlist.add_event(event3, 'jump')
        >>> eventlist.remove_last_event()
        >>> eventlist.remove_last_event()
        >>> eventlist.is_empty()
        >>> True
        """
        # Hint: You should update the previous node's <next_command> as needed

        if self.first is None:
            self.first = event

        else:
            curr = self.first
            while curr.next is not None:
                curr = curr.next
            curr.next = event
            event.prev = curr
            curr.next_command = command
            self.last = event

    def remove_last_event(self) -> None:
        """Remove the last event from this event list.
        If the list is empty, do nothing."""

        # Hint: The <next_command> and <next> attributes for the new last event should be updated as needed

        if self.first is None:
            return

        if self.first.next is None:
            self.first = None
            self.last = None

        else:
            new_last_event = self.last.prev
            new_last_event.next = None
            new_last_event.next_command = None
            self.last = new_last_event

    def get_id_log(self) -> list[int]:
        """Return a list of all location IDs visited for each event in this list, in sequence."""

        if self.first is None:
            return []

        else:
            id_visited_so_far = []
            curr = self.first
            while curr is not None:
                id_visited_so_far.append(curr.id_num)
                curr = curr.next

            return id_visited_so_far

    def undo_last_command(self, command):
        """Undo the last command made by the player."""
        if self.last is None:
            print("No actions to undo.")

        if self.prev is not None:
            self.last = self.prev
            self.prev = self.last.prev  # Update prev to the previous command
        else:
            self.last = None

    # Note: You may add other methods to this class as needed


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

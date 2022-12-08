""" DON'T NEED THE FOLLOWING IMPORTS UNLESS TRYING TO USE THE 'create_cast()' METHOD 
import random

from constants import *

from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.shared.point import Point

"""

class Cast:
    """A collection of actors.

    The responsibility of a cast is to keep track of a collection of actors. It has methods for 
    adding, removing and getting them by a group name.

    Attributes:
        _actors (dict): A dictionary of actors { key: group_name, value: a list of actors }
    """

    def __init__(self):
        """Constructs a new Actor."""
        self._actors = {}
        
    def add_actor(self, group, actor):
        """Adds an actor to the given group.
        
        Args:
            group (string): The name of the group.
            actor (Actor): The actor to add.
        """
        if not group in self._actors.keys():
            self._actors[group] = []
            
        if not actor in self._actors[group]:
            self._actors[group].append(actor)

    def get_actors(self, group):
        """Gets the actors in the given group.
        
        Args:
            group (string): The name of the group.

        Returns:
            List: The actors in the group.
        """
        results = []
        if group in self._actors.keys():
            results = self._actors[group].copy()
        return results
    
    def get_all_actors(self):
        """Gets all of the actors in the cast.
        
        Returns:
            List: All of the actors in the cast.
        """
        results = []
        for group in self._actors:
            results.extend(self._actors[group])
        return results

    def get_single_actor(self, group, actor_number): # changed this from get_first_actor() to accept a parameter for the index number of the actor I want
        """Gets the first actor in the given group.
        
        Args:
            group (string): The name of the group.
            
        Returns:
            List: The first actor in the group.
        """
        result = None
        if group in self._actors.keys():
            result = self._actors[group][actor_number]
        return result

    def remove_actor(self, group, actor):
        """Removes an actor from the given group.
        
        Args:
            group (string): The name of the group.
            actor (Actor): The actor to remove.
        """
        if group in self._actors:
            self._actors[group].remove(actor)

    
    """ DON'T NEED 'create_cast()' METHOD UNLESS TRYING TO IMPLEMENT IT IN THE '__main__.py' TO REPLACE IT'S CAST CREATION """
    """
    def create_cast(self):
            # create the cast
        cast = Cast()
        
        # create the banners
        banner = Actor()
        banner.set_text("")
        banner.set_font_size(FONT_SIZE)
        banner.set_color(WHITE)
        banner.set_position(Point(CELL_SIZE, 0)) # Sets X to CELL_SIZE(15) and Y to 0 for placement in top left corner
        cast.add_actor("banners", banner)

        banner_gold = Actor()
        banner_gold.set_text("")
        banner_gold.set_font_size(FONT_SIZE)
        banner_gold.set_color(WHITE)
        banner_gold.set_position(Point(CELL_SIZE, CELL_SIZE * 1)) # Sets X to CELL_SIZE(15) and Y to CELL_SIZE *1(15)
        cast.add_actor("banners", banner_gold)

        banner_silver = Actor()
        banner_silver.set_text("")
        banner_silver.set_font_size(FONT_SIZE)
        banner_silver.set_color(WHITE)
        banner_silver.set_position(Point(CELL_SIZE, CELL_SIZE * 2)) # Sets X to CELL_SIZE(15) and Y to CELL_SIZE *2(30)
        cast.add_actor("banners", banner_silver)

        banner_coal = Actor()
        banner_coal.set_text("")
        banner_coal.set_font_size(FONT_SIZE)
        banner_coal.set_color(WHITE)
        banner_coal.set_position(Point(CELL_SIZE, CELL_SIZE * 3)) # Sets X to CELL_SIZE(15) and Y to CELL_SIZE *2(45)
        cast.add_actor("banners", banner_coal)
        
        # create the robot
        x = int(MAX_X / 2)
        y = int(MAX_Y / 2)
        position = Point(x, y)

        robot = Actor()
        robot.set_text("#")
        robot.set_image(MINER_IMAGE)
        robot.set_font_size(FONT_SIZE)
        robot.set_color(WHITE)
        robot.set_position(position)
        cast.add_actor("robots", robot)
        
        # create the artifacts
        with open(DATA_PATH) as file:
            data = file.read()
            messages = data.splitlines()

        for n in range(GOLD_ARTIFACTS):
            text = "G" # This sets our gold character as a G
            value = random.choice([100, 500]) # This line uses random to assign a value of either 500 or 1000
            message = f"You have found {value} Gold!" # Message will tell user what they found. Instead of random messages like RFK we have set a message for Gold

            x = random.randint(1, COLS - 1)
            y = random.randint(1, ROWS - 1)
            position = Point(x, y)
            position = position.scale(CELL_SIZE)

            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = Color(r, g, b)
            
            artifact = Artifact()
            artifact.set_text(text)
            artifact.set_image(MINERAL_IMAGE)
            artifact.set_font_size(FONT_SIZE)
            artifact.set_color(color)
            artifact.set_position(position)
            artifact.set_value(value) # Passes our 'value' defined above to instance of 'Artifact()' class called 'artifact' to use the 'set_value()' method
            artifact.set_message(message)
            cast.add_actor("artifacts", artifact)

        for n in range(SILVER_ARTIFACTS):
            text = "S" # This sets our Silver character as an S
            value = random.choice([100, 500]) # This line uses random to assign a value of either 100 or 500
            message = f"You have found {value} Silver!" # Message will tell user what they found. Instead of random messages like RFK we have set a message for Silver

            x = random.randint(1, COLS - 1)
            y = random.randint(1, ROWS - 1)
            position = Point(x, y)
            position = position.scale(CELL_SIZE)

            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = Color(r, g, b)
            
            artifact = Artifact()
            artifact.set_text(text)
            artifact.set_font_size(FONT_SIZE)
            artifact.set_color(color)
            artifact.set_position(position)
            artifact.set_value(value) # Passes our 'value' defined above to instance of 'Artifact()' class called 'artifact' to use the 'set_value()' method
            artifact.set_message(message)
            cast.add_actor("artifacts", artifact)
        
        for n in range(COAL_ARTIFACTS):
            text = "C" # This sets our Coal character as a C
            value = random.choice([200, 500, 800, 1000]) # This line uses random to assign a value of either 100 or 500
            message = f"You have found {value} Coal!" # Message will tell user what they found. Instead of random messages like RFK we have set a message for Coal

            x = random.randint(1, COLS - 1)
            y = random.randint(1, ROWS - 1)
            position = Point(x, y)
            position = position.scale(CELL_SIZE)

            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = Color(r, g, b)
            
            artifact = Artifact()
            artifact.set_text(text)
            artifact.set_font_size(FONT_SIZE)
            artifact.set_color(color)
            artifact.set_position(position)
            artifact.set_value(value) # Passes our 'value' defined above to instance of 'Artifact()' class called 'artifact' to use the 'set_value()' method
            artifact.set_message(message)
            cast.add_actor("artifacts", artifact)

        """
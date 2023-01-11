"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730489785"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other: Point) -> float:
        """Compare the  distance between two Points."""
        between: float = sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)
        return between


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE 

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.
    def tick(self) -> None:
        """Recover cells."""
        self.location = self.location.add(self.direction)
        if self.is_infected() is True:
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()
        
    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable() is True:
            return "gray"
        if self.is_infected() is True:
            return "red"
        if self.is_immune() is True:
            return "light blue"
        return "black"

    def contract_disease(self) -> None:
        """Mark a cell as infected after it contracts disease."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Check if cell is vulnerable."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False

    def is_infected(self) -> bool:
        """Check if cell is infected."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False

    def contact_with(self, another_cell: Cell) -> None:
        """If either cell object is infected, the  other should become vulnerable."""
        if self.is_infected() is True and another_cell.is_vulnerable() is True:
            another_cell.contract_disease()
        if self.is_vulnerable() is True and another_cell.is_infected() is True:
            self.contract_disease()

    def immunize(self) -> None:
        """Assign IMMUNE to sickness attribute."""
        self.sickness = constants.IMMUNE

    def is_immune(self) -> bool:
        """Return True when cell object is IMMUNE."""
        something: bool = False
        if self.sickness == constants.IMMUNE:
            something = True
        return something


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, initially_infected: int, initially_immune: int = 0):
        """Initialize the cells with random locations and directions."""
        if cells <= initially_infected or initially_infected <= 0:
            raise ValueError("Initially- infected- cells must be greater than 0 but less than the total number of cells")

        if cells < initially_immune + initially_infected or initially_immune < 0:
            raise ValueError("Initially immune cells must be __")

        self.population = []
        for i in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            if i < initially_infected:
                cell.contract_disease()
                i += 1
            elif i < initially_infected + initially_immune:
                cell.immunize()
            self.population.append(cell)

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed 
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0

        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0

        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0

        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        a: int = 0
        while a < len(self.population):
            if self.population[a].is_infected() is True:
                return False
            else:
                a += 1
        return True

    def check_contacts(self) -> None:
        """Compare the distance between every two Cell objects' location."""
        a: int = 0
        b: int = 1
        while a < len(self.population):
            while b < len(self.population):
                if self.population[a].location.distance(self.population[b].location) < constants.CELL_RADIUS:
                    self.population[b].contact_with(self.population[a])
                b += 1
            a += 1
            b = a + 1
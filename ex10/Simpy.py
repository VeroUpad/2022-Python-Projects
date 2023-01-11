"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730489785"


class Simpy:
    """Simple version of Numpy."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Initialize the values attribute of the Simply object to the arugements passed in."""
        self.values = values

    def __repr__(self) -> str:
        """Produce a str representation."""
        return f"Simpy({self.values})"

    def fill(self, filler: float, quantity: int) -> None:
        """Fill Simpy's values with a specific number of repeating values."""
        self.values = []
        i: int = 0
        while i < quantity:
            self.values.append(filler)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in values attiribute with range of values."""
        self.values = []
        self.values.append(start)
        new: float = start
        new += step
        while new != stop:
            self.values.append(new)
            new += step
            
    def sum(self) -> float:
        """Return the sum of all things in values."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Return added Simpy."""
        result: Simpy = Simpy([])
        i: int = 0
        if isinstance(rhs, float):
            while i < len(self.values):
                result.values.append(self.values[i] + rhs)
                i += 1
        else:
            assert len(rhs.values) == len(self.values)
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i += 1
        return result
    # work on

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Return power-ed Simpy."""
        result: Simpy = Simpy([])
        i: int = 0
        if isinstance(rhs, float):
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs)
                i += 1
        else:
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs.values[i])
                i += 1
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Check if they're equal."""
        results: list[bool] = []
        i: int = 0
        if isinstance(rhs, float):
            while i < len(self.values):
                if self.values[i] == rhs:
                    results.append(True)
                    i += 1
                else:
                    results.append(False)
                    i += 1
        else:
            while i < len(self.values):
                if self.values[i] == rhs.values[i]:
                    results.append(True)
                    i += 1
                else:
                    results.append(False)
                    i += 1
        return results

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Check if they're equal."""
        results: list[bool] = []
        i: int = 0
        if isinstance(rhs, float):
            while i < len(self.values):
                if self.values[i] > rhs:
                    results.append(True)
                    i += 1
                else:
                    results.append(False)
                    i += 1
        else:
            while i < len(self.values):
                if self.values[i] > rhs.values[i]:
                    results.append(True)
                    i += 1
                else:
                    results.append(False)
                    i += 1
        return results

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Use Simpy with subscription notations."""
        i = 0
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            results: Simpy = Simpy([])
            while i < len(self.values):
                if rhs[i]: 
                    results.values.append(self.values[i])
                i += 1
        return results
from dataclasses import dataclass
from enum import Enum
from typing import List, Dict
import numpy as np
from scipy.optimize import linear_sum_assignment


class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"


@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: List[OperatingSystem]


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem


def sadness(person: Person, laptop: Laptop) -> int:
    """Return the sadness of allocating this laptop to this person."""
    try:
        return person.preferred_operating_system.index(laptop.operating_system)
    except ValueError:
        return 100  # OS not in preferences at all


def allocate_laptops(people: List[Person], laptops: List[Laptop]) -> Dict[Person, Laptop]:
    n = len(people)
    m = len(laptops)

    # Build cost matrix (n people x m laptops)
    cost_matrix = np.array(
        [[sadness(person, laptop) for laptop in laptops] for person in people],
        dtype=float,
    )

    # linear_sum_assignment requires rows <= cols; it assigns each person exactly one laptop.
    # If there are fewer laptops than people this will raise — the problem assumes enough laptops.
    person_indices, laptop_indices = linear_sum_assignment(cost_matrix)

    return {people[i]: laptops[j] for i, j in zip(person_indices, laptop_indices)}
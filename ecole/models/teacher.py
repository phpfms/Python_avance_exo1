# -*- coding: utf-8 -*-

"""
Classe Teacher
"""
from __future__ import annotations
from datetime import date
from typing import Optional, TYPE_CHECKING
from dataclasses import dataclass, field

from .person import Person

if TYPE_CHECKING:
    from .course import Course


@dataclass
class Teacher(Person):
    """Enseignant d'un ou plusieurs cours de l'école :
    - id              : clé primaire de l'entité persistante
    - hiring_date     : date d'arrivée dans l'école
    - courses_teached : cours qu'il ou elle enseigne
    """
    id_teacher: Optional[int] = field(default=None, init=False)
    hiring_date: date
    courses_teached: list[Course] = field(default_factory=list, init=False)

    def add_course(self, course: Course) -> None:
        """Ajoute ce cours à la liste des cours enseignés
        par cet enseignant et définit cet enseignant pour le cours.
        """
        if course not in self.courses_teached:
            self.courses_teached.append(course)

        if course.teacher != self:
            course.teacher = self

    def remove_course(self, course: Course) -> None:
        """Retire ce cours de la liste des cours enseignés
        par cet enseignant et retire l'enseignant du cours.
        """
        if course in self.courses_teached:
            self.courses_teached.remove(course)

        if course.teacher == self:
            course.teacher = None

    def __str__(self) -> str:
        person_str = super().__str__()
        return f"{person_str}, arrivé(e) le {self.hiring_date}"

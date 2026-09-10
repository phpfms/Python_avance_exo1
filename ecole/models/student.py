# -*- coding: utf-8 -*-

"""
Classe Student, fille de la classe Person
"""

from dataclasses import dataclass, field
from typing import ClassVar
from .person import Person
from .course import Course


@dataclass
class Student(Person):
    """Elève suivant un ou plusieurs cours de l'école :
    - students_nb   : nombre total d'élèves
    - student_nbr   : n° d'élève
    - courses_taken : liste des cours pris par cet élève
    """
    student_nbr: Optional[int] = field(default=None, init=False) # lors de la creation de l'etudiant on peut pas donner de numero car c la ase de donnee qui le genere
    courses_taken: list[Course] = field(default_factory=list, init=False)

    def add_course(self, course: Course) -> None:
        """Ajout du cours course à la liste des cours suivis par l'élève."""
        if course not in self.courses_taken:
            self.courses_taken.append(course)

        if self not in course.students_taking_it:
            course.students_taking_it.append(self)

    def __str__(self) -> str:
        person_str = super().__str__()
        return f"{person_str}, n° étudiant : {self.student_nbr}"

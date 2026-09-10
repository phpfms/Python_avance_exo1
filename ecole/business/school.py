# -*- coding: utf-8 -*-

"""
Classe School
"""

from dataclasses import dataclass

from business.business_student import BusinessStudent
from business.business_teacher import BusinessTeacher
from business.business_course import BusinessCourse
from business.business_address import BusinessAddress
from business.business_person import BusinessPerson


@dataclass
class School:
    """Classe principale de gestion de l'école."""

    def __init__(self):
        """Initialise les différents services métier."""

        self.student = BusinessStudent()
        self.teacher = BusinessTeacher()
        self.course = BusinessCourse()
        self.address = BusinessAddress()
        self.person = BusinessPerson()

    def display_students(self) -> None:
        """Affiche la liste des étudiants."""

        self.student.display_students()

    def display_courses_list(self) -> None:
        """Affiche la liste des cours."""

        # Pour le moment, on utilise les cours créés
        # dans init_static().
        self.course.display_courses_list(self.courses)

    def get_course_by_id(self, id_course):
        """Récupère un cours grâce à son identifiant."""

        return self.course.get_course_by_id(id_course)

    def get_student_by_id(self, student_nbr):
        """Récupère un étudiant grâce à son numéro."""

        return self.student.get_student_by_id(student_nbr)

    def get_teacher_by_id(self, id_teacher):
        """Récupère un enseignant grâce à son identifiant."""

        return self.teacher.get_teacher_by_id(id_teacher)

    def get_address_by_id(self, id_address):
        """Récupère une adresse grâce à son identifiant."""

        return self.address.get_address_by_id(id_address)

    def get_person_by_id(self, id_person):
        """Récupère une personne grâce à son identifiant."""

        return self.person.get_person_by_id(id_person)

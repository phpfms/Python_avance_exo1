# -*- coding: utf-8 -*-

"""
Classe School
"""

from dataclasses import dataclass, field
from datetime import date

from daos.course_dao import CourseDao
from daos.address_dao import AddressDao
from daos.student_dao import StudentDao
from models.address import Address
from models.course import Course
from models.teacher import Teacher
from models.student import Student


@dataclass
class School:
    """Couche métier de l'application de gestion d'une école,
    reprenant les cas d'utilisation et les spécifications fonctionnelles :
    - courses : liste des cours existants
    - teachers : liste des enseignants
    - students : liste des élèves"""

    courses: list[Course] = field(default_factory=list, init=False)
    teachers: list[Teacher] = field(default_factory=list, init=False)
    students: list[Student] = field(default_factory=list, init=False)

    def add_course(self, course: Course) -> None:
        """Ajout du cours course à la liste des cours."""
        self.courses.append(course)

    def add_teacher(self, teacher: Teacher) -> None:
        """Ajout de l'enseignant teacher à la liste des enseignants."""
        self.teachers.append(teacher)

    def add_student(self, student: Student) -> None:
        """Ajout de l'élève spécifié à la liste des élèves."""
        self.students.append(student)

    @staticmethod
    def get_course_by_id(id_course: int):
        # print("Module =", CourseDao.__module__)
         course_dao: CourseDao = CourseDao()
         return course_dao.read(id_course)

    def display_courses_list(self) -> None:
        """Affiche la liste des cours avec leur enseignant."""
        for course in self.courses:
            if course.teacher is not None:
                print(
                    f"- {course.name} : "
                    f"{course.teacher.first_name} {course.teacher.last_name}"
                )
            else:
                print(f"- {course.name} : aucun enseignant")

    def display_students(self) -> None:
        """Affiche la liste des étudiants."""

        student_dao = StudentDao()
        students = student_dao.read_all()

        print("\n===== LISTE DES ÉTUDIANTS =====")

        for student in students:
            print(student)

        print()

    def init_static(self) -> None:
        """Initialisation d'un jeu de test pour l'école."""
        
        # création des étudiants et rattachement à leur adresse
        paul: Student    = Student('Paul', 'Dubois', 12, 2)
        valerie: Student = Student('Valérie', 'Dumont', 13, 3)
        louis: Student   = Student('Louis', 'Berthot', 11, 4)
        philippe: Student = Student('philippe', 'philippe', 10, 5)

        paul.address    = Address('12 rue des Pinsons', 'Castanet', '31320')
        valerie.address = Address('43 avenue Jean Zay', 'Toulouse', '31200')
        louis.address   = Address('7 impasse des Coteaux', 'Cornebarrieu', '31150')
        philippe.address = Address('123 rue de loin', 'tatouine', '99999')

        # ajout de ceux-ci à l'école
        for student in [paul, valerie, louis, philippe]:
            self.add_student(student)

        # création des cours
        francais: Course = Course("Français", date(2024, 1, 29),
                                              date(2024, 2, 16))
        histoire: Course = Course("Histoire", date(2024, 2, 5),
                                              date(2024, 2, 16))
        geographie: Course = Course("Géographie", date(2024, 2, 5),
                                                  date(2024, 2, 16))
        mathematiques: Course = Course("Mathématiques", date(2024, 2, 12),
                                                        date(2024, 3, 8))
        physique: Course = Course("Physique", date(2024, 2, 19),
                                              date(2024, 3, 8))
        chimie: Course = Course("Chimie", date(2024, 2, 26),
                                          date(2024, 3, 15))
        anglais: Course = Course("Anglais", date(2024, 2, 12),
                                            date(2024, 2, 24))
        espagnol: Course = Course("espagnol", date(2023, 1, 11),
                                             date(2026, 12, 31))
        sport: Course = Course("Sport", date(2024, 3, 4),
                                        date(2024, 3, 15))

        # ajout de ceux-ci à l'école
        for course in [francais, histoire, geographie, mathematiques,
                       physique, chimie, anglais, espagnol, sport]:
            self.add_course(course)

        # création des enseignants
        victor  = Teacher('Victor', 'Hugo', 23, date(2023, 9, 4))
        jules   = Teacher('Jules', 'Michelet', 32, date(2023, 9, 4))
        sophie  = Teacher('Sophie', 'Germain', 25, date(2023, 9, 4))
        marie   = Teacher('Marie', 'Curie', 31, date(2023, 9, 4))
        william = Teacher('William', 'Shakespeare', 34, date(2023, 9, 4))
        michel  = Teacher('Michel', 'Platini', 42, date(2023, 9, 4))

        # ajout de ceux-ci à l'école
        for teacher in [victor, jules, sophie, marie, william, michel]:
            self.add_teacher(teacher)

        # association des élèves aux cours qu'ils suivent
        for course in [geographie, physique, anglais]:
            paul.add_course(course)

        for course in [francais, histoire, chimie]:
            valerie.add_course(course)

        for course in [mathematiques, physique, geographie, sport]:
            louis.add_course(course)

        for course in [francais, anglais, espagnol, histoire]:
            philippe.add_course(course)

        # association des enseignants aux cours qu'ils enseignent
        victor.add_course(francais)
        michel.add_course(espagnol)
        jules.add_course(histoire)
        jules.add_course(geographie)
        sophie.add_course(mathematiques)
        marie.add_course(physique)
        marie.add_course(chimie)
        william.add_course(anglais)
        michel.add_course(sport)

        # gestion des addresses en BDD
        address_dao = AddressDao()
        address_dao.create(philippe.address)

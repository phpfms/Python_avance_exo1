# permet de récupérer/manipuler les étudiants

# -*- coding: utf-8 -*-

"""
Gestion métier des étudiants
"""

from daos.student_dao import StudentDao
from daos.person_dao import PersonDao


class BusinessStudent:

    def __init__(self):
        self.person_dao = PersonDao()
        self.student_dao = StudentDao()

    def get_student_by_id(self, student_nbr):
        """Récupère un étudiant grâce à son numéro."""
        return self.student_dao.read(student_nbr)

    def get_students(self):
        """Récupère la liste des étudiants."""
        return self.student_dao.read_all()

    def add_student(self, student):
        """Ajoute un étudiant en base de données."""
        # Création de la personne
        # l'ecriture suivante fonctionne car student est une personne
        self.person_dao.create(student)
        # Création de l'étudiant
        return self.student_dao.create(student)

    def update_student(self, student):
        """Modifie un étudiant."""
        self.student_dao.update(student)

    def delete_student(self, student_nbr):
        """Supprime un étudiant."""
        self.student_dao.delete(student_nbr)

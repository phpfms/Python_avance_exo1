# permet de récupérer/manipuler les enseignants

# -*- coding: utf-8 -*-

"""
Gestion métier des enseignants
"""

from daos.teacher_dao import TeacherDao


class BusinessTeacher:

    def __init__(self):
        self.teacher_dao = TeacherDao()

    def get_teacher_by_id(self, id_teacher):
        """Récupère un enseignant grâce à son identifiant."""
        return self.teacher_dao.read(id_teacher)

    def add_teacher(self, teacher):
        """Ajoute un enseignant en base de données."""
        return self.teacher_dao.create(teacher)

    def update_teacher(self, teacher):
        """Modifie un enseignant."""
        self.teacher_dao.update(teacher)

    def delete_teacher(self, id_teacher):
        """Supprime un enseignant."""
        self.teacher_dao.delete(id_teacher)

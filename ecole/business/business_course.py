# permet de récupérer/manipuler les cours

# -*- coding: utf-8 -*-

"""
Gestion métier des cours
"""

from daos.course_dao import CourseDao


class BusinessCourse:

    def __init__(self):
        self.course_dao = CourseDao()

    def get_course_by_id(self, id_course):
        """Récupère un cours grâce à son identifiant."""
        return self.course_dao.read(id_course)

    def get_courses(self):
        """Récupère la liste des cours."""
        return self.course_dao.read_all()

    def add_course(self, course):
        """Ajoute un cours en base de données."""
        return self.course_dao.create(course)

    def update_course(self, course):
        """Modifie un cours."""
        self.course_dao.update(course)

    def delete_course(self, id_course):
        """Supprime un cours."""
        self.course_dao.delete(id_course)

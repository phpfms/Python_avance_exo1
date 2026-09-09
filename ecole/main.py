#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Application de gestion d'une école
"""

from business.school import School
from models.course import Course


def main() -> None:
    """Programme principal."""
    print("""\
--------------------------
Bienvenue dans notre école
--------------------------""")

    school: School = School()

    # initialisation d'un ensemble de cours, enseignants et élèves composant l'école
    school.init_static()

    # affichage de la liste des cours, leur enseignant et leurs élèves
    # school.display_courses_list()
    # course1: Course = school.get_course_by_id(1)
    #print(school.get_course_by_id(2))


if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-

"""
Affichage des cours
"""


class DisplayCourse:

    def display_courses_list(self, courses) -> None:
        """Affiche la liste des cours avec leur enseignant."""

        for course in courses:
            if course.teacher is not None:
                print(
                    f"- {course.name} : "
                    f"{course.teacher.first_name} "
                    f"{course.teacher.last_name}"
                )
            else:
                print(f"- {course.name} : aucun enseignant")
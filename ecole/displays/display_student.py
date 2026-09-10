# -*- coding: utf-8 -*-

"""
Affichage des étudiants
"""


class DisplayStudent:

    def display_students(self, students) -> None:
        """Affiche la liste des étudiants."""

        print("\n===== LISTE DES ÉTUDIANTS =====")

        for student in students:
            print(student)

        # Ligne vide pour aérer l'affichage
        print()


# fichier qui permet à l'utilisateur de faire des choix numeriques

from business.school import School
from menu import Menu


class Application:

    def __init__(self):
        """Initialise l'application."""
        self.school = School()
        self.menu = Menu()

    def run(self):
        """Lance l'application."""

        self.school.init_static()

        conti = True

        while conti:
            choix = self.menu.display_main_menu()

            if choix == "1":
                self.student_menu()

            elif choix == "2":
                self.teacher_menu()

            elif choix == "3":
                self.course_menu()

            elif choix == "4":
                self.address_menu()

            elif choix == "0":
                print("Au revoir.")
                conti = False

            else:
                print("Choix invalide.")

    def student_menu(self):
        """Gère le sous-menu des étudiants."""

        conti = True

        while conti:
            choix = self.menu.display_student_menu()

            if choix == "1":
                print("Afficher les étudiants")
                self.school.display_students()

            elif choix == "2":
                print("Afficher les cours d'un étudiant")
                # self.school.display_student_courses()

            elif choix == "3":
                print("Afficher les enseignants d'un étudiant")
                # self.school.display_student_teachers()

            elif choix == "0":
                print("Retour au menu principal.")
                conti = False

            else:
                print("Choix invalide.")

    def teacher_menu(self):
        """Gère le sous-menu des professeurs."""

        conti = True

        while conti:
            choix = self.menu.display_teacher_menu()

            if choix == "1":
                print("Afficher les professeurs")
                # self.school.display_teachers()

            elif choix == "2":
                print("Afficher les élèves d'un professeur")
                # ...

            elif choix == "3":
                print("Afficher les élèves qui suivent un cours")
                # ...

            elif choix == "4":
                print(
                    "Afficher tous les élèves qui suivent "
                    "au moins un cours du professeur"
                )
                # ...

            elif choix == "5":
                print("Créer un cours")
                # ...

            elif choix == "0":
                print("Retour au menu principal.")
                conti = False

            else:
                print("Choix invalide.")

    def course_menu(self):
        """Gère le sous-menu des cours."""

        conti = True

        while conti:
            choix = self.menu.display_course_menu()

            if choix == "1":
                self.school.display_courses_list()

            elif choix == "2":
                print("Afficher les étudiants d'un cours")
                # ...

            elif choix == "3":
                print("Afficher l'enseignant d'un cours")
                # ...

            elif choix == "0":
                print("Retour au menu principal.")
                conti = False

            else:
                print("Choix invalide.")

    def address_menu(self):
        """Gère le sous-menu des adresses."""

        conti = True

        while conti:
            choix = self.menu.display_address_menu()

            if choix == "1":
                print("Afficher les adresses")
                # ...

            elif choix == "2":
                print("Afficher les personnes habitant à une adresse")
                # ...

            elif choix == "0":
                print("Retour au menu principal.")
                conti = False

            else:
                print("Choix invalide.")


if __name__ == "__main__":
    app = Application()
    app.run()
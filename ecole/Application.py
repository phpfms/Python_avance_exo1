# fichier qui permet à l'utilisateur de faire des choix numeriques,
# il joue un role de controleur

from business.business_student import BusinessStudent
from business.business_teacher import BusinessTeacher
from business.business_course import BusinessCourse
from business.business_address import BusinessAddress
from business.business_person import BusinessPerson

from displays.display_student import DisplayStudent
from displays.display_course import DisplayCourse

from models.student import Student

from menu import Menu


class Application:

    def __init__(self):
        """Initialise l'application."""
        self.menu = Menu()

        # Gestion métier
        self.student = BusinessStudent()
        self.teacher = BusinessTeacher()
        self.course = BusinessCourse()
        self.address = BusinessAddress()
        self.person = BusinessPerson()

        # Affichage
        self.display_student = DisplayStudent()
        self.display_course = DisplayCourse()

    def run(self):
        """Lance l'application et affiche le menu principal."""

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
                students = self.student.get_students()
                self.display_student.display_students(students)

            elif choix == "2":
                print("Afficher les cours d'un étudiant")
                # ...

            elif choix == "3":
                print("Afficher les enseignants d'un étudiant")
                # ...

            elif choix == "4":
                print("\n===== AJOUTER UN ÉTUDIANT =====")

                # Saisie du prénom
                valide = False

                while not valide:
                    first_name = input("Prénom : ").strip()

                    if first_name == "":
                        print("Le prénom ne peut pas être vide.")

                    elif not first_name.replace("-", "").replace(
                        " ", ""
                    ).isalpha():
                        print(
                            "Le prénom ne doit contenir que des lettres."
                        )

                    else:
                        valide = True

                # Saisie du nom
                valide = False

                while not valide:
                    last_name = input("Nom : ").strip()

                    if last_name == "":
                        print("Le nom ne peut pas être vide.")

                    elif not last_name.replace("-", "").replace(
                        " ", ""
                    ).isalpha():
                        print(
                            "Le nom ne doit contenir que des lettres."
                        )

                    else:
                        valide = True

                # Saisie de l'âge
                valide = False

                while not valide:
                    age_input = input("Âge : ").strip()

                    try:
                        age = int(age_input)

                        if age < 1 or age > 130:
                            print(
                                "L'âge doit être compris entre "
                                "1 et 130 ans."
                            )

                        else:
                            valide = True

                    except ValueError:
                        print("Veuillez entrer un nombre entier.")

                # Création de l'étudiant
                student = Student(
                    first_name,
                    last_name,
                    age
                )

                # Enregistrement en BDD
                student_nbr = self.student.add_student(student)

                print(
                    f"Étudiant créé avec succès. "
                    f"Numéro étudiant : {student_nbr}"
                )

            elif choix == "5":
                print("Modifier un etudiant")
                # ...

            elif choix == "6":
                print("Supprimer un etudiant")
                # ...

            elif choix == "7":
                print("Inscrire un étudiant à un cours")
                # ...

            elif choix == "8":
                print("Désinscrire un étudiant d'un cours")
                # ...

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
                # ...

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

            elif choix == "6":
                print("Ajouter un professeur")
                # ...

            elif choix == "7":
                print("Modifier un professeur")
                # ...

            elif choix == "8":
                print("Supprimer un professeur")
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
                print("Afficher la liste des cours")
                courses = self.course.get_courses()
                self.display_course.display_courses_list(courses)

            elif choix == "2":
                print("Afficher les étudiants d'un cours")
                # ...

            elif choix == "3":
                print("Afficher l'enseignant d'un cours")
                # ...

            elif choix == "4":
                print("Ajouter un cours")
                # ...

            elif choix == "5":
                print("Modifier un cours")
                # ...

            elif choix == "6":
                print("Supprimer un cours")
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

            elif choix == "3":
                print("Ajouter une adresse")
                # ...

            elif choix == "4":
                print("Modifier une adresse")
                # ...

            elif choix == "5":
                print("Supprimer une adresse")
                # ...

            elif choix == "0":
                print("Retour au menu principal.")
                conti = False

            else:
                print("Choix invalide.")


if __name__ == "__main__":
    app = Application()
    app.run()

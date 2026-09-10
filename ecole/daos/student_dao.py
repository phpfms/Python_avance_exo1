# fichier de gestion des requetes sql et qui cré un objet etudiant dans read()

# -*- coding: utf-8 -*-

"""
Classe Dao[Student]
"""

from models.student import Student
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional
import mysql.connector

@dataclass
class StudentDao(Dao[Student]):

    def create(self, student: Student) -> int:
        """Crée en BD l'entité Student correspondant au student."""
        with Dao.connection.cursor() as cursor:
            sql = "INSERT INTO student (id_person) VALUES (%s)"
            cursor.execute(sql, (student.id_person, ))
            student_nbr = cursor.lastrowid

        Dao.connection.commit()
        # Récupère le numéro généré par la BDD
        student.student_nbr = student_nbr
        return student_nbr

    def read(self, student_nbr: int) -> Optional[Student]:
        """Renvoie le cours correspondant à l'entité dont l'id est id_student
           (ou None s'il n'a pu être trouvé)
           Fonction qui crée un objet étudient
           """
        student: Optional[Student]

        with Dao.connection.cursor() as cursor:
            sql = """
                SELECT student.student_nbr,
                       person.id_person,
                       person.first_name,
                       person.last_name,
                       person.age
                FROM student
                JOIN person ON student.id_person = person.id_person
                WHERE student.student_nbr=%s
            """

            cursor.execute(sql, (student_nbr,))
            record = cursor.fetchone()

        # ici on cré un objet étudiant
        if record is not None:
            student = Student(
                record['first_name'],
                record['last_name'],
                record['age']
            )
            student.student_nbr = record['student_nbr']
            student.id_person = record['id_person']
        else:
            student = None

        return student

    def read_all(self) -> list[Student]:
        """Renvoie la liste de tous les étudiants. (créé plein d'objets étudiant et les met en liste"""

        students = []

        try:
            with Dao.connection.cursor() as cursor:
                sql = """
                SELECT student.student_nbr,
                       person.id_person,
                       person.first_name,
                       person.last_name,
                       person.age
                FROM student
                JOIN person ON student.id_person = person.id_person
                ORDER BY student.student_nbr
            """

                cursor.execute(sql)
                records = cursor.fetchall()

            for record in records:
                student = Student(
                    record['first_name'],
                    record['last_name'],
                    record['age']
                )

                # Récupération des identifiants venant de la BDD
                student.id_person = record['id_person']
                student.student_nbr = record['student_nbr']

                students.append(student)

        except mysql.connector.Error as error:
            print(f"Erreur lors de la lecture des étudiants : {error}")

        return students

    def update(self, student: Student) -> None:
        """Modifie un étudiant existant en BDD."""

        with Dao.connection.cursor() as cursor:
            sql = """
                UPDATE student
                SET id_person=%s
                WHERE student_nbr=%s
            """

            cursor.execute(
                sql,
                (student.id_person, student.student_nbr)
            )

        Dao.connection.commit()

    def delete(self, student_nbr: int) -> None:
        """Supprime un étudiant de la BDD."""

        with Dao.connection.cursor() as cursor:
            sql = "DELETE FROM student WHERE student_nbr=%s"
            cursor.execute(sql, (student_nbr,))

        Dao.connection.commit()
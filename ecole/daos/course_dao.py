# -*- coding: utf-8 -*-

"""
Classe Dao[Course]
"""

from models.course import Course
from models.teacher import Teacher
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional


@dataclass
class CourseDao(Dao[Course]):
    def create(self, course: Course) -> int:
        """Crée en BD l'entité Course correspondant au cours course
        :param course: à créer sous forme d'entité Course en BD
        :return: l'id de l'entité insérée en BD (0 si la création a échoué)
        """
        with Dao.connection.cursor() as cursor:
            sql = "INSERT INTO course (name, start_date, end_date, id_teacher) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (course.name, course.start_date, course.end_date, course.teacher.id_teacher))
            id_course = cursor.lastrowid
        Dao.connection.commit()
        course.id = id_course
        return id_course

    def read(self, id_course: int) -> Optional[Course]:
        """Renvoie le cours correspondant à l'entité dont l'id est id_course
           (ou None s'il n'a pu être trouvé)"""
        course: Optional[Course]
        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM course WHERE id_course=%s"
            cursor.execute(sql, (id_course,))
            record = cursor.fetchone()
        if record is not None:
            course = Course(record['name'], record['start_date'], record['end_date'])
            course.id = record['id_course']
        else:
            course = None

        return course

    def read_all(self) -> list[Course]:
        """Renvoie la liste de tous les Cours."""

        courses = []

        with Dao.connection.cursor() as cursor:
            sql = """
                SELECT course.id_course,
                       course.name,
                       course.start_date,
                       course.end_date,
                       course.id_teacher,
                       teacher.hiring_date,
                       person.id_person,
                       person.first_name,
                       person.last_name,
                       person.age
                FROM course
                JOIN teacher ON course.id_teacher = teacher.id_teacher
                JOIN person ON teacher.id_person = person.id_person
                ORDER BY course.name;
            """

            cursor.execute(sql)
            records = cursor.fetchall()

        for record in records:
            # Création du cours
            course = Course(
                record['name'],
                record['start_date'],
                record['end_date']
            )
            course.id = record['id_course']

            # Création de l'enseignant
            teacher = Teacher(
                record['first_name'],
                record['last_name'],
                record['age'],
                record['hiring_date']
                )

            teacher.id_teacher = record['id_teacher']
            teacher.id_person = record['id_person']

            # Association du professeur au cours
            course.set_teacher(teacher)

            # Ajout du cours à la liste des cours
            courses.append(course)

        return courses


    def update(self, course: Course) -> bool:
        """Met à jour en BD l'entité Course correspondant à course, pour y correspondre

        :param course: cours déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        with Dao.connection.cursor() as cursor:
            sql = "UPDATE course SET name=%s, start_date=%s, end_date=%s, id_teacher=%s WHERE id_course=%s"
            cursor.execute(sql, (course.name, course.start_date, course.end_date, course.get_id_teacher_in_object(), course.id))
        Dao.connection.commit()
        return True

    def delete(self, course: Course) -> bool:
        """Supprime en BD l'entité Course correspondant à course

        :param course: cours dont l'entité Course correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """
        with Dao.connection.cursor() as cursor:
            sql = "DELETE FROM course WHERE id_course=%s"
            cursor.execute(sql, (course.id,))
        Dao.connection.commit()
        return True
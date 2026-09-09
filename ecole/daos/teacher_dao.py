# -*- coding: utf-8 -*-

"""
Classe Dao[Teacher]
"""

from models.teacher import Teacher
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional

@dataclass
class TeacherDao(Dao[Teacher]):

    def create(self, teacher: Teacher) -> int:
        """Crée en BD l'entité Teacher correspondant au teacher

        :param teacher: à créer sous forme d'entité Teacher en BD
        :return: l'id de l'entité insérée en BD (0 si la création a échoué)
        """
        with Dao.connection.cursor() as cursor:
            sql = "INSERT INTO teacher (hiring_date, id_person) VALUES (%s, %s)"
            cursor.execute(sql, (teacher.hiring_date, teacher.id_person))
            id_teacher = cursor.lastrowid
        Dao.connection.commit()
        teacher.id_teacher = id_teacher
        return id_teacher

    def read(self, id_teacher: int) -> Optional[Teacher]:
        "Renvoie le Teacher correspondant à id_teacher ou None."
        teacher: Optional[Teacher]
        with Dao.connection.cursor() as cursor:
            sql = """SELECT teacher.id_teacher, teacher.hiring_date,
                       person.id_person, person.first_name,
                       person.last_name, person.age
                FROM teacher
                JOIN person ON teacher.id_person = person.id_person
                WHERE teacher.id_teacher=%s"""

            cursor.execute(sql, (id_teacher,))
            record = cursor.fetchone()
        if record is not None:
            teacher = Teacher(record['first_name'], record['last_name'], record['age'], record['hiring_date'])
            teacher.id_teacher = record['id_teacher']
            teacher.id_person = record['id_person']
        else:
            teacher = None

        return teacher
    
    def update(self, teacher: Teacher) -> None:
        """Modifie une adresse existante en BDD."""
        with Dao.connection.cursor() as cursor:
            sql = "UPDATE teacher SET hiring_date=%s WHERE id_teacher=%s"
            cursor.execute(sql, (teacher.hiring_date, teacher.id_teacher))
        Dao.connection.commit()

    def delete(self, id_teacher: int) -> None:
        """Supprime une adresse de la BDD."""
        with Dao.connection.cursor() as cursor:
            sql = "DELETE FROM teacher WHERE id_teacher=%s"
            cursor.execute(sql, (id_teacher,))
        Dao.connection.commit()
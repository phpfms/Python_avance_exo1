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
        """Crée en BD l'entité Teacher correspondant au teacher teacher

        :param teacher: à créer sous forme d'entité Teacher en BD
        :return: l'id de l'entité insérée en BD (0 si la création a échoué)
        """
        ...
        return 0

    def read(self, id_teacher: int) -> Optional[Teacher]:
        """Renvoie le cours correspondant à l'entité dont l'id est id_teacher
           (ou None s'il n'a pu être trouvé)"""
        teacher: Optional[Teacher]

        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM teacher WHERE id_teacher=%s"
            cursor.execute(sql, (id_teacher,))
            record = cursor.fetchone()
        if record is not None:
            teacher = Teacher(record['id_teacher'], record['hiring_date'], record['id_person'])
            teacher.id_teacher = record['id_teacher']
        else:
            teacher = None

        return teacher
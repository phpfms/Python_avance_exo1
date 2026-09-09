# -*- coding: utf-8 -*-

"""
Classe Dao[Student]
"""

from models.student import Student
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional

@dataclass
class StudentDao(Dao[Student]):

    def read(self, id_student: int) -> Optional[Student]:
        """Renvoie le cours correspondant à l'entité dont l'id est id_student
           (ou None s'il n'a pu être trouvé)"""
        student: Optional[Student]

        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM student WHERE student_nbr=%s"
            cursor.execute(sql, (id_student,))
            record = cursor.fetchone()
        if record is not None:
            student = Student(record['student_nbr'],  record['id_person'])
            student.id = record['id_student']
        else:
            student = None

        return student
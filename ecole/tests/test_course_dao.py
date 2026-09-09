# -*- coding: utf-8 -*-

"""
Tests de la classe CourseDao
"""

from datetime import date

from models.course import Course
from models.person import Person
from models.teacher import Teacher
from daos.person_dao import PersonDao
from daos.teacher_dao import TeacherDao
from daos.course_dao import CourseDao


def test_create():
    person_dao = PersonDao()
    teacher_dao = TeacherDao()
    course_dao = CourseDao()

    person = Person("Victor", "Hugo", 23)
    id_person = person_dao.create(person)

    teacher = Teacher("Victor", "Hugo", 23, date(2023, 9, 4))
    teacher.id_person = id_person
    id_teacher = teacher_dao.create(teacher)

    course = Course("Mathématiques", date(2024, 2, 12), date(2024, 3, 8))
    course.set_teacher(teacher)

    id_course = course_dao.create(course)

    assert id_course is not None
    assert course.id == id_course


def test_read():
    person_dao = PersonDao()
    teacher_dao = TeacherDao()
    course_dao = CourseDao()

    person = Person("Victor", "Hugo", 23)
    id_person = person_dao.create(person)

    teacher = Teacher("Victor", "Hugo", 23, date(2023, 9, 4))
    teacher.id_person = id_person
    id_teacher = teacher_dao.create(teacher)

    course = Course("Mathématiques", date(2024, 2, 12), date(2024, 3, 8))
    course.set_teacher(teacher)

    id_course = course_dao.create(course)

    result = course_dao.read(id_course)

    assert result is not None
    assert result.id == id_course
    assert result.name == "Mathématiques"
    assert result.start_date == date(2024, 2, 12)
    assert result.end_date == date(2024, 3, 8)


def test_update():
    person_dao = PersonDao()
    teacher_dao = TeacherDao()
    course_dao = CourseDao()

    person = Person("Victor", "Hugo", 23)
    id_person = person_dao.create(person)

    teacher = Teacher("Victor", "Hugo", 23, date(2023, 9, 4))
    teacher.id_person = id_person
    id_teacher = teacher_dao.create(teacher)

    course = Course("Mathématiques", date(2024, 2, 12), date(2024, 3, 8))
    course.set_teacher(teacher)

    id_course = course_dao.create(course)

    course.name = "Physique"
    course.start_date = date(2024, 2, 19)
    course.end_date = date(2024, 3, 15)

    result = course_dao.update(course)

    assert result is True

    course_updated = course_dao.read(id_course)

    assert course_updated is not None
    assert course_updated.id == id_course
    assert course_updated.name == "Physique"
    assert course_updated.start_date == date(2024, 2, 19)
    assert course_updated.end_date == date(2024, 3, 15)


def test_delete():
    person_dao = PersonDao()
    teacher_dao = TeacherDao()
    course_dao = CourseDao()

    person = Person("Victor", "Hugo", 23)
    id_person = person_dao.create(person)

    teacher = Teacher("Victor", "Hugo", 23, date(2023, 9, 4))
    teacher.id_person = id_person
    id_teacher = teacher_dao.create(teacher)

    course = Course("Mathématiques", date(2024, 2, 12), date(2024, 3, 8))
    course.set_teacher(teacher)

    course_dao.create(course)

    result = course_dao.delete(course)

    assert result is True

    course_deleted = course_dao.read(course.id)

    assert course_deleted is None
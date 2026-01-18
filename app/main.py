from dataclasses import dataclass
from datetime import date
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    nb_students = []
    with open(file="groups.pickle", mode="wb") as file:
        for group in groups:
            pickle.dump(group, file)
            nb_students.append(len(group.students))

    try:
        return max(nb_students)
    except ValueError:
        return 0


def write_students_information(students: list[Student]) -> int:
    with open(file="students.pickle", mode="wb") as file:
        for student in students:
            pickle.dump(student, file)

    return len(students)


def read_groups_information() -> list[Specialty]:

    groups = []
    with open(file="groups.pickle", mode="rb") as file:
        while True:
            try:
                groups.append(pickle.load(file))
            except EOFError:
                break

    specialties = list(set([group.specialty for group in groups]))

    return list(specialties)


def read_students_information() -> list[Student]:

    students = []
    with open(file="students.pickle", mode="rb") as file:
        while True:
            try:
                students.append(pickle.load(file))
            except EOFError:
                break

    return students

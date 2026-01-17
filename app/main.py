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

    return max(nb_students)


def write_students_information(students: list[Student]) -> int:
    with open(file="students.pickle", mode="wb") as file:
        for student in students:
            pickle.dump(student, file)

    return len(students)


def read_groups_information() -> list[Specialty]:

    groups = []

    groups.append(_load_pickle_file(file_name="groups.pickle"))

    specialties = set([speciality for group in groups for
                       speciality in group.speciality])

    return list(specialties)


def read_students_information() -> list[Student]:

    students = []

    students.append(_load_pickle_file(file_name="students.pickle"))

    return students


def _load_pickle_file(file_name: str) -> object:
    with open(file=file_name, mode="rb") as file:
        while True:
            try:
                yield pickle.load(file)
            except EOFError:
                break

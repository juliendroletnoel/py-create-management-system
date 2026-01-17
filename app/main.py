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


def write_groups_information(groups: list[Group],
                             file_name="groups.pickle") -> int:
    with open(file=file_name, mode="b") as file:
        pickle.dump(groups, file)

    nb_students = len([student for group in groups
                       for student in group.students])
    return nb_students


def write_students_information(students: list[Student], 
                               file_name="students.pickle") -> int:
    with open(file=file_name, mode="b") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information(file_name="groups.pickle") -> list[Specialty]:

    groups = []

    groups.append(_load_pickle_file(file_name=file_name))

    specialties = set([speciality for group in groups for
                       speciality in group.speciality])

    return list(specialties)


def read_students_information(file_name="students.pickle") -> list[Student]:

    students = []

    students.append(_load_pickle_file(file_name=file_name))

    return students


def _load_pickle_file(file_name: str) -> object:
    with open(file=file_name, mode="b") as file:
        while True:
            try:
                yield pickle.load(file)
            except EOFError:
                break

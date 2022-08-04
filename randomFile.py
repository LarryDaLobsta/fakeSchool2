import random
import string
from random import seed, randint
import names
from typing import Optional, List, Dict, Tuple
import pandas as pd


# generates random password for the student
def password() -> str:
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.digits
    length = 10
    password_build = lower + upper + num + symbols
    temp = random.sample(password_build, length)
    password_final = "".join(temp)
    return password_final


def full_name() -> str:
    name = names.get_full_name()
    return name


def institution(college_email: str) -> str:
    college_choice: str
    college2: str
    school_list: Tuple[str, str]
    # open the file
    data = pd.read_csv("Institutions/us_universities.csv")
    school_list = [tuple(row) for row in data.values]

    for x, y in school_list:
        if college_email in y:
            college_choice = x
            return college_choice
    
    """
    may need to add a statement to address the condition if the email
    does not exist
    """


# email format take url from file and strip to format
def stud_email(student_name: str) -> str:
    student_email: str
    url_list: List[str] = []
    extension_list: List[str] = []
    sep: str = ".edu"
    sep2: str = ".org"
    sep3: str = ".com"

    if not isinstance(student_name, str):
        raise TypeError("student name given was not a string")
    # may want to add if a student_name was not provided,
    # the ability to generate a full name
    # open the file
    data = pd.read_csv("Institutions/us_universities.csv")
    url_list = data['url'].tolist()

    for index, item in enumerate(url_list):
        strip_url = url_list[index][11:-1]
        if sep in strip_url:
            strip_url2 = strip_url.split(sep, 1)[0]
            strip_url2 = strip_url2 + sep
        if sep2 in strip_url:
            strip_url2 = strip_url.split(sep, 1)[0]
            strip_url2 = strip_url2 + sep2
        if sep3 in strip_url:
            strip_url2 = strip_url.split(sep, 1)[0]
            strip_url2 = strip_url2 + sep3
        extension_list.append(strip_url)

    if student_name is None:
        student_name = full_name()
    extension = random.choice(extension_list)
    student_email = student_name.replace(" ", "") + extension
    return student_email


def student_id_number() -> int:
    student_number: int

    student_number = random.randint(100000, 999999)
    return student_number


def student_status() -> str:
    status: str
    credit_status: Dict[str] = {}

    credit_status = {
        "Full time": 12,
        "3/4 time": 9,
        "Part time": 6,
        "Less than half": 1
    }

    status = random.choice(list(credit_status))
    return status


def student_credit_hours(credit_status: str) -> int:
    credit_hours: int
    credit_status_list = ["Full time", "3/4 time", "Part time", "Less than half"]
    if credit_status not in credit_status_list:
        raise ValueError("The credit status given is not an option listed")
    # may need to add a case if a credit status is not correct

    match credit_status:
        case "Full time":
            credit_hours = random.randint(12, 18)
        case "3/4 time":
            credit_hours = random.randint(9, 11)
        case "Part time":
            credit_hours = random.randint(6, 8)
        case "Less than half":
            credit_hours = random.randint(1, 5)
    return credit_hours


def student_gpa() -> int:
    gpa: int
    student_type: List[str]
    letter_grade: str

    student_type = [
        "good student", "average student", "below average student"
    ]

    letter_grade = random.choice(student_type)
    match letter_grade:
        case "good student":
            gpa = round(random.uniform(3.00, 4.00), 2)
        case "average student":
            gpa = round(random.uniform(2.00, 4.00), 2)
        case "below average student":
            gpa = round(random.uniform(1.00, 2.00), 2)
    return gpa


def student_Degree() -> str:
    degree: List[str]
    degree_choice: str

    degree = [
        "Associate", "Bachelor", "Graduate"]

    degree_choice = random.choice(degree)

    return degree_choice


def student_year() -> str:
    year_choice: List[str]
    year_status: str

    year_choice = [
        "Freshman", "Sophmore", "Junior", "Senior"
    ]
    year_status = random.choice(year_choice)
    return year_status


def credits_completed(degree_type: str) -> int:
    completed_credits: int
    # check to make sure that what is passed down is in the list
    # graduate, Associate, Bachelor
    degree_types_list = ["Graduate", "Associate", "Bachelor"]
    if degree_type not in degree_types_list:
        raise ValueError("The Degree type given is no an option")
    if degree_type != "Graduate":
        if degree_type == "Associate":
            completed_credits = random.randint(0, 60)
            return completed_credits
        # doing a bachelor degree
        if degree_type == "Bachelor":
            completed_credits = random.randint(60, 120)
            return completed_credits
    completed_credits = random.randint(0, 50)
    completed_credits = completed_credits + 120
    return completed_credits


def graduation_status(credits_earned: int, degree_type: str) -> bool:
    status: bool = False
    degree_types_list = ["Graduate", "Associate", "Bachelor"]
    if credits_earned < 0:
        raise ValueError("The credits earned is less than 0")
    if degree_type not in degree_types_list:
        raise ValueError("The Degree type given is no an option")
    if credits_earned == 60 and degree_type == "Associate":
        status = True
        return status
    if credits_earned == 120 and degree_type == "Bachelor":
        status = True
        return status
    if credits_earned >= 170 and degree_type == "Graduate":
        status = True
        return status
    return status



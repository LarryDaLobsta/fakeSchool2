'''
this will test the files that contain the classes for the fake data
'''

from mimetypes import init
import sys
sys.path.append("../")
import randomFile as rf
import pytest


def capital_case(x):
    return x.capitalize()


def test_capital_case():
    assert capital_case('testword') == 'Testword'


"""
def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capital_case(9)
"""

"""
this section will contain the test for what we need
"""


# for the failed test for the TypeError I do not know if I should reject
# the argument and throw an error or set the argument to None
# or accept the argument for possible use

def test_password():
    assert type(rf.password()) == str
    assert rf.password("Yeet")


def test_full_name():
    assert type(rf.full_name()) == str
    assert rf.full_name("Gerald Henderson")


def test_institution():
    assert type(rf.institution("www.acu.edu")) == str
    assert rf.institution("www.acu.edu")
    '''
    there will need to be a statement to address the condition if the institution 
    does not exist
    '''

# next test starts at stud_email

def test_stud_email():
    # test to make sure name is fed to the function
    # test that string is returned
    assert type(rf.stud_email("Todd Ingrams")) == str
    assert rf.stud_email("Terry Jones")
    assert rf.stud_email(1234)


def test_student_id_number():
    assert type(rf.student_id_number()) == int
    assert rf.student_id_number(123)


def test_student_status():
    assert type(rf.student_status()) == str
    assert rf.student_status("Hello")

def test_student_credit_hours():
    assert type(rf.student_credit_hours("Full time")) == int
    assert rf.student_credit_hours("No Time")


# left off on student gpa


def test_student_gpa():
    assert type(rf.student_gpa()) == int
    assert rf.student_gpa("Hello there")
    assert rf.student_gpa(1234)


def test_student_Degree():
    assert type(rf.student_Degree()) == str
    assert rf.student_Degree("No string")
    assert rf.student_Degree(1234)

def test_student_year():
    assert type(rf.student_year()) == str
    assert rf.student_year("No string")
    assert rf.student_year(1234)


def test_credits_completed():
    assert type(rf.credits_completed("Associate")) == int
    assert rf.credits_completed("Bachelor")
    assert rf.credits_completed(1234)


# need to finish with graduation status
def test_graduation_status():
    assert type(rf.graduation_status(120, "Bachelor"))
    assert rf.graduation_status(-15, "Bachelor")



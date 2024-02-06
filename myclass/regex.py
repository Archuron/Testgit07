import re

def isStudentIDValid(test_id):
    # Corrected regular expression for university student ID validation
    regex = r'^(1[7-9]|[2-9]\d)[1-9]\d{4}$'

    if re.match(regex, test_id):
        return True
    else:
        return False

def test_student_id():
    student_id1 = '5802868'  # Invalid, third digit cannot be 0
    student_id2 = '1610001'  # Invalid, Buddhist year not greater than 16
    student_id3 = '1800120'  # Invalid, Semester cannot be 0
    student_id4 = '5812868'  # Valid
    student_id5 = '2233010'  # Valid
    student_id6 = '1900000'  # Invalid, Semester cannot be 0

    print(f'{student_id1} is {"Valid" if isStudentIDValid(student_id1) else "Invalid"}')
    print(f'{student_id2} is {"Valid" if isStudentIDValid(student_id2) else "Invalid"}')
    print(f'{student_id3} is {"Valid" if isStudentIDValid(student_id3) else "Invalid"}')
    print(f'{student_id4} is {"Valid" if isStudentIDValid(student_id4) else "Invalid"}')
    print(f'{student_id5} is {"Valid" if isStudentIDValid(student_id5) else "Invalid"}')
    print(f'{student_id6} is {"Valid" if isStudentIDValid(student_id6) else "Invalid"}')

# Run the test
test_student_id()

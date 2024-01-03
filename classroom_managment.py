classroom = [
    {
        'name': 'Alice',
        'email': 'alice@example.com',
        'grades': [
            ('math', 91),
            ('english', 78),
            ('math', 90),
            ('history', 34),
            ('math', 95),
        ],
    },
    {
        'name': 'Bob',
        'email': 'bob@example.com',
        'grades': [
            ('math', 85),
            ('english', 92),
            ('history', 75),
        ],
    },
    {
        'name': 'Charlie',
        'email': 'charlie@example.com',
        'grades': [
            ('physics', 78),
            ('english', 81),
            ('english', 89),
            ('history', 68),
            ('english', 82),
            ('physics', 91),
        ],
    },
]


def add_student(name, email=None):
    """Add a new student to the classroom
    with the following keys:
    'name': the given name
    'email': if email is given use it otherwise use <name>@example.com
             in lowercase, you can use the `s.lower()` method
    'grade': initialize with empty list
    """
    student = {"name":name, "grades":[]}
    student ["email"]=email or f'{name.lower()}@example.com'
    classroom.append(student)
    pass


def delete_student(name):
    """Delete a student from the classroom"""
    filtered_classroom = []
    for student in classroom:
        if name != student['name']:
           filtered_classroom.append(student)
    classroom = filtered_classroom

    pass


def set_email(name, email):
    """Sets the email of the student"""
    for student in classroom:
        if name == student['name'] and email == student['email']:
            return student

    pass



def add_grade(name, profession, grade):
    """Adds a new grade to the student grades"""
    for student in classroom:
        if name == student['name']:
            student.grades.Add(profession, grade)

    pass


def avg_grade(name, profession):
    """Returns the average of grades of the student
    in the specified profession
    """
    for student in classroom:
            if name == student['name']:
                count=0
                sum_grade=0
                for grade in profession:
                   sum_grade=sum_grade+grade
                   count+=1
    return (float) (sum_grade/count)
                

    pass


def get_professions(name):
    """Returns a list of unique professions that student has grades in"""
    for student in classroom:
        if name == student['name']:
            new_profession=[]
            for i in student.grades:
                new_profession.append(i)
    return new_profession

    pass

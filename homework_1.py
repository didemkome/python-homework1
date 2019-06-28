import sys

def extract_data(filename):
    """
    >>> extract_data('./test_data.txt')
    [{'student_name': 'John Doe', 'student_score': 22}]
    """

    lines = list()
    result = list()
    with open(filename, 'r') as file_pointer:
        lines = file_pointer.readlines()

    for line in lines:
        line = line.rstrip('\n').split(',')
        student_name = line[0]
        student_score = int(line[1])

        result.append(dict(student_name=student_name, student_score=student_score))
    return result


def analyse_data():
    data = extract_data('./student_data.txt')

    average_point = int(sum(x["student_score"] for x in data))
    # average_point = 0
    # for person_data in data:
    #     student_score = person_data.get('student_score')
    #     average_point += student_score

    average_point = average_point / len(data)

    students_grater_then_average = list()

    students_grater_then_average = [i for i in data if i['student_score'] >= average_point]

    # for person_data in data:
    #     student_score = person_data.get('student_score')
    #     if student_score > average_point:
    #         students_grater_then_average.append(person_data)

    students_grater_then_average = sorted(students_grater_then_average, key=lambda k: k['student_score'], reverse=True)

    if students_grater_then_average:
        sys.stdout.write('Students scored greater then %d\n' % average_point)
        for student in students_grater_then_average:
            sys.stdout.write('%-30s %s\n' % (student.get('student_name'), student.get('student_score')))

    total_ranks = sorted(data, key=lambda k: k['student_score'], reverse=True)

    sys.stdout.write('-' * 50)
    sys.stdout.write('\n')
    sys.stdout.write('Scores\n')
    for student in total_ranks:
        sys.stdout.write('%-30s %s\n' % (student.get('student_name'), student.get('student_score')))


if __name__ == '__main__':
    import doctest

    doctest.testmod()

analyse_data()

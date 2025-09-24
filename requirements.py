list_of_subs = [
    {
        "quizName": "Geometry",
        "quizModule": "Math",
        "quizScore": 50,
        "studentId": 1,
        "studentName": "Jasmine",
        "submissionDate": "2025-07-08",
    },
    {
        "quizName": "World history",
        "quizModule": "History",
        "quizScore": 80,
        "studentId": 1,
        "studentName": "Jasmine",
        "submissionDate": "2024-10-23",
    },
    {
        "quizName": "Math with functions",
        "quizModule": "Math",
        "quizScore": 85,
        "studentId": 2,
        "studentName": "Joe",
        "submissionDate": "2020-07-10",
    },
    {
        "quizName": "Parameters",
        "quizModule": "Math",
        "quizScore": 95,
        "studentId": 3,
        "studentName": "Kim",
        "submissionDate": "2024-11-20",
    },
]


def filter_by_date(date, Submissions):
    """
    Filter through a list of objects of submissions to get all the submissions on that date you enter.

    Parameters:
        date (a string), Submissions(a list of dictionaries): A list of numerical and string values.

    Returns:
        A list of dictionaries.
    """
    list_of_filter_submissions = []

    if Submissions == []:
        return list_of_filter_submissions

    for submission in Submissions:
        if submission["submissionDate"] == date:
            list_of_filter_submissions.append(submission)

    return list_of_filter_submissions


def filter_by_student_id(studentId, submissions):
    """
    Filter through the students id and get list

    Parameters:

    """
    list_of_studentsIds = []
    for submission in submissions:
        if submission["studentId"] == studentId:
            list_of_studentsIds.append(submission)

    if list_of_studentsIds == []:
        return list_of_studentsIds

    return list_of_studentsIds


def get_students_name(submissions):
    new_list = []
    for submission in submissions:
        new_list.append(submission["studentName"])
    return new_list


def find_unsubmitted(date, students_name, submissions):
    """ """
    completed_list = filter_by_date(date, submissions)
    return [student for student in students_name if student not in completed_list]


def get_average_score(submissions):
    """
    Calculates the average of each list of submissions of quiz scores.

    Parameters:
        submissions (list of dictionaries): A list of numerical and string values.

    Returns:
        float: average of all the quiz scores.
    """
    total = 0
    l = 0
    for submission in submissions:
        total += submission["quizScore"]
        l += 1

    return round(total / l, 1)


def get_average_score_by_module(submissions):
    modules_averages = {}
    counts = {}
    scores = {}

    for submission in submissions:
        module = submission["quizModule"]
        score = submission["quizScore"]

        if module not in scores:
            scores[module] = 0
            counts[module] = 0
        scores[module] += score
        counts[module] += 1

    # for submission in submissions:
    #     modules_averages[submission["quizModule"]] = submission["quizScore"]

    return modules_averages


get_average_score_by_module(list_of_subs)

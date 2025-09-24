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
        "quizName": "Periodiac table",
        "quizModule": "Science",
        "quizScore": 60,
        "studentId": 4,
        "studentName": "Kate",
        "submissionDate": "2024-2-13",
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
    Filter through the students id and get list.

    Parameters:
        studentId(number), submissions(list of dictionaries): A list of numerical and string values.

    Returns:
        list: A list of dictionaries.
    """
    list_of_studentsIds = []
    for submission in submissions:
        if submission["studentId"] == studentId:
            list_of_studentsIds.append(submission)

    if list_of_studentsIds == []:
        return list_of_studentsIds

    return list_of_studentsIds


def get_students_names(submissions):
    """
    Give you students names out of the list of dictionaries.

    Parameters:
         submissions (list of dictionaries): A list of numerical and string values.

    Returns:
        list: A list of all the students names.
    """
    new_list = []
    for submission in submissions:
        new_list.append(submission["studentName"])
    return new_list


def valid_students_names(submissions, students_names):
    """
    Make sure input that was recieve has names in the list of submissions.

    Parameters:
        submissions(list of dictonaries), student_names(list of a strings).

    Returns:
        list: A list of all the students names in the submission.
    """
    valid_names = []
    for submission in submissions:
        for student in students_names:
            if student == submission["studentName"]:
                valid_names.append(submission["studentName"])
    return valid_names


def find_unsubmitted(date, students_names, submissions):
    """
     Will find all the unsubmitted date.

     Parameters:
        date(a string), student_name(a list of strings), submissions(list of dictionaries): A list of numerical and string values.

    Returns:
        list: A list of all unsubmitted students.
    """
    completed_list = filter_by_date(date, submissions)
    valid_list = valid_students_names(submissions, students_names)

    if valid_list == []:
        return valid_list

    return [student for student in students_names if student not in completed_list]


def get_average_score(submissions):
    """
    Calculates the average of each list of submissions quiz scores.

    Parameters:
        submissions (list of dictionaries): A list of numerical and string values.

    Returns:
        float: average of all the quiz scores.
    """
    total = 0
    count = 0
    for submission in submissions:
        total += submission["quizScore"]
        count += 1

    return round(total / count, 1)


def get_average_score_by_module(submissions):
    """
    Calculate the average of each quiz score in the module out of the list of submissions.

    Parameters:
        submissions (list of dictionaries): A list of numerical and string values.

    Returns:
        list: a list of dictionaries with the average score for each module.
    """
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

    for module in scores:
        modules_averages[module] = round(scores[module] / counts[module], 1)

    return modules_averages

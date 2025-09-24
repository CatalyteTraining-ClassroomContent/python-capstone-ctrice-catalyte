list_of_subs = [
    {
        "quizName": "Math",
        "quizModule": "Geometry",
        "quizScore": 50,
        "studentId": 1,
        "studentName": "Jasmine",
        "submissionDate": "2025-07-08",
    },
    {
        "quizName": "History",
        "quizModule": "World History",
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
        "quizModule": "Geometry",
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
    completed_list = filter_by_date(date, submissions)
    print(completed_list)
    new_list = []
    # i = 0
    # for student in students_name:
    #     if student != not_completed_list[i]["studentName"]:
    #         # i += 1
    #         new_list.append(student)

    return [name for name in students_name if name not in completed_list]


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


# Quiz Average by Module Feature (get_average_score_by_module)
# 1. Given I have a list of submission objects, when I supply that list to the
# get_average_score_by_module function, I am returned an object.
# 2. Given that I have received an object from this feature, then there is one key for
# every unique module name in the submission list, and the keys are the module
# names.
# 3. Given that I have a list of submission objects from only one module, when I use the
# quiz average by module feature, then the resulting object contains only one key.
# 4. When I have received an object from this feature, the value of each key should be
# the average of quiz scores from that module.
# Example:
# {
# "Statistics": 83.5,
# "Algebra": 79.6,
# "History": 80.1
# }
def get_list(module, submissions):
    list = []
    for submission in submissions:
        if submission["quizModule"] == module:
            list.append(submission)
    return list


def get_average_score_by_module(submissions):
    modules_averages = {}

    for submission in submissions:
        for key, value in modules_averages.items():
            if key == submission["quizModule"]:
                value += submission["quizScore"]
        if modules_averages[submission["quizModule"]] != submission["quizModule"]:
            modules_averages[submission["quizModule"]] = submission["quizScore"]

    return modules_averages


print(get_average_score_by_module(list_of_subs))
# print(get_list("Geometry", list_of_subs))
# print(get_students_name(list_of_subs))
# print(find_unsubmitted("2025-07-08", ["Jasmine", "Kim"], list_of_subs))
# # print(filter_by_date("2020-07-10", list_of_subs))
# print(get_average_score(list_of_subs))
# print(filter_by_student_id(2, list_of_subs))

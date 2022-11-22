from csv import reader as csv_reader


def get_subject_list(marks):
    """
    Time Complexity : O(n)
    Space Complexity : O(n)
    """
    sub_list = []
    for sub in marks[0]:
        if sub not in sub_list:
            sub_list.append(sub)
    return sub_list

def total_marks_list(sub_list):
    """
    Time Complexity : O(n^2)
    Space Complexity : O(n)
    """
    total_list = []
    for ind_mark in marks:
        total = 0
        for sub in sub_list[1:]:
            total += int(ind_mark[sub])
        total_list.append(total)
    return total_list  

def get_subject_toppers(marks):
    """
    Time Complexity : O(n^2)
    Space Complexity : O(1)
    """
    for sub in get_subject_list(marks)[1:]:
        sub_top = {
            "mark" : -1,
            "name" : ""
            }
        for ind_mark in marks:
            if ind_mark[sub] != "name" and int(ind_mark[sub]) < sub_top["mark"]:
                pass
            elif ind_mark[sub] != "name" and int(ind_mark[sub]) > sub_top["mark"]:
                sub_top["mark"] = int(ind_mark[sub])
                sub_top["name"] =  ind_mark["name"]
            elif ind_mark[sub] != "name" and int(ind_mark[sub]) == sub_top["mark"]:
                sub_top["mark"] = int(ind_mark[sub])
                sub_top["name"] = sub_top["name"] +","+ ind_mark["name"]
        if len(sub_top["name"].split(","))==1:
            print("Topper in {} is {}.".format(sub, sub_top["name"]))
        else:
            print("Topper in {} are {}.".format(sub, sub_top["name"]))

def get_class_toppers(marks):
    """
    Time Complexity : O(1)
    Space Complexity : O(1)
    """
    total_list = total_marks_list(get_subject_list(marks))
    first = ""
    maximum = total_list[0]
    idx = 0
    for num in range(len(total_list)):
        if total_list[num] > maximum:
            maximum = total_list[num]
            idx = num
    first += marks[idx]["name"]
    total_list[idx] = -1

    second = ""
    maximum = total_list[0]
    idx = 0
    for num in range(len(total_list)):
        if total_list[num] > maximum:
            maximum = total_list[num]
            idx = num
    second += marks[idx]["name"]
    total_list[idx] = -1

    third = ""
    maximum = total_list[0]
    idx = 0
    for num in range(len(total_list)):
        if total_list[num] > maximum:
            maximum = total_list[num]
            idx = num
    third += marks[idx]["name"]

    return "Best students in the class are {}, {} and {}.".format(first, second, third)


headers = True
marks = []
# read csv file
try:
    """
    Time Complexity : O(n^2)
    Space Complexity : O(n)
    """
    with open("marks_list.csv", 'r') as file:
        fileReader = csv_reader(file)
        if headers:
            columns = next(fileReader)
        for row in fileReader:
            row_data = {}
            for i in range(len(row)):
                if headers:
                    row_key = columns[i].lower()
                else:
                    row_key = i
                row_data[row_key] = row[i]
            marks.append(row_data)
except Exception as e:
    print(repr(e))
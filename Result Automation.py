import requests
import os


# This is Beta version, it includes only Two college and particular course.

# Pdf having 13KB size, Not a valid result, Soo delete that PDF

# The advance Version includes All the college and all courses which belongs to Patliputra University

branch_choice = int(input(" Enter Branch:-\n"
                          "    1. Rajendra nagar\n"
                          "    2.Saguna more \n"
                          "    :- "))
course = int(input(" Enter Course:-\n"
                   "    1. BCA\n"
                   "    2. BBM\n"
                   "    :- "))
session = int(input(" Enter Session:-\n"
                    "    1. 2019-2022 \n"
                    "    2. 2020-2023\n"
                    "    3. 2021-2024\n"
                    "    :- "))
part = int(input(" Enter Year:-\n"
                 "    1. 1st year Result\n"
                 "    2. 2nd year Result\n"
                 "    3. 3rd year Result\n"
                 "    :- "))

total_student = int(input(" Enter Total no. of student (Max)\n"
                          "    :- "))

# Variables ----------------
branch_code = 0
session_code = 0
course_code = 0

# Conditions----------------
if branch_choice == 1:
    branch_code = 439
elif branch_choice == 2:
    branch_code = 440
else:
    "INVALID BRANCH"

if session == 1:
    session_code = 20
elif session == 2:
    session_code = 21
elif session == 3:
    session_code = 22
else:
    "INVALID SESSION"

if course == 1:
    course_code = 40080000
elif course == 2:
    course_code = 40070000
else:
    "INVALID COURSE"

year = str(session_code + part -1)

dir_name = "Section "+ str(session_code-1)+"-"+ str(session_code+2) + f" Part {part}"

if not os.path.isdir(dir_name):
    os.mkdir(dir_name)

if year == "20":
    part = "I"


url1 = "https://lu.indiaexaminfo.co.in/PATLIPUTRA/YEAR-20"
url2 = "/Vocational/PART-"

for i in range(1,total_student+1):
    roll = course_code + i
    exten = ".pdf"
    url_roll = str(session_code) + str(branch_code) + str(roll) + exten
    url_link = url1 + year + url2 + str(part) + "/" + url_roll
    f_name = dir_name+ "/" + url_roll
    r = requests.get(url_link, allow_redirects=True)
    open(f_name, 'wb').write(r.content)
    print(url_link)
    print(url_roll)
# gender : "male" or "femaile"
# race/ethinicity : "group A" to "group E"
# parental level of education : "bachelor's degree" / "some college" / "master's degree" / "associate's degree" / "some college" / "high school"
# lunch : type of lunch - "standard" or "free/reduced"
# test preparation course : If a student did the test preparation course before the exams - completed / none
# math score : 0 to 100
# reading score : 0 to 100
# writing score : 0 to 100

import pandas as pd
import random


genders = ["Male", "male", "Female", "female", "M", "F"]
race = ["group A", "group b", "group c", "Group D", "group A", "group e"]
parental_level_of_edu = ["bachelor's degree", "some college", "master's degree", "associate's degree", "high school"]
lunch = ["standard", "Standard", "Free", "free/reduced"]
test_preparation_course = ["completed"]


def random_null(value):
    probability = 0.1
    return None if random.random() < probability else value
    

rows = []
for i in range(1000):
    row = {
        "gender" : random_null(random.choice(genders)),
        "race/ethnicity" : random_null(random.choice(race)),
        "parental_level_of_edu" : random_null(random.choice(parental_level_of_edu)),
        "lunch" : random_null(random.choice(lunch)),
        "test_preparation_course" : random_null(random.choice(test_preparation_course)),
        "math_score" : random_null(random.randint(25,90)),
        "reading_score" : random_null(random.randint(15,97)),
        "writing_score" : random_null(random.randint(13,85)),
    }
    
    rows.append(row)

df  = pd.DataFrame(rows)

df.to_csv('Assignment_02/dataset.csv', index=False)

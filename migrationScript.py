import os,sys

os.chdir("/home/mamata/kemo/")
os.getcwd()


import json

from courses.CoursesDB import CoursesDB
from pathlib import Path
parentFolder = str(Path(__file__).resolve().parent)
coursesDB =  CoursesDB()       
with open(parentFolder + '/courses.json', 'r') as file:
    courses = json.loads(file.read())
    result = coursesDB.collection.insert_many(courses)
    if result.acknowledged:
        coursesDB.collection.create_index("domain")
        print("SUCCESSFULLY INSERTED")
    else:
        print("FAILED TO INSERT")
   
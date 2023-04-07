from fastapi.testclient import TestClient
import json
from .apps import app
import difflib
from pathlib import Path
parentFolder = str(Path(__file__).resolve().parent)
client = TestClient(app)


def test_post_chapter_rating():
    print("isnide")
    response = client.post(
        "/chapterrating",
       
        json={
                "coursename": "Highlights of Calculus",
                "username": "user123",
                "chaptername": "Big Picture: Derivatives",
                "chapterdetail": "Highlights of Calculus",
                "rating": 4
            },
    )
    assert response.status_code == 200

def test_get_courses():
    
    response = client.post(
        "/courses",
       
        json={"sort": {} , 
              "filters" : {}},
    )
    response = response.json()
    with open('/home/mamata/kimogit/kemo/courses.json', 'r') as file:
        courses = json.loads(file.read())

        for course in response:
            if course not in courses:
                if "rating" not in course :
                    assert False
    assert True

def test_get_courses_in_ascending_order_name():
    
    response = client.post(
        "/courses",
       
        json={"sort": {"name" : 1} , 
              "filters" : {}},
    )
    response = response.json()
    with open('/home/mamata/kimogit/kemo/courses.json', 'r') as file:
        courses = json.loads(file.read())
        courses = sorted(courses, key=lambda i: i['name'])
       
        for i in range(len(courses)):
            if(courses[i] != response[i]):
                if "rating" not in response[i] :
                    assert False
    assert True

def test_get_courses_in_descending_order_date():
    
    response = client.post(
        "/courses",
       
        json={"sort": {"date" : -1} , 
              "filters" : {}},
    )
    response = response.json()
    with open('/home/mamata/kimogit/kemo/courses.json', 'r') as file:
        courses = json.loads(file.read())
        courses = sorted(courses, key=lambda i: i['date'], reverse=True)
       
        for i in range(len(courses)):
            if(courses[i] != response[i]):
                if "rating" not in response[i] :
                    assert False
    assert True

def test_get_courses_detail():
    
    response = client.post(
        "/coursedetail",
       
        json={"sort": {} , 
              "filters" :  {"name" : "Introduction to Programming"}},
    )
    response = response.json()
    if "rating" in response[0]:
        response[0].pop("rating")
   
    
    with open('/home/mamata/kimogit/kemo/courses.json', 'r') as file:
        courses = json.loads(file.read())
        
                       
        if response[0] not in courses:
                assert False
  
    assert True

def test_get_chapter_detail():
    
    response = client.post(
        "/chapterdetail",
       
        json={"sort": {} , 
              "filters" :  {"name" : "Introduction to Programming" , "chapterName" : "CS50 2021 in HDR - Lecture 3 - Algorithms"}},
    )
    response = response.json()
   
    assert response["name"] == "Introduction to Programming"


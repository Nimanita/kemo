from pymongo import MongoClient
from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import List
from courses.CoursesService import CoursesService
from courses.UsersService import UsersService
from typing import Union

# Message class defined in Pydantic
class Courses(BaseModel):
    name: str
    date: int
    description: str
    domain : list
    chapters : list
    rating : Union[float, None] = None

class UserRating(BaseModel):
    coursename: str
    username : str
    chaptername : str
    chapterdetail : str
    rating : float
    
    

class Parameters(BaseModel):
    sort: dict
    filters: dict
# Instantiate the FastAPI
app = FastAPI()


    


@app.post("/courses" ,status_code=status.HTTP_200_OK)
def get_course(filterParameter : Parameters):
 
    courses = CoursesService.getCourses(filterParameter.sort , filterParameter.filters)
    
    response_msg_list = []
 
    for course in courses:
        response_msg_list.append(Courses(**course))
    return response_msg_list

@app.post("/coursedetail" ,status_code=status.HTTP_200_OK)
def get_course_detail(filterParameter : Parameters):
    if "name" not in filterParameter.filters:
        return status.HTTP_400_BAD_REQUEST
    
    courses = CoursesService.getCourses(filterParameter.sort , filterParameter.filters)
    
    response_msg_list = []
 
    for course in courses:
        response_msg_list.append(Courses(**course))
    return response_msg_list

@app.post("/chapterdetail" ,status_code=status.HTTP_200_OK)
def get_chapter_detail(filterParameter : Parameters):
  
    if "name" not in filterParameter.filters or "chapterName" not in filterParameter.filters:
        return status.HTTP_400_BAD_REQUEST
    
    chapterDetail = CoursesService.getCourseChapter(filterParameter.filters)
  
    return chapterDetail

@app.post("/chapterrating" ,status_code=status.HTTP_200_OK)
def post_chapter_rating(userRating : UserRating):
    userRating_dict = userRating.__dict__
    chapterDetail = UsersService.insertOrUpdateRating(userRating_dict)
    return status.HTTP_200_OK
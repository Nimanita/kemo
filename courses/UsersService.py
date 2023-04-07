from logging import exception
from courses.UsersDB import UsersDB
from courses.CoursesDB import CoursesDB
import copy

class UsersService:
    usersDb = UsersDB()
    coursesDb = CoursesDB()
    
    @classmethod
    def insertOrUpdateRating(cls , userRating):
        try: 
            filterQuery = copy.deepcopy(userRating)
            filterQuery.pop("rating")
            print("userrating " , filterQuery , userRating)
            result = cls.usersDb.insertOrUpdateRating( userRating["rating"] , filterQuery)
            if result:
                filterQuery = {"chaptername" : userRating["chaptername"] , "coursename" : userRating["coursename"]}
                averagerating = cls.usersDb.getAverageRating(filterQuery)
                averagerating = round(averagerating , 1)
                print(averagerating)
                courseRatingfilterquery = {
                    "chapters" : { "$elemMatch" : {"name" : userRating["chaptername"]}},
                    "name" : userRating["coursename"]
                    }
                result = cls.coursesDb.updateCourseRating(courseRatingfilterquery , averagerating)
                return result
        except Exception as ex:
            return False
from courses.MongoConnection import MongoConnection

class CoursesDB(MongoConnection):

    def __init__(self):
        super(CoursesDB, self).__init__()
        self.get_collection("courses")
    
    def getCourses(self, filterQuery, sortQuery):
        print(sortQuery , "filterquery" , filterQuery)
        cursor = self.collection.find(filterQuery).sort(sortQuery)
        courses = list(cursor)
        return courses
    
    def getCourseChapterDetail(self, filterQuery):

        course = self.collection.find_one(filterQuery)
        
        return course
    
    def updateCourseRating(self, filterQuery , rating):

        result = self.collection.update_one(
            filterQuery,
            {"$set" : {"rating" : rating}},
           )
        return result.acknowledged
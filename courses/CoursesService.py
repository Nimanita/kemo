from courses.CoursesDB import CoursesDB


class CoursesService:
    coursesDb = CoursesDB()
    
    @classmethod
    def generateSortQueries(cls , sortingParams):
        sortQuery = []
        if sortingParams == {}:
            return True , [["_id" , 1]]
        for key in sortingParams:
            if sortingParams[key] != 1 and sortingParams[key] != -1:
                return False , [["_id" , 1]]
            sortQuery.append([key , sortingParams[key]])
                
        return True, sortQuery       
            
    @classmethod
    def generateFilterQueries(cls , filterParams):
        filterQuery = {}
        if filterParams == {}:
           return True , {}
        if "domain" in filterParams:
            filterQuery["domain"] = filterParams["domain"]
        if "name" in filterParams:
            filterQuery["name"] = filterParams["name"]
     
        return True, filterQuery
            
    @classmethod
    def getCourses(cls , sortParameter, filterParameter):
        try:
            result , sortQuery = cls.generateSortQueries(sortParameter)    
            result , filterQuery = cls.generateFilterQueries(filterParameter) 
            print("sortfilter query", sortQuery , filterQuery)  
            courses = cls.coursesDb.getCourses(filterQuery , sortQuery)
            
            return courses
        except Exception as ex:
            return []
     
    @classmethod
    def getCourseChapter(cls , filterParameter):
        
        result , filterQuery = cls.generateFilterQueries(filterParameter) 
        filterQuery["chapters"] = {"$elemMatch" : {"name" : filterParameter["chapterName"]}}
        course = cls.coursesDb.getCourseChapterDetail(filterQuery)
        if course:
            courseChapters = course["chapters"]
            for chapter in courseChapters:
                if chapter["name"] == filterParameter["chapterName"]:
                    return chapter
        else:
            return {}
    
    @classmethod
    def getCourseChapter(cls , filterParameter):
        
        result , filterQuery = cls.generateFilterQueries(filterParameter) 
        filterQuery["chapters"] = {"$elemMatch" : {"name" : filterParameter["chapterName"]}}
        course = cls.coursesDb.getCourseChapterDetail(filterQuery)
        updateQuery = {}
        if course:
            courseChapters = course["chapters"]
            for chapter in courseChapters:
                if chapter["name"] == filterParameter["chapterName"]:             
                    return chapter
        else:
            return {}
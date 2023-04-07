from courses.MongoConnection import MongoConnection

class UsersDB(MongoConnection):

    def __init__(self):
        super(UsersDB, self).__init__()
        self.get_collection("users")
    
    def insertOrUpdateRating(self, rating , filterQuery):
        
        result = self.collection.update_one(
            filterQuery,
            {"$set" : {"rating" : rating}},
            upsert = True)
            
        return result.acknowledged
    
    def getAverageRating(self , filterQuery):
        print(filterQuery)
        averageRating = self.collection.aggregate(
            [{
                "$match": filterQuery
            },
            {
                "$group": {
                    "_id" : {"chaptername": "$chaptername","coursename" : "$coursename"},
                    "AverageRating": { "$avg": "$rating" }
                }
            }
        ]
        )
        averageRating = list(averageRating)
        return averageRating[0]["AverageRating"]
       
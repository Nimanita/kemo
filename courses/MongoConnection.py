from pymongo import MongoClient



class MongoConnection(object):
    def __init__(self):
     
        DATABASES = {'MONGO': {
        'HOST': f"mongodb://127.0.0.1:27017",
        'USERNAME': 'user123',
        'PASSWORD': 'password',
        'DATABASE': 'kimo',
        'AUTH_DATABASE': 'kimo',
    }}
        self.client = MongoClient(
            host=[DATABASES['MONGO']['HOST']],
            username=DATABASES['MONGO']['USERNAME'],
            password=DATABASES['MONGO']['PASSWORD'],
            authSource=DATABASES['MONGO']['AUTH_DATABASE']
        )
        # self.client = MongoClient(host=[DATABASES['MONGO']['HOST']])
        self.db = self.client[DATABASES['MONGO']['DATABASE']]
        self.collection = None

    def get_collection(self, name):
        self.collection = self.db[name]
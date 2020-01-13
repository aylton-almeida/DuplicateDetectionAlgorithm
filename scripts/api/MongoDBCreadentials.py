# Insert your credentials for the atlas mongo db
mongo_pass = "OifBihkGxuGrI5bY"
mongo_url = "mongodb+srv://admin:{}@datawranglingwithmongodb-grevy.gcp.mongodb.net/test?retryWrites=true&w=majority"
mongo_database = "duplicateDetectionApp"
mongo_collection = "uniqueRestaurants"

mongo_credentials = {
    'connection': mongo_url.format(mongo_pass),
    'database': mongo_database,
    'collection': mongo_collection
}


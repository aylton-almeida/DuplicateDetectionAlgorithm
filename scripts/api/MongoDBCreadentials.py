# Insert your credentials for the atlas mongo db
mongo_pass = "<YOUR_PASSWORD>"
mongo_url = "<YOUR_URL>"
mongo_database = "<YOUR_DATABASE>"
mongo_collection = "<YOUR_COLLECTION>"

mongo_credentials = {
    'connection': mongo_url.format(mongo_pass),
    'database': mongo_database,
    'collection': mongo_collection
}


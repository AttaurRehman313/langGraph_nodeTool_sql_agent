import os


# Configure database credentials using pymysql in Python
# class DBConfig:
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     SQLALCHEMY_DATABASE_URI = (
#         'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'
#         .format(
#             username='root',  # Your database username
#             password='1234',  # Your database password
#             host='127.0.0.1',  # Your database host
#             port=3310,  # Your database port
#             database='rms-backend'  # Your database name
#         )
#     )




# from pymongo import MongoClient

# # Define your MongoDB connection URL
# mongo_uri = "mongodb://ask-dubai:ask-dubai@34.16.43.4:27017/ask-dubai"

# # Create a MongoClient instance
# client = MongoClient(mongo_uri)

# # Access the database (in this case, "ask-dubai")
# db = client["ask-dubai"]

# # Optionally, list the collections in the database to verify the connection
# try:
#     collections = db.list_collection_names()
#     print("Connected to MongoDB successfully!")
#     print("Collections in the database:", collections)
# except Exception as e:
#     print("An error occurred while connecting to MongoDB:", e)


from pymongo import MongoClient

class DBConfig:
    # MongoDB Configuration
    MONGO_URI = "mongodb://ask-dubai:ask-dubai@34.16.43.4:27017/ask-dubai"

    @classmethod
    def get_mongo_client(cls):
        return MongoClient(cls.MONGO_URI)

    @classmethod
    def get_mongo_database(cls):
        client = cls.get_mongo_client()
        return client["ask-dubai"]

 

# Example usage
# try:
#     db = DBConfig.get_database()
#     collections = db.list_collection_names()
#     print("Connected to MongoDB successfully!")
#     print("Collections in the database:", collections)
# except Exception as e:
#     print("An error occurred while connecting to MongoDB:", e)




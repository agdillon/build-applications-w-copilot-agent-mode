from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Update with your MongoDB URI if needed
db = client["octofit_db"]

# Create users collection with a unique index on email
db.users.create_index("email", unique=True)

# Initialize other collections
db.teams.insert_one({})  # Placeholder document
db.activity.insert_one({})
db.leaderboard.insert_one({})
db.workouts.insert_one({})

print("Collections initialized:")
print(db.list_collection_names())

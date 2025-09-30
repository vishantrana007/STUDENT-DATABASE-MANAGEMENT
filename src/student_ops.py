from db_config import db
from bson.objectid import ObjectId

# ------------------ COLLECTION ------------------
students = db["students"]  # Student collection

# ------------------ CREATE ------------------
def insert_student(student_data):
    """
    Insert a new student record into the database.

    Parameters:
    student_data (dict): Student info (name, age, course, enrollment_date, status, etc.)

    Returns:
    str: Inserted student ID
    """
    result = students.insert_one(student_data)
    return str(result.inserted_id)


# ------------------ READ ------------------
def get_all_students():
    """
    Retrieve all student records from the database.

    Returns:
    list: List of all student documents
    """
    return list(students.find())


def find_student(query):
    """
    Retrieve student(s) matching an exact query.

    Parameters:
    query (dict): Query dictionary, e.g., {"name": "Vishant Rana"}

    Returns:
    list: List of matching student documents
    """
    return list(students.find(query))


def find_students_with_filter(filter_query):
    """
    Advanced filtering/search for students using MongoDB operators.

    Parameters:
    filter_query (dict): Filter dictionary, e.g., {"age": {"$gt": 20}}

    Returns:
    list: List of matching student documents
    """
    results = students.find(filter_query)
    return list(results)


# ------------------ UPDATE ------------------
def update_student(student_id, update_data):
    """
    Update a student record by _id.

    Parameters:
    student_id (str): Student ID (ObjectId as string)
    update_data (dict): Fields to update, supports nested updates

    Returns:
    int: Number of documents modified
    """
    result = students.update_one(
        {"_id": ObjectId(student_id)},
        {"$set": update_data}
    )
    return result.modified_count


# ------------------ DELETE ------------------
def delete_student(student_id):
    """
    Delete a student record by _id.

    Parameters:
    student_id (str): Student ID (ObjectId as string)

    Returns:
    int: Number of documents deleted
    """
    result = students.delete_one({"_id": ObjectId(student_id)})
    return result.deleted_count


# ------------------ INDEXING ------------------
def create_indexes():
    """
    Create indexes on frequently queried fields for faster retrieval.
    """
    students.create_index("name")           # Simple field
    students.create_index("age")            # Simple field
    students.create_index([("course.name", 1)])  # Nested field – Atlas friendly
    print("Indexes created successfully!")

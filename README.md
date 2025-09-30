# Student Database Management (MongoDB)

## Description
A backend application to manage student records using MongoDB.  
Supports **CRUD operations**, **advanced query filtering**, **optimized schema**, and **indexing for faster retrieval**.  
Designed with a focus on flexibility and NoSQL document structure.  

## Features
- **CRUD Operations**: Create, Read, Update, Delete student records  
- **Advanced Queries / Filtering**:
  - Filter by age (`$gt`, `$in`)  
  - Search by course name using regex  
  - Combine multiple query operators  
- **Optimized Schema**:
  - Flexible document structure for storing courses, enrollment date, and status  
  - Supports scalability for large datasets  
- **Indexing**: Ensures faster retrieval for commonly queried fields  
- **Modular Python Code**:
  - `db_config.py` → Database connection setup  
  - `student_ops.py` → CRUD & query functions  
  - `test_student_ops.py` → Demo & testing script  

## Project Structure

STUDENT_DATABASE_MANAGEMENT/
│
├─ src/
│ ├─ db_config.py # MongoDB connection setup
│ ├─ student_ops.py # CRUD & advanced query operations
│ └─ test_student_ops.py # Demo & testing script
│
├─ .env # MongoDB URI and credentials (keep private)
├─ requirements.txt # Python dependencies with versions
└─ README.md # Project description & instructions


## Setup & Installation

1. **Clone the repository**
```bash
git clone git@github.com:vishantrana007/student-database-management.git
cd student-database-management

Create virtual environment and activate -:

# Windows
python -m venv venv
venv\Scripts\activate

# Linux / Mac
python3 -m venv venv
source venv/bin/activate

Install dependencies -:

pip install -r requirements.txt

Add your MongoDB URI in the .env file -:

MONGO_URI="your_mongodb_connection_string"

Run the test/demo script -:

python src/test_student_ops.py

requirements.txt -:

pymongo==4.15.1
python-dotenv==1.1.1

Output Example -:

✅ MongoDB Connection Successful
=== CREATING INDEXES ===
Indexes created successfully!

=== CREATE OPERATION ===
Inserted Student ID: 68dba26fbb4065b757cc045f

=== READ OPERATION ===
All Students:
{'_id': ObjectId('68dba26fbb4065b757cc045f'), 'name': 'Vishant Rana', 'age': 22, 'course': {'name': 'Python Backend', 'duration': '3 months', 'level': 'Beginner'}, 'enrollment_date': '2025-09-30', 'status': 'active'}

Find Student by Name:
{'_id': ObjectId('68dba26fbb4065b757cc045f'), 'name': 'Vishant Rana', 'age': 22, 'course': {'name': 'Python Backend', 'duration': '3 months', 'level': 'Beginner'}, 'enrollment_date': '2025-09-30', 'status': 'active'}

=== ADVANCED QUERIES ===
Students with Age > 20:
{'_id': ObjectId('68dba26fbb4065b757cc045f'), 'name': 'Vishant Rana', 'age': 22, 'course': {'name': 'Python Backend', 'duration': '3 months', 'level': 'Beginner'}, 'enrollment_date': '2025-09-30', 'status': 'active'}

Students enrolled in Python Backend:
{'_id': ObjectId('68dba26fbb4065b757cc045f'), 'name': 'Vishant Rana', 'age': 22, 'course': {'name': 'Python Backend', 'duration': '3 months', 'level': 'Beginner'}, 'enrollment_date': '2025-09-30', 'status': 'active'}

Students with Age 18 or 22:
{'_id': ObjectId('68dba26fbb4065b757cc045f'), 'name': 'Vishant Rana', 'age': 22, 'course': {'name': 'Python Backend', 'duration': '3 months', 'level': 'Beginner'}, 'enrollment_date': '2025-09-30', 'status': 'active'}

=== UPDATE OPERATION ===
Number of records updated: 1

=== DELETE OPERATION ===
Number of records deleted: 1

=== FINAL DATABASE STATE ===
[]

Notes -: .gitignore keeps sensitive files out of GitHub -:

venv/
.env
__pycache__/
.DS_Store
Thumbs.db

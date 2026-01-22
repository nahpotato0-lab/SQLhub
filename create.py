import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sql123",
  database="darsh"
)

mycursor = mydb.cursor()

# Create metadata table - stores all objects (commits, branches, files, etc.)
metadata_query = """CREATE TABLE IF NOT EXISTS metadata (
  hash VARCHAR(64) PRIMARY KEY,
  type VARCHAR(20) NOT NULL,
  data JSON NOT NULL,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
)
"""

# Create data_ledger table - stores file chunks
data_ledger_query = """CREATE TABLE IF NOT EXISTS data_ledger (
  hash VARCHAR(64) PRIMARY KEY,
  chunk_data LONGBLOB NOT NULL,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
)
"""

# Create repositories table
repos_query = """CREATE TABLE IF NOT EXISTS repositories (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL UNIQUE,
  initial_commit_hash VARCHAR(64),
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
)
"""

mycursor.execute(metadata_query)
mycursor.execute(data_ledger_query)
mycursor.execute(repos_query)

mydb.commit()
mycursor.close()
mydb.close()

print("Database schema created successfully!")
print("Tables: metadata, data_ledger, repositories")
print("metadata: Stores commits, branches, file metadata")
print("data_ledger: Stores file chunks with deduplication")
print("repositories: Repository management")

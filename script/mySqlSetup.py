import mysql.connector
# Establish a connection to the MySQL server
conn = mysql.connector.connect(
    host="localhost",  # Replace with your MySQL server host
    user="root",  # Replace with your MySQL username
    password="1234"  # Replace with your MySQL password
)

# Create a new database 
database_name = "OxygenDB"  # Replace with your desired database name
cursor = conn.cursor()
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")

# Switch to the newly created database
cursor.execute(f"USE {database_name}")

# Create a table
table_name = "AC_Event"  # Replace with your desired table name
cursor = conn.cursor()
create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        event VARCHAR(64) NOT NULL,
        temp DECIMAL(6,2) NOT NULL         
    )
"""
cursor.execute(create_table_query)

# Close the cursor
cursor.close()
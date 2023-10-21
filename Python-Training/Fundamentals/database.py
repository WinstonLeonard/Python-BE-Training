# Create an empty list to simulate a "database"
local_database = []

# Create (Insert) Operation
def create_record(name, email):
    # TODO
    # Step 1:Create a dictionary entry representing a record with 'name' and 'email'
    thisdict = {
        "name": name,
        "email": email
    }

    # Step 2: Add the record to the local database list
    local_database.append(thisdict)
    

# Read Operation
def read_records():
    # TODO
    # Step 1: Return the entire local database list
    for x in local_database:
        print(x)
    

# Update Operation
def update_record(record_index, name, email):
    # TODO
    # Step 1: Check if the provided index is valid
    # Step 2: Update the record at the specified index with the new 'name' and 'email'
    length = len(local_database)
    if (record_index < length):
        newEntry = {
            "name": name,
            "email": email
        }
        local_database[record_index] =  newEntry
    
    

# Delete Operation
def delete_record(record_index):
    # TODO
    # Step 1: Check if the provided index is valid
        
    # Step 2: Delete the record at the specified index
    length = len(local_database)
    if (record_index < length):
        del local_database[record_index]

# Test Code
# Create records
create_record('John Doe', 'john@example.com')
create_record('Jane Smith', 'jane@example.com')

# Read records
records = read_records()
print("Records:")
for idx, record in enumerate(records):
    # Print the index, 'name', and 'email' for each record
    print(f"Index: {idx}, Name: {record['name']}, Email: {record['email']}")

# Update a record
update_record(0, 'Updated John', 'updatedjohn@example.com')

# Read records again
records = read_records()
print("Updated Records:")
for idx, record in enumerate(records):
    # Print the index, 'name', and 'email' for each record
    print(f"Index: {idx}, Name: {record['name']}, Email: {record['email']}")

# Delete a record
delete_record(1)

# Read records after deletion
records = read_records()
print("Records after deletion:")
for idx, record in enumerate(records):
    # Print the index, 'name', and 'email' for each record
    print(f"Index: {idx}, Name: {record['name']}, Email: {record['email']}")

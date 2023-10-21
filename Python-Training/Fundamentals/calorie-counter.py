# Create a dictionary to store user-specific calorie databases
user_calorie_databases = {}

# Create (Insert) Operation for a specific user
def create_calorie_entry(username, food, calories):
    # TODO
    # Step 1: Create a dictionary representing a calorie entry with 'food' and 'calories'
    
    # Step 2: Check if the user exists in the dictionary, and create a database if not
    
    # Step 3: Append the entry to the user's calorie database

# Read Operation for a specific user
def read_calorie_entries(username):
    # TODO
    # Step 1: Return the list of calorie entries for the specific user
    # Return an empty list if the user does not exist
    

# Update Operation for a specific user
def update_calorie_entry(username, entry_index, food, calories):
    # TODO
    # Step 1: Check if the user exists and if the provided index is valid

    # Step 2: Update the calorie entry at the specified index with the new 'food' and 'calories'


# Delete Operation for a specific user
def delete_calorie_entry(username, entry_index):
    # TODO
    # Step 1: Check if the user exists and if the provided index is valid

    # Step 2: Delete the calorie entry at the specified index


# Search Operation for a specific user
def search_calorie_entries(username, search_term):
    # TODO
    # Step 1: Check if the user exists

    # Step 2: Search for calorie entries containing the given search term in the 'food' field
    # Return an empty list for a user that doesn't exist
    

# Get a Single Entry for a specific user
def get_calorie_entry(username, entry_index):
    # TODO
    # Step 1: Check if the user exists and if the provided index is valid

    # Step 2: Retrieve and return the calorie entry at the specified index
    # Return None for an invalid username or index
    

# Clear All Entries for a specific user
def clear_calorie_entries(username):
    # TODO
    # Step 1: Check if the user exists
    # Step 2: Clear (empty) the entire calorie database for the specific user
    


# Test Code
# Create calorie entries for user 'Alice'
create_calorie_entry('Alice', 'Breakfast', 350)
create_calorie_entry('Alice', 'Lunch', 600)
create_calorie_entry('Alice', 'Dinner', 450)

# Create calorie entries for user 'Bob'
create_calorie_entry('Bob', 'Breakfast', 400)
create_calorie_entry('Bob', 'Lunch', 750)

# Read entries for 'Alice'
alice_entries = read_calorie_entries('Alice')
print("Calorie Entries for Alice:")
for idx, entry in enumerate(alice_entries):
    print(f"Index: {idx}, Food: {entry['food']}, Calories: {entry['calories']}")

# Read entries for 'Bob'
bob_entries = read_calorie_entries('Bob')
print("Calorie Entries for Bob:")
for idx, entry in enumerate(bob_entries):
    print(f"Index: {idx}, Food: {entry['food']}, Calories: {entry['calories']}")

# Update an entry for 'Alice'
update_calorie_entry('Alice', 1, 'Updated Lunch', 700)

# Read entries for 'Alice' again
alice_entries = read_calorie_entries('Alice')
print("Updated Entries for Alice:")
for idx, entry in enumerate(alice_entries):
    print(f"Index: {idx}, Food: {entry['food']}, Calories: {entry['calories']}")

# Delete an entry for 'Bob'
delete_calorie_entry('Bob', 0)

# Read entries for 'Bob' after deletion
bob_entries = read_calorie_entries('Bob')
print("Entries for Bob after Deletion:")
for idx, entry in enumerate(bob_entries):
    print(f"Index: {idx}, Food: {entry['food']}, Calories: {entry['calories']}")

# Search for entries for 'Alice'
search_results = search_calorie_entries('Alice', 'Lunch')
print("Search Results for Alice:")
for idx, entry in enumerate(search_results):
    print(f"Index: {idx}, Food: {entry['food']}, Calories: {entry['calories']}")

# Get a single entry for 'Bob'
single_entry = get_calorie_entry('Bob', 0)
if single_entry:
    print("Single Entry for Bob:")
    print(f"Food: {single_entry['food']}, Calories: {single_entry['calories']}")
else:
    print("Entry not found for Bob.")

# Clear all entries for 'Alice'
clear_calorie_entries('Alice')
print("Calorie Entries for Alice cleared.")

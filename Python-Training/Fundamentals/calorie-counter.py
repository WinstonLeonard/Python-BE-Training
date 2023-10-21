# Create a dictionary to store user-specific calorie databases
user_calorie_databases = {}

# Create (Insert) Operation for a specific user
def create_calorie_entry(username, food, calories):
    # TODO
    # Step 1: Create a dictionary representing a calorie entry with 'food' and 'calories'
    calorieEntry = {"food": food,
                    "calories": calories}

    # Step 2: Check if the user exists in the dictionary, and create a database if not
    if username in user_calorie_databases:
        user_calorie_databases[username].append(calorieEntry)
    else:
        user_calorie_databases[username] = [calorieEntry]

    # Step 3: Append the entry to the user's calorie database

# Read Operation for a specific user
def read_calorie_entries(username):
    # TODO
    # Step 1: Return the list of calorie entries for the specific user
    # Return an empty list if the user does not exist
    if username in user_calorie_databases:
        return (user_calorie_databases[username])
    else:
        return []
    

# Update Operation for a specific user
def update_calorie_entry(username, entry_index, food, calories):
    # TODO
    # Step 1: Check if the user exists and if the provided index is valid
    if username in user_calorie_databases:
        userArray = user_calorie_databases[username]
        arrayLength = len(userArray)
        if(entry_index < arrayLength):
            userArray[entry_index] = {"food": food, "calories": calories}

    # Step 2: Update the calorie entry at the specified index with the new 'food' and 'calories'


# Delete Operation for a specific user
def delete_calorie_entry(username, entry_index):
    # TODO
    # Step 1: Check if the user exists and if the provided index is valid
        if username in user_calorie_databases:
            userArray = user_calorie_databases[username]
            arrayLength = len(userArray)
            if(entry_index < arrayLength):
                userArray.pop(entry_index)

    # Step 2: Delete the calorie entry at the specified index


# Search Operation for a specific user
def search_calorie_entries(username, search_term):
    # TODO
    # Step 1: Check if the user exists
    result = []
    
    # Step 2: Search for calorie entries containing the given search term in the 'food' field
    # Return an empty list for a user that doesn't exist
    if username in user_calorie_databases:
        userArray = user_calorie_databases[username]
        for entry in userArray:
            if entry['food'] == search_term:
                result.append(entry)
    return result

# Get a Single Entry for a specific user
def get_calorie_entry(username, entry_index):
    # TODO
    # Step 1: Check if the user exists and if the provided index is valid
    if username in user_calorie_databases:
        userArray = user_calorie_databases[username]
        arrayLength = len(userArray)
        if (entry_index < arrayLength):
            return userArray[entry_index]

    # Step 2: Retrieve and return the calorie entry at the specified index
    # Return None for an invalid username or index
    

# Clear All Entries for a specific user
def clear_calorie_entries(username):
    # TODO
    # Step 1: Check if the user exists
    # Step 2: Clear (empty) the entire calorie database for the specific user
    if username in user_calorie_databases:
        del user_calorie_databases[username]
    


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

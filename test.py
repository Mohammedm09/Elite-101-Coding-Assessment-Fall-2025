data = [
    {"name": "Item A", "is_active": True},
    {"name": "Item B", "is_active": False},
    {"name": "Item C", "is_active": True},
    {"name": "Item D", "is_active": False},
]

# The variable to compare against
target_status = True

# Iterate through the list of dictionaries
for item in data:
    # Access the boolean value within the current dictionary
    current_status = item["is_active"]

    # Compare the current boolean value with the target variable
    if current_status == target_status:
        print(f"'{item['name']}' has a matching status: {current_status}")
    else:
        print(f"'{item['name']}' has a non-matching status: {current_status}")
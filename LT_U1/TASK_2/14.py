# 14. Nested Dictionary of Employee Performance Ratings
employees = {
    "E101": {
        "Work Quality": 9,
        "Attendance": 8,
        "Punctuality": 7
    },
    "E102": {
        "Work Quality": 7,
        "Attendance": 9,
        "Punctuality": 8
    }
}

# Print specific field
print("E102's Punctuality Rating:", employees["E102"]["Punctuality"])

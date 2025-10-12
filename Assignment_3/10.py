import pandas as pd

employees = pd.DataFrame({
    'Full Name': ['Alice Johnson', 'Bob Smith', None, 'Charlie Brown'],
    'Email': ['alice@abc.com', 'bob@xyz.com', 'invalid_email', 'charlie@abc.com']
})

employees['Full Name'] = employees['Full Name'].fillna('Unknown')

employees[['First Name', 'Last Name']] = employees['Full Name'].str.split(' ', n=1, expand=True)

employees['Email'] = employees['Email'].apply(lambda x: x if '@' in x else 'Unknown')

print("Cleaned Employee Data:\n", employees)
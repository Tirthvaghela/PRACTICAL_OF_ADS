import pandas as pd

hospital = pd.DataFrame({
    'Patient': ['A', 'B', 'C', 'D'],
    'Age': [30, -1, 0, 40],
    'Gender': ['M', 'F', None, 'M']
})

valid_mean = hospital.loc[hospital['Age'] > 0, 'Age'].mean()
hospital['Age'] = hospital['Age'].apply(lambda x: valid_mean if x <= 0 else x)
hospital['Gender'] = hospital['Gender'].fillna('Unknown')

print("Cleaned Hospital Data:\n", hospital)

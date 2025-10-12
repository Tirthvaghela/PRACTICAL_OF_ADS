# 7. Country population:
# {'India':1400,'USA':331,'Nepal':29,'Bhutan':0.8} (in millions)
# Display countries with pop <50 million.

import pandas as pd


country_population = {'India':1400, 'USA':331, 'Nepal':29, 'Bhutan':0.8}

df = pd.DataFrame(list(country_population.items()), columns=['Country', 'Population'])

filtered = df[df['Population'] < 50]

for country in filtered['Country']:
    print(country)
    print("=====================================================")

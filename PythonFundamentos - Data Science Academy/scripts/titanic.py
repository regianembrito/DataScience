import pandas as pd

titanic = pd.read_csv('arquivos/titanic.csv')
print(titanic.head())

# What is the average age of the titanic passengers?
print("Average Age: ", int(titanic["Age"].mean()))

# What is the median age and ticket fare price of the titanic passengers?
print("Median", titanic[["Age", "Fare"]].median())

print(titanic[["Age", "Fare"]].describe())

print("Agg\n", titanic.agg({'Age': ['min', 'max', 'median', 'skew'],
                   'Fare': ['min', 'max', 'median', 'mean']}))


#print("Survived", titanic["Survived"].count())
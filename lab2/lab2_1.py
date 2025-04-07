import pandas as pd
from google.colab import files

uploaded = files.upload()

for filename in uploaded.keys():
    data = pd.read_csv(filename)

print('вывод нескольких строк')
print(data.head(5))
print(data.info())

nan_chek= data.isna()
print("Проверка на наличие NaN:")
print(nan_chek)

data_filled=data.fillna(0)
print("DataFrame с заполненными NaN нулями:")
print(data_filled.head())

data_droped=data.dropna()
print("none удален")
print(data_droped.head())

select_column = data['Sex']
print('столбец с полом')
print(select_column)

select_columns = data[['Sex', 'Age']]
print('столбецы с полом и возрастом')
print(select_columns)

row_index=data.loc[1]
print('строка с индексом 1:')
print(row_index)

mans = data[(data['Age'] > 30) & (data['Sex'] == 'male')]
print('мужики старше 30')
print(mans)

sort_column=data.sort_values('Age')
print('возраст по возрастанию')
print(sort_column)

survival_rate = data.groupby('Pclass')['Survived'].mean()
print("Доля выживших")
print(survival_rate)

#------------------------------------

data_new=data.fillna(0)
print("вывод первых 10 строк")
print(data.head(10))
mans = data[data['Age'] > 30]
print('люди Старше 30')
print(mans)
sort_new=data.sort_values('Fare', ascending=False)
print("сортировка по fare по убыванию ")
print(sort_new)

average_age_by_class = data.groupby('Pclass')['Age'].mean()
print("Средний возраст по классам:")
print(average_age_by_class)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
dataFrame = pd.read_csv('lab5_dop_data.csv', sep=';') # считывание данных
dataFrame = dataFrame.drop(['<TICKER>', '<PER>', '<TIME>', '<VOL>'], axis=1) # удаление ненужных столбцов
pd.to_numeric(dataFrame['<OPEN>'])
pd.to_numeric(dataFrame['<HIGH>'])
pd.to_numeric(dataFrame['<LOW>'])
pd.to_numeric(dataFrame['<CLOSE>'])
# преобразование данных в стобцы
dataFrame = pd.melt(dataFrame, id_vars=['<DATE>'], value_vars=['<OPEN>', '<HIGH>', '<LOW>', '<CLOSE>'])
# print(dataFrame)
# построение box plot
sns.boxplot(x='<DATE>',  y='value', data=dataFrame, palette='dark:tomato', hue='variable')
plt.legend()
plt.show()
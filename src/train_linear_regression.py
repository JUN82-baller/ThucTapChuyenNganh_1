import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

#2 doc du lieu tu file
df = pd.read_csv('data/earthquake_data_tsunami.csv')

#3 chon cac cot can thiet va loai bo gia tri null
df = df.dropna(subset=['magnitude', 'latitude', 'longitude', 'Year','Month','tsunami'])

#4 chon dau vao X and dau ra (y)
x=df[['latitude','longitude','Year','Month','tsunami']]
y=df['magnitude']

#5 chia du lieu thanh tap train va test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#6 khoi tao mo hinh tuyen tinh
model =LinearRegression()
model.fit(x_train,y_train)

#7 du doan tren tap test
y_pred = model.predict(x_test)

#8 danh gia mo hinh
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: (MSE) : {mse:.2f}')
print(f'R-squared: {r2:.2f}')

#9 Du doan thu 1 tran dong dat gia dinh
sample = pd.DataFrame([[10.5, 20.3, 2022, 5, 1]], columns=x.columns)
prediction = model.predict(sample)
print(f'Du doan do lon dong dat:{prediction}')
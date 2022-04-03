### Работа с данными Pandas
import pandas as pd
import numpy as np

### задание 1

authors = pd.DataFrame({'author_id':[1, 2, 3],'author_name':['Тургенев','Чехов', 'Островский']})

print(authors)

book = pd.DataFrame({'author_id':[1, 1, 1, 2, 2, 3, 3],'book_title':['Отцы и дети', 'Рудин', 'Дворянское гнездо','Тостый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'], 'price':[450, 300, 350, 500, 450, 370, 290]})
book.set_index('author_id', inplace = True)
print(book)

### задание 2

authors_price = pd.merge(authors, book, on= 'author_id', how='inner')
authors_price.set_index('author_id', inplace = True)
print(authors_price)

### задание 3

top5 = authors_price.nlargest(5,'price')
print(top5)

### задание 4

min_price_df = authors_price.groupby('author_name').agg({'price': 'min'})
min_price_df = min_price_df.rename(columns={'price':'min_price'})
print(min_price_df)

max_price_df = authors_price.groupby('author_name').agg({'price': 'max'})
max_price_df = max_price_df.rename(columns={'price':'max_price'})
print(max_price_df)

mean_price_df = authors_price.groupby('author_name').agg({'price': 'mean'})
mean_price_df = mean_price_df.rename(columns={'price':'mean_price'})
print(mean_price_df)

authors_stat_temp = pd.merge(min_price_df, max_price_df, on= 'author_name', how='inner')
print(authors_stat_temp)

authors_stat = pd.merge(authors_stat_temp, mean_price_df, on= 'author_name', how='inner')
print(authors_stat)

### задание 5

cover = ['твердая','мягкая','мягкая','твердая','твердая','мягкая','мягкая']
authors_price['cover'] = cover
print(authors_price)
book_info = pd.pivot_table(authors_price, index="author_name", columns = "cover", aggfunc = np.sum, fill_value = 0)
print(book_info)
book_info.to_pickle('book_info.pkl')
book_info2 = pd.read_pickle('book_info.pkl')
print(book_info2)

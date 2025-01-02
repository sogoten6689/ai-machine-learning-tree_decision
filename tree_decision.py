# levels = [
#     {"nhe": 1, "nang": 5},
#     {"thap": 2, "trung binh": 3, "cao": 4},
#     {"it": 6, "nhieu": 7}
# ]

# b1: thu thap du lieu
# b2: xử lý dữ liệu
# b3: trainning model
# b4: dự đoán
# b5: validation

from sklearn import tree

my_tree = tree.DecisionTreeClassifier()


dactrung = [
    [1, 3, 3, 7],
    [5, 2, 4, 6],
    [1, 2, 4, 6],
    [5, 4, 4, 3],
    [1, 4, 4, 7],
    [1, 2, 3, 7],
    [3, 3, 3, 6],
    [5, 2, 2, 7],
    ]

nhan = [0, 1, 1, 0, 0, 0, 0, 1]

my_tree.fit(dactrung, nhan)

kq = my_tree.predict([[1, 4, 3, 6]])
kq2 = my_tree.predict([[1, 4, 3, 7]])

print(kq)
print(kq2)
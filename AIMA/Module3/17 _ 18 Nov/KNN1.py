from sklearn import neighbors

knn = neighbors.KNeighborsClassifier(n_neighbors=2)
print(knn)

knn.fit([[1], [2], [3], [4], [5], [6]], [0, 0, 0, 1, 1, 1])
pr1 = knn.predict(5.5)
print(pr1)
print("prob in class 0  and prob in class 1")
pr2 = knn.predict_proba(1.5)
print(pr2)
pr3 = knn.predict_proba(37)
print(pr3)
pr4 = knn.predict_proba(3.5)
print(pr4)

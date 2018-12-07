from sklearn.preprocessing import Binarizer

X = [[1., -1., 2.],
     [2., 0., 0.],
     [0., 1., -1.]]

binarizer = Binarizer().fit(X)  # fit does nothing
print(binarizer)
print(binarizer.transform(X))
X = [[1., 5., 2.],
     [2., 0., 6.],
     [0., 1., 1.]]
print('---------------------')
binarizer = Binarizer(threshold=3)
print(binarizer.transform(X))

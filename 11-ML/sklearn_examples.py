from sklearn import datasets
from sklearn import svm

iris = datasets.load_iris()
print(iris)

# from the svm module
# use SVC (Support Vector Classification)
classifier = svm.SVC()

# Use data and expected result to
# teach the classifier
classifier.fit(iris.data, iris.target)

import pickle

# Save the classifier:
file = open("iris.pkl", "bw")
pickle.dump(classifier, file)

# load the classifier:
file = open("iris.pkl", "br")
iris_classifier = pickle.load(file)

new_data = [[5.1, 3.5, 1.4, 0.2],  # 0
            [4.9, 3.0, 1.4, 0.2],  # 0
            [6.1, 2.6, 5.6, 1.4],  # 2
            [7.7, 3., 6.1, 2.3],  # 2
            [6.1, 3., 4.6, 1.4]  # 1
            ]

print(iris_classifier.predict(new_data))

from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the Iris dataset

iris = load_iris()
X=iris.data  # Features (sepal length, sepal width, petal length, petal width)
y=iris.target  # Target labels (species: Setosa, Versicolor, Virginica)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# Initialize the Decision Tree model with hyperparameters
model = DecisionTreeClassifier(
    criterion='entropy', # Split using Information Gain
    max_depth=4,         # Limit the depth of the tree to prevent overfitting
    min_samples_split=4, # Minimum samples required to split a node
    min_samples_leaf=2,  # Minimum samples required to be at a leaf node
    max_features='sqrt', # Consider at most sqrt(number of features) for each split
    random_state=42      # Set the random state for reproducibility
)

# Train the model on the training data
model.fit(X_train,y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

# Plot the decision tree
plt.figure(figsize=(12,8))
plot_tree(model,filled=True,feature_names=iris.feature_names,
          class_names=iris.target_names, rounded=True)
plt.show()

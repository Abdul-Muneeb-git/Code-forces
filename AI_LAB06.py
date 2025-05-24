import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Generate synthetic binary classification data
X, y = make_classification(n_samples=500, n_features=2, n_redundant=0, 
                           n_clusters_per_class=1, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 1. Data Preprocessing
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Plot the data points
plt.figure(figsize=(8, 6))
plt.scatter(X_train[y_train == 0, 0], X_train[y_train == 0, 1], color='blue', label='Class 0')
plt.scatter(X_train[y_train == 1, 0], X_train[y_train == 1, 1], color='red', label='Class 1')
plt.title("Data Distribution Before Training")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.grid(True)
plt.show()

# 2. Logistic Regression Implementation
def sigmoid(z):
    """Compute the sigmoid of z."""
    return 1 / (1 + np.exp(-z))

def cross_entropy_loss(y_true, y_pred):
    """Compute binary cross-entropy loss."""
    epsilon = 1e-15  # To avoid log(0)
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
    return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

def gradient_descent(X, y, weights, learning_rate, iterations):
    """Perform gradient descent to optimize weights."""
    m = len(y)
    loss_history = []
    
    for _ in range(iterations):
        # Calculate predictions
        z = np.dot(X, weights)
        y_pred = sigmoid(z)
        
        # Calculate gradient
        gradient = np.dot(X.T, (y_pred - y)) / m
        
        # Update weights
        weights -= learning_rate * gradient
        
        # Calculate and store loss
        loss = cross_entropy_loss(y, y_pred)
        loss_history.append(loss)
        
    return weights, loss_history

def predict(X, weights):
    """Predict using sigmoid function."""
    return np.round(sigmoid(np.dot(X, weights)))

def logistic_regression(X, y, learning_rate=0.01, iterations=1000):
    """Fit logistic regression model."""
    # Add intercept term (column of 1s)
    X = np.c_[np.ones((X.shape[0], 1)), X]
    
    # Initialize weights
    weights = np.zeros(X.shape[1])
    
    # Run gradient descent
    weights, loss_history = gradient_descent(X, y, weights, learning_rate, iterations)
    
    return weights, loss_history

def evaluate(y_true, y_pred):
    """Evaluate the model's accuracy."""
    return np.mean(y_true == y_pred)

# 3. Model Training
learning_rates = [0.001, 0.01, 0.1]
iterations = 1000

plt.figure(figsize=(12, 8))

for lr in learning_rates:
    weights, loss_history = logistic_regression(X_train, y_train, learning_rate=lr, iterations=iterations)
    
    # Plot loss curves
    plt.plot(loss_history, label=f"LR={lr}")

plt.title("Loss Convergence with Different Learning Rates")
plt.xlabel("Iterations")
plt.ylabel("Loss")
plt.legend()
plt.grid(True)
plt.show()

# Train with best learning rate
best_lr = 0.1
weights, _ = logistic_regression(X_train, y_train, learning_rate=best_lr, iterations=iterations)

# 4. Model Evaluation
# Add intercept term to test data
X_test_with_intercept = np.c_[np.ones((X_test.shape[0], 1)), X_test]
y_pred = predict(X_test_with_intercept, weights)

accuracy = evaluate(y_test, y_pred)
print(f"Test Accuracy: {accuracy:.4f}")

# 5. Decision Boundary Visualization
def plot_decision_boundary(X, y, weights):
    """Visualize the decision boundary."""
    # Create a mesh grid
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                         np.linspace(y_min, y_max, 100))
    
    # Predict for each point in the grid
    Z = predict(np.c_[np.ones(xx.ravel().shape[0]), xx.ravel(), yy.ravel()], weights)
    Z = Z.reshape(xx.shape)
    
    # Plot
    plt.figure(figsize=(8, 6))
    plt.contourf(xx, yy, Z, alpha=0.4)
    plt.scatter(X[:, 0], X[:, 1], c=y, s=20, edgecolor='k')
    plt.title("Decision Boundary Visualization")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.show()

plot_decision_boundary(X_train, y_train, weights)
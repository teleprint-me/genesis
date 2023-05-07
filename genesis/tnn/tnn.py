# Tiny Neural Network
# genesis/tnn/tnn.py
import numpy as np

np.random.seed(0)


# Activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# Derivative of the activation function
def sigmoid_derivative(x):
    return x * (1 - x)


# Define dimensions
input_dim = 2
hidden_dim = 2
output_dim = 1

# Initialize weights and biases
W1 = np.random.randn(input_dim, hidden_dim)
b1 = np.zeros((1, hidden_dim))
W2 = np.random.randn(hidden_dim, output_dim)
b2 = np.zeros((1, output_dim))

# Define input data and labels
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Training parameters
epochs = 10000
learning_rate = 0.1

# Training loop
for epoch in range(epochs):
    # Forward pass
    layer1 = sigmoid(np.dot(X, W1) + b1)
    layer2 = sigmoid(np.dot(layer1, W2) + b2)

    # Compute the error
    error = y - layer2

    # Backward pass
    delta2 = error * sigmoid_derivative(layer2)
    delta1 = np.dot(delta2, W2.T) * sigmoid_derivative(layer1)

    # Update weights and biases
    W2 += learning_rate * np.dot(layer1.T, delta2)
    b2 += learning_rate * np.sum(delta2, axis=0, keepdims=True)
    W1 += learning_rate * np.dot(X.T, delta1)
    b1 += learning_rate * np.sum(delta1, axis=0, keepdims=True)

# Test the trained model
test_input = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
layer1 = sigmoid(np.dot(test_input, W1) + b1)
layer2 = sigmoid(np.dot(layer1, W2) + b2)

print("Output after training:")
print(layer2)

# Save model weights and biases
np.save("model_weights.npy", [W1, b1, W2, b2])


# Load model and perform inference
def load_and_inference(test_input, model_path):
    W1, b1, W2, b2 = np.load(model_path, allow_pickle=True)
    layer1 = sigmoid(np.dot(test_input, W1) + b1)
    layer2 = sigmoid(np.dot(layer1, W2) + b2)
    return layer2


# Test the loaded model
test_input = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
output = load_and_inference(test_input, "model_weights.npy")
print("Output after loading the model:")
print(output)

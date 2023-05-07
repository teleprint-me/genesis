import numpy as np


class TinyNeuralNetwork:
    def __init__(self, input_dim, hidden_dim, output_dim):
        np.random.seed(0)
        self.W1 = np.random.randn(input_dim, hidden_dim)
        self.b1 = np.zeros((1, hidden_dim))
        self.W2 = np.random.randn(hidden_dim, output_dim)
        self.b2 = np.zeros((1, output_dim))

    @staticmethod
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    @staticmethod
    def sigmoid_derivative(x):
        return x * (1 - x)

    def train(self, X, y, epochs=10000, learning_rate=0.1):
        for epoch in range(epochs):
            layer1 = self.sigmoid(np.dot(X, self.W1) + self.b1)
            layer2 = self.sigmoid(np.dot(layer1, self.W2) + self.b2)

            error = y - layer2

            delta2 = error * self.sigmoid_derivative(layer2)
            delta1 = np.dot(delta2, self.W2.T) * self.sigmoid_derivative(layer1)

            self.W2 += learning_rate * np.dot(layer1.T, delta2)
            self.b2 += learning_rate * np.sum(delta2, axis=0, keepdims=True)
            self.W1 += learning_rate * np.dot(X.T, delta1)
            self.b1 += learning_rate * np.sum(delta1, axis=0, keepdims=True)

    def predict(self, test_input):
        layer1 = self.sigmoid(np.dot(test_input, self.W1) + self.b1)
        layer2 = self.sigmoid(np.dot(layer1, self.W2) + self.b2)
        return layer2

    def save_model(self, model_path):
        np.save(model_path, [self.W1, self.b1, self.W2, self.b2])

    def load_model(self, model_path):
        self.W1, self.b1, self.W2, self.b2 = np.load(model_path, allow_pickle=True)


# Define input data and labels
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Initialize and train the network
tnn = TinyNeuralNetwork(input_dim=2, hidden_dim=2, output_dim=1)
tnn.train(X, y)

# Test the trained model
test_input = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
output = tnn.predict(test_input)
print("Output after training:")
print(output)

# Save and load the model
tnn.save_model("model_weights.npy")
tnn.load_model("model_weights.npy")

# Test the loaded model
test_input = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
output = tnn.predict(test_input)
print("Output after loading the model:")
print(output)

# Digit Recognition with Neural Network (NumPy and Pandas)

## Overview
This project implements a simple neural network for digit recognition using only NumPy and Pandas. The neural network architecture consists of three layers: two hidden layers with 16 nodes each and an output layer with 10 nodes corresponding to the digits 0-9.

## Features
- **Neural Network Architecture:**
  - Input Layer: 784 nodes (28x28 pixels for each digit image)
  - Hidden Layer 1: 16 nodes
  - Hidden Layer 2: 16 nodes
  - Output Layer: 10 nodes (0-9 digits)

- **Activation Function:**
  - Rectified Linear Unit (ReLU) for hidden layers
  - Softmax for the output layer

- **Training Data:**
  - MNIST dataset used for training and testing
  - The data used was the data provided for the [Kaggle Digit Recognizer Task](https://www.kaggle.com/competitions/digit-recognizer/overview)
  - I downloaded the training data and split it into training and testing sets.
  - 20% for the testing set and 80% for the training set.

- **Dependencies:**
  - NumPy for numerical operations
  - Pandas for data manipulation

## Results
- **Training Accuracy:** [90%]
- **Testing Accuracy:** [89%]


## Acknowledgments
- The MNIST dataset is used for training and testing, and it can be found [here](https://www.kaggle.com/competitions/digit-recognizer/data).

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

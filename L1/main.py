import numpy as np
import pandas as pd

input_dim = 3
learning_rate = 0.01
Weights = np.random.rand(input_dim)
Weights[0] = 0.5
Weights[1] = 0.5
Weights[2] = 0.5

Training_Data = pd.read_csv("SET_ANTRENARE.csv")
print(Training_Data)
Expected_Output = Training_Data.output
Training_Data = Training_Data.drop(["output"], axis=1)
Training_Data = np.asarray(Training_Data)

training_count = len(Training_Data[:,0])

def sigmoid(x):
  return 1/(1 + np.exp(-x))

def relu(x):
  return np.maximum(0, x)

for epoch in range(0, 5):
  for datum in range(0, training_count):
    output_sum = np.sum(np.multiply(Training_Data[datum,:], Weights))
    output_value = relu(output_sum)
    error = Expected_Output[datum] - output_value
    for n in range(0, input_dim):
      Weights[n] = Weights[n] + learning_rate * error * Training_Data[datum,n]

print("w_0 = %.3f", Weights[0])
print("w_1 = %.3f", Weights[1])
print("w_2 = %.3f", Weights[2])

def aplicatie(d_intrare):
  element = 0
  for i in range(0, input_dim):
    element = element + d_intrare[i] * Weights[i]
    iesire = relu(element)
    print("Pentru intrarea ", d_intrare, ", iesirea este ", iesire)

intrare1 = [2, -5, 8]
intrare2 = [-3, 4, -2]
aplicatie(intrare1)
aplicatie(intrare2)
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd

import alegrete


dataset = pd.read_csv('alegrete.csv', names=['Land area (ha)', 'Price (R$ 1.000)'])


#Gráfico dos dados
plt.figure(figsize=(6, 2))
plt.scatter(dataset['Land area (ha)'], dataset['Price (R$ 1.000)'])
plt.xlabel('Land area (ha)')
plt.ylabel('Price (R$ 1.000)')
plt.title('Dados Alegrete')
plt.show()

print(alegrete.compute_mse(0, 1, dataset))

b_history, w_history = alegrete.fit(
    dataset, b=0, w=0,
    alpha=0.0001, num_iterations=100
)
print(b_history)
print(w_history)
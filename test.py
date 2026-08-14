print("We have one more hour")

import matplotlib.pyplot as plt

data = [12, 7, 22, 16, 15, 13, 17, 9, 18, 10, 7, 12, 19, 21, 13, 14]

plt.hist(data, bins=5, edgecolor='black')
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
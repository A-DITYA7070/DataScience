import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

# df = sns.load_dataset('tips')
# # print(df.head())

# # sns.histplot(x=df["total_bill"])

# mean = np.mean(df['total_bill'])
# print("mean",mean)

# median = np.median(df['total_bill'])
# print("median",median)

# mode = stats.mode(df["total_bill"])
# print("mode",mode.mode)

# plt.figure(figsize=(10, 6))

# plt.scatter(mean, median, color='red', label=f'Mean: {mean:.2f}, Median: {median:.2f}')

# sns.histplot(x=df["total_bill"], kde=True)

# plt.annotate(f'Mean: {mean:.2f}', (mean, median), textcoords="offset points", xytext=(0,10), ha='center', color='red')
# plt.annotate(f'Median: {median:.2f}', (mean, median), textcoords="offset points", xytext=(0,-15), ha='center', color='red')

# plt.xlabel('Total Bill')
# plt.ylabel('Frequency')
# plt.title('Distribution of Total Bill with Mean and Median')
# plt.legend()

# plt.show()


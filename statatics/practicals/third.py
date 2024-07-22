import seaborn as sns


df = sns.load_dataset('healthexp')
# print(df.head())

df1 = df.select_dtypes(include=[float, int])
print(df1.cov())

print(df1.corr(method='pearson'))

print(df1.corr(method='kendall'))

print(df1.corr(method='spearman'))
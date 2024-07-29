# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Load the JSON file into a DataFrame
# csv = pd.read_json("json.json")
# findings = pd.json_normalize(csv['findings'])

# # Print column names to debug
# print("Columns in findings DataFrame:", findings.columns)

# # Extract the relevant columns
# names = findings['name']
# cweId = findings['cweId']
# risk_severity = findings['risk.severity']

# # Create a DataFrame for plotting
# plot_data = pd.DataFrame({
#     'name': names,
#     'cweId': cweId,
#     'risk_severity': risk_severity
# })

# # Plot the data
# plt.figure(figsize=(12, 8))
# sns.scatterplot(data=plot_data, x='name', y='cweId', hue='risk_severity', palette='viridis')

# plt.xticks(rotation=90)
# plt.xlabel('Finding Name')
# plt.ylabel('CWE ID')
# plt.title('Scatter Plot of Findings by Name, CWE ID, and Risk Severity')
# plt.legend(title='Risk Severity')
# plt.show()

# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Load the JSON file into a DataFrame
# csv = pd.read_json("json.json")
# findings = pd.json_normalize(csv['findings'])

# # Print column names to debug
# print("Columns in findings DataFrame:", findings.columns)

# # Extract the relevant columns
# risk_severity = findings['risk.severity']
# names = findings['name']

# # Create a DataFrame for plotting
# plot_data = pd.DataFrame({
#     'name': names,
#     'risk_severity': risk_severity
# })

# # Count the number of findings by risk severity
# risk_count = plot_data['risk_severity'].value_counts().reset_index()
# risk_count.columns = ['risk_severity', 'count']

# # Plot the data
# plt.figure(figsize=(10, 6))
# sns.barplot(data=risk_count, x='risk_severity', y='count', palette='viridis')

# plt.xlabel('Risk Severity')
# plt.ylabel('Number of Findings')
# plt.title('Count of Findings by Risk Severity')
# plt.xticks(rotation=45)
# plt.show()


# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Load the JSON file into a DataFrame
# csv = pd.read_json("json.json")
# findings = pd.json_normalize(csv['findings'])

# # Print column names to debug
# print("Columns in findings DataFrame:", findings.columns)

# # Extract the relevant columns
# names = findings['name']
# risk_severity = findings['risk.severity']

# # Create a DataFrame for plotting
# plot_data = pd.DataFrame({
#     'name': names,
#     'risk_severity': risk_severity
# })

# # Ensure no missing values for plotting
# plot_data = plot_data.dropna(subset=['risk_severity'])

# # Plot the data
# plt.figure(figsize=(12, 8))
# sns.scatterplot(data=plot_data, x='risk_severity', y='name', palette='viridis')

# plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
# plt.xlabel('Finding Name')
# plt.ylabel('Risk Severity')
# plt.title('Risk Severity of Findings by Name')
# plt.show()


# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Load the JSON file into a DataFrame
# csv = pd.read_json("json2.json")
# findings = pd.json_normalize(csv['findings'])

# # Print column names to debug
# print("Columns in findings DataFrame:", findings.columns)

# # Extract the relevant columns
# names = findings['name']
# risk_severity = findings['risk.severity']

# # Create a DataFrame for plotting
# plot_data = pd.DataFrame({
#     'name': names,
#     'risk_severity': risk_severity
# })

# # Ensure no missing values for plotting
# plot_data = plot_data.dropna(subset=['risk_severity'])

# # Create the plot with increased figure size
# plt.figure(figsize=(14, 10))  # Increase size to ensure names are visible
# sns.barplot(data=plot_data, x='name', y='risk_severity', palette='viridis')

# # Rotate x-axis labels and adjust alignment
# plt.xticks(rotation=45, ha='right')  # Rotate labels and align them to the right
# plt.xlabel('Finding Name')
# plt.ylabel('Risk Severity')
# plt.title('Risk Severity of Findings by Name')
# plt.tight_layout()  # Adjust layout to fit labels and titles
# plt.show()


# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Load the JSON file into a DataFrame
# csv = pd.read_json("json.json")
# findings = pd.json_normalize(csv['findings'])

# # Print column names to debug
# print("Columns in findings DataFrame:", findings.columns)

# # Extract the relevant columns
# names = findings['name']
# risk_severity = findings['risk.severity']

# # Create a DataFrame for plotting
# plot_data = pd.DataFrame({
#     'name': names,
#     'risk_severity': risk_severity
# })

# # Ensure no missing values for plotting
# plot_data = plot_data.dropna(subset=['risk_severity'])

# # Create the plot with increased figure size
# plt.figure(figsize=(14, 10))  # Increase size to ensure names are visible
# sns.barplot(data=plot_data, y='name', x='risk_severity', palette='viridis')

# # Rotate y-axis labels for better readability
# plt.xlabel('Risk Severity')
# plt.ylabel('Finding Name')
# plt.title('Risk Severity of Findings by Name')
# plt.tight_layout()  # Adjust layout to fit labels and titles
# plt.show()



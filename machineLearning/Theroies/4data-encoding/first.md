<!-- Data Encoding -->
(input feature)                        (dependent feature)
Exp   Education                        salary(output feature)
4     BE                               50k
6     PHD                              100k
3     ME                               70k
6     BE                               45k


DATA Encoding :- 

Data encoding in machine learning is the process of transforming categorical data into a numerical format that can be processed by machine learning algorithms.
Many algorithms cannot work directly with categorical data and require all input features to be numeric.

There are several common techniques for data encoding:

    Label Encoding:
        Each category is assigned a unique integer. For example, if a feature "color" has categories "red," "green," and "blue," they might be encoded as 0, 1, and 2, respectively.
        This method is simple but can introduce ordinal relationships that don't exist.

    One-Hot Encoding:
        Creates binary columns for each category. For example, the "color" feature with categories "red," "green," and "blue" would be transformed into three columns:
        "color_red," "color_green," and "color_blue," with 1s and 0s indicating the presence of each category.
        This method avoids introducing ordinal relationships but can lead to high-dimensional data if the feature has many categories.

    Binary Encoding:
        Combines the properties of label encoding and one-hot encoding. Each category is first encoded as an integer and then converted to binary. The binary digits are split into separate columns.
        This method reduces dimensionality compared to one-hot encoding.

    Frequency Encoding:
        Each category is replaced by the frequency of its occurrence in the dataset. For example, if "red" appears 10 times, "green" 20 times, and "blue" 30 times, the encoded values would be 10, 20, and 30, respectively.
        This method can be useful when the frequency of categories carries significant information.

    Target Encoding (Mean Encoding):
        Each category is replaced with the mean of the target variable for that category. This method can be powerful but risks overfitting if not handled properly.

    Hashing Encoding:
        Uses a hash function to assign categories to a fixed number of bits. This method can handle a large number of categories and is often used in streaming data or very large datasets.


Choosing the right encoding method depends on the specific dataset and the machine learning algorithm being used.
It's essential to consider the trade-offs in terms of introducing ordinal relationships, increasing dimensionality, and the risk of overfitting.
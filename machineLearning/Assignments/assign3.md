<!-- Feature Engineering Assignment 2 -->

Q1.     What is Min-Max scaling, and how is it used in data preprocessing? Provide an example to illustrate its
        application ?
ans:-   Min-Max scaling is a technique used in data preprocessing to rescale numeric features to a specific range, typically
        between 0 and 1. It is done by subtracting the minimum value of the feature and then dividing by the range of the feature
        (the difference between the maximum and minimum values). 
        The formula for Min-Max scaling is:  (X - Xmin)/(Xmax - Xmin)

Q2.     What is the Unit Vector technique in feature scaling, and how does it differ from Min-Max scaling?
        Provide an example to illustrate its application ? 
ans:-   The Unit Vector technique, also known as Normalization, is another method used for feature scaling
        in data preprocessing. Unlike Min-Max scaling which scales the data to a specific range (often between 0 and 1),
        Normalization scales each feature such that the magnitude of each feature vector is 1. 
        This technique is particularly useful when the magnitude of the features varies widely.

        Normalization :- |X| = sqrt(x1*x1 + x2*x2 + x3*x3+...) and then x1/|X|, x2/|X|, x3/|X|, ...
        Min-Max scaling :- (X-Xmin)/(Xmax-Xmin)

Q3.     What is PCA (Principle Component Analysis), and how is it used in dimensionality reduction? Provide an
        example to illustrate its application ?
ans:-   Principal Component Analysis (PCA) is a dimensionality reduction technique that is widely used to transform
        a dataset into a new coordinate system such that the greatest variance by any projection of the data comes to
        lie on the first coordinate (called the first principal component), the second greatest variance on the second
        coordinate, and so on. PCA aims to find a lower-dimensional representation of the data while retaining as much variance as possible.
        Steps of PCA:
        Standardize the Data: If the features in the dataset have different scales, it's important to standardize them (mean = 0, variance = 1).
        Compute the Covariance Matrix: Calculate the covariance matrix of the standardized feature matrix.
        Compute Eigenvectors and Eigenvalues: Eigenvectors and eigenvalues of the covariance matrix are computed. Eigenvectors represent the
          directions or components (principal components), and eigenvalues represent their magnitude.
        Select Principal Components: Sort the eigenvalues in descending order to rank the corresponding eigenvectors.
         Choose the top kk eigenvectors based on the explained variance needed.
        Project Data onto Principal Components: Construct a projection matrix from the selected top kk eigenvectors.
         Use this matrix to transform the original data into the new feature space.

Q4.     What is the relationship between PCA and Feature Extraction, and how can PCA be used for Feature
        Extraction? Provide an example to illustrate this concept.
ans:-   PCA (Principal Component Analysis) can be directly used for feature extraction. In the context of feature extraction,
        PCA refers to the process of using PCA to transform the original features into a new set of features (principal components)
        that are linear combinations of the original features. These principal components are chosen to capture the maximum variance
        in the data, thereby summarizing the essential characteristics of the dataset with fewer dimensions.

        Relationship between PCA and Feature Extraction:
        Dimensionality Reduction: PCA reduces the dimensionality of the data by transforming it into a lower-dimensional space spanned
        by the principal components. This reduction can help in mitigating the curse of dimensionality, simplifying models, and improving computational efficiency.
        Feature Combination: PCA constructs new features (principal components) that are linear combinations of the original features. These components are chosen
        based on their ability to capture the variance in the data, effectively combining the information from correlated original features into fewer, orthogonal components.

Q5.     You are working on a project to build a recommendation system for a food delivery service. The dataset
        contains features such as price, rating, and delivery time. Explain how you would use Min-Max scaling to
        preprocess the data ?
ans:-   In the context of building a recommendation system for a food delivery service, preprocessing the data using
        Min-Max scaling can be beneficial, especially when the features have different scales and ranges. Here’s how
        Min-Max scaling can be applied to the dataset containing features like price, rating, and delivery time:

        Steps to Use Min-Max Scaling:

        Understand the Range of Each Feature:
            Price: Typically, prices can range from a minimum value to a maximum value (e.g., $5 to $50).
            Rating: Ratings often range from a minimum value (e.g., 1 star) to a maximum value (e.g., 5 stars).
            Delivery Time: Delivery times can vary from a minimum (e.g., 10 minutes) to a maximum (e.g., 60 minutes).

        Apply Min-Max Scaling:
            For each feature, subtract the minimum value to shift the range to start from 0.
            Ex :- (X-Xmin)/(Xmax-Xmin)

Q6.     You are working on a project to build a model to predict stock prices. The dataset contains many
        features, such as company financial data and market trends. Explain how you would use PCA to reduce the
        dimensionality of the dataset.
ans:-   n the context of building a model to predict stock prices using a dataset with numerous features (such as company financial data and market trends),
        PCA (Principal Component Analysis) can be employed to reduce the dimensionality of the dataset. This reduction is beneficial for several reasons,
        including simplifying the model, improving computational efficiency, and potentially improving predictive performance by focusing on the most
        informative components of the data.
       Steps to Use PCA for Dimensionality Reduction:

    Data Preprocessing:
        Standardize the Data: Ensure all features have zero mean and unit variance. This step is crucial for PCA as it assumes that the data is centered.

    Apply PCA:

        Compute the Covariance Matrix: Calculate the covariance matrix of the standardized feature matrix. 
        The covariance matrix captures the pairwise covariances between different features, providing insight into their relationships.

        Compute Eigenvectors and Eigenvalues: Compute the eigenvectors and eigenvalues of the covariance matrix.
        Eigenvectors represent the directions (principal components) and eigenvalues represent the magnitude of variance explained by these components.

        Select Principal Components: Sort the eigenvalues in descending order and choose the top kk eigenvectors corresponding to the largest eigenvalues.
        These eigenvectors will form the basis for the new feature subspace.

        Project Data onto Principal Components: Construct a projection matrix from the selected top kk eigenvectors and project the original data onto this matrix.
        This transforms the data onto a new coordinate system defined by the principal components.

Q7.     For a dataset containing the following values: [1, 5, 10, 15, 20], perform Min-Max scaling to transform the
        values to a range of -1 to 1.
ans:-   import numpy as np
        
        def Min_Max(l):
            min = np.min(l)
            max = np.max(l)
            ans = []
            for ele in l:
                num = (ele - min)/(max - min)
                ans.append(num)
            return ans
        
        l = [1,5,10,15,20]
        ans = Min_Max(l)
        print("After min max scaling",ans)

        <!-- Method 2 using sklearn -->
        from sklearn.preprocessing import  MinMaxScaler
        l=[1,5,10,15,20]

        min_max = MinMaxScaler()
        min_max.fit(l)
        normalised_min_max = min_max.fit_transform(l)
        print("After min max scaling",normalised_min_max)

Q8.     For a dataset containing the following features: [height, weight, age, gender, blood pressure], perform
        Feature Extraction using PCA. How many principal components would you choose to retain, and why?
ans:-   import numpy as np
        from sklearn.preprocessing import StandardScaler
        from sklearn.decomposition import PCA

        X = np.array([
            [170, 65, 30, 1, 120],
            [165, 60, 35, 0, 130],
            [180, 70, 40, 1, 125],
            [175, 68, 28, 1, 115],
            [160, 55, 32, 0, 135]
        ])
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        pca = PCA()
        X_pca = pca.fit_transform(X_scaled)

        explained_variance_ratio = pca.explained_variance_ratio_
        cumulative_explained_variance_ratio = np.cumsum(explained_variance_ratio)

        print("Explained Variance Ratio:")
        print(explained_variance_ratio)

        print("\nCumulative Explained Variance Ratio:")
        print(cumulative_explained_variance_ratio)

        n_components = np.argmax(cumulative_explained_variance_ratio >= 0.95) + 1
        print(f"\nNumber of components to retain: {n_components}")

        pca = PCA(n_components=n_components)
        X_final = pca.fit_transform(X_scaled)

        principal_components = pca.components_
        print("\nPrincipal Components:")
        print(principal_components)

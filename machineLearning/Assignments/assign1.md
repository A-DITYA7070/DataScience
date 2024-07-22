Assignment 01

Q.1 Explain the following with Example ?
    a) Artificial Intelligence
    b) Machine Learning
    c) Deep Learning.

Ans :- 
     a) Artificial Intelligence :- It is a science of developing smart machines that can think and act like human,using algorithm,data and 
                                   computational power to mimic human intelligence. A.I can be used in almost every field including Medicals,
                                   Agriculture,Defence,Space,Construction etc, using different algorithms smart machines are built that can think
                                   this is achieved by training the model.
                                    
   b) Machine Learning :- Ml is a subset of a.i that is used to build complex machine that can perform complex task with little to no human interventions, it is used in prediction, like in price prediction, recommendation systems etc.

   Ex of Ml :- facial recognition, product recomendations,finanicial accuracy,social media optimisaiton, predictive analytic.

    c) Deep learning :- Dl is a type of ai that teaches computers to process data like the human brain. DL models can identify complex patterns in pictures,sounds,texts and other data to make accurate predictions and insights. DL is a subset of ml, which uses algos to learn from the data and make decisions. DL structures algos in layers to create an artificial neural network that can make decisions on its own.

Q 2. What is supervised learning ? list some examples ?
ans :- In supervised learning the machine is trained on the basis of labelled data set means the input data is paired with output data and machine is trained 
       based on that and when test  data is fed to the machine the machine predicts on the basis of the training.
       This model is often used for classification, regression and object detection problem.

Ex :- spam filtering, image classification,fraud detection etc.

Q3. What is unsupervised learning ? list some examples?

ans :- In unsupervised learning the model is trained based on unlabelled data set means in this data set input is not mapped with the output, the goal of unsupervised learning is to discover pattern in the dataset and relation in them without any guidance.
here the task is to cluster of group data based on some pattern,similarity or relationship.

Ex:- anamoly detection, price prediction etc.


Q4. What is thK differencK between AI, ML, DL, and DS?
ans :- A.I is the super set, smart application that can perform its own task without human intervention.
       Ex:- self driving car,robots,alexa etc.
       ML :- Ml is subset of A.I which is used to build models that can predict/forecast.
       Ex:- Recommendation system.
       DL :-Deep learning mimics the human brain (it has multilayers in which models are trained).
       ex:- recommendation system,multilayered net.
       DS :- Data science is the process of extracting knowledge from data, it is used to solve business problems,
             It uses all the techniques a.i,ml,Dl to solve a problem and make a decision.

Q5- What are the main differences between supervised, unsupervised, and semi-supervised learning?
ans :- supervised learning :- In supervised learning the model is trained on the basis of labelled data set.
                              The output feature is known
                              Classification :- categorical classification
                              Regression :- continuous classification
        unsupervised learning :- In unsupervised learning the model is trained based on unlabelled data set,
                                 The output feature is not known.
        ex :- clustering problem
        Semi-Supervised Learning :- It used both the technique supervised and unsupervised learning to solve a problem.
                                   
Q6. What is train, test and validation split? E=plain thK importance of each term.
ans :- Train split :- This data is used to train the model.
       validation split :- This data set is used for hyper-parameter tuning.
       test split :- This data set is used to test the model. (it is unique to the model)

Q7. How can unsupervised learning be used in anamoly detection ?
ans:- 
        Unsupervised learning can be effectively used in anomaly detection by leveraging the ability to identify patterns and structures in data without needing
        labeled examples. Here are several common approaches:

        1. Clustering-Based Methods
        In clustering-based methods, data points are grouped into clusters based on similarity. Anomalies are detected as data points that do not fit well into any
        cluster or are far from the nearest cluster centroid. Common clustering algorithms include:

        K-Means: Data points far from their assigned cluster centroids are considered anomalies.
        DBSCAN (Density-Based Spatial Clustering of Applications with Noise): Points in low-density regions (not belonging to any cluster) are identified as anomalies.
        2. Density-Based Methods
        Density-based methods estimate the density of data points and identify anomalies as points in low-density regions.

        Local Outlier Factor (LOF): Measures the local density deviation of a data point with respect to its neighbors. Points with significantly lower density compared
        to their neighbors are considered anomalies.
        3. Autoencoders
        Autoencoders are neural networks used for feature learning. They are trained to compress the data into a lower-dimensional representation and then reconstruct it back.
        Anomalies are detected based on the reconstruction error:

        Autoencoder: Train the autoencoder on normal data. Anomalies will have higher reconstruction errors since the autoencoder will not be able to reconstruct them well.
        4. Principal Component Analysis (PCA)
        PCA is a dimensionality reduction technique that can be used to identify the principal components of the data.

        PCA-Based Anomaly Detection: Anomalies are identified as data points that have large distances from the principal components, indicating they do not conform
        to the normal data distribution.
        5. One-Class SVM (Support Vector Machine)
        One-Class SVM is trained on normal data to learn a decision boundary that encompasses the normal data points. Any point falling outside this boundary
        is considered an anomaly.

        One-Class SVM: Suitable for scenarios where you have a clear understanding of what constitutes normal data.
        Importance of Unsupervised Learning in Anomaly Detection
        No Labeled Data Required: Unsupervised learning is particularly useful when labeled data is scarce or unavailable.
        Adaptability: These methods can adapt to changes in data patterns, making them suitable for dynamic environments.
        Versatility: Applicable to various domains such as fraud detection, network security, healthcare, and manufacturing.
        By identifying patterns and deviations in data without predefined labels, unsupervised learning methods provide robust tools for detecting anomalies
        across different applications.

Q8.  List down common supervised learning and unsupervised learning algorithms ?
ans :- 
    Common Supervised Learning Algorithms
        Linear Regression: Used for predicting a continuous target variable based on input features.
        Logistic Regression: Used for binary classification problems.
        Decision Trees: A tree-like model used for both classification and regression tasks.
        Random Forests: An ensemble of decision trees, typically used for classification and regression.
        Support Vector Machines (SVM): Used for classification and regression by finding the optimal hyperplane that separates classes.
        k-Nearest Neighbors (k-NN): A simple, instance-based learning algorithm used for classification and regression.
        Naive Bayes: A probabilistic classifier based on Bayes' theorem with strong independence assumptions.
        Gradient Boosting Machines (GBM): An ensemble technique that builds models sequentially, each correcting errors of the previous one.
        Neural Networks: Models inspired by the human brain, capable of capturing complex patterns in data. Includes:
        Multi-Layer Perceptron (MLP)
        Convolutional Neural Networks (CNNs): For image data.
        Recurrent Neural Networks (RNNs): For sequential data.

    Common Unsupervised Learning Algorithms
        K-Means Clustering: Partitions data into k clusters based on feature similarity.
        Hierarchical Clustering: Builds a tree of clusters by either a bottom-up or top-down approach.
        DBSCAN (Density-Based Spatial Clustering of Applications with Noise): Identifies clusters based on the density of data points.
        Gaussian Mixture Models (GMM): A probabilistic model that assumes all data points are generated from a mixture of several Gaussian distributions.
        Principal Component Analysis (PCA): A dimensionality reduction technique that transforms data into a set of orthogonal components.
        t-Distributed Stochastic Neighbor Embedding (t-SNE): A technique for dimensionality reduction, particularly suited for visualization of high-dimensional data.
        Autoencoders: Neural networks used for unsupervised feature learning and dimensionality reduction.
        Isolation Forest: A tree-based anomaly detection algorithm that isolates anomalies based on random partitioning.
        Self-Organizing Maps (SOMs): A type of neural network used for clustering and visualization of high-dimensional data.
        Local Outlier Factor (LOF): Identifies anomalies by comparing the local density of data points.
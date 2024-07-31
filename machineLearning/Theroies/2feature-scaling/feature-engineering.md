Feature Engineering :- It refers to the process of using domain knowledge to select and transform the most relevant variables from raw data when creating a predictive model using.
ml or statistical modelling.

Goal :- Goal of feature engineering and selection is to improve the performance of ml algos.

Feature selection --> selecting optimal and best features for ml models.

=> Feature selection techniques find a smaller subset for many dimensional data set to create data model.
=> The complexity depends upon size of data sample,no of input dimension, and selected dimensions k.
=> It is a technique of finding k features of the d dimensions that gives us the most info and discards the other (d-k) dimensions.

** Feature Selection Techniques ::- 
i) Supervised Feature Selection.
ii) Unsupervised Feature Selection.

i) Supervised Feature Selection :-
a) Filter methods.
b) Embedded Methods.
c) Wrapper methods.

a) Filter method.
        => Features are filtered based on general characteristics metric such as correlation of the dataset(correlation with dependent variable)
        => It is faster and usually the better approach when no of features are huge.
        => avoids overfitting but sometime may fail to select best features.

        ==> Types of Filter method of Feature selection :-
        
        i) Information gain.
        ii) Chi-Square method.
        iii) Variance Threshold.


        i) Filter method : - Information gain.

            Finds meaningfull attributes and features, commonly used method in feature selection.
            It measures the amount of info a feature provides about the target varible in a classification or regression problem.

                NOTE :- The higher the information gain of a feature the more relevant it is predicting the target variable.

                => The basic idea is to rank the features on the basis of their information gain values and select the 
                top k features that contribute the most to the prediction task.
                
                Calculation of information gain :-
                a) Entropy (H(y)) :- Entropy is a measure of randomness or uncertainity in the target variable y.
                for classification problem :-  [ H(y) = -sum of(p(y)) * log2(p(y)) ] (p(y) is probablity of particular class y occuring in the target variable.)
                b) Conditional Entropy (H(y/x)) :- It measures the uncertanity in the target variable y given a particular feature x.
                c) For Discrete Feature x H(y/x) :- sum of p(x) * H(y/x) p(x) is probablity of a particular value of x occuring for the feature x and H(y/x) is the entropy 
                                                    of the target variable y conditioned on the feature x having the value x.

                NOTE :- Information gain is the reduction in entropy of the target variable y when we know the value of a feature x.
                for discrete feature x :-

                IG(x) = H(y) - H(y/x)

                NOTE :- the higher the information gain the more info the feature x contributes to the prediction of the target variable ..

                STEPS FOR USING IG FOR FEATURE SELECTION :-
                i) calculate the entropy of target variable y.
                ii) for each feature x 
                    a) calculate the conditional entropy H(y/x) by considering the possible values of x.
                    b) calculate the IG(x) by subtracting H(y/x) from the entropy H(y).
                => Rank the feature based on their IG values and select the top - k features for your model.


        ii) Filter method : - Chi-Square method.




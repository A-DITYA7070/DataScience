<!-- Feature extraction -->

=> It it the process of selecting and extracting the most important features from raw data.

==> ML apps --> 1000 features --> Most important features --> Machine learning algo


i) Feature scaling.. :- It is the process of bringing down or scaling down the datasets between some given range so that,
                        model can be trained easily and should produce fast results.

ii) feature selection :- In this technique we just select the most important feature from the datasets.
                         Ex :- from 500 feature we select top 10 feature.
                         i) filter method ii) embedded method iii) pca (principle component analysis).



i) Feature scaling techinques :::---
I) Standralization -> Z-Score
II) Min-Max Scaling -> Normalization
III) unit vector.


i) standralization :- mean = 0 , s.d = 1
   Z-score = (x - mean) / std
   ex :- age = 24,25,26,27,28
         then we will calculate mean first mean and then std.
         and we will then calculate age' using Z-Score
         age' will have mean = 0 and std = 1


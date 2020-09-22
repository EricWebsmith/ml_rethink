# Using Medoid-Radius Clustering in Stacking Estimator Selection and Bundling.



Cluster-based Feature selection has be adopted by many researchers. We can reuse those cluster-based feature selection methods for estimator selection for stacking. However, estimator predictions are significantly similar to each other. Thus, We propose  a new cluster algorithm, namely medoid-radius to cluster the estimators. We first fit n estimators and generate their predictions. We filter out poor-performed learners and put the rest n predictions into further study. We calculate their pair-wise correlation. The distance is 1 minus correlation. All pair-wise correlations will form a distance matrix. We than use this matrix to cluster estimators. In Medoid-Radius, We do not feed the algorithm with a k, like k-mean and k-medoid that are used in previous studies. Instead, we use a radius **r** to determine if two estimators are to be put in one cluster. If for an estimator, there is no any  other estimator with a distance smaller than **r**, that estimator will be consider an independent estimator. In ensemble, an independent base estimator provides a unique view of the data and it is suggested to keep. Thus, we will keep those independent learners intact. For the estimators in the clusters, we will average their predictions such that the similar estimators are bundled into one. 





# Reference

cluster based hybrid feature selection stacking


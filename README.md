# Collaborative Filtering with ALS Model

## Overview

This project focuses on evaluating the accuracy of the ALS (Alternating Least Squares) model in collaborative filtering. The ALS model is a popular algorithm used for recommendation systems. The program uses the ratings data provided in the "ratings.dat" file and splits it into training and testing sets. The model is trained on the training set and then evaluated on the testing set to compute the Mean Squared Error (MSE) as a measure of accuracy.

## Prerequisites

Before running the code, ensure you have the following:

- Apache Spark installed and properly configured.
- The "ratings.dat" file, which contains the ratings data in the format: User id :: Movie id :: Rating :: Timestamp.

## Steps

1. **Load Ratings Data:** Read the "ratings.dat" file and load the data into a PySpark DataFrame. Ensure that the appropriate delimiter is used to separate the columns.

2. **Split Data:** Split the ratings data into a training set and a testing set. Allocate 60% of the data for training and 40% for testing. This ensures that the model is trained on a majority of the data while having a separate set for evaluation.

3. **Build the ALS Model:** Construct the ALS model using the training data. Set the necessary parameters such as the rank (dimensionality of the latent factors), the number of iterations, and the regularization parameter. The ALS algorithm learns latent factors to make predictions and recommends items based on user ratings.

4. **Evaluate the Model:** Use the testing set to evaluate the accuracy of the ALS model. Compute the Mean Squared Error (MSE) between the predicted ratings and the actual ratings. MSE provides a measure of how well the model performs in predicting ratings for unseen data.

5. **Report the Accuracy:** Display the computed MSE value as a measure of the accuracy of the ALS model. A lower MSE indicates better accuracy, as it reflects the average squared difference between the predicted and actual ratings.

## Usage

1. Set up the environment by installing and configuring Apache Spark.

2. Ensure that the "ratings.dat" file is available in the appropriate format and location.

3. Customize the provided code to fit your specific dataset and requirements.

4. Run the code using a PySpark-compatible environment or submit it as a Spark job.

## Conclusion

By following the outlined steps and customizing the code to your specific dataset, you can evaluate the accuracy of the ALS model in collaborative filtering. The project allows you to split the data into training and testing sets, train the ALS model, and compute the Mean Squared Error (MSE) as a measure of accuracy. This information can be valuable in assessing the performance of recommendation systems and improving user experiences.

Please refer to the accompanying documentation or code comments for more detailed instructions on running the program and interpreting the results. Feel free to explore and modify the code as needed to suit your requirements or extend its functionality.

Enjoy using the Collaborative Filtering with ALS Model project! If you have any questions or feedback, please don't hesitate to reach out.

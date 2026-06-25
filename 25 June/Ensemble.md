### Ensemble Learning Methods

##### Ensemble learning is a method where multiple models are combined instead of using just one. Even if individual models are weak, combining their results gives more accurate and reliable predictions.

### Techniques
- **Bagging(Bootstrap Aggregation)**
- **Boosting**
- **Stacking**

### Bagging
- **Models are trained independently on different random subsets of the training data. Their results are then combined—usually by averaging (for regression) or voting (for classification). This helps reduce variance and prevents overfitting.**
- **Bagging classifier can be used for both regression and classification tasks. Here is an overview of Bagging classifier algorithm:**
    - **Bootstrap Sampling : The dataset is divided into multiple subsets by sampling with replacement, creating diverse training data**
    - **Base Model Training : A separate model is trained on each subset independently, often in parallel for efficiency**
    - **Prediction Aggregation : Predictions from all models are combined using majority voting (classification) or averaging (regression)**
    - **OOB Evaluation : Samples not included in a subset are used to evaluate model performance without cross-validation**
    - **Final Prediction : The combined output of all models gives a more reliable and accurate result**

    ![Screenshot](Screenshot%202026-06-25%20120223.png)

### Boosting
- **Models are trained one after another. Each new model focuses on fixing the errors made by the previous ones. The final prediction is a weighted combination of all models, which helps reduce bias and improve accuracy.**

<<<<<<< HEAD
    ![Screenshot](Screenshot%202026-06-25%20120728.png)**
=======
  ![Screenshot](Screenshot%202026-06-25%20120728.png)**
>>>>>>> 89b132ee3bca3fa9fbf2474bef5a9320a04a53d1

# TOPICS

## Confusion matrix
## Evaluation matrix

## 1. Confustion matrix
- **Confusion matix:**
    - **N x N matrix where N is the predicted class**
    - **TP(True Positives) : Correct ones**
    - **TN(True Negative) : Correct negatives**
    - **FP(False Positive) : Type 1 error -> reality: Negative, Predicated: Positive**
    - **FN(False Negative) : Type 2 error -> reality: positive, Predicated: Negative**


## 2. Evaluation matrix

### 2.1 Accuracy:
###### Total percentage of correct ones
###### (TP + TN)/ (TP+TN+FP+FN)


### 2.2 Precision:
###### predicted correct amoungs all correct
###### high precision means very less negative values predicted
###### (TP)/ (TP + FP)


### 2.3 Recall:
###### Total positives amoungs actual positives
###### High recall means you missed almost no positive values
###### (TP)/ (TP + FN)


## 3. ROC Curve

###### The ROC Curve (Receiver Operating Characteristic) is a graph that evaluates how powerful a classification model is at separating two classes (like distinguishing between "Legitimate Transactions" and "Fraud").

###### When a model makes a prediction, it calculates a probability score (e.g., "There is an 85% chance this email is spam"). Instead of just testing the model at a single setting, the ROC Curve shows how your model behaves across every possible sensitivity setting (from 0% to 100%).

### 3.1 AUC(Area Under the curve)
- **To read an ROC graph, you look at the total area underneath the curved line:**
    - **AUC = 1.0 (The Mind Reader): The line shoots straight to the top-left corner immediately. It catches 100% of targets with zero false alarms.**
    - **AUC = 0.5 (The Coin Flipper): The line is a useless diagonal shortcut across the screen. The model is just randomly guessing.**


## 4. Bias (Underfitting)
###### Bias happens when a model is too simple and rigid. It makes strong assumptions about the data and ignores the nuances.
###### The Analogy: Imagine a student who prepares for the exam by only memorizing one basic formula ($y = mx + b$). No matter what complex question appears on the test, they try to use that same simple formula.
###### The Result: They perform poorly on the practice worksheets, and they perform poorly on the actual final exam. In data science, this is called Underfitting. Your model is too dumb to see the actual patterns.


## 5. Variance (Overfitting)
###### Variance happens when a model is too complex, hyper-sensitive, and flexible. It shuffles and warps its decision line to perfectly touch every single individual data dot.
###### The Analogy: Imagine a student who prepares for the exam by completely memorizing the exact answers to the practice textbook questions word-for-word. They don't learn the concepts; they just memorize the exact layout of the homework sheet.
###### The Result: They score a perfect 100% on their homework practice data. But when they sit down for the actual final exam and face brand-new questions they haven’t seen before, they panic and fail completely. In data science, this is called Overfitting. The model memorized the training noise and fails to generalize to real-world data.

## 6. The Trade-off: Finding the Sweet Spot
###### Your goal as an engineer is to adjust your model's complexity to minimize both errors at the same time:
###### If you have High Bias, your model lacks capacity (Underfitting). You need to add more features, train longer, or switch to a stronger model like a Random Forest.
###### If you have High Variance, your model is hyper-sensitive (Overfitting). You need to clean your outliers, feed it more raw data rows, or use regularization to restrain its complexity.

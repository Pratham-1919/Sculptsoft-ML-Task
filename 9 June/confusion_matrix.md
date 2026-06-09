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
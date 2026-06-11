### Skewness

#### Skewness is a measure of the asymmetry or "lopsidedness" in a dataset. In a perfect world, real-world data would look like a symmetric bell curve, but in practice, data often tilts heavily to one side.

#### The Three Types of Skewness

- **1. Zero Skewness (Symmetric Distribution)**
    - **The data is perfectly balanced on both sides of the center.**
    - **The Shape: A clean, classic Bell Curve.**
    - **The Relationship: The Mean, Median, and Mode are all exactly equal and sit right in the dead center.**
    - **Example: Human adult heights or standardized exam scores.**

- **2. Right Skewed / Positive Skewness**
    - **The data piles up heavily on the left side (near lower numbers), while a few extreme outlier values stretch a long "tail" out to the right (higher numbers).**
    - **The Shape: The peak is on the left; the thin tail points to the right.**
    - **The Relationship: Mean > Median > Mode. The mean gets dragged upward toward the right by those massive outliers.**
    - **Example: Household income or wealth. Most people earn a baseline salary (the peak on the left), but a few multi-billionaires pull the mathematical average (mean) way to the right.**

- **3. Left Skewed / Negative Skewness**
    - **The data piles up heavily on the right side (near higher numbers), while a few extreme outlier values stretch a long "tail" out to the left (lower numbers).**
    - **The Shape: The peak is on the right; the thin tail points to the left.**
    - **The Relationship: Mean < Median < Mode. The mean gets dragged downward toward the left by the low outliers.**
    - **Example: The age of retirement. Most people retire in their 60s or 70s (the peak on the right), but a few people retire very early due to health or sudden wealth, creating a tail stretching down toward younger ages.**


### How to Overcome Skewed Data

#### To fix skewed columns before training a model, data scientists use mathematical operations to "compress" the long tail, pulling the skewed distribution back into a normal shape.

- **1. Log Transformation (Best for Right Skew)**
    - **This is the most common fix for severely right-skewed columns (like income or pricing arrays). It applies a logarithm to every single number.**
    - **The Math: np.log1p(x) (We use log1p because if a value is 0, $log(0)$ is undefined, so it automatically calculates $log(x+1)$ to keep the code safe).**
    - **Why it works: It acts like a compressor. It barely changes small numbers (e.g., $log(10)$ is small), but it massively collapses huge numbers down to a tiny scale, shrinking your long tail instantly.**

- **2. Square Root Transformation**
    - **A milder version of the log transformation.**
    - **The Math: np.sqrt(x)**
    - **When to use: Excellent for data that represents counts (e.g., "number of website clicks per hour") that have a moderate right skew.**

- **3. Box-Cox or Yeo-Johnson Power Transforms**
    - **Instead of guessing whether a log or square root will work best, you can use Scikit-Learn's automated transformers.**
    - **How it works: These algorithms mathematically analyze your column, find the exact optimal power parameter ($\lambda$), and transform the data into a normal distribution curve.**
    - **Note: Box-Cox only works if your data contains strictly positive numbers ($>0$). If your data has zeros or negative numbers, you must use Yeo-Johnson.**



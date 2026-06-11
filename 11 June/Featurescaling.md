### Feature Scaling

##### Feature Scaling is a preprocessing step that translates columns with wildly different measurement units into a shared, standardized mathematical scale without altering the underlying shape of the data.


### The 3 Core Concepts inside Feature Scaling

- **1. Min-Max Scaling (Also called "Normalization" in Machine Learning)**
    - **This technique squashes your entire dataset down so that every single number falls strictly between a fixed boundary, usually 0 and 1.**

    ![Screenshot](Screenshot%202026-06-11%20170651.png)

    - **Visual Result: The absolute smallest value in your column becomes exactly 0, the absolute largest becomes 1, and everything else becomes a decimal in between.**
    - **When to use: Excellent when you know your data has definitive boundaries, or when you are using algorithms that don't assume a normal distribution (like K-Nearest Neighbors, Neural Networks, or Image Pixel Data ranging from 0–255).**
    - **The Weakness: It is incredibly sensitive to extreme outliers. If you have one rogue billionaire with an income of $10,000,000 in your dataset, everyone else’s scaled income will get compressed into a tiny, useless decimal fraction between 0.00 and 0.01.**

- **2. Standardization (Z-Score Scaling)**
    - **Instead of forcing data between 0 and 1, Standardization shifts your data so that its Mean becomes exactly 0 and its Standard Deviation becomes exactly 1.**

    ![Screenshot](Screenshot%202026-06-11%20171325.png)

    - **Visual Result: The data centers directly around 0. Most of your data points will land comfortably between $-3$ and $+3$.**
    - **When to use: This is the preferred baseline for a majority of machine learning models (like Support Vector Machines, Linear Regression, and Logistic Regression).**
    - **The Strength: Unlike Min-Max scaling, it handles outliers much better. An extreme outlier will simply receive a high Z-score (like $+7.5$) instead of compressing and crushing the rest of your normal data points.**

- **3. Robust Scaling (Outlier-Resistant Scaling)**
    - **If your dataset is riddled with extreme, unavoidable outliers that you cannot drop, standard scaling methods break down. Robust Scaling fixes this by ignoring the absolute minimums and maximums entirely.**
    - **The Math: It subtracts the Median and divides by the Interquartile Range (IQR) (the distance between the 25th and 75th percentiles).**
    - **Visual Result: It centers the data around the median, scaling it based on where the safe "middle 50%" of your data lives.**
    - **When to use: When your dataset has severe outlier spikes that you want to keep in your model without letting them distort the scale of your regular data points.**

- **4. Max Absolute Scaling (MaxAbsScaler)**
    - **Max Absolute Scaling scales your data strictly by dividing each value by the maximum absolute value in that column.**
    ![Screenshot](Screenshot%202026-06-11%20173440.png)
    - **The Bounds: It forces all numbers to land strictly inside the range $-1.0$ to $+1.0$.**
    - **The Unique Feature: It never destroys sparsity. If your matrix contains thousands of zeros (like a sparse database table or a text One-Hot Encoded array), it preserves those zeros exactly as 0.0.**
    - **When to use: It is the industry standard for scaling high-cardinality sparse matrices or text vectors (TF-IDF tokens) right before passing them into linear models or deep neural networks.**


- **Other Advanced Technique**
    - **Unit Vector Scaling**
    - **Binning / Quantization**
    - **Log Scaling**
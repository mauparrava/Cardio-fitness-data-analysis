Project Overview
This project analyzes the "CardioGoodFitness" dataset to identify patterns in customer behavior and product usage. By performing deep exploratory data analysis (EDA), I identified how demographics like age, gender, and income influence treadmill preferences.

The project concludes with a Linear Regression model that predicts the distance a customer is likely to run based on their usage frequency and self-reported fitness level.

📊 Key Features
Exploratory Data Analysis (EDA): Comprehensive profiling of customers using pandas and numpy.

Data Visualization: Distribution plots, boxplots for gender/age analysis, and heatmaps to identify feature correlations.

Customer Segmentation: Cross-tabulation and pivot tables to compare product popularity across different marital statuses and genders.

Predictive Modeling: A Linear Regression model to estimate customer "Miles" based on "Usage" and "Fitness" metrics.

🛠️ Tech Stack
Language: Python

Libraries: * Pandas & NumPy: Data manipulation and cleaning.

Matplotlib & Seaborn: Advanced data visualization and heatmaps.

Scikit-Learn: Machine Learning (Linear Regression).

📂 Project Structure
fitness data analysis.py: The main script containing the data processing, visualization, and modeling logic.

CardioGoodFitness.csv: The dataset containing customer attributes (Age, Education, Income, etc.).

🚀 Insights & Modeling
The project uses a correlation heatmap to identify the strongest predictors for treadmill usage.

Regression Model:
The final predictive model for expected miles is:
Miles Predicted = -56.74 + 20.21 * (Usage) + 27.20 * (Fitness)

This formula allows the business to estimate customer engagement based on their planned frequency and fitness goals.

📈 How to Run
Clone the repository:

Bash
git clone https://github.com/mauparrava/Cardio-fitness-data-analysis.git
Ensure you have the required libraries:

Bash
pip install pandas numpy matplotlib seaborn scikit-learn
Run the script:

Bash

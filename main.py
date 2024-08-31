import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data = pd.read_csv('data/student-scores.csv')

# Feature selection (excluding non-numeric and non-relevant columns)
features = data[['absence_days', 'weekly_self_study_hours', 'math_score']]
target = data['math_score']

# For prediction, we will use the rest of the columns
X = data[['absence_days', 'weekly_self_study_hours']]
y = target

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Print metrics
print(f'Mean Squared Error: {mean_squared_error(y_test, y_pred)}')

# Plotting
plt.figure(figsize=(10, 6))
sns.scatterplot(x=X_test['weekly_self_study_hours'], y=y_test, color='blue', label='Actual')
sns.lineplot(x=X_test['weekly_self_study_hours'], y=y_pred, color='red', label='Predicted')
plt.xlabel('Weekly Self Study Hours')
plt.ylabel('Math Score')
plt.title('Weekly Self Study Hours vs Math Score')
plt.legend()
plt.show()

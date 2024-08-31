# Student Score Prediction

This project uses linear regression to predict student math scores based on various features such as weekly self-study hours and absence days.

## Project Structure

- `data/` - Contains the dataset used for training and testing the model.
- `main.py` - The main script for loading data, training the model, making predictions, and visualizing results.
- `.gitignore` - Specifies files and directories to be ignored by Git.
- `requirements.txt` - Lists the Python packages required to run the project.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/bs-tech-project/student-score-prediction.git

2. Navigate to the project directory:

    ```bash
    cd student-score-prediction

3. Install the required packages:

    ```bash
    pip install -r requirements.txt

## Usage

1. Run the main script:

   ```bash
   python main.py

2. Script Explanation:

- Load Data: Placed/Loads the dataset from data/student-scores.csv.
- Feature Selection: Uses absence_days and weekly_self_study_hours to predict math_score.
- Model Training: Trains a linear regression model on the selected features.
- Prediction & Evaluation: Predicts math scores for the test set and calculates the Mean Squared Error.
- Visualization: Generates a scatter plot with a regression line showing the relationship between weekly_self_study_hours and math_score.

## Acknowledgements

- The dataset and sources referenced in this README.
- Special thanks to the open-source community for the tools and libraries used in this project.
# Solar Radiation Measurement EDA

This project involves an Exploratory Data Analysis (EDA) of Solar Radiation Measurement data collected from three different countries. The goal is to analyze and visualize the data to uncover patterns, relationships, and potential anomalies.

## Table of Contents

- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Exploratory Data Analysis (EDA) Overview](#exploratory-data-analysis-eda-overview)
- [Data Cleaning](#data-cleaning)
- [Visualizations](#visualizations)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Installation

To set up this project on your local machine, follow the steps below:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/brukGit/tenx-w0.git
   cd app

2. **Create a virtual environment (optional but recommended)**:
    ```bash
    python3 -m venv venv
    source venv\Scripts\activate  # On Linux, use `venv/bin/activate`

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt


## Project Structure
    ```bash
        ├── data/                  # Directory containing raw datasets
        ├── notebooks/             # Jupyter notebooks for EDA and analysis
        ├── scripts/               # Python scripts for data processing and visualization
        ├── tests/                 # Unit tests for the project
        ├── .github/workflows/     # GitHub Actions for CI/CD
        ├── .vscode/               # Visual Studio Code settings and configurations
        ├── requirements.txt       # Python dependencies
        ├── README.md              # Project documentation (this file)
        └── LICENSE                # License for the project


## Usage
### Running the Notebooks
1. Navigate to the notebooks/ directory.
2. Open and run the Jupyter notebooks in order to perform the EDA.
3. To run the Streamlit app locally:
    ```bash
    streamlit run app/main.py

## Exploratory Data Analysis (EDA) Overview
The EDA conducted in this project covers several key areas:

1. Data loading and initial inspection
2. Data cleaning and preprocessing
3. Statistical analysis of solar radiation measurements
4. Time series analysis
5. Correlation analysis between different variables
6. Visualization of key findings


## Data Cleaning
The data cleaning process involves:

1. Handling missing values
2. Removing duplicates
3. Correcting data types
4. Dealing with outliers

## Visualizations
The project includes various visualizations to help understand the solar radiation data:
- Time series plots of solar radiation measurements
- Correlation heatmaps
- Distribution plots for key variables
- Scatter plots to show relationships between variables
- Effect of 'Cleaning' on ModA and ModB over time

## Deployment
To deploy the Streamlit app to Streamlit Community Cloud:
1. Push your code to a GitHub repository.
2. Go to Streamlit Community Cloud.
3. Click on "New app" and select your GitHub repository.
4. Choose the main file path (e.g., app/main.py).
5. Click "Deploy".
Ensure your requirements.txt file is up to date with all necessary dependencies.


## Contributing
Contributions to this project are welcome! If you have suggestions or improvements, feel free to open a pull request or issue on GitHub.

## License
This project is licensed under the MIT License - see the LICENSE file for details.



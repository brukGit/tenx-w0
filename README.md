# Solar Radiation Measurement EDA

This project involves an Exploratory Data Analysis (EDA) of Solar Radiation Measurement data collected from three different countries. The goal is to analyze and visualize the data to uncover patterns, relationships, and potential anomalies.

## Table of Contents

- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Exploratory Data Analysis (EDA) Overview](#exploratory-data-analysis-eda-overview)
- [Data Cleaning](#data-cleaning)
- [Contributing](#contributing)
- [License](#license)

## Installation

To set up this project on your local machine, follow the steps below:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/brukGit/tenx-w0.git
   cd notebooks

2. **Create a virtual environment (optional but recommended)**:
    ```bash
    python3 -m venv venv
    source venv\Scripts\activate  # On Linux, use `venv/bin/activate`

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt


## Project Structure
    ```bash
        ├── data/                  # Directory containing raw and cleaned datasets
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
To perform the EDA, navigate to the notebooks/ directory and open the provided Jupyter notebook. The notebook focuses on different aspects of the analysis, including summary statistics, time series analysis, and correlation analysis.
    ```bash
    jupyter notebook notebooks/eda_analysis.ipynb

### Running Tests
If you want to run unit tests to ensure that the functions work as expected (although, sorry, currently no test code is provided.):
    
```bash
    pytest

## Exploratory Data Analysis (EDA) Overview
The EDA conducted in this project covers several key areas:

1. Summary Statistics: Calculation of basic statistical measures (mean, median, standard deviation, etc.) for each numeric column to understand the distribution of the data.

2. Data Quality Check: Inspection of missing values, outliers, or incorrect entries, with a focus on columns like GHI, DNI, DHI, and sensor readings (ModA, ModB).

3. Time Series Analysis: Visualization of time-dependent variables such as GHI, DNI, DHI, and ambient temperature (Tamb) to observe patterns, seasonal trends, and anomalies.

4. Impact of Cleaning: Evaluation of the impact of cleaning operations on sensor readings (ModA, ModB) over time.

5. Correlation Analysis: Visualization of correlations between solar radiation components (GHI, DNI, DHI) and temperature measures (TModA, TModB), as well as relationships between wind conditions (WS, WSgust, WD) and solar irradiance.

6. Wind Analysis: Polar plots to identify trends and significant wind events, showing the distribution of wind speed and direction.

7. Temperature Analysis: Investigation of the influence of relative humidity (RH) on temperature readings and solar radiation.

8. Histograms: Frequency distribution visualizations for variables like GHI, DNI, DHI, WS, and temperature metrics.

9. Z-Score Analysis: Calculation of Z-scores to flag data points that are significantly different from the mean.

10. Bubble Charts: Exploration of complex relationships between variables, such as GHI vs. Tamb vs. WS, with bubble size representing an additional variable like RH or BP (Barometric Pressure).


## Data Cleaning
Based on the initial analysis, the dataset was cleaned by removing the column Comments which was identified as having many null values.

## Contributing
Contributions to this project are welcome! If you have suggestions or improvements, feel free to open a pull request or issue on GitHub.

## License
This project is licensed under the MIT License - see the LICENSE file for details.



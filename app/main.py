import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO
from datetime import datetime

# Optimize Streamlit configuration
st.set_page_config(layout="wide")

@st.cache_data
def load_csv_file(file_name):
    df = pd.read_csv(f'./data/{file_name}', parse_dates=['Timestamp'])
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    return df

@st.cache_data
def filter_data(df, start_date, end_date):
    """Filter the DataFrame based on the selected date range."""
    return df[(df['Timestamp'] >= start_date) & (df['Timestamp'] <= end_date)]

@st.cache_data
def downsample_data(df, n=1000):
    return df.sample(n=min(n, len(df)))

@st.cache_data
def create_bubble_chart(df):
    """Generate a bubble chart based on the DataFrame."""
    df_downsampled = downsample_data(df)
    fig, ax = plt.subplots(figsize=(10, 6))
    
    scatter = ax.scatter(df_downsampled['GHI'], df_downsampled['Tamb'], 
                         s=df_downsampled['WS']*20, c=df_downsampled['RH'], 
                         cmap='viridis', alpha=0.7)
    
    ax.set_xlabel('Global Horizontal Irradiance (W/m²)')
    ax.set_ylabel('Ambient Temperature (°C)')
    ax.set_title('GHI, Temperature, Wind Speed, and Humidity')
    
    cbar = plt.colorbar(scatter)
    cbar.set_label('Relative Humidity (%)')
    
    handles, labels = scatter.legend_elements(prop="sizes", alpha=0.6, num=4)
    ax.legend(handles, labels, loc="upper right", title="Wind Speed (m/s)")
    
    plt.tight_layout()
    return fig

@st.cache_data
def create_summary_plot(df):
    """Generate a summary plot based on the DataFrame."""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    sns.boxplot(data=df[['GHI', 'Tamb', 'WS', 'RH']], ax=ax)
    ax.set_title('Summary Statistics')
    ax.set_ylabel('Value')
    ax.set_xlabel('Variable')
    
    plt.tight_layout()
    return fig

@st.cache_data
def create_correlation_heatmap(df):
    """Generate a correlation heatmap."""
    corr_columns = ['GHI', 'DNI', 'DHI', 'TModA', 'TModB']
    df_selected = df[corr_columns]
    correlation_matrix = df_selected.corr()

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', vmin=-1, vmax=1, center=0, square=True, linewidths=0.5, ax=ax)
    ax.set_title('Correlation Heatmap')
    
    plt.tight_layout()
    return fig

@st.cache_data
def create_scatter_matrix(df):
    """Generate a scatter matrix (pair plot)."""
    corr_columns = ['GHI', 'DNI', 'DHI', 'WS', 'WSgust', 'WD']
    df_selected = df[corr_columns]

    fig = sns.pairplot(df_selected, height=2, aspect=1)
    fig.fig.suptitle('Scatter Matrix of Selected Columns', y=1.02)
    
    return fig

def app():
    st.title("Dashboard | Solar Radiation Measurement")
    st.write("Link to GitHub repo: [https://github.com/brukGit/tenx-w0/tree/dashboard-dev](https://github.com/brukGit/tenx-w0/tree/dashboard-dev)")

    # Create three columns
    left_column, middle_column, right_column = st.columns([1, 2, 2])

    # Left column for navigation
    with left_column:
        st.subheader("Navigation")
        file_options = ['benin-malanville.csv', 'sierraleone-bumbuna.csv', 'togo-dapaong_qc.csv']
        file_selection = st.selectbox("Select a CSV file", file_options)
        
        if file_selection:
            df = load_csv_file(file_selection)
            
            min_date =pd.to_datetime(df['Timestamp']).min().date()
            max_date = pd.to_datetime(df['Timestamp']).max().date()
            
            st.write("Select Date Range:")
            start_date = st.date_input("Start Date", min_date, min_value=min_date, max_value=max_date)
            end_date = st.date_input("End Date", max_date, min_value=min_date, max_value=max_date)
            
            all_time = st.checkbox("Select All Time Range")
            
            if all_time:
                start_date = min_date
                end_date = max_date

    if file_selection:
        df = load_csv_file(file_selection)
        filtered_df = filter_data(df, pd.Timestamp(start_date), pd.Timestamp(end_date))
        
        if not filtered_df.empty:
            # Middle column for summary statistics and plots
            with middle_column:
                st.subheader(f"Summary Statistics - {file_selection}")
                st.dataframe(filtered_df.describe())
                
                st.subheader("Summary Plot")
                summary_fig = create_summary_plot(filtered_df)
                st.pyplot(summary_fig)
                
                st.subheader("Correlation Heatmap")
                heatmap_fig = create_correlation_heatmap(filtered_df)
                st.pyplot(heatmap_fig)

            # Right column for bubble chart and scatter matrix
            with right_column:
                st.subheader("Bubble Chart")
                bubble_fig = create_bubble_chart(filtered_df)
                st.pyplot(bubble_fig)
                
                st.subheader("Scatter Matrix")
                scatter_fig = create_scatter_matrix(filtered_df)
                st.pyplot(scatter_fig)
        else:
            st.write("No data available for the selected date range.")
    
if __name__ == "__main__":
    app()
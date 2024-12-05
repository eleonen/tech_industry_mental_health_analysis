# Exploratory Data Analysis of Mental Health in the Tech Industry

## **Project Overview**
This project aims to explore mental health trends in the tech industry, focusing on employer-provided mental health resources, the prevalence of mental health issues, and attitudes toward mental versus physical health. By identifying key patterns and trends, this analysis seeks to uncover actionable insights for improving mental health support in tech workplaces.

## **Table of Contents**
1. [Goals of the Analysis](#goals-of-the-analysis)
2. [Dataset Overview](#dataset-overview)
3. [Data Cleaning](#data-cleaning)
4. [Analysis Highlights](#analysis-highlights)
    - [Sampling Bias](#sampling-bias)
    - [Mental Health Resources](#mental-health-resources)
    - [Prevalence of Mental Health Issues](#prevalence-of-mental-health-issues)
    - [Mental vs. Physical Health](#mental-vs-physical-health)
5. [Key Findings](#key-findings)
6. [Improvements and Future Work](#improvements-and-future-work)

## Setup

### Prerequisites
- Python 3.x
- Poetry for dependency management
- Jupyter Notebook (optional, for viewing the analysis)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/TuringCollegeSubmissions/eleone-DS.v3.2.1.5/
   cd eleone-DS.v3.2.1.5
   ```

2. Set up a virtual environment and install dependencies using Poetry:
   ```bash
   poetry install
   ```

3. Activate the virtual environment:
   ```bash
   poetry shell
   ```

4. (Optional) If using Jupyter Notebook to view or modify the analysis:  
   ```bash
   poetry add notebook
   ```

## Project Structure
- `pyproject.toml`: Poetry configuration file listing dependencies.
- `poetry.lock`: Lock file with exact package versions.
- `mental_health.sqlite`: 
- `eda_mental_health_in_tech_industry.ipynb`: Jupyter notebook with the analysis and insights derived from the data.
- `src/utilities.py`: Contains helper functions like `find_outliers` and other graphing functions for visualizations.

## Usage

### Running the Jupyter Notebook
To interact with the data analysis or run your own queries, use the Jupyter notebook:
1. Start Jupyter Notebook:
   ```bash
   jupyter eda_mental_health_in_tech_industry.ipynb
   ```
2. Follow the cells to explore the analysis, or modify them to perform your own exploration.

## **Goals of the Analysis**

1. **Primary Objective:** To explore and visualize mental health trends in the tech industry.  
2. **Key Focus Areas:**
   - Sampling bias in age, gender, and race distributions.
   - Trends in employer-provided mental health resources over time.
   - Common mental health issues within the industry.
   - Comparison between employer attitudes toward mental and physical health.

## **Data Cleaning**

1. **Missing Values:** Cleaned and inspected null entries, particularly in open-ended responses.  
2. **Duplicates:** Verified that no duplicate rows exist in the dataset.  
3. **Outliers:** Identified outliers in survey years (2014 and 2019) based on participation rates.  

## **Analysis Highlights**

#### **Sampling Bias**
- **Age Distribution:** Respondents predominantly aged between 25–50, with fewer participants at extremes.  
- **Gender Representation:** Males accounted for ~70%, aligning with tech industry demographics.  
- **Race Distribution:** Majority identified as White, with limited representation from other racial groups.

#### **Mental Health Resources**
- **Trends Over Time:** Employers providing mental health resources increased significantly between 2014 and 2019.  
- **Current vs. Previous Employers:** Current employers show greater improvement compared to previous employers.

#### **Prevalence of Mental Health Issues**
- **Most Common Disorders:** Mood disorders, anxiety disorders, and ADHD were the most prevalent, with mood disorders affecting up to 31% of positively diagnosed respondents.

#### **Mental vs. Physical Health**
- **Employer Attitudes:** Employers placed greater importance on physical health but showed a positive trend in recognizing mental health concerns over time.  
- **Correlation Analysis:** Highlighted areas where mental health importance is improving alongside with physical health support.

## **Key Findings**

1. **Sampling Bias:** The dataset's open survey nature introduces bias, particularly in age, gender, and racial representation.  
2. **Resource Availability:** Current employers are progressively improving mental health resources, while previous employers lag significantly.  
3. **Prevalence Rates:** High-stress tech environments contribute to common mental health issues, with mood and anxiety disorders being most reported.  
4. **Physical vs. Mental Health:** Although physical health is still prioritized, the gap is narrowing with increasing mental health awareness campaigns.

## **Improvements and Future Work**    

1. **Address Sampling Bias**:
    - Recruit a more diverse group of respondents, particularly from underrepresented races and gender groups, to improve the dataset's representativeness.
    - Target outreach to older professionals in tech to ensure better age representation.

2. **Expand Longitudinal Analysis**:
    - Incorporate data beyond 2019 to observe trends in mental health awareness and resource allocation in the tech industry.

3. **Enhance Statistical Analysis**:
    - Apply weighting techniques to adjust for biases and improve the validity of findings.

4. **Improved Race Data**:
    - Encourage respondents to disclose their race to better understand diversity within the tech industry and its impact on mental health trends.

## Contributors
- [Erikas Leonenka](https://github.com/Vixamon)

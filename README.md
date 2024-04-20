# Mobile Store Data Analysis and Machine Learning Project
Quera Data Science Bootcamp / Winter 2024 / Team G5

## :bulb: Tools
<code><img title="Python" alt="python" width="35px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" /></code>
<code><img title="MySQL" alt="MySQL" width="35px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original-wordmark.svg" /></code>
<code><img title="Power BI" alt="Power BI" width="35px" src="https://github.com/microsoft/PowerBI-Icons/blob/main/PNG/Power-BI.png" /></code>

## 📌 Introduction

This project involves scraping, cleaning, and analyzing mobile store data from the [**GSM Arena**](https://www.gsmarena.com/). Utilizing multithreading for efficiency, the data was then structured into MySQL tables and imported using SQLAlchemy. Further, the project extends into implementing machine learning techniques, including classification, regression, and clustering, to derive actionable insights from mobile feature data. Outputs from these analyses were visualized using PowerBI to aid in decision-making processes.

## 🎯 Problem Statement

The mobile industry is rapidly evolving, necessitating up-to-date analysis to stay competitive. Our objective is to:
1. **Accurately Predict Consumer Preferences**: Use machine learning to predict trends and consumer preferences in the mobile market.
2. **Optimize Inventory and Pricing Strategy**: By understanding popular features and their impact on pricing, we aim to guide stores in inventory management.
3. **Enhance User Experience**: Apply clustering to segment users and tailor marketing strategies effectively.

## 🔍 Repository Structure

```
- Cleaning
  ├── Data Cleaning.ipynb [Cleaning scraped mobile data]
  ├── Cleaned_df.csv [Output of this step]
- Scrape
  ├── crawl_links.py [Script for crawling links]
  ├── scrape links.py [Script for storing all links]
  ├── scrape features multithread.py [Script for crawling links with multithreading]
  ├── AllLinks.csv [Output of 'scrape links.py']
  ├── Scraped_DataSet_MultiThread.csv [Output of 'scrape features multithread.py']
- DataBase
  ├── db_gsmarena.py [Script for setting up the database]
  ├── Data Base Structure.png [Shows structure of database]
  ├── Output_Tables.rar [Tables for creating database - it is the output of Cleaning/Data Cleaning.ipynb]
- Statistics
  ├── Descriptive statistics.ipynb [Notebook for descriptive statistical analysis]
  ├── Descriptive statistics.zip [Output of descriptive statistical analysis]
  ├── Hypo Test.ipynb [Notebook for Hypothesis statistical analysis]
- Machine Learning
  ├── Market_Q1_Clustering_KMeans_DBScan.ipynb [Notebook for clustering analysis]
  ├── Market_dataset_Q2_Q3_Classification_Regression.ipynb [Notebook for classification and regression analysis]
  - Powerbi [PowerBI dashboard directory for ML part]
      ├── ML_Powerbi.pbix [PowerBI dashboard file for ML part]
      ├── clf_result.csv [Input for PowerBI dashboard file]
      ├── reg_result.csv [Input for PowerBI dashboard file]
      ├── DataSet for powerbi.csv [Input for PowerBI dashboard file]
- PowerBI
  ├── Reports.pbix [PowerBI dashboard file]
- requirements.txt [Python dependencies for the project]
```

## 🚀 Getting Started

1. **Clone the Repository**:
```bash
git clone git@github.com:sinaaasghari/Mobile-Store.git
```

2. **Install Dependencies**:
```bash
pip install -r requirements.txt
```

3. **Data Scraping**:
   - Execute `Scrape/scrape links.py` to scrape links of mobiles in the GSM website.
   - Utilize `Scrape/crawl_links.py` for getting data of each link and doing any modifications needed during scraping.
   - Utilize `Scarpe/scrape features multithread.py` for doing the previous step in multithreading way. (optional)

4. **Database Setup and Import**:
   - Initialize your MySQL database system.
   - Use `Cleaning/Data Cleaning.ipynb` to set up tables from scraped data.
   - Use `DataBase/db_gsmarena.py` to import tables.

5. **Perform Analysis**:
   - Launch `Statistics/Descriptive statistics.ipynb` and `Statistics/Hypo Test.ipynb` to run statistical analysis.
   - Launch `Machine Learning/Market_dataset_Q2_Q3_Classification_Regression` and `Machine Learning/Market_Q1_Clustering_KMeans_DBScan.ipynb` to run Machine Learning analysis.

6. **Visualize Results**:
   - Open and explore the `PowerBI/Reports.pbix` to interact with visual data representations.

## 🤝 Feedback
We welcome any feedback, bug reports, and suggestions. Please let us know if you encounter any issues or have ideas for improvement.

## ⚽️ Meet Our Team 
  - [Zahra](https://github.com/ZahraTavakkol)
  - [Armaghan](https://github.com/ArmaghanAA)
  - [Mahdi](https://github.com/mahdibch)
  - [Reyhane](https://github.com/reyhane79)
  - [Mehran](https://github.com/M1994kh)

#### And special thanks to our mentor [Sina Asghari](https://github.com/sinaaasghari) for leading us through this project.

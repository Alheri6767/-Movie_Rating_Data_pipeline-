# Movie_Rating_Data_pipeline-
Creating a Datapipeline for jordan stream

## Problem Statement

JordanStream wants to improve customer recommendations using movie ratings data. The raw Netflix dataset contains missing values and inconsistent formats, making it unsuitable for direct analysis. This project builds a pipeline to clean the data, load it into PostgreSQL, and automate the process.

## Setup Instructions

1. Clone the repository:

   bash
   git clone https://github.com/yourusername/movie-ratings-pipeline.git
   cd movie-ratings-pipeline
   
2. Place the dataset (`netflix_titles.csv`) in the `data/` folder.
3. Start services:

   bash
   docker-compose up -d
   
4. Run the preprocessing and loading script:

   bash
   docker exec -it python-container python scripts/preprocessing.py
   
## Pipeline Steps

1. Extract: Load raw dataset with Pandas.
2. Transform: Handle missing values, clean text, remove duplicates, format dates.
3. Load: Create PostgreSQL table (if not exists) and insert cleaned data.
4. Automate: Use cron job (`run_pipeline.sh`) to run pipeline on schedule.

## Usage Guide

 To check if data is loaded into PostgreSQL:

  bash
  docker exec -it postgres-container psql -U postgres -d ETL
  

  sql
  SELECT COUNT(*) FROM netflix_titles;
  SELECT * FROM netflix_titles LIMIT 5;
  
  ## To schedule daily runs at midnight:

  bash
  0 0 * * * /path/to/run_pipeline.sh >> pipeline.log 2>&1
  


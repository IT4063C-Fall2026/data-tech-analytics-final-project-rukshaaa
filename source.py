#!/usr/bin/env python
# coding: utf-8

# # {Project Title}📝
# 
# ![Banner](./assets/banner.jpeg)
# 

# ## Topic
# 
# _What problem are you (or your stakeholder) trying to address?_
# 📝 <!-- Answer Below -->
# I'm exploring what factors contribute to quality of life across U.S. cities. People often
# compare cities based on cost of living, job opportunities, safety, education, transportation,
# and housing — but I want to use data to see how these factors actually vary and relate to
# each other. This matters because where someone lives affects their finances, career
# opportunities, education access, and overall wellbeing. Using data gives a more objective
# way to compare cities than anecdote or reputation alone.
# 

# ## Project Question
# 
# _What specific question are you seeking to answer with this project?_
# _This is not the same as the questions you ask to limit the scope of the project._
# 📝 <!-- Answer Below -->
# What relationships exist between economic conditions (income, unemployment), housing costs,
# crime rates, and public transit access across U.S. cities, and which factors are most
# strongly associated with overall quality of life?
# 

# ## What would an answer look like?
# 
# _What is your hypothesized answer to your question?_
# 📝 <!-- Answer Below -->
# I expect cities with higher median household income to have higher housing costs (rent),
# and lower unemployment. I also expect cities with lower crime rates to have stronger public
# transit systems and higher income levels. My answer will look like scatterplots (income vs.
# rent, population vs. unemployment), bar charts comparing crime and transit stats across
# cities, and a correlation heatmap showing which factors move together most strongly.
# 

# ## Data Sources
# 
# _What 3 data sources have you identified for this project?_
# _How are you going to relate these datasets?_
# 📝 <!-- Answer Below -->
# 
# 1. **U.S. Census Bureau ACS 5-Year API** (API) — city-level population, median household
#    income, poverty count, unemployment count, median gross rent, and educational attainment.
#    Pulled via `census_city_demographics.py`.
# 2. **Bureau of Labor Statistics API** (API) — national monthly CPI and unemployment rate,
#    used as a macroeconomic backdrop. Pulled via `bls_economic_data.py`.
# 3. **City Index file** (File, `city-index.csv`) — city-level infrastructure/transit data.
# 
# These relate through a shared **city + state** key (Census and city-index data), while the
# BLS national data is joined by **year** as a comparison backdrop rather than merged directly
# by city.
# 

# ## Approach and Analysis
# 
# _What is your approach to answering your project question?_
# _How will you use the identified data to answer your project question?_
# 📝 <!-- Start Discussing the project here; you can add as many code cells as you need -->
# I will load all three datasets into pandas, clean and standardize city/state naming so they
# can be merged, handle missing values, and merge the Census and city-index data on city and
# state. I'll then use NumPy/pandas to compute summary statistics and correlations, and use
# scatterplots, bar charts, and a correlation heatmap to explore relationships between income,
# housing cost, unemployment, crime, and transit access.
# 

# In[2]:


import pandas as pd

bls_df = pd.read_csv("bls_economic_data.csv")
census_df = pd.read_csv("census_city_demographics.csv")
city_index_df = pd.read_csv("city-index.csv")

bls_df.head()
census_df.head()
city_index_df.head()


# ## Resources and References
# 
# _What resources and references have you used for this project?_
# 📝 <!-- Answer Below -->
# 
# - U.S. Census Bureau, American Community Survey (ACS) 5-Year Estimates API documentation:
#   https://www.census.gov/data/developers/data-sets/acs-5year.html
# - U.S. Bureau of Labor Statistics, Public Data API documentation:
#   https://www.bls.gov/developers/
# - Federal Transit Administration, National Transit Database (NTD): annual reporting on
#   ridership, service levels, and operating metrics submitted by U.S. public transit agencies:
#   https://www.transit.dot.gov/ntd
# 

# In[ ]:





# In[ ]:





# In[ ]:


# ⚠️ Make sure you run this cell at the end of your notebook before every submission!
get_ipython().system('jupyter nbconvert --to python source.ipynb')


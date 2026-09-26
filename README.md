# Quality-of-life, Infrastructure and Economics Analysis Across U.S. Cities

## Project Overview

### Project Questions

1. **How do housing costs relate to median household income across cities?**
   a scatterplot of median rent vs. median household income per city, colored by
   region, to see if higher-income cities also have proportionally higher rent.

2. **What relationship exists between unemployment and city population size?**
   a scatterplot of population vs. unemployment count/rate, to see if larger cities
   trend toward higher or lower unemployment.

3. **How do crime rates and public transit access differ across cities?**
   a bar chart ranking cities by violent crime rate, layered against a bar chart of
   transit ridership (unlinked passenger trips) per city.

4. **What is the relationship between education levels and income/poverty?**
   a scatterplot of % population with a bachelor's degree vs. median household
   income and poverty rate.

5. **Are there patterns between affordability (income vs. rent) and other quality-of-life
   factors like crime and transit access?**
   a correlation heatmap across all merged variables (income, rent, crime rate,
   transit ridership, education) to see which factors move together.

6. **What factors appear most strongly associated with overall quality of life?**
   a ranked bar chart of correlation coefficients between each variable and a
   simple composite quality-of-life score constructed from the merged data.

### Data Sources

1. **U.S. Census Bureau ACS 5-Year API** (API) — city-level population, median household
   income, poverty count, unemployment count, median gross rent, and educational
   attainment. Pulled via `Dataset3.py`.
2. **FBI/city crime data** (file, `crime_data.json`) — violent crime rate, murder rate,
   property crime rate by city.
3. **National Transit Database** (file, `transit_data.csv`) — ridership and service stats
   by transit agency/city.
4. **Bureau of Labor Statistics API** (API) — national monthly CPI and unemployment rate,
   used as a macroeconomic backdrop. Pulled via `dataset4.py`.

**How they relate:** the Census, crime, and transit datasets all share a **city + state**
key and will be merged on that. The BLS dataset has no city column and will instead be
joined by **year**, to show how city-level trends compare against the national economic
picture over time.

## Self Assessment and Reflection

<!-- Edit the following section with your self assessment and reflection -->

### Self Assessment

<!-- Replace the (...) with your score -->

| Category          | Score   |
| ----------------- | ------- |
| **Setup**         | 10 / 10 |
| **Execution**     | 20 / 20 |
| **Documentation** | 10 / 10 |
| **Presentation**  | 30 / 30 |
| **Total**         | 70 / 70 |

### Reflection

<!-- Edit the following section with your reflection -->

#### What went well?

Successfully identifying three distinct datasets across two different ingestion methods (local CSV file and two REST APIs). The Census ACS API and BLS API integration successfully fetched and parsed demographic and economic indicators that join directly with the city infrastructure data.

#### What did not go well?

Setting up the API authentication for the Census Bureau required key activation troubleshooting.

#### What did you learn?

I learned how to query REST APIs programmatically using Python `requests`, parse JSON responses into pandas DataFrames, and structure multiple disparate datasets using shared relational keys (`City`, `State`, and `Year`).

#### What would you do differently next time?

I would set up virtual environments and handle data cleaning functions in modular Python scripts earlier in the workflow to streamline dataset integration from the start.

---

---

## Getting Started

### Installing Dependencies

To ensure that you have all the dependencies installed, and that we can have a reproducible environment, we will be using `pipenv` to manage our dependencies. `pipenv` is a tool that allows us to create a virtual environment for our project, and install all the dependencies we need for our project. This ensures that we can have a reproducible environment, and that we can all run the same code.

```bash
pipenv install
```

This sets up a virtual environment for our project, and installs the following dependencies:

- `ipykernel`
- `jupyter`
- `notebook`
- `black`
  Throughout your analysis and development, you will need to install additional packages. You can can install any package you need using `pipenv install <package-name>`. For example, if you need to install `numpy`, you can do so by running:

```bash
pipenv install numpy
```

This will update update the `Pipfile` and `Pipfile.lock` files, and install the package in your virtual environment.

## Helpful Resources:

- [Markdown Syntax Cheatsheet](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [Dataset options](https://it4063c.github.io/guides/datasets)

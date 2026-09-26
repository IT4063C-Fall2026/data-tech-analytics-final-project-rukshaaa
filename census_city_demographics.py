import pandas as pd
import requests

url = "https://api.census.gov/data/2022/acs/acs5"
api_key = "958f1c2e27eff45cbd525aaca5f20f5d41aad12c"

params = {
    "get": (
        "NAME,B01003_001E,B19013_001E,B17001_002E,B23025_005E,"
        "B25064_001E,B15003_001E,B15003_022E"
    ),
    "for": "place:*",
    "key": api_key,
}

print("Fetching data from US Census API...")
response = requests.get(url, params=params)

if response.status_code == 200:
    try:
        data = response.json()

        df = pd.DataFrame(data[1:], columns=data[0])

        df.rename(
            columns={
                "NAME": "full_location_name",
                "B01003_001E": "population",
                "B19013_001E": "median_household_income",
                "B17001_002E": "poverty_count",
                "B23025_005E": "unemployed_count",
                "B25064_001E": "median_gross_rent",
                "B15003_001E": "pop_25_plus",
                "B15003_022E": "bachelors_degree_count",
            },
            inplace=True,
        )

        numeric_cols = [
            "population",
            "median_household_income",
            "poverty_count",
            "unemployed_count",
            "median_gross_rent",
            "pop_25_plus",
            "bachelors_degree_count",
        ]
        for col in numeric_cols:
            df[col] = pd.to_numeric(df[col], errors="coerce")
        df[numeric_cols] = df[numeric_cols].where(df[numeric_cols] >= 0)

        df["pct_bachelors_degree"] = (
            df["bachelors_degree_count"] / df["pop_25_plus"] * 100
        ).round(2)

        df[["city", "state"]] = df["full_location_name"].str.extract(
            r"^(.*)\s(?:city|town|village|CDP|borough),\s(.*)$"
        )

        df.to_csv("census_city_demographics.csv", index=False)
        df.to_json("census_city_demographics.json", orient="records", indent=2)

        print(
            "Success! Saved to 'census_city_demographics.csv' and "
            "'census_city_demographics.json'."
        )
        print(
            df[
                [
                    "city",
                    "state",
                    "population",
                    "median_household_income",
                    "median_gross_rent",
                    "pct_bachelors_degree",
                ]
            ].head()
        )

    except Exception as e:
        print("Failed to decode JSON response.")
        print("Raw API Response text was:\n", response.text)
else:
    print(f"API Error. Status Code: {response.status_code}")
    print("Raw API Response text was:\n", response.text)
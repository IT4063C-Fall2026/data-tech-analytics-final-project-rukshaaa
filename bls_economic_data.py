import pandas as pd
import requests

url = "https://api.bls.gov/publicAPI/v2/timeseries/data/"
headers = {"Content-type": "application/json"}
payload = {
    "seriesid": ["CUUR0000SA0", "LNS14000000"],
    "startyear": "2020",
    "endyear": "2024",
}

print("Fetching economic data from BLS API...")
response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    json_data = response.json()

    records = []
    for series in json_data["Results"]["series"]:
        series_id = series["seriesID"]
        for item in series["data"]:
            records.append(
                {
                    "series_id": series_id,
                    "year": item["year"],
                    "period": item["period"],
                    "period_name": item["periodName"],
                    "value": float(item["value"]),
                }
            )

    df_bls = pd.DataFrame(records)

    # Save outputs locally
    df_bls.to_csv("bls_economic_data.csv", index=False)
    df_bls.to_json("bls_economic_data.json", orient="records", indent=2)

    print("Success! Saved to 'bls_economic_data.csv' and 'bls_economic_data.json'.")
    print(df_bls.head())
else:
    print(f"Failed to fetch data. Status Code: {response.status_code}")
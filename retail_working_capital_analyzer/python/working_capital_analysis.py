import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/cleaned_data/retail_working_capital_clean_ver.csv")

print(df.head())
print(df.info())

# Chart 1: Presenting the cash conversion cycle of each company between the years 2021 and 2025
for company in df["company"].unique():
    company_data = df[df["company"] == company].sort_values("fiscal_year")

    plt.plot(
        company_data["fiscal_year"],
        company_data["cash_conversion_cycle"],
        marker="o",
        label=company
    )

plt.title("Cash Conversion Cycle by Company (2021–2025)")
plt.xlabel("Fiscal Year")
plt.ylabel("Cash Conversion Cycle (Days)")
plt.xticks([2021, 2022, 2023, 2024, 2025])
plt.axhline(0, linewidth=1)
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("../dashboard/ccc_trend_2021_2025.png", dpi=300)
plt.show()


# Chart 2: Presenting the average DIO, DPO, and DSO
avg_metrics = (
    df.groupby("company")[["dio", "dpo", "dso"]]
    .mean()
    .round(2)
)

print(avg_metrics)

avg_metrics.plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Average Working Capital Metrics by Company")
plt.xlabel("Company")
plt.ylabel("Days")
plt.xticks(rotation=0)
plt.grid(axis="y")
plt.tight_layout()

plt.savefig("../dashboard/avg_working_capital_metrics.png", dpi=300)
plt.show()



ccc_2025 = (
    df[df["fiscal_year"] == 2025]
    .sort_values("cash_conversion_cycle")
)

plt.figure(figsize=(8, 5))

plt.bar(
    ccc_2025["company"],
    ccc_2025["cash_conversion_cycle"]
)

plt.title("2025 Cash Conversion Cycle by Company")
plt.xlabel("Company")
plt.ylabel("Cash Conversion Cycle (Days)")
plt.axhline(0, linewidth=1)
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("../dashboard/ccc_2025_comparison.png", dpi=300)
plt.show()
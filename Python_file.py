# Loading Dataset
import pandas as pd

info = pd.read_excel(r"C:\Users\sarayu\Downloads\top 100 insta followers dataset.xlsx")
print(info)

# Summary Statistics of rank, influence score, 60 days engagement rate
# print("statistics of rank", info[["rank(Ordinal)"]].describe())
# print("median of rank", info[["rank(Ordinal)"]].median())
# print("mode of rank", info[["rank(Ordinal)"]].mode())
# print("statistics of influence_score", info[["influence_score(Interval)"]].describe())
# print("median of influence_score", info[["influence_score(Interval)"]].median())
# print("mode of influence_score", info[["influence_score(Interval)"]].mode())
# print("statistics of 60_day_eng_rate", info[["60_day_eng_rate(Interval)"]].describe())
# print("median of 60_day_eng_rate", info[["60_day_eng_rate(Interval)"]].median())
# print("mode of 60_day_eng_rate", info[["60_day_eng_rate(Interval)"]].mode())


# Country with most number of top influencers
maxinflu_country = info.groupby('country(Nominal)')['country(Nominal)'].count().idxmax()
influ_count = info.groupby('country(Nominal)')['country(Nominal)'].count().max()
print("The country with most number of top instagram influencers is", maxinflu_country, "with", influ_count, 
"followers.")

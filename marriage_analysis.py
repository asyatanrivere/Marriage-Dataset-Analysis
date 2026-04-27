import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

df=pd.read_csv("dataset/marriage.csv")

print(df.head(10))
"""
   id  gender height   religion            caste mother_tongue                        profession               location          country  age_of_marriage
0   1  female   5'4"        NaN           others        Telugu                               NaN                 London   United Kingdom             21.0
1   2    male   5'7"       Jain       Shwetamber      Gujarati  Doctor / Healthcare Professional            Fairfax- VA              USA             32.0
2   3    male   5'7"      Hindu          Brahmin         Hindi         Entrepreneurs / Business               Begusarai            India             32.0
3   4  female   5'0"      Hindu           Thakur         Hindi                         Architect                 Mumbai            India             30.0
4   5    male   5'5"  Christian       Born Again     Malayalam    Sales Professional / Marketing        Sulthan Bathery            India             30.0
5   6    male   5'5"      Hindu          Valmiki         Hindi                         Sportsman                  Delhi            India             29.0
6   7  female   5'2"      Hindu   Rajput - Lodhi         Hindi              Banking Professional                Jodhpur            India             28.0
7   8    male   5'5"      Hindu           Bhatia       Punjabi         Entrepreneurs / Business               Faridabad            India             30.0
8   9  female   5'5"       Jain       Shwetamber      Gujarati             Software Professional               Vadodara            India             35.0
9  10  female   5'1"      Hindu          Billava          Tulu                   HR Professional  Bengaluru / Bangalore            India             32.0
"""
print(df.tail(10))
"""
        id  gender height   religion       caste mother_tongue             profession               location  country  age_of_marriage
2557  2558    male   5'5"        NaN      others         Hindi                Farming                 Nagpur    India             26.0
2558  2559    male   5'8"       Sikh      Khatri       Punjabi       Pilot / Co-Pilot                Toronto   Canada             30.0
2559  2560  female   5'3"       Sikh    Ramdasia       Punjabi            Not working                 Punjab    India             31.0
2560  2561  female    NaN        NaN      others       Kannada                Teacher  Bengaluru / Bangalore    India             24.0
2561  2562    male  5'11"      Hindu   Kshatriya          Odia    VP / AVP / GM / DGM                 Mumbai    India             30.0
2562  2563  female   5'3"      Hindu      Thakur         Hindi   Banking Professional                   Agra    India             27.0
2563  2564    male  5'11"      Hindu      Thakur         Hindi  Software Professional                 Ottawa   Canada             31.0
2564  2565  female   5'3"      Hindu     Baishya       Bengali    Software Consultant  Bengaluru / Bangalore    India             28.0
2565  2566  female  4'11"        NaN      others        Telugu            Not working              Hyderabad    India             26.0
2566  2567  female   5'2"  Christian    Marthoma     Malayalam  Software Professional                   Pune    India             32.0"""
print(df.describe())
"""
                id  age_of_marriage
count  2567.000000      2548.000000
mean   1284.000000        29.648352
std     741.173394         2.802414
min       1.000000        20.000000
25%     642.500000        28.000000
50%    1284.000000        30.000000
75%    1925.500000        32.000000
max    2567.000000        36.000000"""

print(df.info())
"""
<class 'pandas.DataFrame'>
RangeIndex: 2567 entries, 0 to 2566
Data columns (total 10 columns):
 #   Column           Non-Null Count  Dtype  
---  ------           --------------  -----  
 0   id               2567 non-null   int64  
 1   gender           2538 non-null   str    
 2   height           2449 non-null   str    
 3   religion         1932 non-null   str    
 4   caste            2425 non-null   str    
 5   mother_tongue    2403 non-null   str    
 6   profession       2237 non-null   str    
 7   location         2412 non-null   str    
 8   country          2551 non-null   str    
 9   age_of_marriage  2548 non-null   float64
dtypes: float64(1), int64(1), str(8)
memory usage: 200.7 KB
None"""

print(df.duplicated().sum()) # 0 --> no repeated row
print(df.isnull().sum())
"""
id                   0
gender              29
height             118
religion           635
caste              142
mother_tongue      164
profession         330
location           155
country             16
age_of_marriage     19
dtype: int64

we'll drop these rows"""

df.dropna(inplace=True)

df["height"]=df["height"].str.replace('"',"")
df["height"]=df["height"].str.replace("'",".")
df["height"]=df["height"].astype(float)
df["height"]=df["height"]*30.48
# Note: This conversion assumes values like 5'7" as 5.7 feet, which is not mathematically correct.
# A more accurate conversion would separately handle feet and inches.

df["age_of_marriage"]=df["age_of_marriage"].astype(int)

print(df.corr(numeric_only=True))
"""
                       id    height  age_of_marriage
id               1.000000  0.027677         0.006820
height           0.027677  1.000000         0.203399
age_of_marriage  0.006820  0.203399         1.000000

There is a weak positive correlation (~0.20) between height and age_of_marriage,
but it is not strong enough to indicate a meaningful relationship.
"""


# What can we say about the number of women and men who got married?
genders=df["gender"].value_counts()
sb.barplot(x=genders.index,y=genders.values)
plt.title("Number of Men And Women Who Got Married")
plt.xlabel("Genders")
plt.ylim(900,)
plt.grid()
plt.savefig("images/genders.png")
plt.show()
# The dataset shows a slightly higher number of males than females.
# However, this reflects the dataset distribution, not real-world proportions.


religions=df["religion"].value_counts()
sb.barplot(x=religions.index,y=religions.values)
plt.title("The Religions Of Those Getting Married")
plt.xlabel("Religions")
plt.grid()
plt.savefig("images/religions.png")
plt.show()
# The dataset is heavily dominated by Hindu individuals.
# This does NOT imply higher marriage rates, only that Hindus are more represented in this dataset.


castes=df["caste"].value_counts()
plt.figure(figsize=(9,8))
sb.barplot(y=castes.index,x=castes.values)
plt.title("Number of People Who Got Married by Caste")
plt.ylabel("Castes")
plt.grid(axis="x")
plt.tight_layout()
plt.savefig("images/caste.png")
plt.show()

# The distribution is uneven, with certain caste groups (e.g., Brahmin) appearing more frequently.
# This reflects representation in the dataset, not necessarily actual marriage preferences.


mother_tongues=df["mother_tongue"].value_counts()
plt.figure(figsize=(9,8))
sb.barplot(y=mother_tongues.index,x=mother_tongues.values)
plt.title("Number of People Who Got Married by Their Mother Tongues")
plt.ylabel("Mother Tongues")
plt.grid(axis="x")
plt.tight_layout()
plt.savefig("images/mother_tongues.png")
plt.show()

# Hindi appears most frequently, indicating the dataset is largely composed of individuals from Hindi-speaking regions.
# This suggests a geographical concentration (likely India), rather than a causal relationship with marriage.


df=df[df["profession"]!="Not Specified"]

jobs=df["profession"].value_counts().head(20)
plt.figure(figsize=(9,8))
sb.barplot(y=jobs.index,x=jobs.values)
plt.title("Number of People Who Got Married by Their Professions")
plt.ylabel("Professions")
plt.grid(axis="x")
plt.tight_layout()
plt.savefig("images/professions.png")
plt.show()

# Some professions appear more frequently, including "Not working".
# This does not imply causation between profession and marriage, only dataset representation differences.


countries=df["country"].value_counts().head(10)
sb.barplot(y=countries.index,x=countries.values)
plt.title("Number of People Who Got Married by Countries")
plt.ylabel("Countries")
plt.grid(axis="x")
plt.tight_layout()
plt.savefig("images/country.png")
plt.show()

# India dominates the dataset, indicating strong sampling bias toward that country.
# This does not reflect actual global marriage rates.


locations=df["location"].value_counts().head(20)
sb.barplot(y=locations.index,x=locations.values)
plt.title("Number of People Who Got Married by Locations")
plt.ylabel("Locations")
plt.grid(axis="x")
plt.tight_layout()
plt.savefig("images/locations.png")
plt.show()

# Most locations are from India, confirming the dataset is geographically concentrated.
# Other countries appear but with significantly lower representation.


gendervsageofmarriage=df.groupby("age_of_marriage")["gender"].value_counts().reset_index(name="counts")
plt.figure(figsize=(8,8))
sb.lineplot(data=gendervsageofmarriage, x="age_of_marriage", y="counts",hue="gender")
plt.title("Age Of Marriage by Genders")
plt.xlabel("Age Of Marriage")
plt.tight_layout()
plt.grid()
plt.savefig("images/ageofmarriage_by_genders.png")
plt.show()

# This visualization shows how marriage counts vary by age for each gender.
# It is not a true normal distribution, but it suggests that women tend to marry slightly earlier than men on average.


print(df.groupby("gender")["age_of_marriage"].max())
"""
gender
female    36
male      36
Name: age_of_marriage, dtype: int64

Both genders have the same maximum recorded marriage age in this dataset.
"""
print(df.groupby("gender")["age_of_marriage"].min())
"""
gender
female    24
male      26
Name: age_of_marriage, dtype: int64

The minimum marriage age differs slightly between genders (about 2 years),
indicating women tend to marry earlier in this dataset.
"""

minagebyreligion=df.groupby("religion")["age_of_marriage"].min().sort_values(ascending=True)
plt.figure(figsize=(5,5))
sb.barplot(x=minagebyreligion.index, y=minagebyreligion.values)
plt.title("Min Age Of Marriage by Religions")
plt.ylabel("Min Age Of Marriage")
plt.xlabel("Religions")
plt.tight_layout()
plt.grid()
plt.savefig("images/minageofmarriage_by_religions.png")
plt.show()

# This shows the minimum observed marriage age per religion.
# However, minimum values are sensitive to outliers and do not represent general trends.
# Median or mean would provide more reliable insights.


minagebycountry=df.groupby("country")["age_of_marriage"].min().sort_values(ascending=True)
plt.figure(figsize=(5,5))
sb.barplot(y=minagebycountry.index, x=minagebycountry.values)
plt.title("Min Age Of Marriage by Country")
plt.xlabel("Min Age Of Marriage")
plt.ylabel("Countries")
plt.tight_layout()
plt.grid()
plt.savefig("images/minageofmarriage_by_countries.png")
plt.show()

# This visualization shows minimum marriage age by country.
# It does NOT represent marriage rates.
# Differences may be due to dataset size and sampling bias rather than real-world patterns.
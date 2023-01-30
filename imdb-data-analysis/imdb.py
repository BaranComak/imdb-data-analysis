import numpy as np
import pandas as pd
#
df = pd.read_csv("imdb.csv")


result = df.head()

result = df.head(10)

result = df.tail()

result = df.tail(10)

result = df["Title"]
result = df.agg("Title") # Pratik Yol

result = df["Title"].head()
result = df.agg("Title").head() # Pratik Yol

result = df[["Title","Rated"]].head()

result = df[["Title","Rated"]].tail(7)


result = df[5:10][["Title","Rated"]]
result = df[5:15][["Title","Rated"]].head()


result = df[(df["imdbRating"]>8.0)].head(50)[["Title","Rated","imdbRating"]]
result = df.query("imdbRating > 8.0").head(50)[["Title","Rated","imdbRating"]]


result = df[(df["Year"]==2014) | (df["Year"]==2015)][["Title","Year"]]
result = df.query("Year == 2014 | Year == 2015")[["Title","Year"]]


result = df[(df["imdbRating"] >=8 ) & (df["imdbRating"]<=9)][["Title","imdbRating"]]
result = df.query("imdbRating >=8 & imdbRating <=9")[["Title","imdbRating"]]














print(result)
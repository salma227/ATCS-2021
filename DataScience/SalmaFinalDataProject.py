#
# Salma Siddiqui
# December 7, 2021
#
import pandas as pd
import matplotlib.pyplot as plt

#data sheet
df = pd.read_csv("./north_america_bear_killings.csv")
#locations --> countries dataset
dfc = pd.read_csv("./ATCS states data - Sheet1.csv")
#months --> seasons dataset
dfs = pd.read_csv("seasons.csv")
#cleaning up the data and combining the three sets
pd.set_option("display.max_columns", None)
df = df.drop(["Name", "Date", "Description", "Grizzly"], axis=1)
df["Location"] = df["Location"].str.split(", ").str[1]
df2 = pd.merge(df, dfc, how="inner", left_on="Location", right_on="state")
df3 = pd.merge(df2, dfs, how="inner", left_on="Month", right_on="month")


#pie chart of captive vs wild bears
df4 = df.groupby("Type").count()
df4.plot.pie(y="Type of Bear", labels=df4.index)
plt.show()

#pie chart of attacks by country
df5 = df3.groupby("country").count()
df5.plot.pie(y="Location", labels=df5.index)
plt.show()

#pie chart of attacks by season
df6 = df3.groupby("season").count()
axis = df6.plot.pie(y="Location", labels=df6.index, legend =None)
axis.set_ylabel("season")
plt.show()

#boxplot of age
df3["age"].plot(kind="box")
plt.show()

#bar chart of hunters or not
df7 = df3.groupby("Hunter").count()
axis1 = df7.plot.bar(y="Hikers", color=("firebrick", "mediumseagreen"), legend=None)
axis1.set_xlabel("Hunters")
plt.show()

#bar chart of hiker or not
df8 = df3.groupby("Hikers").count()
axis = df8.plot.bar(y="Hunter", color=("lightcoral", "darkseagreen"), legend=None)
axis.set_xlabel("Hikers")
plt.show()

#bar chart year of attack
df9 = df3.groupby("Year").count()
df9.plot.bar(y="Hunter", legend=None)
plt.show()

#bar chart of hiker or not
df10 = df3.groupby("Only one killed").count()
df10.plot.bar(y="Hunter", color=("cadetblue", "darkkhaki"), legend=None)
plt.show()


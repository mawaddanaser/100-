import pandas as pd
import numpy as np

table = [
    ["mawadda", 23, "data engineer"],
    ["muhammed", 24, "backend engineer"],
]

s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(s)

# Date range
dates = pd.date_range("20130101", periods=6)
# print(dates)


df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
# print(df)

# dataframe dict
df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
# print(df2)
print(df2.dtypes)
print(df2.columns)
print(type(df2))
print(df2.head(1))
print("hamody")
print(df2.tail(1))
print(df2.to_numpy())

# Selection
# df.A = df["A"]
# df[0:3]
# df["20130102":"20130104"]
# In a DataFrame, each row and column has an associated label, which is typically either a string or an integer.
# These labels serve as identifiers for the rows and columns of the DataFrame.

import pandas as pd

file = "SMSSpamCollection"

df = pd.read_csv(
    file,
    sep="\t",
    header=None,
    names=["label", "text"]
)

print("Total messages:", len(df))
print(df.head())

df.to_csv("spam.csv", index=False)

print("✅ spam.csv created")
import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("spam.csv")

print(df.head())

# Convert labels to numbers
df["label"] = df["label"].map({
    "ham": 0,
    "spam": 1
})

# Features and labels
X = df["text"]
y = df["label"]

# Convert text into numbers
vectorizer = TfidfVectorizer(stop_words="english")

X = vectorizer.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = MultinomialNB()

model.fit(X_train, y_train)

# Test accuracy
prediction = model.predict(X_test)

accuracy = accuracy_score(y_test, prediction)

print(f"Accuracy : {accuracy*100:.2f}%")

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save vectorizer
with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ model.pkl created")
print("✅ vectorizer.pkl created")
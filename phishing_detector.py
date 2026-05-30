import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt

# Sample Dataset
data = {
    "email": [
        "Congratulations! You won a free iPhone. Click here now",
        "Your bank account has been suspended. Verify immediately",
        "Meeting scheduled tomorrow at 10 AM",
        "Project report submitted successfully",
        "Claim your lottery prize now",
        "Team meeting postponed to Friday",
        "Update your password urgently",
        "Invoice attached for your purchase"
    ],
    "label": [
        "Phishing",
        "Phishing",
        "Safe",
        "Safe",
        "Phishing",
        "Safe",
        "Phishing",
        "Safe"
    ]
}

df = pd.DataFrame(data)

# Convert labels to numeric
df["label"] = df["label"].map({"Safe": 0, "Phishing": 1})

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    df["email"], df["label"], test_size=0.3, random_state=42
)

# Feature Extraction
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train Model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Predictions
y_pred = model.predict(X_test_vec)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", round(accuracy * 100, 2), "%")

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print(cm)

# Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Test Custom Email
email = input("\nEnter Email Content: ")
email_vec = vectorizer.transform([email])

prediction = model.predict(email_vec)

if prediction[0] == 1:
    print("Result: PHISHING EMAIL")
else:
    print("Result: SAFE EMAIL")

# Plot Confusion Matrix
plt.imshow(cm)
plt.title("Confusion Matrix")
plt.colorbar()
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

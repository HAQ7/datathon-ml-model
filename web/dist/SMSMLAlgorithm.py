import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load your dataset with the correct encoding
data = pd.read_csv("spam.csv", encoding="ISO-8859-1")

# Data preprocessing
data["v1"] = data["v1"].map({"ham": 0, "spam": 1})

# Text preprocessing
tfidf_vectorizer = TfidfVectorizer()
X = tfidf_vectorizer.fit_transform(data["v2"])
y = data["v1"]

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model building
model = LogisticRegression()
model.fit(X_train, y_train)

# Model evaluation
y_pred = model.predict(X_test) 

def classify_text(input_text):
    # Preprocess the input text using the same TF-IDF vectorizer
    input_text_transformed = tfidf_vectorizer.transform([input_text])
    # Predict using the trained model
    prediction = model.predict(input_text_transformed)
    # Convert prediction label to 'spam' or 'ham'
    result = 'spam' if prediction[0] == 1 else 'ham'
    return result

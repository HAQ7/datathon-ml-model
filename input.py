from EmailMLAlgorithm import classify_text

input_text = "https://briefingday.us8.list-manage.com/unsubscribe"
classification_result = classify_text(input_text)
print("Classification Result:", classification_result)
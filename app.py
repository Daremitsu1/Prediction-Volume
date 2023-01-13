# 1. Import necessary libraries
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd 
import streamlit as st

# 2. Load the data
def load_data():
    data = pd.read_csv("sales_data.csv")
    return data

# 3. Build the Model
def build_model(data):
    # Split the data into features and target
    X = data[["Order_Quantity", "Unit_Cost", "Unit_Price"]]
    y = data["Product_Category"]

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the model
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    return clf, X_train, X_test, y_train, y_test

# 4. Evaluate the model
def evaluate_model(clf, X_test, y_test):
    # Make predictions
    y_pred = clf.predict(X_test)
    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy

# 5. Streamlit app
def run():
    # Load the data
    data = load_data()
    # Build the model
    clf, X_train, X_test, y_train, y_test = build_model(data)
    # Evaluate the model
    accuracy = evaluate_model(clf, X_test, y_test)
    st.write("Accuracy: ", accuracy)

    # Create a sidebar for uploading test data
    uploaded_file = st.sidebar.file_uploader("Upload a test file in csv format", type=["csv"])
    if uploaded_file is not None:
        test_data = pd.read_csv(uploaded_file)
        test_X = test_data[["Order_Quantity", "Unit_Cost", "Unit_Price"]]
        # Make predictions
        test_predictions = clf.predict(test_X)
        # Add the predictions to the test data
        test_data["Product_Category"] = test_predictions
        # Visualize the results
        st.line_chart(test_data.groupby(["Product_Category"]).count()["Order_Quantity"])
        # Download the predictions
        st.write("Download predictions")
        st.dataframe(test_data)

if __name__ == '__main__':
    run()

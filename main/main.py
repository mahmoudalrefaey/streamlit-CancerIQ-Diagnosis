import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import pickle



def get_data_clean():

    # Read the data
    data = pd.read_csv(r"D:\Cancer-App\dataset\data.csv")

    # Clean the data
    data = data.drop(['Unnamed: 32', 'id'], axis=1)
    data['diagnosis'] = [1 if value == "M" else 0 for value in data['diagnosis']]
    return data

def create_model(data):
    
    # Split data to X, y
    X = data.drop(['diagnosis'], axis=1)
    y = data['diagnosis']

    # Scale the data
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    #Split trainig and testing
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # Train the model with Logistic Regression
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # Test the model
    y_pred = model.predict(X_test)
    
    # Model Evaluation
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy: .2f}")
    print(f"Classification report: \n {classification_report(y_pred, y_test)}")
    return model, scaler

def main():
    data = get_data_clean()
    model, scaler = create_model(data)
    with open('D:\Cancer-App\main\model.pkl', 'wb') as f:
        pickle.dump(model, f)
    with open('D:\Cancer-App\main\scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)
        
        
if __name__ == '__main__':
    main()
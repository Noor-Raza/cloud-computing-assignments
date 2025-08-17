import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.impute import SimpleImputer

file_path = '/Users/noor/Downloads/hotel_bookings.csv'
df = pd.read_csv(file_path)

df.describe()

df.info()

df.shape

# Identify duplicate rows
duplicates = df[df.duplicated()]

duplicates

# Count the number of duplicate rows
print(f"Number of duplicate rows: {len(duplicates)}")

# Remove duplicate rows
df_no_duplicates = df.drop_duplicates()

print(f"Number of rows after removing duplicates: {len(df_no_duplicates)}")

# Step 1: Preprocess the Data
# Features and target
features = ['lead_time', 'previous_cancellations', 'total_of_special_requests', 'adr', 'stays_in_week_nights']
target = 'is_canceled'

# Remove duplicates
df_no_duplicates = df_no_duplicates[features + [target]]

# Handle missing values
imputer = SimpleImputer(strategy='median')  # Replace missing values with the median
df_no_duplicates[features] = imputer.fit_transform(df_no_duplicates[features])  # Impute features
df_no_duplicates = df_no_duplicates.dropna(subset=[target])  # Drop rows with missing target values

# Define X (features) and y (target)
X = df_no_duplicates[features]
y = df_no_duplicates[target]

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 2: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Step 3: Train the Logistic Regression Model
# Initialize the logistic regression model with class imbalance handling
logistic_model = LogisticRegression(class_weight='balanced', random_state=42)
logistic_model.fit(X_train, y_train)

# Step 4: Evaluate Initial Model
# Predict on the test set
y_pred = logistic_model.predict(X_test)

# Print initial evaluation metrics
print("Initial Logistic Regression Model Performance:")
print("Coefficients:", logistic_model.coef_)
print("Intercept:", logistic_model.intercept_)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
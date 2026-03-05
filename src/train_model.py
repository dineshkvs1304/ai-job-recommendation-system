import joblib
from sklearn.neighbors import NearestNeighbors
from data_preprocessing import load_data
from feature_engineering import create_feature_matrix


def train_model():

    # Load dataset
    df = load_data()

    # Convert skills into ML features
    feature_matrix, vectorizer = create_feature_matrix(df)

    # Create recommendation model
    model = NearestNeighbors(n_neighbors=3, metric="cosine")

    # Train the model
    model.fit(feature_matrix)

    # Save the trained model
    joblib.dump(model, "model/job_recommendation_model.pkl")

    # Save the vectorizer
    joblib.dump(vectorizer, "model/vectorizer.pkl")

    print("Model trained and saved successfully")


if __name__ == "__main__":
    train_model()
import pandas as pd
from feature_engineering import create_feature_matrix


def load_data():

    # Load dataset
    df = pd.read_csv("data/jobs_dataset.csv")

    return df


if __name__ == "__main__":

    df = load_data()

    features, vectorizer = create_feature_matrix(df)

    print("Dataset loaded successfully")
    print("Feature matrix shape:", features.shape)
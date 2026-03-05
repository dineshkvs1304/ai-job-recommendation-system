import joblib
import pandas as pd


# Load trained model and vectorizer
model = joblib.load("model/job_recommendation_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

# Load job dataset
df = pd.read_csv("data/jobs_dataset.csv")


def recommend_jobs(user_skills):

    # Convert user skills to vector
    user_vector = vectorizer.transform([user_skills])

    # Find similar jobs
    distances, indices = model.kneighbors(user_vector)

    # Extract job titles
    recommended_jobs = df.iloc[indices[0]]["job_title"].tolist()

    return recommended_jobs


if __name__ == "__main__":

    skills = input("Enter your skills: ")

    results = recommend_jobs(skills)

    print("\nRecommended Jobs:")
    
    for job in results:
        print("-", job)
from sklearn.feature_extraction.text import TfidfVectorizer


def create_feature_matrix(df):
    
    # Extract the skills column
    skills = df["skills"]

    # Create TF-IDF vectorizer
    vectorizer = TfidfVectorizer()

    # Convert skills text into numerical features
    skill_matrix = vectorizer.fit_transform(skills)

    return skill_matrix, vectorizer
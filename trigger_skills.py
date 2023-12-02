import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def read_skills_from_csv(csv_path='skills.csv'):
    df = pd.read_csv(csv_path)
    return df['skills'].tolist()

def preprocess_text(text):
    # You can add your text preprocessing logic here
    return text.lower()

def trigger_skills(description):
    skills_list = read_skills_from_csv()

    description = preprocess_text(description)
    skills_list = [preprocess_text(skill) for skill in skills_list]

    # Create a tfidfVectorizer instance
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform([description] + skills_list)
    cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    target_skills = []
    for i, similarity in enumerate(cosine_similarities):
        if similarity >= 0.2:  # Threshold taken as 20%
            target_skills.append(skills_list[i])

    print("The target skills are: ", target_skills)
    return target_skills

if __name__ == "__main__":
    user_input = input("Enter a description: ")
    trigger_skills(user_input)

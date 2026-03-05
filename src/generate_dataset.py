import pandas as pd
import random

job_titles = [
    "Machine Learning Engineer",
    "Data Scientist",
    "AI Engineer",
    "Data Analyst",
    "Backend Developer",
    "Cloud Engineer",
    "DevOps Engineer",
    "NLP Engineer",
    "Computer Vision Engineer",
    "Software Engineer"
]

skills_list = [
    "python machine learning tensorflow sql",
    "python pandas statistics machine learning",
    "python deep learning pytorch nlp",
    "excel sql python visualization",
    "java spring sql microservices",
    "aws cloud infrastructure python",
    "docker kubernetes ci cd aws",
    "python nlp transformers deep learning",
    "python opencv cnn deep learning",
    "java dsa algorithms system design"
]

domains = [
    "AI",
    "Data Science",
    "Software",
    "Analytics",
    "Cloud",
    "DevOps"
]


rows = []

for i in range(10000):

    job = random.choice(job_titles)
    skills = random.choice(skills_list)
    domain = random.choice(domains)
    experience = random.randint(0,5)

    rows.append([job, skills, domain, experience])


df = pd.DataFrame(rows, columns=["job_title","skills","domain","experience"])

df.to_csv("data/jobs_dataset.csv", index=False)

print("Large dataset generated successfully")
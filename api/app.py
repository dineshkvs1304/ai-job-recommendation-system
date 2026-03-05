from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.recommend import recommend_jobs

app = FastAPI()

# Enable CORS so frontend can call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Job Recommendation API running"}

@app.get("/recommend")
def recommend(skills: str):

    jobs = recommend_jobs(skills)

    return {"recommended_jobs": jobs}
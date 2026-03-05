async function getRecommendations() {

    const skills = document.getElementById("skills").value;

    const response = await fetch(
        `http://127.0.0.1:8000/recommend?skills=${skills}`
    );

    const data = await response.json();

    const results = document.getElementById("results");

    results.innerHTML = "";

    data.recommended_jobs.forEach(job => {

        const li = document.createElement("li");

        li.className = "job-card";

        li.textContent = job;

        results.appendChild(li);

    });

}
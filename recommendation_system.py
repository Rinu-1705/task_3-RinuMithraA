from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Extended dataset of job roles
items = {
    "Data Scientist": "Python SQL Machine Learning AWS Statistics Data Analysis",
    "DevOps Engineer": "AWS Docker Kubernetes CI/CD Terraform Cloud Automation",
    "Backend Developer": "Java Python SQL APIs Spring Hibernate Microservices",
    "System Admin": "Linux Networking Automation Cloud Security Shell Scripting",
    "Frontend Developer": "HTML CSS JavaScript React Angular UI UX",
    "Mobile Developer": "Java Kotlin Swift Flutter Android iOS",
    "AI Engineer": "Python TensorFlow PyTorch Machine Learning Deep Learning NLP",
    "Cloud Architect": "AWS Azure GCP Cloud Security DevOps Infrastructure",
    "Cybersecurity Analyst": "Security Networking Firewalls Encryption Penetration Testing",
    "Database Administrator": "SQL Oracle MySQL PostgreSQL Data Modeling Performance Tuning"
}

# Step 1: Take user skills interactively
user_input = input("Enter your skills (space-separated): ")
user_profile = user_input

# Step 2: Vectorization
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform([user_profile] + list(items.values()))

# Step 3: Scoring
scores = cosine_similarity(vectors[0], vectors[1:]).flatten()

# Step 4: Sorting & Filtering
ranked = sorted(zip(items.keys(), scores), key=lambda x: x[1], reverse=True)
top_n = ranked[:3]

print("\nTop Recommendations:")
for role, score in top_n:
    print(f"{role} (score: {score:.2f})")

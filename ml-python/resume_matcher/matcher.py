from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def match_resume(resume_text, jd_text):
    documents=[resume_text, jd_text]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    score=cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return round(float(score[0][0])*100, 2)
if __name__ == "__main__":
    resume="Python machine learning sql data analysis"
    jd="Python deep learning tensorflow sql"
    result=match_resume(resume,jd)
    print(f"Resume match score: {result}%")
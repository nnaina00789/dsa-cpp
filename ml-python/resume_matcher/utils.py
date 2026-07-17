import string 
def clean_text(text):
    text=text.lower()
    text="".join(ch for ch in text if ch not in string.punctuation)
    text=" ".join(text.split())
    return text
def get_keywords(text):
    words=clean_text(text).split()
    unique_words=list(dict.fromkeys(words))
    return unique_words
def get_missing_skills(resume_text,jd_text):
    resume_keywords=set(get_keywords(resume_text))
    jd_keywords=set(get_keywords(jd_text))
    missing=jd_keywords-resume_keywords
    return list(missing)
if __name__=="__main__":
    sample="Hello, World! This is a sample text."
    print("Cleaned Text:", clean_text(sample))
    print("Keywords:", get_keywords(sample))

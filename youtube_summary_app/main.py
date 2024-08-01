import re
import nltk
from youtube_transcript_api import YouTubeTranscriptApi
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from googleapiclient.discovery import build

# YouTube API credentials
API_KEY = # ENTER YOUR YOUTUBE API KEY
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# Setup YouTube API client
try:
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)
except Exception as e:
    print(f"Error setting up YouTube API client: {e}")
    exit(1)

# Get English stopwords
stop_words = set(stopwords.words('english'))

def extract_video_id(url):
    pattern = r"(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=))([\w\-]+)"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        return None

def get_video_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([line["text"] for line in transcript])
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return ""

def summarize_text(text):
    if not text:
        return "No transcript available."
    
    # Tokenize text into words and sentences
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    
    # Remove certain punctuation marks
    words = [word for word in words if word.isalpha() or word in ["'", "-"]]
    
    # Remove stopwords
    words = [word for word in words if word.lower() not in stop_words]
    
    # Calculate sentence scores using TF-IDF
    from sklearn.feature_extraction.text import TfidfVectorizer
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(sentences)
    scores = tfidf_matrix.toarray().sum(axis=1)
    
    # Select top-scoring sentences as summary
    summary_sentences = []
    for i in range(min(3, len(scores))):
        idx = scores.argmax()
        summary_sentences.append(sentences[idx])
        scores[idx] = -1  # Set to -1 to avoid re-selecting the same sentence
    return "".join(summary_sentences)

def main():
    url = input("\nENTER YOUR YOUTUBE VIDEO URL: ")
    video_id = extract_video_id(url)
    if video_id:
        transcript = get_video_transcript(video_id)
        summary = summarize_text(transcript)
        print(f"\nHere is the summary:\n-------------------------------------------------------\n{summary}")
    else:
        print("Invalid YouTube video URL")

if __name__ == "__main__":
    main()
    

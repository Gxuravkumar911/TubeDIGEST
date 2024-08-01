TubeDIGEST

YouTube Video Summary Web App

TubeDigest is a web application that provides concise summaries of YouTube videos using AI-powered natural language processing techniques.

Technologies Used:-
- Python: Backend programming language
- Django: Web framework for building and maintaining the web application
- NLTK: Natural Language Toolkit for text processing and tokenization
- YouTube API: For fetching video transcripts and metadata
- scikit-learn: Machine learning library for building and training the summarization model
- TF-IDF: Term Frequency-Inverse Document Frequency algorithm for calculating sentence scores

How it Works:-
1. User enters a YouTube video URL
2. TubeDigest fetches the video transcript using the YouTube API
3. NLTK is used for text processing and tokenization
4. scikit-learn and TF-IDF are used to build and train a summarization model
5. The model extracts the most important sentences from the transcript
6. The summary is displayed on the web page

Features:-
- Automatic summarization of YouTube videos
- Easy-to-use web interface
- Fast and efficient summarization algorithm

Installation:
1. Clone the repository: git clone https://github.com/your-username/TubeDigest.git
2. Install dependencies: pip install -r requirements.txt
3. Run the app: python manage.py runserver

Contributing

Contributions are welcome! Please submit a pull request with your changes.

License

MIT License

Author:
Gaurav Kumar

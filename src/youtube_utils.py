import re
from youtube_transcript_api import YouTubeTranscriptApi

# Extract the YouTube video ID from a URL
def extract_youtube_id(url):
    pattern = r'(?:v=|\/)([0-9A-Za-z_-]{11}).*'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        raise ValueError('Invalid YouTube URL')

# Get the transcript of a YouTube video
def get_transcript(video_id):
    try:
        # Create an instance and use fetch directly
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id, languages=['en'])
        
        # Extract text from snippets
        full_text = " ".join([snippet.text for snippet in transcript.snippets])
        return full_text
    except Exception as e:
        raise Exception(f"Could not retrieve transcript: {e}")
    
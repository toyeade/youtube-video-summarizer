from youtube_utils import extract_youtube_id, get_transcript
from openai_utils import summarize_with_gpt
import os
from dotenv import load_dotenv

load_dotenv()

# Main function
def main():
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    api_key = os.getenv('OPENAI_API_KEY')
    
    try:
        video_id = extract_youtube_id(video_url)
        transcript = get_transcript(video_id)
        summary = summarize_with_gpt(transcript, api_key)
        print("Video Summary:\n", summary)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
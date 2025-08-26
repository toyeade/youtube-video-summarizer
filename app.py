from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from src.youtube_utils import extract_youtube_id, get_transcript
from src.openai_utils import summarize_with_gpt, create_enhanced_summary

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        data = request.get_json()
        video_url = data.get('url')
        
        if not video_url:
            return jsonify({'error': 'URL is required'}), 400
        
        # Extract video ID and get transcript
        video_id = extract_youtube_id(video_url)
        transcript = get_transcript(video_id)
        
        # Get API key
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            return jsonify({'error': 'OpenAI API key not configured'}), 500
        
        # Create enhanced summary with highlights and bullet points
        enhanced_summary = create_enhanced_summary(transcript, api_key)
        
        return jsonify({
            'success': True,
            'video_id': video_id,
            'transcript': transcript,
            'summary': enhanced_summary
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
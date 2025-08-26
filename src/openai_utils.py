from openai import OpenAI

# Make a prompt for the summary
def make_summary_prompt(transcript):
    return f"Summarize the following YouTube video transcript in 5-7 sentences:\n\n{transcript[:3500]}"

# Summarize the transcript with GPT
def summarize_with_gpt(transcript, api_key):
    client = OpenAI(api_key=api_key)
    prompt = make_summary_prompt(transcript)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300
    )
    return response.choices[0].message.content.strip()


# Enhanced prompt for detailed summary with highlights
def make_enhanced_summary_prompt(transcript):
    return f"""
    Analyze the following YouTube video transcript and provide a comprehensive summary with the following structure:
    
    1. **Main Topic**: What is this video about?
    2. **Key Highlights**: List 3-5 most important points (use bullet points)
    3. **Summary**: Provide a 5-7 sentence summary of the content
    4. **Key Takeaways**: List 3-4 actionable insights or important conclusions
    
    Transcript:
    {transcript[:4000]}
    
    Format your response in HTML with proper headings and bullet points.
    """

# Create enhanced summary with highlights and bullet points
def create_enhanced_summary(transcript, api_key):
    client = OpenAI(api_key=api_key)
    prompt = make_enhanced_summary_prompt(transcript)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=800
    )
    return response.choices[0].message.content.strip()
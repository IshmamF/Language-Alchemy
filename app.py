import streamlit as st
#from youtube_transcript_api import YouTubeTranscriptApi as yta
#import re

with st.container():
    st.subheader("LingoAlchemy.yt")

user_text = st.text_input("Input URL here", "https://www.youtube.com")

def extract_video_id(url):
    # Splitting the URL by the 'v=' parameter
    split_url = url.split('v=')
    
    # Checking if the URL format is valid for extraction
    if len(split_url) > 1:
        # Getting the part after 'v=' which should be the video ID
        video_id = split_url[1]
        
        # Extracting only the video ID (removing any additional parameters)
        video_id = video_id.split('&')[0]
        
        return video_id
    else:
        return "Invalid YouTube URL format"

video_id = extract_video_id(user_text)
video_id = 'your_youtube_video_id_here'

# YouTube video URL
youtube_url = f'https://www.youtube.com/watch?v={video_id}'

st.write("Embedded Video:")
#video_display = YouTubeVideo(video_id)
#st.write(video_display)
st.video(user_text)


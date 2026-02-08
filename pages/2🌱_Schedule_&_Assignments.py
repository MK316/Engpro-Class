import streamlit as st
import requests

tabs = st.tabs(["💧 Hey Jude", "Todolist", "💧 Schedule"])


##############################
# Content for the Schedule tab
with tabs[0]:
    st.markdown("### 🎼  Hey Jude (HW #4)")

    # Define the URLs for the YouTube videos
    st.markdown("#### 1. Hey Jude (Beatles)")
    video_url1 = "https://www.youtube.com/embed/mQER0A0ej0M?si=eSi7vtIJzot9cqAf"
    st.video(video_url1, format="video/mp4", start_time=0)

    st.markdown("---")
    st.markdown("""
    #### 🎼 Lyrics

    1.  
    Hey Jude, don't make it bad.  
    Take a sad song and make it better.  
    Remember to let her into your heart,  
    Then you can start to make it better.  
    
    2.  
    Hey Jude, don't be afraid.  
    You were made to go out and get her.  
    The minute you let her under your skin,  
    Then you begin to make it better.  

    3.  
    And anytime you feel the pain, hey Jude, refrain,  
    Don't carry the world upon your shoulders.  
    For well you know that it's a fool who plays it cool  
    By making his world a little colder.  

    4.  
    Hey Jude, don't let me down.  
    You have found her, now go and get her.  
    Remember to let her into your heart,  
    Then you can start to make it better.  
    
    5.  
    So let it out and let it in, hey Jude, begin,  
    You're waiting for someone to perform with.  
    And don't you know that it's just you, hey Jude, you'll do,  
    The movement you need is on your shoulder.  
    
    6.  
    Hey Jude, don't make it bad.  
    Take a sad song and make it better.  
    Remember to let her under your skin,  
    Then you'll begin to make it  
    Better better better better better better, oh.  
    
    Na na na nananana, nannana, hey Jude...  
    (repeat X number of times, fade)

    """)

    st.markdown("[samples on Padlet](https://padlet.com/mirankim316/S26Engpro)")

with tabs[1]:
    st.markdown("To be announced")

with tabs[2]:
    st.write("To be updated")

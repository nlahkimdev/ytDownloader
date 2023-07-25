import streamlit as st
from pytube import YouTube

st.title("YouTube Video Downloader")
st.subheader("Enter the URL:")
url = st.text_input(label='URL')
# print('url', url)
if url != '':
    yt = YouTube(url)
    st.image(yt.thumbnail_url, width=300)
    st.subheader('''
    {}
    * Length: {} seconds
    * Rating: {} 
    '''.format(yt.title, yt.length, yt.rating))
    video = yt.streams
    resol = []
    for stream in video:
        if stream.resolution:
            resol.append(stream.resolution)
    res = list(set(resol))
    if len(video) > 0:
        downloaded, download_audio = False, False
        download_video = st.button("Download Video")
        reso = st.sidebar.selectbox(
            label='Select Video Resolution', options=res)
        if yt.streams.filter(only_audio=True):
            download_audio = st.button("Download Audio Only")
        if download_video:
            if yt.streams.filter(resolution=reso):
                video.filter(resolution=reso).first().download()
                downloaded = True
        if download_audio:
            audio = video.filter(
                only_audio=True).first().download()
            downloaded = True
        if downloaded:
            st.subheader("Download Complete")
            import subprocess
            subprocess.run(["ls -Alsh"])
    else:
        st.subheader("Sorry, this video can not be downloaded")

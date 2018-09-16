import cmu_sphinx4
audio_url = "https://soundcloud.com/scumgang6ix9ine/fefe-feat-nicki-minaj"
transcriber = cmu_sphinx4.Transcriber(audio_url)
for line in transcriber.transcript_stream():
    print (line)

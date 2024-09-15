#python code to convert video to audio
import moviepy.editor as mp

#insert video file

clip=mp.VideoFileClip(r"video sample.mp4")

#insert audio file path
clip.audio.write_audiofile(r"audio.wav")

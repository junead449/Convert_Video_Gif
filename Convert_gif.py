from moviepy.editor import*

# Enter your File name 
video=VideoFileClip("Baraa Masoud - Love and Life.mp4 ").subclip(00,10 )
video.write_gif("test1.gif")
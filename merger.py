from user_info import username
import moviepy.editor as mpe
user = username()
user_mp3 = user + '.mp3'
clip = mpe.VideoFileClip("stock/video.mp4")
audio_bg = mpe.AudioFileClip(f'user/{user_mp3}')
final_audio = mpe.CompositeAudioClip([audio_bg])
final_clip = clip.set_audio(final_audio)
user_output = user + '.mp4'
final_clip.write_videofile(f'user/output/{user_output}')

import imageio
import os
try:
    imageio.plugins.ffmpeg.download()
except:
    print("Some cause an error, please execute is as root.")
finally:
    os.remove("ffmpeg-ins.py")

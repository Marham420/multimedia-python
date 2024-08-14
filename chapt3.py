# from moviepy.editor import VideoFileClip

# # Memuat file video
# video = VideoFileClip('video.mp4')

# # Menyimpan file video
# video.write_videofile('result.mp4')

# #pemotongan
# short_video = video.subclip(0, 10)  # Mendapatkan 10 detik pertama
# short_video.write_videofile('short_result.mp4')

# #penggabungan
# from moviepy.editor import concatenate_videoclips

# combined_video = concatenate_videoclips([video, short_video])
# combined_video.write_videofile('combined_result.mp4')

# from moviepy.editor import vfx


# #penambahan efek
# reversed_video = short_video.fx(vfx.time_mirror)  # Membalikkan video
# reversed_video.write_videofile('reversed_result.mp4')

# #pengaturan kecepatan
# sped_up_video = short_video.fx(vfx.speedx, 2)  # Mempercepat video 2x
# sped_up_video.write_videofile('sped_up_result.mp4')

# import tkinter as tk

# # Membuat jendela utama
# root = tk.Tk()
# root.title("Multimedia Application")

# # Menjalankan loop acara Tkinter
# root.mainloop()

# #menampilkan gambar
# from PIL import Image, ImageTk

# # Memuat gambar menggunakan Pillow
# image = Image.open('zoro.jpg')
# photo = ImageTk.PhotoImage(image)

# # Membuat label untuk menampilkan gambar
# label = tk.Label(root, image=photo)
# label.pack()

# #menampilkan audio
# from tkinter import filedialog
# from pydub import AudioSegment
# from pydub.playback import play

# # Definisikan fungsi untuk memutar musik
# def play_music():
#     file_path = filedialog.askopenfilename()
#     if file_path:
#         audio = AudioSegment.from_file(file_path)
#         play(audio)

# # Membuat tombol untuk memutar musik
# play_button = tk.Button(root, text="Play", command=play_music)
# play_button.pack()

# import tkinter as tk
# from PIL import Image, ImageTk

# # Buat root window
# root = tk.Tk()

# # Lanjutkan dengan logika lainnya
# image = Image.open("zoro.jpg")
# photo = ImageTk.PhotoImage(image)

# # Gunakan gambar dalam widget tkinter
# label = tk.Label(root, image=photo)
# label.pack()

# # Jalankan loop tkinter
# root.mainloop()

import tkinter as tk
from PIL import Image, ImageTk

# Buat root window
root = tk.Tk()

# Lanjutkan dengan logika lainnya
image = Image.open("zoro.jpg")
photo = ImageTk.PhotoImage(image)

# Gunakan gambar dalam widget tkinter
label = tk.Label(root, image=photo)
label.pack()

# Fungsi yang akan dipanggil ketika tombol play ditekan
def play():
    print("Tombol play ditekan!")

# Tambahkan tombol play
play_button = tk.Button(root, text="Play", command=play)
play_button.pack()

# Jalankan loop tkinter
root.mainloop()


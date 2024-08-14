import pygame
pygame.init()

# Mengatur tampilan
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Game")

# Loop utama permainan
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Memperbarui tampilan
    pygame.display.flip()

pygame.quit()

#memuat gambar
# Memuat gambar
image = pygame.image.load('zoro1.jpeg')

# Loop utama permainan
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Menggambar gambar
    screen.blit(image, (100, 100))

    # Memperbarui tampilan
    pygame.display.flip()

pygame.quit()

# Memuat suara
sound = pygame.mixer.Sound('victim.mp3')

# Memutar suara
sound.play()

#menambahkan animasi
# Loop utama permainan dengan animasi
x = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Memperbarui posisi
    x += 5
    if x > 800:
        x = 0

    # Menggambar gambar di posisi baru
    screen.fill((0, 0, 0))
    screen.blit(image, (x, 100))

    # Memperbarui tampilan
    pygame.display.flip()

pygame.quit()
from PIL import Image, ImageDraw

# Resim boyutları ve arkaplan rengi
width, height = 400, 200
bg_color = "white"

# Resim ve çizim nesnesi oluştur
image = Image.new("RGB", (width, height), bg_color)
draw = ImageDraw.Draw(image)

# Kırmızı bir daire çiz
draw.ellipse((50, 50, 150, 150), fill="red")

# Yeşil bir dikdörtgen çiz
draw.rectangle((200, 50, 300, 150), fill="green")

# Mavi bir çizgi çiz
draw.line((50, 160, 350, 160), fill="blue", width=5)

# Resmi göster
image.show()

# Resmi kaydet
image.save("example.png")

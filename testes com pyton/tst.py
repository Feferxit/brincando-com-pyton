from rembg import remove
from PIL import Image

# Abra a imagem
url = Image.open('satoru.jpg')

# Remova o fundo
output = remove(url)

# Salve o resultado
output.save('gojo.png')

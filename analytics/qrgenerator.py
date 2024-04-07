import qrcode
import matplotlib.pyplot as plt

#Esta funcion genera el codigo QR, al llamarla se necesita los datos a codificar y muestra la imagen
#La funcion devuelve la imagen creada (que se puede guardar) y el ok informando que se produjo correctamente el qr
def qrcreator (data):
    qr = qrcode.QRCode(None, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=20, border=1,)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    plt.imshow(img, cmap='gray')
    plt.axis('off')
    plt.show()
    return img, 'Qr generado'

if __name__ == '__main__':
    print('Generador de QR')
    producto = '0001'
    img, ok = qrcreator(producto)
    #qr = img.save(f'{producto}.png') si desean que la imagen del QR generado se grabe automaticamente descomentar esta linea
    print(ok)
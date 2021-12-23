import qrcode

def run():
    uInput=str(input("\nQué quieres inluir en tu codigo QR? \n"))
    
    img = qrcode.make(uInput)

    f = open("qrcode.png", "wb")
    img.save(f)
    f.close()

    print("\n Tu codigo QR se ha creado! \n")

if __name__ == '__main__':
    run()
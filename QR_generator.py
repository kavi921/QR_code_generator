import qrcode

def QR_Code(text,text_2):
    qr= qrcode.QRCode() 

    qr.add_data(text) 

    qr.make() 

    output_image = qr.make_image()
    
    output_image.save(f"{text_2}.png") 
    print("Your QRCode was successfully create!")
    print(f"name of the file: {text_2}")


def main():
    print("---QR code translator---")
    user_input = input("Enter the text you want to translate: ")
    name_of_qr = input("Enter the name of your QRCode: ")

    QR_Code(user_input,name_of_qr)
    
if __name__ == "__main__":
    main()
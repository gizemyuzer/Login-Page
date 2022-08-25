
sys_username="gizemitto"
sys_password= "123456"

giris_hakki= 3

while True:
    username=input("Enter the username:")
    password=input("Enter the password:")
    if(username!=sys_username and password==sys_password ):
        print("You entered your username wrong...")
        giris_hakki -=1
        print("Kalan giriş hakkınız: {}".format(giris_hakki))

    elif(username== sys_username and password!=sys_password):
        print("You entered your password wrong...")
        giris_hakki-=1
        print("Kalan giriş hakkınız: {}".format(giris_hakki))

    elif(username!=sys_username and password!=sys_password):
        print("Both username and password are wrong...")
        giris_hakki -=1
        print("Kalan giriş hakkınız: {}".format(giris_hakki))

    else:
        print("You entered...")
        break

    if(giris_hakki ==0):
        print("Giriş hakkınız kalmadı.")
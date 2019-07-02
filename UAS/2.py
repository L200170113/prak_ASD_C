print("====NOMOR 2====\n")

email = input("Masukkan email: ")

data = email.split("@")
uname = data[0]
host = data[1]

print ("Username : "+uname+" dan Host : "+host)

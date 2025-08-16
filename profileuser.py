print("\n")
print("Hello and welcome, Please provide the information below to be sure it's you logging in")
print("\n")

user = input("Username :")
password = input("Password : ")

print((user == "admin") and (password == "admin123")) and print("Access Granted\nLogin Successful") or print("Access Denied\nLogin Failed")
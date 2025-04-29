dic = {
    "Nanditha@gmail.com":"12345678",
    "Ankitha@gmail.com":"anki8765"
}

def Login(email, password):
    if email in dic:
        if dic[email] == password:
            return "Login successfull"
        else:
            return "Invalid password"
    else:
        return "Invalid email"
    
print(Login("Nanditha@gmail.com", "12345678"))
print(Login("Nanditha@gmail.com", "12378"))
print(Login("Asha@gmail.com", "12345678"))
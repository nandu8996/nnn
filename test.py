from login import Login

def test_cases():
    assert Login("Nanditha@gmail.com", "12345678") == "Login successfull"
    assert Login("Nanditha@gmail.com", "12378") == "Invalid password"
    assert Login("Asha@gmail.com", "12345678") == "Invalid email"
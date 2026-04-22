class A: 
    def __secret(self):
        print("This is top secret but you could still access it")
    

    def _protectedSecret(self):
        print("this is a protected secret, yet you could still access it")
        


b = A()
b._protectedSecret()
print()


c = A()
try:
    print("Attempting cracking into the secret\n ")
    c.__secret()
except Exception as err:
    print("ERROR: ", err)

print("attempting via the mangled trick")
c._A__secret()





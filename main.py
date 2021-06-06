import random
import string

number = int(input("[>] Combien de caractère aura ton password : "))
While = int(input("[>] Combien de password veux-tu : "))
counter = 0

while While > counter:
    code = "".join(random.choices( 
        string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = number
    ))
    print(code)
    counter += 1
print("")
input(f"[+] {While} on bien était généré !")
input("[!] Appuie sur entrer pour quitter.")

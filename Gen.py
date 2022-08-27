
import requests
import random
import string
import time

print("""

""")
time.sleep(2)
print("Générateur nitro")
time.sleep(0.5)
print("")
print("rejoins mon discord pour plus")
time.sleep(1)
print("")
print("créer par Rakzie")
time.sleep(1)
print("")
num = int(input('Combien de cide veut tu générer : '))

with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    print("t'es code nitro on bien été générer")

    start = time.time()

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")

    print(f"Generated {num} codes | Time taken: {time.time() - start}\n")

with open("Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f" Valid | {nitro} ")
            break
        else:
            print(f" Invalid | {nitro} ")

input("regarde dans Valid Codes.txt pour voir si il y a un cidz valide.")

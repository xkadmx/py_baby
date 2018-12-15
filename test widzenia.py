from sys import argv
script, sees, lives, computer, user_name = argv

prompt = " > "

print(f'Cześć, {user_name}, jestem skryptem {script}.')
print(f"Chciałbym zadać Ci kilka pytań.")
sees=input("Widzisz mnie, {user_name}?: ")


print(f"Gdzie mieszkasz, {user_name}?")
lives =input("Gdzie mieszkasz {user_name}?: ")

print("Jaki masz komputer?")
computer = input (prompt)

print(f"""
Ok, gdy zapytałem, czy mnie widzisz, odpowiedziałeś {sees}.
Mieszkasz w {lives}. Nie jestem pewien, gdzie to jest.
I masz komputer {computer}. Fajnie.
""")
guests = ["Leonardo da vinci", "Kanya West", "tupac shakur", "Tom Hanks", "Jay Z", "Thomas Edison"]

print("Good news! I found a bigger dinner table, so we can invite more guests!")

guests.insert(0, "Leonardo da Vinci")
guests.insert(2, "Isaac Newton")
guests.append("Thomas Edison")

print("\nUnfortunately, the new dinner table won't arrive in time.")
print("I can invite only two people for dinner.")

removed_guest = guests.pop()
print(f"Sorry {removed_guest}, I can't invite you to dinner.")

removed_guest = guests.pop()
print(f"Sorry {removed_guest}, I can't invite you to dinner.")

removed_guest = guests.pop()
print(f"Sorry {removed_guest}, I can't invite you to dinner.")

removed_guest = guests.pop()
print(f"Sorry {removed_guest}, I can't invite you to dinner.")

print(f"\n{guests[0]}, you are still invited to dinner!")
print(f"{guests[1]}, you are still invited to dinner!")

del guests[1]
del guests[0]

print("\nGuest list:", guests)
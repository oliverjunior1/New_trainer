# class two and a half man
class two_and_a_half:
    def __init__(self, character, doll):
        self.character = character
        self.doll = doll

    def __str__(self):
        return f"The character {self.character} has {self.doll} dolls in his bedroom."

Charlie = two_and_a_half("Charlie", 2)
Alan = two_and_a_half("Alan", 25)
Jake = two_and_a_half("Jake", 5)

print(Charlie)
print(Alan)
print(Jake)
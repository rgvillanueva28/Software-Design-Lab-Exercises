import random

class Doctor():
    def __init__(self):
        self.hedges = ("Please tell me more.",
                "Many of my patients tell me the same thing.",
                "Please coninue.")

        self.qualifiers = ("Why do you say that ",
                    "You seem to think that ",
                    "Can you explain why ")

        self.replacements = {"I":"you", "me":"you", "my":"your",
                        "we":"you", "us":"you", "mine":"yours"} 

    def reply(self, sentence):
        """Implements two different reply strategies."""
        probability = random.randint(1, 4)
        if probability == 1:
            return random.choice(self.hedges)
        else:
            return random.choice(self.qualifiers) + self.changePerson(sentence)

    def changePerson(self, sentence):
        """Replaces first person pronouns with second person
        pronouns."""
        words = sentence.split()
        replyWords = []
        for word in words:
            replyWords.append(self.replacements.get(word, word))
        return " ".join(replyWords) 

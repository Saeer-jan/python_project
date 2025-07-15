# i have to generate fake news headlines
#and make some funny headlines
import random

subjects = [
    "Scientists",
    "Experts",
    "Researchers",
    "Officials",
    "Activists",
    "Politicians",
    "Economists",
    "Doctors",
    "Teachers",
    "Engineers",
    "Celebrities",
    "Journalists",
    "Inventors",
    "Historians",
    "Philosophers",
]

verbs = [
    "discover",
    "announce",
    "warn",
    "claim",
    "reveal",
    "predict",
    "suggest",
    "report",
    "debunk",
    "expose"
    "investigate",
    "challenge",
    "criticize",
    "support",
]

objects = [
    "new species of alien life",
    "cure for all diseases",
    "secret government project",
    "massive conspiracy",
    "ancient civilization",
    "hidden treasure",
    "miracle drug",
    "global warming hoax",
    "new form of energy",
    "breakthrough in artificial intelligence",
    "revolutionary technology",
    "unprecedented economic growth",
    "unbelievable scientific breakthrough",
    "unexpected political alliance",
    "groundbreaking educational reform",
]

def generate_fake_news():
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    obj = random.choice(objects)
    headline = f"{subject} {verb} {obj}!"
    return headline

if __name__ == "__main__":
    for _ in range(5):  # Generate 5 fake news headlines
        print(generate_fake_news())
    # This code generates random fake news headlines by combining random subjects, verbs, and objects.
    # It uses the random library to select items from predefined lists and formats them into a headline.
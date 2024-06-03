
subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Cricket", "Ludo"]
sentences = []
for subject in subjects:
    for verb in verbs:
        for obj in objects:
            sentences.append(f"{subject} {verb} {obj}")
for sentence in sentences:
    print(sentence)

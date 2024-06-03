import demoji
demoji.download_codes()
text_with_emojis = "I love playing cricket 🏏 and ludo 🎲!"
text_with_descriptions = demoji.replace_with_desc(text_with_emojis, ":{bat&cube}:")
print(text_with_descriptions)

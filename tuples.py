imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))


title, artist, year, tracks = imelda

print(title)
print(artist)
print(year)

for i in range(0, len(tracks)):
    print("   ", tracks[i])
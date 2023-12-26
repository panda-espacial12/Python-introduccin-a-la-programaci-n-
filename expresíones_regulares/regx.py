import re 

text = "the quick brown fox jumps over the lazy dog"

x = re.search("^the.*dog$", text)

if x:
    print("SI")
else:
    print("no")
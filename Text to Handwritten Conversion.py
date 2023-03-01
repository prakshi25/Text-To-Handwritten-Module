from PIL import Image

txt = input('Enter the text you want to convert into handwritten notes: ')
BG = Image.open("Letters/bg.png")
sheet_width = BG.width
gap, ht = 0, 0


for i in txt:
    if i in [" ", ".", ",", ":", ";"]:
        gap += size // 2
    elif i == "\n":
        gap, ht = 0, ht + 140
    else:
        try:
            cases = Image.open("Letters/{}.png".format(str(ord(i.lower()))))
        except FileNotFoundError:
            print("Error: Please write a short paragraph.", i)
            continue
        BG.paste(cases, (gap, ht))
        size = cases.width
        gap += size

        if sheet_width < gap or len(i)*115 >(sheet_width-gap):
            gap,ht = 0,ht+140

print(gap)
print(sheet_width)
BG.show()

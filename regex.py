import re

teks = "kisa w #panse de sitiyasyon #peyi a ? #"

def ranplase(ekriti):
    return re.sub("#[\w]+", lambda x: "<a href='blablabla'>{}</a>".format(x.group()), ekriti)

print(ranplase(teks))
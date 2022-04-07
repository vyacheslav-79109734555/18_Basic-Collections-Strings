upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_letters = 'abcdefghijklmnopqrstuvwxyz'
sym_list = list('.,;:/?!()"+-=' + ' ')
k = int(input('Сдвиг для дешифровки сообщения: '))  # TODO: -1

new_str = ''
code = []
new_txt = []
start = 0
encoded = []

text = ('vujgvmCfb tj ufscfu ouib z/'
        'vhm jdjuFyqm jt fscfuu uibo jdju/'
        'jnqm fTjnqm tj scfuuf ibou fy/'
        'dpnqm yDpnqmf jt cfuufs boui dbufe/'
        'dpnqmj uGmb tj fuufsc ouib oftufe/'
        ' bstfTq jt uufscf uibo otf/'
        'ef uzSfbebcjmj vout/'
        'dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/'
        'svmf ipvhiBmu zqsbdujdbmju fbutc uz/'
        'qvsj Fsspst tipvme wfsof qbtt foumz/'
        'tjm omfttV mjdjumzfyq odfe/'
        'tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/'
        'hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/'
        ' Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/'
        'Evud xOp tj scfuuf ibou /'
        'ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/'
        'op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /'
        'jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/'
        ' bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip')

for i in text:
    if i in upper_letters:
        new_str += upper_letters[(upper_letters.index(i) + k) % 26]
    elif i in lower_letters:
        new_str += lower_letters[(lower_letters.index(i) + k) % 26]
    elif i in sym_list:
        new_str += i
txt = new_str.split()

for symbol in txt:
    if '/' not in symbol:
        code.append(symbol)
    else:
        code.append(symbol)
        new_txt.append(code)
        code = []
for i in reversed(txt[0]):
    start += 1
    if i in upper_letters:
        break

for row in new_txt:
    for word in row:
        encoded.append(word[len(word) - (start % len(word)):] + word[:len(word) - (start % len(word))])
    start += 1

decoder_text = '\n'.join(' '.join(encoded).split('/'))
print(decoder_text)


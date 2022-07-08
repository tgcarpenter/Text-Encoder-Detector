c_dia = 'chinese, gan, mandarin, hui, jin, hakka, min, wu, xiang, yue, pinghua, ba-shu'
weu_dia = str('english, french, spanish, catalan, basque, italian, indonesian, '
              'albanian, swedish, finnish, estonian, luxembourgish, '
              'faroese, icelandic, irish, scottish, occitan, afrikaans, '
              'galician, breton, corsican, leonese, malay, manx, gaelic, '
              'romansh, scots, southern sami, south sami, tagalog, walloon, '
              'portuguese, german, danish, norwegian, icelandic, scottish gaelic, '
              'greenlandic, sami, estonian,')
baltic_dia = 'latvian, lithuanian, estonian'
cyril_dia = 'bulgarian, belorussian, macedonian, russian, serbian'
meu_dia = 'czech, slovene, slovak, polish, hungarian, bosnian, croatian, serbian'
english = 'english, canadian, british'

newcodex = {'ascii': english, 'cp037': 'portuguese, ' + english, 'cp437': english, 'cp500': weu_dia, 'cp850': weu_dia,
            'cp863': 'french, canadian, french canadian, french-canadian', 'iso8859_15': weu_dia, 'cp858': weu_dia,
            'cp1252': weu_dia, 'cp1140': 'portuguese, ' + english, 'latin_1': weu_dia, 'mac_roman': weu_dia,
            'iso2022_jp_2': english + ', japanese, korean, greek, ' + c_dia, 'big5': c_dia, 'big5hkscs': c_dia,
            'gb2312': c_dia, 'gbk': c_dia, 'gb18030': c_dia, 'hz': c_dia, 'cp273': 'german', 'cp424': 'hebrew',
            'cp856': 'hebrew', 'cp862': 'hebrew', 'cp1255': 'hebrew', 'iso8859_8': 'hebrew', 'cp720': 'arabic',
            'cp864': 'arabic', 'cp1256': 'arabic', 'iso8859_6': 'arabic', 'cp737': 'greek', 'cp869': 'greek',
            'cp875': 'greek', 'cp1253': 'greek', 'iso8859_7': 'greek', 'mac_greek': 'greek', 'cp775': baltic_dia,
            'cp1257': baltic_dia, 'iso8859_4': 'greenlandic, sami, ' + baltic_dia, 'cp950': c_dia,
            'iso8859_13': 'greenlandic, sami, ' + baltic_dia, 'cp855': cyril_dia,
            'cp1251': 'ukrainian, bosnian, rusyn, ' + cyril_dia, 'iso8859_5': cyril_dia,
            'mac_cyrillic': cyril_dia, 'cp857': 'turkish', 'cp1026': 'turkish', 'cp1254': 'turkish',
            'iso8859_9': 'turkish', 'mac_turkish': 'turkish', 'cp860': 'portuguese', 'cp865': 'danish, norwegian',
            'iso8859_10': 'danish, norwegian, icelandic, faroese', 'cp861': 'icelandic', 'mac_iceland': 'icelandic',
            'cp866': 'russian, bulgarian', 'koi8_r': 'russian, bulgarian', 'cp874': 'thai', 'iso8859_11': 'thai',
            'cp932': 'japanese', 'euc_jp': 'japanese', 'euc_jis_2004': 'japanese', 'euc_jisx0213': 'japanese',
            'iso2022_jp': 'japanese', 'iso2022_jp_1': 'japanese', 'iso2022_jp_2004': 'japanese',
            'iso2022_jp_3': 'japanese', 'iso2022_jp_ext': 'japanese', 'shift_jis': 'japanese',
            'shift_jis_2004': 'japanese', 'shift_jisx0213': 'japanese', 'cp949': 'korean', 'euc_kr': 'korean',
            'iso2022_kr': 'korean', 'johab': 'korean', 'cp1006': 'urdu, persian', 'cp1125': 'ukrainian, belorussian',
            'koi8_u': 'ukrainian, bulgarian, russian', 'cp1258': 'vietnamese',
            'iso8859_3': 'maltese, esperanto, turkish', 'koi8_t': 'tajik, persian', 'kz1048': 'kazakh',
            'ptcp154': 'kazakh', 'iso8859_14': 'irish, manx, gaelic, welsh, cornish, breton, scottish gaelic',
            'cp852': 'romanian, ' + meu_dia, 'cp1250': 'montenegrin, romanian, ' + meu_dia,
            'iso8859_2': 'albanian, german, upper sorbian, lower sorbian, turkmen, ' + meu_dia,
            'mac_latin2': 'czech, slovak, polish, ' + baltic_dia,
            'iso8859_16': 'albanian, croatian, bosnian, serbian, hungarian, polish, romanian, slovene'}

codex = list()

while True:
    temp_f_dir = input("Enter File Directory:")
    f_dir = temp_f_dir.strip()
                                #Directory error checking
    try:
        open(r"{}".format(f_dir))   #Could go in 'for' loop, but this is cleaner.
        break
    except:
        print('\nInvalid Directory')

                                #Language Input List Creator
while True:
    in_lang = input('Enter Language (Optional),*Press "Enter" For No Input:')
    language = in_lang.strip()

    if language is str(''):
        codex = list(newcodex)
        break
    for encoding, lang in newcodex.items():
        try:
            lang2 = lang.split(', ')
            if lang2.index(language.casefold()) >= 0:
                codex.append(encoding)
        except:
            continue
    if codex:
        break
    else:
        print('Invalid Language Input')

tal = 0
c_tal = 0
c_dic = dict()
o_checks = list()
                                #Possible Codex Library Creator
for encode in codex:
    c_tal = c_tal + 1
    f_open = open(r"{}".format(f_dir), encoding=encode)
    try:
        f_open.read(10000)
        f_read = f_open.read()
        if f_read.count(' ™') > 0:  #Placeholder search, could add other searches later
            o_checks.append(encode)
            continue
        s_count = f_read.count(' ')    #End goal:print the encoders with the most amount of spaces.
        c_dic[encode] = s_count        #Use a Dictionary to keep track of {encoder: # of spaces}.
    except:
        tal = tal + 1
        continue

if tal == c_tal:
    print("Not Python Compatible Encoding")
    quit()
else:                                   #List Filtering
    temp_count = 0
    templ_list = list()
    for encode, s_count in c_dic.items():
        if s_count > temp_count:
            temp_count = s_count
    for encode, s_count in c_dic.items():
        if s_count != temp_count:
            templ_list.append(encode)
    for b_encode in templ_list:
        del c_dic[b_encode]
    for o_encode in o_checks:
        try:
            del c_dic[o_encode]
        except:
            continue

    dir_split = f_dir.split('\\')
    c_dic_s = str([x for x in c_dic.keys()])
    c_dic_s2 = c_dic_s.strip('[')
    c_dic_print = c_dic_s2.strip(']')
    print('File Initialized:', dir_split[-1], '\nEncoding Type(s):', c_dic_print)

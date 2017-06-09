
meta=[]
title=[]
good=[]

meta_n=[]
title_n=[]
good_n=[]


if __name__ == '__main__':

    # with open('invalid_title') as invalid_t:
    #     for line in invalid_t:
    #         title.append(line)
    # invalid_t.close()

    # with open('good_movies') as good_m:
    #     for line in good_m:
    #         good.append(line)
    # good_m.close()

    # print "meta",len(meta)
    # print "title",len(title)
    # print "good",len(good)

    with open('invalid_metascore1.txt') as invalid_m:
        for line in invalid_m:
            meta.append(line)
    invalid_m.close()

    with open('invalid_metascore.txt') as invalid_m:
        for line in invalid_m:
            meta_n.append(line)
    invalid_m.close()

    print len(meta)
    print len(meta_n)


    print list(set(meta_n) ^ set(meta))
    print len(list(set(meta_n) ^ set(meta)))





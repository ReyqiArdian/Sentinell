def fungsi_pertama(a="input"):
    print ("ayam")
    def fungsi_ketiga(a):
        if a=="input":
            return a[:2]

    return fungsi_kedua(a), fungsi_ketiga(a)

def fungsi_kedua(a) :
    print ("AAA")
    if a =="input" : return a
    if a =="output" : return "ini "

    fungsi_2, fungsi_3 = fungsi_pertama()


print ("fungsi_2")
print ("fungsi_3")


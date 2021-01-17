import chatMain

while (True):

    soru = input("Sen: ")

    if soru == "kapat":
        break
    else:
        cevap = chatMain.chat(soru)[0]
        tag = chatMain.chat(soru)[1]
        # sorgu  = "INSERT INTO sorular VALUES(?,?,?,?)", (str(my_id), tag,soru,cevap)
        # print(sorgu)
#        c.execute("INSERT INTO sorular VALUES(?,?,?,?,?)", (str(my_id), tag, soru, cevap, " "))
       # conn.commit()
        print("Robot : ", cevap)
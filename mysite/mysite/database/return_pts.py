def return_pts(res_a , gab):
    #compara 
    pts = 0
    if (res_a == [-1, -1] or gab == [-1,-1]): #tratamento para os jogos que não foram palpitados e são dados um placar 100x100,
                             #pois é um placar impossível.
        return pts
    if (res_a == gab):
        pts = 10
        return pts
    else:
        if(res_a[0] == gab[0] or res_a[1] == gab[1] ):
            pts = pts + 2
        if((res_a[0] > res_a[1] and gab[0] > gab[1]) or (res_a[0] < res_a[1] and gab[0] < gab[1]) or (res_a[0] == res_a[1] and gab[0] == gab[1])):
            pts = pts + 5
            return pts
    return pts



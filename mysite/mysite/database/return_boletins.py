def return_boletins(boletins,nomes,pontos_totais):
    for key in boletins.keys():
        print("\n" +"="*53)
        #print(key+1,end='')
        print(key+1," - " + nomes[key] + " "*(29-len(nomes[key])) + "Total de Pontos: ", pontos_totais[key])
        #print(" - " + nomes[key] + " "*(29-len(nomes[key])) + "Total de Pontos: ",end='')
        #print(pontos_totais[key])
        print("-"*53)
        print(boletins[key])
        
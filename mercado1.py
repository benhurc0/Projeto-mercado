def mercado():
    while True:
        try:
            produto = int(input('Digite o Valor: ' ))#.strip()#.title()
        except:
            print('Digite certo')
            continue
        else:
            print('Ok Registrado')    
            break

mercado()
import os
import random

#definiciones de funciones
def cabeza(n):
    for _ in range(n):
        print()
    print('-------------------------------------   NAUTICA   -----------------------------------')
    for _ in range(n):
        print()

def imprenta(n):
    if n == 0:
        print(' ', end=' ')
    elif n == 1:
        print('O', end=' ')
    elif n == 2:
        print('X', end=' ')
    else:
        print('#', end=' ')

def salto(n):
    for _ in range(n):
        print()

def gen_0():
    return list(tuple(0 for _ in range(10)) for _ in range(10))

def gen_0m():
    return list(list(0 for _ in range(10)) for _ in range(10))

def mapa(a, j):
    print(f'           jugador {j}')
    print('             a b c d e f g h i j')
    f = 1
    for i in a:
        if f < 10:
            print(' ', end='')
        print(f'          {f}|', end='')
        for j in i:
            imprenta(j)
        f += 1
        print()
    
def mapa_2(a,b):
    print('           jugador 1                                  jugador 2')
    print('             a b c d e f g h i j                        a b c d e f g h i j')
    f = 1
    for i,j in list(zip(a,b)):
        if f < 10:
            print(' ', end='')
        print(f'          {f}|', end='')
        for k in i:
            imprenta(k)
        print('                    ', end='')
        if f < 10:
            print(' ', end='')
        print(f'{f}|', end='')
        for l in j:
            imprenta(l)
        f += 1
        print()

def l_n(s):
    cad = 'abcdefghij'
    num = (1,2,3,4,5,6,7,8,9,10)
    n = cad.index(s)
    return num[n]

def sum_2(a,b):
    new_l = []
    for i,j in list(zip(a,b)):
        x = []
        for k,l in list(zip(i,j)):
            x.append(k+l)
        new_l.append(tuple(x))
    return new_l

def cor_lis(s, r=1):
    l = l_n(s[0]) - 1
    n = int(s[1:]) - 1
    lis = gen_0m()
    lis[n][l] = r
    new_l = []
    for i in lis:
        new_l.append(tuple(i))
    return new_l

def barco_inst(n=1):
    print('introduzca la cordenada # y la direccion del barco')
    print(f'          barco 1x{n}')
    print()
    print('       |         y')
    print('       |         O')
    print('       |         O')
    print('       | nx  O O # O O  x')
    print('       |         O')
    print('       |         O')
    print('       |        ny')

def barco_n(cor,n,sen):
    if n < 1:
        return []
    #if n == 1:
        #return list(cor)
    a = 'abcdefghij'
    b = [1,2,3,4,5,6,7,8,9,10]
    l = cor[0]
    cut_l = a.find(l)
    cut_lp = cut_l + n
    cut_ln = cut_l-n+1
    nu = cor[1:]
    cut_n = int(nu)
    cut_np = cut_n-n
    r = []
    if sen == 'x':
        new_l = a[cut_l:cut_lp]
        for i in new_l:
            r.append(i + str(nu))
    elif sen == 'nx':
        new_l = a[cut_ln:cut_l+1]
        for i in new_l:
            r.append(i + str(nu))
    elif sen == 'y':
        new_n = b[cut_np:cut_n]
        for i in new_n:
            r.append(l + str(i))
    elif sen == 'ny':
        new_n = b[cut_n-1:cut_n+n-1]
        for i in new_n:
            r.append(l + str(i))
    if r == []:
        r = barco_n(cor, n-1, sen)
    return r
        
def cor_mat(a,n):
    for i in n:
        b = cor_lis(i)
        a = sum_2(a, b)
    return a

def perimetro(c):
    a = 'abcdefghij'
    b = [1,2,3,4,5,6,7,8,9,10]
    l = ''
    n = []
    r = []
    le = c[0]
    nu = int(c[1:])
    if le == 'a':
        l = 'ab'
    elif le == 'j':
        l = 'ij'
    else:
        cut = a.find(le)
        l = a[cut-1:cut+2]
    if nu == 1:
        n = [1,2]
    elif nu == 10:
        n = [9,10]
    else:
        cut = b.index(nu)
        n = b[cut-1:cut+2]
    for i in l:
        for j in n:
            k = i + str(j)
            r.append(k)
    return r

def peinar(sen:str, in_l:list, lis:list, n:int):
    new_l = in_l
    if n == 1:
        return list(i for i in new_l if i not in lis)
    if sen == 'x':
        for i in lis:
            new_t = barco_n(i,n,'nx')
            new_l = list(i for i in new_l if i not in new_t)
        for i in ['j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'j8', 'j9', 'j10']:
            new_t = barco_n(i, n-1, 'nx')
            new_l = list(i for i in new_l if i not in new_t)
    elif sen == 'nx':
        for i in lis:
            new_t = barco_n(i, n, 'x')
            new_l = list(i for i in new_l if i not in new_t)
        for i in ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10']:
            new_t = barco_n(i, n-1, 'x')
            new_l = list(i for i in new_l if i not in new_t)
    elif sen == 'y':
        for i in lis:
            new_t = barco_n(i,n,'ny')
            new_l = list(i for i in new_l if i not in new_t)
        for i in ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1', 'i1', 'j1']:
            new_t = barco_n(i, n-1, 'ny')
            new_l = list(i for i in new_l if i not in new_t)
    elif sen == 'ny':
        for i in lis:
            new_t = barco_n(i,n,'y')
            new_l = list(i for i in new_l if i not in new_t)
        for i in ['a10', 'b10', 'c10', 'd10', 'e10', 'f10', 'g10', 'h10', 'i10', 'j10']:
            new_t = barco_n(i, n-1, 'y')
            new_l = list(i for i in new_l if i not in new_t)
    return new_l

def cordenandas_perimetricas(m):
    r = []
    for i in m:
        r = r + perimetro(i)
    r = list(set(r))
    return r

def cordenadas_lista(c):
    r = gen_0()
    for i in c:
        r = sum_2(r,cor_lis(i))
    return r

def hp_bar(n):
    k = n//3
    l1 = '  '*k
    l2 = '0 '*(8-k)
    return f'|{l1}{l2}|'

def count_n(g,n=1):
    count = 0
    for i in g:
        for j in i:
            if j == 2:
                count += 1
    return count

cordenadas_t = ['a1'  , 'b1'  , 'c1'  , 'd1'  , 'e1'  , 'f1'  , 'g1'  , 'h1'  , 'i1'  , 'j1' , 
                'a2'  , 'b2'  , 'c2'  , 'd2'  , 'e2'  , 'f2'  , 'g2'  , 'h2'  , 'i2'  , 'j2' , 
                'a3'  , 'b3'  , 'c3'  , 'd3'  , 'e3'  , 'f3'  , 'g3'  , 'h3'  , 'i3'  , 'j3' , 
                'a4'  , 'b4'  , 'c4'  , 'd4'  , 'e4'  , 'f4'  , 'g4'  , 'h4'  , 'i4'  , 'j4' , 
                'a5'  , 'b5'  , 'c5'  , 'd5'  , 'e5'  , 'f5'  , 'g5'  , 'h5'  , 'i5'  , 'j5' , 
                'a6'  , 'b6'  , 'c6'  , 'd6'  , 'e6'  , 'f6'  , 'g6'  , 'h6'  , 'i6'  , 'j6' , 
                'a7'  , 'b7'  , 'c7'  , 'd7'  , 'e7'  , 'f7'  , 'g7'  , 'h7'  , 'i7'  , 'j7' , 
                'a8'  , 'b8'  , 'c8'  , 'd8'  , 'e8'  , 'f8'  , 'g8'  , 'h8'  , 'i8'  , 'j8' , 
                'a9'  , 'b9'  , 'c9'  , 'd9'  , 'e9'  , 'f9'  , 'g9'  , 'h9'  , 'i9'  , 'j9' , 
                'a10' , 'b10' , 'c10' , 'd10' , 'e10' , 'f10' , 'g10' , 'h10' , 'i10' , 'j10']


while True:
    #menu
    cabeza(5)
    input('presione enter para continuar...')
    os.system('cls')

    #quien juega primero
    cabeza(5)
    input('                    escojer entre X y O ')
    pri_j = random.choice(('X','O'))
    print(f'                    inicia {pri_j}')
    salto(5)
    input('presione enter para continuar...')
    os.system('cls')

    #ventana en bucle jugador 1
    sj1_gra = gen_0()
    cj1 = []
    barcos = [4,4,3,3,2,2,2,1,1,1,1]
    cabeza(3)
    print('jugador 1')
    salto(2)
    aleatorio = input('eleccion aleatoria? si o no : ')
    os.system('cls')
    if aleatorio == 'no':
        while True:
            cabeza(3)
            mapa(sj1_gra, 1)
            salto(2)
            if len(barcos) == 0:
                break
            barco_inst(barcos[0])
            salto(2)
            cordenada = input('cordenada #: ')
            if barcos[0] == 1:
                direc == 'x'
            else:
                direc = input('orientacion del barco: ') 
            lis_peinada = peinar(direc,cordenadas_t,cj1,barcos[0])
            if cordenada in lis_peinada:
                cord_barco = barco_n(cordenada, barcos[0],direc)
                if barcos[0] != 1:
                    cj1 = cj1 + cord_barco
                    sj1_gra = sum_2(sj1_gra,cordenadas_lista(cord_barco))
                else:
                    cj1 = sum_2(cj1,cord_barco)
                    sj1_gra = sum_2(sj1_gra,cor_lis(cord_barco))
                barcos = barcos[1:]
            else:
                input('el barco no cumple las condiciones, vuelve a intentar por favor...')
            os.system('cls')
        print('gracias por haber ubicado todos los barcos')
        
    else:
        cabeza(3)
        print('          definiendo elementos...')
        lista_perimetrica = []
        for i in barcos:
            direc = random.choice(('x','nx','y','ny'))
            lis_peinada = peinar(direc,cordenadas_t,lista_perimetrica,i)
            cordenada = random.choice(lis_peinada)
            cord_barco = barco_n(cordenada, i, direc)
            if barcos[0] != 1:
                cj1 = cj1 + cord_barco
                sj1_gra = sum_2(sj1_gra,cordenadas_lista(cord_barco))
            else:
                cj1 = sum_2(cj1,cord_barco)
                sj1_gra = sum_2(sj1_gra,cor_lis(cord_barco))
            lista_perimetrica = lista_perimetrica + cordenandas_perimetricas(cord_barco)
        os.system('cls')
        cabeza(3)
        mapa(sj1_gra, 1)
        salto(3)
    input('presione enter para continuar...')
    os.system('cls')

    #ventana en bucle jugador 2
    sj2_gra = gen_0()
    cj2 = []
    barcos = [4,4,3,3,2,2,2,1,1,1,1]
    cabeza(3)
    print('jugador 2')
    salto(2)
    aleatorio = input('eleccion aleatoria? si o no : ')
    os.system('cls')
    if aleatorio == 'no':
        while True:
            cabeza(3)
            mapa(sj2_gra, '1')
            salto(2)
            if len(barcos) == 0:
                break
            barco_inst(barcos[0])
            salto(2)
            cordenada = input('cordenada #: ')
            if barcos[0] == 1:
                direc == 'x'
            else:
                direc = input('orientacion del barco: ') 
            lis_peinada = peinar(direc,cordenadas_t,cj2,barcos[0])
            if cordenada in lis_peinada:
                cord_barco = barco_n(cordenada, barcos[0],direc)
                if barcos[0] != 1:
                    cj2 = cj2 + cord_barco
                    sj2_gra = sum_2(sj2_gra,cordenadas_lista(cord_barco))
                else:
                    cj2 = sum_2(cj2,cord_barco)
                    sj2_gra = sum_2(sj2_gra,cor_lis(cord_barco))
                barcos = barcos[1:]
            else:
                input('el barco no cumple las condiciones, vuelve a intentar por favor...')
            os.system('cls')
        print('gracias por haber ubicado todos los barcos')
    else:
        cabeza(3)
        print('          definiendo elementos...')
        lista_perimetrica = []
        for i in barcos:
            direc = random.choice(('x','nx','y','ny'))
            lis_peinada = peinar(direc,cordenadas_t,lista_perimetrica,i)
            cordenada = random.choice(lis_peinada)
            cord_barco = barco_n(cordenada, i, direc)
            if barcos[0] != 1:
                cj2 = cj2 + cord_barco
                sj2_gra = sum_2(sj2_gra,cordenadas_lista(cord_barco))
            else:
                cj2 = sum_2(cj2,cord_barco)
                sj2_gra = sum_2(sj2_gra,cor_lis(cord_barco))
            lista_perimetrica = lista_perimetrica + cordenandas_perimetricas(cord_barco)
        os.system('cls')
        cabeza(3)
        mapa(sj2_gra, 2)
        salto(3)
    input('presione enter para continuar...')
    os.system('cls')

    #juego principal
    cabeza(3)
    salto(3)
    g_j12 = input('habilitar jugadas hechas. si, no : ')
    salto(3)
    os.system('cls')
    j1 = gen_0()
    j2 = gen_0()
    t = 0
    aviso = 0
    jugadas_j1 = []
    jugadas_j2 = []
    hp_1 = 0
    hp_2 = 0
    while True:
        cabeza(3)
        mapa_2(j1,j2)
        salto(1)
        hp_1 = count_n(j1)
        hp_2 = count_n(j2)
        if (hp_1 == 24) or (hp_2 == 24):
            break
        print(f'            {hp_bar(hp_1)}                         {hp_bar(hp_2)}')
        salto(3)
        if aviso == 1:
            print('la anterior jugada fue invalida!!!')
            salto(3)
        if g_j12 == 'si':
            print(f'jugadas jugador 1 {jugadas_j1}')
            print(f'jugadas jugador 2 {jugadas_j2}')
            salto(3)
        jugada = input(f'turno del jugador {(t%2)+1}: ')
        if jugada in cordenadas_t:
            if t%2 == 0:
                if jugada not in jugadas_j1:
                    if jugada in cj2:
                        j2 = sum_2(j2, cor_lis(jugada, 2))
                    else:
                        j2 = sum_2(j2, cor_lis(jugada))
                        t += 1
                    jugadas_j1.append(jugada)
                else:
                    t += 1
            else:
                if jugada not in jugadas_j2:
                    if jugada in cj1:
                        j1 = sum_2(j1, cor_lis(jugada, 2))
                    else:
                        j1 = sum_2(j1, cor_lis(jugada))
                        t += 1
                    jugadas_j2.append(jugada)
                else:
                    t += 1
            aviso = 0
        else:
            if jugada == 'qqq':
                os.system('cls')
                cabeza(3)
                if t%2 == 0:
                    mapa(sj2_gra,2)
                else:
                    mapa(sj1_gra,1)
                salto(2)
                input('enter para continuar...')
            elif jugada == '000':
                aviso_e = 0
                while True:
                    os.system('cls')
                    cabeza(3)
                    mapa_2(j1,j2)
                    salto(3)
                    print(f'          modo edicion del jugador{(t%2)+1}')
                    salto(2)
                    if aviso_e == 1:
                        print('     la cordenada introducida no es correcta')
                        salto(3)
                    new_p = input('     cordenada a editar: ')
                    if new_p == '000':
                        break
                    if new_p in cordenadas_t:
                        if t%2 == 0:
                            j2 = sum_2(j2, cor_lis(new_p, 5))
                        else:
                            j1 = sum_2(j1, cor_lis(new_p, 5))
                        aviso_e = 0
                    else:
                        aviso_e = 1    
            elif jugada == 'win':
                if t%2 == 0:
                    hp_2 = 24
                else: 
                    hp_1 = 24          
            else:
                aviso = 1
                t += 1
        os.system('cls')

    #parte final
    os.system('cls')
    cabeza(5)
    ju_q_g = 0
    if hp_1 == 24:
        ju_q_g = 2
    else:
        ju_q_g = 1
    print(f'          FELICIDADEZ EL JUGADOR {ju_q_g} GANA!!!')
    salto(8)
    repetir = input('desea volver a jugar?. si, no:  ')
    if repetir == 'no':
        break
    os.system('cls')
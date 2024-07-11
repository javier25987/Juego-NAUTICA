# ====================================================== importacion de modulos
import os
import random
import numpy as np 
# ============================================================= apartado logico
'''
todo el formato de golpes y demas esta dado en formato letras, las matrices son solo para los graficos
'''
barcos_existentes = [4,4,3,3,2,2,2,1,1,1,1]

cordenadas_tablero = [['a1' , 'b1' , 'c1' , 'd1' , 'e1' , 'f1' , 'g1' , 'h1' , 'i1' , 'j1'], 
                      ['a2' , 'b2' , 'c2' , 'd2' , 'e2' , 'f2' , 'g2' , 'h2' , 'i2' , 'j2'], 
                      ['a3' , 'b3' , 'c3' , 'd3' , 'e3' , 'f3' , 'g3' , 'h3' , 'i3' , 'j3'], 
                      ['a4' , 'b4' , 'c4' , 'd4' , 'e4' , 'f4' , 'g4' , 'h4' , 'i4' , 'j4'], 
                      ['a5' , 'b5' , 'c5' , 'd5' , 'e5' , 'f5' , 'g5' , 'h5' , 'i5' , 'j5'], 
                      ['a6' , 'b6' , 'c6' , 'd6' , 'e6' , 'f6' , 'g6' , 'h6' , 'i6' , 'j6'], 
                      ['a7' , 'b7' , 'c7' , 'd7' , 'e7' , 'f7' , 'g7' , 'h7' , 'i7' , 'j7'], 
                      ['a8' , 'b8' , 'c8' , 'd8' , 'e8' , 'f8' , 'g8' , 'h8' , 'i8' , 'j8'], 
                      ['a9' , 'b9' , 'c9' , 'd9' , 'e9' , 'f9' , 'g9' , 'h9' , 'i9' , 'j9'], 
                      ['a10', 'b10', 'c10', 'd10', 'e10', 'f10', 'g10', 'h10', 'i10', 'j10']]

def elemento_en_matriz(matriz:list, elemento:int):
    '''
    como la sentencia in no funciona en un lista de listas hice esta funcion
    la cual rectifica en cada lista de la lista mayor
    '''
    for i in matriz:
        if elemento in i:
            return True
    return False
        
def matriz_transpuesta(m:list):
    '''
    nada que explpicar solo se transpone la matriz
    '''
    return list(map(list, zip(*m)))
        
def peinar_tablero(direcion, elementos):
    global cordenadas_tablero
    '''
    dada una direccion limpia una longitud en una direccion en el tablero de juego
    '''
    if direcion == 'x':
        matriz = matriz_transpuesta(cordenadas_tablero)
        matriz = matriz[:-elementos]
        matriz = matriz_transpuesta(matriz)
    elif direcion == 'y':
        matriz = cordenadas_tablero
        matriz = matriz[elementos:]
    elif direcion == 'nx':
        matriz = matriz_transpuesta(cordenadas_tablero)
        matriz = matriz[elementos:]
        matriz = matriz_transpuesta(matriz)
    elif direcion == 'ny':
        matriz = cordenadas_tablero
        matriz = matriz[:-elementos]
    else:
        return None
    return matriz

def letra_a_numero(s:str):
    '''
    pasa una letra de la a a la j a el numero de su posicion
    '''
    cadena = 'abcdefghij'
    numero = (1,2,3,4,5,6,7,8,9,10)
    n = cadena.index(s)
    return numero[n]

def numero_a_letra(s:int):
    '''
    pasa un numero de el 1 al 10 a una letra en la posicion de ese numero
    '''
    cadena = 'abcdefghij'
    numero = (1,2,3,4,5,6,7,8,9,10)
    n = numero.index(s)
    return cadena[n]
    
def hacer_barco(direcion:str, cordenada:str, longitud:int):
    global cordenadas_tablero
    '''
    esta funcion hace un barco en el tablero dada una longitud
    '''
    if elemento_en_matriz(cordenadas_tablero, cordenada):
        if longitud == 1:
            return [cordenada]
        if longitud == 0:
            return []
        
        while not elemento_en_matriz(peinar_tablero(direcion, longitud-1), cordenada):
            longitud -= 1
        
        cordenadas = []
        
        k = letra_a_numero(cordenada[0])
        
        for i in range(longitud):
            if direcion == 'x':
                numero = cordenada[1:]
                letra = numero_a_letra(k + i)
            elif direcion == 'y':
                numero = str(int(cordenada[1:]) - i)
                letra = cordenada[0]
            elif direcion == 'nx':
                numero = cordenada[1:]
                letra = numero_a_letra(k - i)
            elif direcion == 'ny':
                numero = str(int(cordenada[1:]) + i)
                letra = cordenada[0]
                
            cordenadas.append(letra + numero)
        
        return cordenadas
    
    else:
        return None
    
def perimetro(cordenada:str):
    '''
    dada una cordenada devuelve todas las cordenadas al rededor de esto
    '''
    cadena = 'abcdefghij'
    perimetro_c = []
    letra_c = cordenada[0]
    numero_c = cordenada[1:]
    
    if letra_c == 'a':
        letras = 'ab'
    elif letra_c == 'j':
        letras = 'ij'
    else:
        k = cadena.find(letra_c)
        letras = cadena[k-1:k+2]
        
    if numero_c == '1':
        numeros = ['1', '2']
    elif numero_c == '10':
        numeros = ['9', '10']
    else:
        k = int(numero_c)
        numeros = list(map(str, [k-1, k, k+1]))
        
    for i in letras:
        for j in numeros:
            k = i + j
            perimetro_c.append(k)
    
    return perimetro_c

def perimetro_de_un_barco(barco:list, barco_integrado=False):
    if barco == []:
        return []
    lados = []
    for i in barco:
        lados += perimetro(i)
    if barco_integrado:
        k = list(set(lados))
    else:
        k = list(set(lados) - set(barco))
    return k

def relieve_de_barcos_hundidos(barcos, golpes_dados):
    relieves = []
    for i in barcos:
        if all(map(lambda x: x in golpes_dados, i)):
            relieves += perimetro_de_un_barco(i)
            
    return relieves

def matriz_a_linea(m:list):
    k = []
    for i in m:
        k += i
    return k

def crear_barcos_random():
    global barcos_existentes
    barcos_random = []
    
    for i in barcos_existentes:
        direccion = random.choice(('x', 'y'))
        ndireccion = 'nx' if direccion == 'x' else 'ny'
        
        k = peinar_tablero(direccion, i)
        k = set(matriz_a_linea(k))
        
        puntos_erroneos = []
        
        for j in barcos_random:
            puntos = perimetro_de_un_barco(j, barco_integrado=True)
            for l in puntos:
                puntos_erroneos += hacer_barco(ndireccion, l, i)
                
        puntos_erroneos = set(puntos_erroneos)
        
        k -= puntos_erroneos
            
        b_cordeanda = random.choice(list(k))
        
        barcos_random.append(hacer_barco(direccion, b_cordeanda, i))
        
    return barcos_random
    
class Jugador():
    def __init__(self, barcos, nombre):
        '''
        barco a de ser una matriz de matrices
        '''
        self.nombre = nombre
        self.golpes_recibidos = []
        self.barcos = barcos
        self.relieves = []
        self.golpes_acertados = []
        self.vida = 24
        
    def recibir_golpe(self, golpe):
        if elemento_en_matriz(self.barcos, golpe):
            self.golpes_acertados.append(golpe)
            self.vida -= 1
        else:
            self.golpes_recibidos.append(golpe)
            
    def confirmar_relieves(self):
        self.relieves = relieve_de_barcos_hundidos(self.barcos, self.golpes_acertados)
        self.golpes_recibidos = list(set(self.golpes_recibidos) - set(self.relieves))
        
    def saber_puntos_disponibles(self):
        global cordenadas_tablero
        k_1 = set(matriz_a_linea(cordenadas_tablero))
        k_2 = set(self.golpes_recibidos)
        k_3 = set(self.golpes_acertados)
        k_4 = set(self.relieves)
        k_5 = k_2 | k_3 | k_4
        k = k_1 - k_5
        return list(k)

# ============================================================ apartado grafico
def salto(n):
    for _ in range(n):
        print()
        
def cabeza(n):
    salto(n)
    print('-------------------------------------   NAUTICA   -----------------------------------')
    salto(n)
    
def cordenada_a_array(cordenada:str, valor:int):
    k = np.zeros((10, 10))
    row = int(cordenada[1:]) - 1 
    colum = letra_a_numero(cordenada[0]) - 1
    k[row, colum] = valor
    return k

def cordenadas_a_array(cordenadas:list, valor:int):
    k = np.zeros((10, 10))
    if cordenadas == []:
        return k
    for i in cordenadas:
        k += cordenada_a_array(i, valor)
    return k

def imprenta(n):
    if n == 0:
        print(' ', end=' ')
    elif n == 1:
        print('O', end=' ')
    elif n == 2:
        print('X', end=' ')
    else:
        print('#', end=' ')
        
def creacion_de_el_mapa(jugador:Jugador):
    k = cordenadas_a_array(jugador.golpes_recibidos, 1)
    k += cordenadas_a_array(jugador.golpes_acertados, 2)
    k += cordenadas_a_array(jugador.relieves, 3)

    return k
        
def mapa_unijugador(jugador:Jugador):
    print(f'           jugador {jugador.nombre}')
    print('             a b c d e f g h i j')
    mapa = creacion_de_el_mapa(jugador)
    mapa += cordenadas_a_array(matriz_a_linea(jugador.barcos), 1)
    
    k = 1
    for i in mapa:
        if k < 10:
            print(' ', end='')
        print(f'          {k}|', end='')
        for j in i:
            imprenta(j)
        k += 1
        print()
        
def mapa_bijugador(jugador_1:Jugador, jugador_2:Jugador, mostrar_barcos=False, modo_de_juego=2):
    if modo_de_juego == 2:
        print('           jugador 1                                  jugador 2')
    else:
        print('           jugador                                    maquina')
    print('             a b c d e f g h i j                        a b c d e f g h i j')
    if mostrar_barcos:
        mapa_1 = cordenadas_a_array(matriz_a_linea(jugador_1.barcos), 1)
        mapa_2 = cordenadas_a_array(matriz_a_linea(jugador_2.barcos), 1)
    else:
        mapa_1 = creacion_de_el_mapa(jugador_1)
        mapa_2 = creacion_de_el_mapa(jugador_2)
    f = 1
    for i in range(0, 10):
        if f < 10:
            print(' ', end='')
        print(f'          {f}|', end='')
        for k in mapa_1[i]:
            imprenta(k)
        print('                    ', end='')
        if f < 10:
            print(' ', end='')
        print(f'{f}|', end='')
        for k in mapa_2[i]:
            imprenta(k)
        f += 1
        print()
    print()
    print(f'           > vida: {jugador_1.vida}                                 > vida: {jugador_2.vida}')
    print()

def barco_inst(n=1):
    print('introduzca la cordenada # y la direccion del barco')
    print(f'          barco 1x{n}')
    print()
    print('       |  y')
    print('       |')
    print('       |  O')
    print('       |  O')
    print('       |  # O O  x')
    
# funciones para el propio juego de la maquina
def posibles_direcciones(cordenada:str):
    letra = cordenada[0]
    numero = cordenada[1:]
    
    direciones = []
    
    match numero:
        case '1':
            direciones += ['ny']
        case '10':
            direciones += ['y']
        case _:
            direciones += ['y', 'ny']
    
    match letra:
        case 'a':
            direciones += ['x']
        case 'j':
            direciones += ['nx']
        case _:
            direciones += ['x', 'nx']
            
    return direciones
            
def cordenada_imediata(cordenada:str, direccion:str):
    try:
        letra = cordenada[0]
        numero = cordenada[1:]
        
        match direccion:
            case 'x':
                letra = numero_a_letra(letra_a_numero(letra) + 1)
            case 'nx':
                letra = numero_a_letra(letra_a_numero(letra) - 1)
            case 'y':
                numero = str(int(numero) - 1)
            case 'ny':
                numero = str(int(numero) + 1)
                
        return letra + numero
    except:
        return 'error'

def direccion_opuesta(direccion):
    match direccion:
        case 'x':
            return 'nx'
        case 'nx':
            return 'x'
        case 'y':
            return 'ny'
        case 'ny':
            return 'y'
 
# ================================================ inicio de el bucle principal
while True:
    #menu
    while True:
        os.system('cls')
        cabeza(5)
        print('     > Seleccione el modo de juego:')
        print()
        print('          1. jugador vs computador.')
        print('          2. jugador vs jugador.')
        print()
        try:
            modo_de_juego = int(input('> ___ : '))
            if modo_de_juego in [1, 2]:
                break
            else:
                input('  No existe tal variante...')
        except:
            input('  No existe tal variante...')
    
    os.system('cls')
    
    if modo_de_juego == 2:
        #quien juega primero
        cabeza(5)
        input('                    Escojan entre X y O:')
        print()
        primer_jugador = random.choice(('X','O'))
        print(f'                     Inicia {primer_jugador}:')
        salto(5)
        input('> Presione enter para continuar...')
        os.system('cls')
        
        #barcos de el jugador 1
        cabeza(3)
        input('          Por favor el jugador 2 no puede mirar...')
        os.system('cls')
        cabeza(3)
        
        barcos_1 = crear_barcos_random()
        jugador_1 = Jugador(barcos_1, '1')
        
        mapa_unijugador(jugador_1)
        
        salto(2)
        print('          Estos son los barcos de el jugador 1.')
        print()
        input('     > Siguiente, jugador 2...')
        os.system('cls')
        
        #barcos de el jugador 2
        cabeza(3)
        input('          Por favor el jugador 1 no puede mirar...')
        os.system('cls')
        cabeza(3)
        
        barcos_2 = crear_barcos_random()
        jugador_2 = Jugador(barcos_2, '2')
        
        mapa_unijugador(jugador_2)
        
        salto(2)
        print('          Estos son los barcos de el jugador 2.')
        print()
        input('     > Siguiente, inicia el juego...')
        os.system('cls')
        
        #juego principal
        jugadas_jugador_1 = []
        jugadas_jugador_2 = []
        
        turno = 0
        comando_barcos = False
        mensage = ''
        ganador = ''
        
        while True:
            os.system('cls')
            if jugador_1.vida == 0:
                ganador = 'EL JUGADOR 2'
                break
            if jugador_2.vida == 0:
                ganador = 'EL JUGADOR 1'
                break
            
            cabeza(3)
            
            mapa_bijugador(jugador_1, jugador_2, mostrar_barcos=comando_barcos)
            
            print(f'Jugadas hechas:')
            print(f'> Jugador_1: {jugadas_jugador_1}')
            print(f'> Jugador_2: {jugadas_jugador_2}')
            print()
            print(mensage)
            print()
            
            if comando_barcos:
                input('> Volver a el modo normal...')
                jugada = 'mmm'
            else:
                jugada = input(f'> Turno del jugador {(turno%2)+1}:  ')
            
            if elemento_en_matriz(cordenadas_tablero, jugada):
                if turno%2 == 0:
                    if jugada in jugadas_jugador_1:
                        mensage = '> Nota: Movimiento repetido.'
                        turno += 1
                    else:
                        jugadas_jugador_1.append(jugada)
                        jugador_2.recibir_golpe(jugada)
                        jugador_2.confirmar_relieves()
                        if elemento_en_matriz(barcos_2, jugada):
                            mensage = '> Nota: Movimiento acertado, repite turno.'
                        else:
                            mensage = '> Nota: Movimento fallido, siguiente turno.'
                            turno += 1
                else:
                    if jugada in jugadas_jugador_2:
                        mensage = '> Nota: Movimiento repetido, siguiente turno.'
                        turno += 1
                    else:
                        jugadas_jugador_2.append(jugada)
                        jugador_1.recibir_golpe(jugada)
                        jugador_1.confirmar_relieves()
                        if elemento_en_matriz(barcos_1, jugada):
                            mensage = '> Nota: Movimiento acertado, repite turno.'
                        else:
                            mensage = ''
                            turno += 1
            else:
                match jugada:
                    case 'mmm':
                        comando_barcos = not comando_barcos
                    case _:
                        mensage = '> Nota: Movimiento no valido.'
                        turno += 1
    else:
        #barcos de el jugador 
        cabeza(3)
        
        barcos_jugador = crear_barcos_random()
        jugador = Jugador(barcos_jugador, '1')
        
        barcos_maquina = crear_barcos_random()
        maquina = Jugador(barcos_maquina, 'm')
        
        mapa_unijugador(jugador)
        salto(3)

        input('     > estos son tus barcos, siguiente, juego principal.')
        
        # juego principal
        jugadas_jugador = []
        jugadas_maquina = []
        
        turno = 0
        comando_barcos = False
        mensage = ''
        
        escojer_barco_al_azar = True
        definir_cordenada_acierto = True
        m_barco_hundido = False
        m_posibles_direcciones = []
        m_direccion_recomendada = ''
        cordenada_de_acierto = ''
        maquina_ultima_jugada = ''
        
        def limpiar_maquina():
            global escojer_barco_al_azar, definir_cordenada_acierto, m_barco_hundido, m_posibles_direcciones, m_direccion_recomendada, cordenada_de_acierto, maquina_ultima_jugada
            escojer_barco_al_azar = True
            definir_cordenada_acierto = True
            m_barco_hundido = False
            m_posibles_direcciones = []
            m_direccion_recomendada = ''
            cordenada_de_acierto = ''
            maquina_ultima_jugada = ''
        
        while True:
            
            # contador de vida
            os.system('cls')
            if jugador.vida == 0:
                ganador = 'LA MAQUINA'
                break
            if maquina.vida == 0:
                ganador = 'EL JUGADOR'
                break
            
            cabeza(3)
            
            mapa_bijugador(jugador, maquina, mostrar_barcos=comando_barcos, modo_de_juego=1)
            
            print(f'Jugadas hechas:')
            print(f'> Jugador: {jugadas_jugador}')
            print(f'> maquina: {jugadas_maquina}')
            print()
            print(mensage)
            print()
            
            if comando_barcos:
                input('> Volver a el modo normal...')
                jugada = 'mmm'
            else:
                if turno%2 == 0:
                    jugada = input(f'> Turno del jugador:  ')
                else:
                    print('---')
                    if escojer_barco_al_azar:
                        jugada = random.choice(jugador.saber_puntos_disponibles())
                    else:
                        m_jugada = cordenada_imediata(maquina_ultima_jugada, m_direccion_recomendada)
                            
                        if maquina_ultima_jugada == cordenada_de_acierto:
                            repeticion_bucle = 0
                            while m_jugada in jugadas_maquina:
                                if repeticion_bucle > 10:
                                    m_jugada = random.choice(jugador.saber_puntos_disponibles())
                                    limpiar_maquina()
                                m_posibles_direcciones = m_posibles_direcciones[1:]
                                if m_posibles_direcciones != []:
                                    m_direccion_recomendada = m_posibles_direcciones[0]
                                else:
                                    m_direccion_recomendada = 'x'
                                m_jugada = cordenada_imediata(maquina_ultima_jugada, m_direccion_recomendada)
                                repeticion_bucle += 1
                                
                        if m_jugada in jugador.relieves:
                            m_jugada = random.choice(jugador.saber_puntos_disponibles())
                            limpiar_maquina()
                        
                        if m_jugada in jugadas_maquina:
                            m_direccion_recomendada = direccion_opuesta(m_direccion_recomendada)
                            maquina_ultima_jugada = cordenada_de_acierto
                            m_jugada = cordenada_imediata(maquina_ultima_jugada, m_direccion_recomendada)
                            
                        jugada = m_jugada
                    
            if elemento_en_matriz(cordenadas_tablero, jugada):
                if turno%2 == 0:
                    if jugada in jugadas_jugador:
                        mensage = '> Nota: Movimiento repetido.'
                        turno += 1
                    else:
                        jugadas_jugador.append(jugada)
                        maquina.recibir_golpe(jugada)
                        maquina.confirmar_relieves()
                        if elemento_en_matriz(barcos_maquina, jugada):
                            mensage = '> Nota: Movimiento acertado, repite turno.'
                        else:
                            mensage = '> Nota: Movimento fallido, siguiente turno.'
                            turno += 1
                else:
                    if jugada in jugadas_maquina:
                        limpiar_maquina()
                        mensage = '> Nota: La maquina repitio un turno, posible error!!.'
                        turno += 1
                    else:
                        jugadas_maquina.append(jugada)
                        jugador.recibir_golpe(jugada)
                        jugador.confirmar_relieves()
                        if elemento_en_matriz(barcos_jugador, jugada):
                            maquina_ultima_jugada = jugada
                            if definir_cordenada_acierto:
                                m_barco_hundido = False
                                escojer_barco_al_azar = False
                                cordenada_de_acierto = jugada
                                m_posibles_direcciones = posibles_direcciones(jugada)
                                m_direccion_recomendada = m_posibles_direcciones[0]
                                definir_cordenada_acierto = False
                            mensage = '> Nota: Movimiento acertado por la maquina.'
                        else:                                
                            if not escojer_barco_al_azar:
                                if maquina_ultima_jugada == cordenada_de_acierto:
                                    m_posibles_direcciones = m_posibles_direcciones[1:]
                                    m_direccion_recomendada = m_posibles_direcciones[0]
                                    mensage = '> Nota: Movimiento fallido, rectificacion de primer acierto.'
                                else:
                                    m_direccion_recomendada = direccion_opuesta(m_direccion_recomendada)
                                    maquina_ultima_jugada = cordenada_de_acierto
                            
                            turno += 1
                            
                    if jugada in jugador.relieves:
                        limpiar_maquina()   
            else:
                if turno%2 == 1:
                    limpiar_maquina()
                    
                match jugada:
                    case 'mmm':
                        comando_barcos = not comando_barcos
                    case 'vvv':
                        print()
                        print(f'''escojer_barco_al_azar = {escojer_barco_al_azar}
definir_cordenada_acierto = {definir_cordenada_acierto}
m_posibles_direciones = {m_posibles_direcciones}
m_direccion_recomendada = {m_direccion_recomendada}
cordenada_de_acierto = {cordenada_de_acierto}
maquina_ultima_jugada = {maquina_ultima_jugada}''')
                        print()
                        input('   > presione entrer para continuar...')
                    case _:
                        mensage = '> Nota: Movimiento no valido.'
                        turno += 1
                        
    #parte final
    os.system('cls')
    cabeza(5)
    print(f'          FELICIDADEZ {ganador} GANA!!!')
    salto(8)
    repetir = input('> Desea volver a jugar? [s/n]:  ')
    
    if repetir == 'n':
        os.system('cls')
        break
    os.system('cls')

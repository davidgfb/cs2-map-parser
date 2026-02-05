patrones = 'm_meshes', 'm_Triangles', '#[', ']'

'''
patron_M_Meshes = 'm_meshes'
patron_M_Triangles = 'm_Triangles'
patron_Alm_Ab_Corc = '#['
'''
#NO hace falta encontrar ] de m_meshes porque solo hay 1 al menos en dust 

encontrado_M_Meshes = False
encontrado_M_Triangles = False
encontrado_M_Vertices = False

#dentro_Str_BB_Sep_Esp = False
hay_Cambio = False

# Nivel anidamiento de m_Triangles tan solo varia entre 0 y 1
nivel_Anidamiento = {'m_meshes': 0,'m_Triangles':0,'m_Vertices':0}

# nivel_Anidamiento n veces que se abren y cierran corchetes -> 0 

with open('C:/Users/Gracia/Documents/cli-windows-x64/de_dust2/datos_Bloque_PHYS/world_physics.vphys',"r",encoding="utf-8") as doc_phys:
    enumeracion_doc_phys = enumerate(doc_phys, 1)

    for num_linea, linea in enumeracion_doc_phys: 
        for patron in patrones:
            if linea.find(patron)!=-1:#find devuelve -1 si no se encuentra
                if patron == 'm_meshes':
                    encontrado_M_Meshes=True#condicion para m_Triangles y m_Vertices
                    hay_Cambio = True#imprime(patron, num_linea, linea)#enumeracion_doc_phys)#

                if encontrado_M_Meshes:
                    #********* m_Triangles ***********
                    if patron == 'm_Triangles':
                       encontrado_M_Triangles = True
                       hay_Cambio = True#imprime(patron, num_linea, linea)#enumeracion_doc_phys)#

                    if encontrado_M_Triangles:
                        if patron == '#[':
                            nivel_Anidamiento['m_Triangles'] += 1
                            hay_Cambio = True#imprime(patron, num_linea, linea)#enumeracion_doc_phys)#
                            print(f'{30*"#"}\nDecision: entro en anidamiento m_Triangles\n\nAumento nivel anidamiento m_Triangles = {nivel_Anidamiento["m_Triangles"]}\n')
                            #dentro_Str_BB_Sep_Esp = True
                            
                        if patron == ']':
                            nivel_Anidamiento['m_Triangles'] -= 1
                            hay_Cambio = True#imprime(patron, num_linea, linea)#enumeracion_doc_phys)#
                            print(f'{30*"#"}\nReduzco nivel anidamiento m_Triangles = {nivel_Anidamiento["m_Triangles"]}\n')

                            if nivel_Anidamiento['m_Triangles']==0:
                                encontrado_M_Triangles = False
                                hay_Cambio = True#imprime(patron, num_linea, linea)#enumeracion_doc_phys)#
                                print('Decision: salgo de anidamiento m_Triangles\n')

                    #********** m_Vertices ************
                    if patron == 'm_Vertices':
                        encontrado_M_Vertices = True
                        hay_Cambio = True#imprime(patron, num_linea, linea)#enumeracion_doc_phys)#

                    if encontrado_M_Vertices:                  
                        if patron == '#[':
                            nivel_Anidamiento['m_Vertices'] += 1
                            hay_Cambio = True#imprime(patron, num_linea, linea)#enumeracion_doc_phys)#
                            print(f'{30*"#"}\nDecision: entro en anidamiento m_Vertices\n\nAumento nivel anidamiento m_Vertices = {nivel_Anidamiento["m_Vertices"]}\n')

                        if patron == ']':
                            nivel_Anidamiento['m_Vertices'] -= 1
                            hay_Cambio = True#imprime(patron, num_linea, linea)#enumeracion_doc_phys)#
                            print(f'{30*"#"}\nReduzco nivel anidamiento m_Vertices = {nivel_Anidamiento["m_Vertices"]}\n')

                            if nivel_Anidamiento['m_Vertices']==0:
                                encontrado_M_Vertices = False
                                hay_Cambio = True#imprime(patron, num_linea, linea)#enumeracion_doc_phys)#
                                print('Decision: salgo de anidamiento m_Vertices\n')
                            
                if hay_Cambio: 
                    hay_Cambio = False
                    print(f"{patron} encontrado en la línea {num_linea}: {linea.strip()}\n")

#if linea.find(patron_M_Triangles)!=-1:print(f"{patron_M_Triangles} encontrado en la línea {num_linea}: {linea.strip()}")
                
#if linea.find(patron_Alm_Ab_Corc)!=-1:print(f"{patron_Alm_Ab_Corc} encontrado en la línea {num_linea}: {linea.strip()}")

'''
if dentro_Str_BB_Sep_Esp and patron == ']':
   dentro_Str_BB_Sep_Esp = False
   hay_Cambio = True
'''

'''
def imprime(patron, num_linea, linea): #enumeracion_doc_phys):
    #num_linea, linea = enumeracion_doc_phys

    print(f"{patron} encontrado en la línea {num_linea}: {linea.strip()}\n")
'''

'''
import struct

# String de bytes original
m_Triangles_str = "27 08 00 00 28 08 00 00 26 08 00 00 29 08 00 00 26 08 00 00 28 08 00 00 FB 07 00 00 FC 07 00 00 FA 07 00 00 04 08 00 00 05 08 00 00 FC 07 00 00 06 08 00 00 FC 07 00 00 05 08 00 00 20 08 00 00"

# 1. Convertir string a lista de bytes individuales
# entero base 16 hex
bytes_list=[int(_2_BB,16)for _2_BB in m_Triangles_str.split()]#sep str esps

# bytes_list) # arr 00 ... ff, -> 0 ... 255,

# 2. Agrupar de 4 en 4 bytes y convertir a enteros de 32 bits (little-endian)
m_Triangles = []

# múltiplos de 4: 4k, k e Z
for i in range(0, len(bytes_list), 4): # de 4 en 4
    chunk = bytes(bytes_list[i : i + 4])

    # bytes_list[i : i + 4]) # arr anido n x 4 enteros

    # Usamos little-endian ('little') dado que los bytes bajos van primero (ej. 27 08 00 00)
    value = int.from_bytes(chunk, byteorder='little',signed=False)

    # value) # arr anido n x 4 enteros -> entero
    
    m_Triangles.append(value)

print(m_Triangles)


# 2. Convertir la cadena de texto a un objeto de bytes real
# Eliminamos los espacios y convertimos de hexadecimal a bytes
raw_bytes = bytes.fromhex(hex_string.replace(" ", ""))

# 3. Desempaquetar los bytes como enteros de 32 bits (I = unsigned int, l = signed int)
# El símbolo '<' indica Little Endian (el primer byte es el menos significativo)
num_integers = len(raw_bytes) // 4
m_Triangles = struct.unpack(f'<{num_integers}I', raw_bytes)

# Convertir a lista (unpack devuelve una tupla)
m_Triangles = list(m_Triangles)
'''

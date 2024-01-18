from os import strerror

def validar(file):
    try:
        stream = open(file, "rt")
        stream.close()
        return True
    except IOError as e:
        print("Se ha producido un errror de E/S: ", strerror(e.errno))
        return False

dicc_ordenado = lambda dicc: {key: dicc[key] for key in sorted(dicc, key=dicc.get, reverse=True)}
file = input("Ingrese el nombre del archivo: ")
dicc = {}

if validar(file):
    try:
        stream = open(file, 'rt')
        chr = stream.read(1)
        while chr != '':           
            if chr not in dicc:
                dicc[chr.lower()] = 1
            else:
                dicc[chr.lower()] = dicc[chr.lower()] + 1
            chr = stream.read(1)
        stream.close()
        dicc = dicc_ordenado(dicc)
        for chr in dicc:
            if chr != '\n' and chr != ' ':
                print(chr,' -> ', dicc[chr])
    except IOError as e:
        print("Ha ocurrido un error: ", strerror(e.errno))
        stream.close()
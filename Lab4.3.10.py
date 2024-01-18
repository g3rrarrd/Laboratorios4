from os import strerror

class StudentDataException(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)

class BadLine(StudentDataException):
    def __init__(self, badline, message):
        StudentDataException.__init__(self, message)
        self.badline = badline

class FileEmpty(StudentDataException):
    def __init__(self, file, message):
        StudentDataException.__init__(self, message)
        self.file = file

alumnos = {}
counter = 0


ordenar_alumnos = lambda alumnos: {key: alumnos[key] for key in sorted(alumnos)}

def registrar_alumnos(file):
    try:
        stream = open(file, 'rt')
        lines = stream.readlines(5)
        while len(lines) != 0:
            for line in lines:
                alumno = line.split(' ')
                i = 0
            while i != 2:
               alumno[i] = alumno[i].capitalize()
               i += 1
            if alumno[0] + ' ' + alumno[1] not in alumnos:
                alumnos[alumno[0] + ' ' + alumno[1]] = float(alumno[2])
            else:
                alumnos[alumno[0] + ' ' + alumno[1]] += float(alumno[2])
            lines = stream.readlines(5) 
        stream.close()
        print(ordenar_alumnos(alumnos))
    except IOError as e:
        raise StudentDataException("Error al abrir el archivo: " + strerror(e.errno))

def verificar_contenido(file):
    counter = 0
    try:
        stream = open(file, 'rt')
        chr = stream.readlines(5)
        if len(chr) == 0:
            raise FileEmpty(file, "No posee contenido")
        else: 
           while len(chr) > 0:
                counter += 1
                for line in chr:
                    alumno = line.split(' ')
                    if len(alumno) <= 2 or len(alumno) > 3:
                        raise BadLine(counter, "Fallo en el ordenamiento nombre/apellido/nota")        
                chr = stream.readlines(5)
    except IOError as e:
        raise StudentDataException("Error al abrir el archivo: " + strerror(e.errno))

try:
    file = input('Ingrese el nombre del archivo: ')
    verificar_contenido(file)
    registrar_alumnos(file)
except BadLine as bl:
    print("Error en la linea: ", bl.badline, ' ', bl)
except FileEmpty as fe:
    print("Archivo: ", fe.file, "; ", fe)
except StudentDataException as sde:
    print(sde)
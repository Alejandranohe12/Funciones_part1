"""
la utilidad de la funciones es la reutilización de código.
La reutilización de código se refiere al comportamiento y a las técnicas que garantizan que una parte o la totalidad de un programa informático existente, se pueda emplear en la construcción de otro programa.
De esta forma se aprovecha el trabajo anterior, se economiza tiempo, y se reduce el exceso/abundancia.
 
Aparte de la función "print" hay funciones predefinidas y funciones propias.
Un ejemplo es "print" es una función predefinida por el lenguaje, es decir, que ya viene con el lenguaje 
Y lo mejor es qu podemos tenerla a nuestra disposición cuando queramos
Y luego estan las funciones creadas por nosotros mismos. Para definir y crear una funcion se utiliza el "def"
"""
def mensaje(): #Aquí se hace una declaración o nombre de la función propia "def mensaje()"
    print("Estoy aprendiendo en Python")
    print("Estoy aprendiendo intrucciones") #ESTOS tres primeros print son el cuerpo de la función
    print("Poco a poco ire avanzando")
mensaje() #----->>> Ahora hacemos una llamada a la función

"Otro ejemplo:"
def funcion(nombre, edad): #declaramos nuestros parametros dentro de nuestra funcion. Podemos declarar mas parametros si queremos, pero separandolos siempre con comas
    print('hola desde mi funcion')
    print(f'Nombre: {nombre}, Edad: {edad}')
funcion('Marisol', 28 ) #aquí ponemos los valores de los parametros declarados
funcion("Josefina", 45)



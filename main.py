from usuario import Usuario

usuario = Usuario("Luis", "luis@gmail.com", "papo321")

print ('Bienvenido al sistema de compras')

while True:
    print('Menú de opciones')
    if usuario == None:
        print('1) iniciar sesion')
        print('2) crear cuenta')
        print('0) salir')

    else:
        print('1) ver carrito')
        print('2) ver productos disponibles')
        print('3) rpoceder a comprar')
        print('0) salir')

    opción = int(input('Ingresa una opcion: '))


print('*** Bienvenido al sistema de generador de emails de Ciudad Gotica***')
nombre = input('Cual es tu nombre?: ').lower()
apellido = input('Cual es tu apellido?: ').lower()
email = (f'{nombre}.{apellido}@ciudadgotica.com')

print(f'''
    Tu nuevo email generado por el sistema es:
        {email}
        ***Felicidades***
''')
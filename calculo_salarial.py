def salario():
    while True:
        valor_salario = input("Cuanto es el monto de su salario mensual?: ")
        if valor_salario.isdigit():
            valor_salario = int(valor_salario)
            if valor_salario > 0:             
                      break
            else:
              print("porfavor introduce un valor mayor a 0")
        else:
            print("por favor ingrese un numero")
    return valor_salario


def tiempo():
    while True:
          dias_trabajados = input("cuantos dias de trabajo lleva este año?: ")
          if dias_trabajados.isdigit():
              dias_trabajados = int(dias_trabajados)
              if dias_trabajados > 0:
                   break
              else: 
                print("Por favor introduce un numero de dias valido")
          else: 
            print("por favor ingresa el numero de dias trabajados")
    return dias_trabajados

prima = (salario() * tiempo()) / 360
print("Tu prima de este semestre tiene un valor de: " , prima)

class Calculator:

    def __init__(self):
        pass
    
    def add(self, a, b):
        return a + b
    
    def substract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        return a / b
    
    def modulo(self, a, b):
        return a % b

if __name__ == "__main__":
    my_calculator = Calculator()

    while True:
        print("\nOpciones: 1=sumar 2=restar 3=multiplicar 4=dividir 5=modulo 6=salir ")
        try:
            opcion = int(input(" seleccione una opción del (1-6): "))

            if opcion == 6:
                print("saliendo de la calculadora...")
                break
            if opcion <1 or opcion > 6:
                print("Opción invalida, ingrese un valor de (1 - 6)")
                continue

            num1= float(input("ingrese su primer numero: "))
            num2= float(input("Ingrese su segundo numero: "))

            if opcion == 1:
                print("Su resultado es: ", my_calculator.add(num1, num2))
            
            elif opcion == 2:
                print("su resultado es: ", my_calculator.substract(num1, num2))
            elif opcion == 3:
                print("Su resultado es: ", my_calculator.multiply(num1, num2))
            elif opcion == 4:
                print("Su resultado es: ", my_calculator.divide(num1, num2))
                if num2 == 0:
                    raise ZeroDivisionError("No se puede dividir por cero")
                print("Resultado: ", my_calculator.modulo(num1,num2))

        except ValueError:
            print("error, ingrese numeros validos. ")
        except ZeroDivisionError as e:
            print("error: ", e)
        except Exception as e:
            print("error: ", e)
        finally: 
            print(" operacion completada! ")

    #print(my_calculator.add(5, 7))
    #print(my_calculator.subtract(45, 11))
    #print(my_calculator.multiply(3, 2))
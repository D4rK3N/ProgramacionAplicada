import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk

class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("No se puede dividir por cero")
        return a / b
    
    def modulo(self, a, b):
        if b == 0:
            raise ZeroDivisionError("No se puede calcular el módulo por cero")
        return a % b

class FrutigerAeroCalculator(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora Aero")
        self.geometry("340x540") # Ajustado para mejor proporción y espaciado
        self.resizable(False, False)
        
        # Tema personalizado para evocar Frutiger Aero
        ctk.set_appearance_mode("dark") # Base oscura para contraste
        # Colores personalizados que sugieren tonos azules y grises translúcidos
        ctk.set_default_color_theme("blue") # Puedes experimentar con "dark-blue" o "green" también.

        self.calculator = Calculator()
        self.expression = ""
        self.current_operand = "" # Para construir el número actual

        # --- Frame Principal para el Fondo (simula una capa "aero") ---
        # Usamos un frame más grande para dar la sensación de profundidad
        self.main_frame = ctk.CTkFrame(
            self, 
            fg_color="#0D47A1", # Un azul oscuro que sirve de fondo "profundo"
            bg_color="transparent", # Necesario si la ventana principal fuera translúcida
            corner_radius=20, # Bordes redondeados para el "vidrio" principal
            border_width=3,
            border_color="#4FC3F7" # Borde brillante, tipo "glow"
        )
        self.main_frame.pack(fill="both", expand=True, padx=15, pady=15)

        # --- Display de Resultado (Pantalla) ---
        self.result_display = ctk.CTkEntry(
            self.main_frame, # Anclado al main_frame
            width=290, 
            height=70, 
            font=ctk.CTkFont(family="Segoe UI", size=32, weight="bold"), # Fuente similar a Windows Aero
            justify="right",
            fg_color="#E0F2F7", # Azul muy pálido, casi blanco translúcido
            text_color="#0A3D62", # Azul oscuro para el texto
            corner_radius=18, # Esquinas más pronunciadas
            border_width=2,
            border_color="#90CAF9" # Borde suave que sugiere brillo
        )
        self.result_display.pack(pady=(25, 15), padx=20, fill="x") # Pack para centrar y espaciar
        self.result_display.insert(0, "0")
        self.result_display.configure(state="readonly")

        # --- Contenedor de Botones (con espaciado para efecto "flotante") ---
        self.button_grid_frame = ctk.CTkFrame(
            self.main_frame, # Anclado al main_frame
            fg_color="transparent" # Frame transparente para que el fondo del main_frame se vea
        )
        self.button_grid_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Configuración de las columnas y filas del grid para los botones
        for i in range(4):
            self.button_grid_frame.grid_columnconfigure(i, weight=1, uniform="button_col")
        for i in range(5):
            self.button_grid_frame.grid_rowconfigure(i, weight=1, uniform="button_row")

        # --- Botones ---
        buttons = [
            ('C', 0, 0, 1, self.clear_display, "#FF6B6B", "#FF3B3B"), # Rojo suave
            ('+/-', 0, 1, 1, self.negate_number, "#78909C", "#607D8B"), # Gris para utilidades
            ('%', 0, 2, 1, lambda: self.on_operator_click('%'), "#78909C", "#607D8B"),
            ('/', 0, 3, 1, lambda: self.on_operator_click('/'), "#007AFF", "#0056B3"), # Azul vibrante

            ('7', 1, 0, 1, lambda: self.on_digit_click('7'), "#E0F2F7", "#C6EEFA"), # Tonos claros de azul/blanco
            ('8', 1, 1, 1, lambda: self.on_digit_click('8'), "#E0F2F7", "#C6EEFA"),
            ('9', 1, 2, 1, lambda: self.on_digit_click('9'), "#E0F2F7", "#C6EEFA"),
            ('*', 1, 3, 1, lambda: self.on_operator_click('*'), "#007AFF", "#0056B3"),

            ('4', 2, 0, 1, lambda: self.on_digit_click('4'), "#E0F2F7", "#C6EEFA"),
            ('5', 2, 1, 1, lambda: self.on_digit_click('5'), "#E0F2F7", "#C6EEFA"),
            ('6', 2, 2, 1, lambda: self.on_digit_click('6'), "#E0F2F7", "#C6EEFA"),
            ('-', 2, 3, 1, lambda: self.on_operator_click('-'), "#007AFF", "#0056B3"),

            ('1', 3, 0, 1, lambda: self.on_digit_click('1'), "#E0F2F7", "#C6EEFA"),
            ('2', 3, 1, 1, lambda: self.on_digit_click('2'), "#E0F2F7", "#C6EEFA"),
            ('3', 3, 2, 1, lambda: self.on_digit_click('3'), "#E0F2F7", "#C6EEFA"),
            ('+', 3, 3, 1, lambda: self.on_operator_click('+'), "#007AFF", "#0056B3"),

            ('0', 4, 0, 2, lambda: self.on_digit_click('0'), "#E0F2F7", "#C6EEFA"), # El 0 ocupa 2 columnas
            ('.', 4, 2, 1, lambda: self.on_digit_click('.'), "#E0F2F7", "#C6EEFA"),
            ('=', 4, 3, 1, lambda: self.on_operator_click('='), "#28A745", "#218838") # Verde para igual (acción final)
        ]

        for (text, r, c, cs, cmd, fg, hg) in buttons:
            button = ctk.CTkButton(
                self.button_grid_frame, 
                text=text, 
                command=cmd,
                font=ctk.CTkFont(family="Segoe UI", size=24, weight="bold"),
                fg_color=fg, # Color base
                hover_color=hg, # Color al pasar el mouse
                text_color="#0A3D62" if fg == "#E0F2F7" else "white", # Texto oscuro para botones claros
                corner_radius=15, # Esquinas redondeadas
                height=65 # Altura uniforme para los botones
            )
            button.grid(row=r, column=c, columnspan=cs, padx=6, pady=6, sticky="nsew") # Espaciado y relleno

    def update_display(self, value):
        self.result_display.configure(state="normal")
        self.result_display.delete(0, tk.END)
        self.result_display.insert(0, str(value))
        self.result_display.configure(state="readonly")

    def clear_display(self):
        self.expression = ""
        self.current_operand = ""
        self.update_display("0")

    def on_digit_click(self, digit):
        if self.result_display.get() == "Error" or self.result_display.get() == "0":
            self.expression = ""
            self.current_operand = ""

        if digit == '.' and '.' in self.current_operand:
            return # Evitar múltiples puntos

        self.expression += digit
        self.current_operand += digit
        self.update_display(self.expression)

    def on_operator_click(self, operator):
        if operator == '=':
            try:
                # Reemplazar operadores en la expresión para ser evaluados por Python
                # En una calculadora real se necesitaría un analizador más robusto (eval es peligroso con entradas de usuario)
                # Para este ejemplo, intentamos simular la evaluación directa para simplificar
                
                # Buscamos el último operador para dividir la expresión
                parts = []
                last_op_index = -1
                for i in range(len(self.expression) -1, -1, -1):
                    if self.expression[i] in ['+', '-', '*', '/', '%']:
                        last_op_index = i
                        break
                
                if last_op_index != -1:
                    num1_str = self.expression[:last_op_index].strip()
                    op = self.expression[last_op_index]
                    num2_str = self.expression[last_op_index+1:].strip()

                    num1 = float(num1_str)
                    num2 = float(num2_str)

                    result = None
                    if op == '+':
                        result = self.calculator.add(num1, num2)
                    elif op == '-':
                        result = self.calculator.subtract(num1, num2)
                    elif op == '*':
                        result = self.calculator.multiply(num1, num2)
                    elif op == '/':
                        result = self.calculator.divide(num1, num2)
                    elif op == '%':
                        result = self.calculator.modulo(num1, num2)
                    
                    self.update_display(str(result))
                    self.expression = str(result)
                    self.current_operand = str(result) # El resultado es el nuevo operando actual
                else:
                    # Si no hay operador, significa que solo hay un número, no hay que calcular
                    self.update_display(self.expression or "0")

            except ZeroDivisionError as e:
                messagebox.showerror("Error", str(e))
                self.clear_display()
                self.update_display("Error")
            except ValueError:
                messagebox.showerror("Error", "Entrada inválida. Asegúrate de ingresar números.")
                self.clear_display()
                self.update_display("Error")
            except Exception as e:
                messagebox.showerror("Error", "Error de cálculo: " + str(e))
                self.clear_display()
                self.update_display("Error")
        else:
            # Si el último carácter es un operador, reemplazarlo
            if self.expression and self.expression[-1] in ['+', '-', '*', '/', '%']:
                self.expression = self.expression[:-1] + operator
            else:
                self.expression += operator
            
            self.current_operand = "" # Resetear el operando actual para el siguiente número
            self.update_display(self.expression)


    def negate_number(self):
        current_text = self.result_display.get()
        if current_text == "0" or not self.current_operand:
            return

        try:
            # Buscar el último número en la expresión y negarlo
            last_op_index = -1
            for i in range(len(self.expression) - 1, -1, -1):
                if self.expression[i] in ['+', '-', '*', '/', '%']:
                    last_op_index = i
                    break
            
            num_to_negate_str = ""
            if last_op_index != -1:
                num_to_negate_str = self.expression[last_op_index+1:]
            else:
                num_to_negate_str = self.expression

            if num_to_negate_str:
                negated_num = float(num_to_negate_str) * -1
                
                # Reconstruir la expresión
                if last_op_index != -1:
                    self.expression = self.expression[:last_op_index+1] + str(negated_num)
                else:
                    self.expression = str(negated_num)
                
                self.current_operand = str(negated_num)
                self.update_display(self.expression)
            
        except ValueError:
            messagebox.showwarning("Advertencia", "No se puede negar este valor.")
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    app = FrutigerAeroCalculator()
    app.mainloop()
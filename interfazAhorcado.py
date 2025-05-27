__author__ = "Jenifer U. C. Andres B. C. , Zara C. B."
__version__ = "1.0.0"
__license__ = "GPL"
__email__ = "jenifer.urbano@campusucc.edu.co"

"""
Ahorcado - Interfaz Gráfica cn Tkinter

"""

import tkinter as tk
from tkinter import messagebox, font
from src.JuegoAhorcado import JuegoAhorcado, Estado
from src.Letra import Letra

class AhorcadoGUI:
    COLORS = {
        'bg_primary': '#3f343a',      # color1 - fondo principal
        'bg_secondary': '#59494f',    # color2 - fondo secundario
        'accent': '#8e6f74',          # color3 - acentos
        'text_light': '#cda8ad',      # color4 - texto claro
        'text_highlight': '#e0c9c7',  # color5 - texto destacado
        'letter_unused': '#8e6f74',   # letra no usada
        'letter_correct': '#2d5016',  # letra correcta (verde oscuro)
        'letter_incorrect': '#7d1538', # letra incorrecta (rojo oscuro)
        'button_hover': '#6b565c'     # hover de botones
    }
    
    def __init__(self):
        self.juego = JuegoAhorcado()
        self.palabras_usadas = set()  # Set para almacenar palabras ya usadas
        self.root = tk.Tk()
        self.setup_window()
        self.create_fonts()
        self.create_widgets()
        
    def setup_window(self):
        """Configuración inicial de la ventana"""
        self.root.title(" AHORCADO ")
        self.root.geometry("1000x900")
        self.root.configure(bg=self.COLORS['bg_primary'])
        self.root.resizable(False, False)
        
        # Centrar ventana
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (800 // 2)
        y = (self.root.winfo_screenheight() // 2) - (700 // 2)
        self.root.geometry(f"1200x700+{x}+{y}")
    
    def create_fonts(self):
        """Crear fuentes Press Start 2P"""
        try:
            # Intentar cargar la fuente Press Start 2P
            self.pixel_font_large = font.Font(family="Press Start 2P", size=20)
            self.pixel_font_medium = font.Font(family="Press Start 2P", size=12)
            self.pixel_font_small = font.Font(family="Press Start 2P", size=10)
            self.pixel_font_tiny = font.Font(family="Press Start 2P", size=8)
            self.pixel_font_mini = font.Font(family="Press Start 2P", size=6)
        except tk.TclError:
            # Si Press Start 2P no está disponible, usar alternativas pixeladas
            try:
                # Alternativa 1: Courier New (monoespaciada)
                self.pixel_font_large = font.Font(family="Courier New", size=24, weight="bold")
                self.pixel_font_medium = font.Font(family="Courier New", size=16, weight="bold")
                self.pixel_font_small = font.Font(family="Courier New", size=12, weight="bold")
                self.pixel_font_tiny = font.Font(family="Courier New", size=10, weight="bold")
                self.pixel_font_mini = font.Font(family="Courier New", size=8)
                print("Usando Courier New como alternativa a Press Start 2P")
            except:
                # Alternativa 2: Terminal/monospace
                self.pixel_font_large = font.Font(family="monospace", size=24, weight="bold")
                self.pixel_font_medium = font.Font(family="monospace", size=16, weight="bold")
                self.pixel_font_small = font.Font(family="monospace", size=12, weight="bold")
                self.pixel_font_tiny = font.Font(family="monospace", size=10, weight="bold")
                self.pixel_font_mini = font.Font(family="monospace", size=8)
                print("Usando monospace como alternativa a Press Start 2P")
    
    def create_widgets(self):
        """Crear todos los widgets de la interfaz"""
        # Frame principal
        main_frame = tk.Frame(self.root, bg=self.COLORS['bg_primary'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Título
        title_frame = tk.Frame(main_frame, bg=self.COLORS['bg_secondary'], relief='raised', bd=3)
        title_frame.pack(fill=tk.X, pady=(0, 20))
        
        title_label = tk.Label(
            title_frame, 
            text="🎮 AHORCADO 🎮",
            font=self.pixel_font_large,
            bg=self.COLORS['bg_secondary'],
            fg=self.COLORS['text_highlight'],
            pady=15
        )
        title_label.pack()
        
        # Frame del juego (izquierda y derecha)
        game_frame = tk.Frame(main_frame, bg=self.COLORS['bg_primary'])
        game_frame.pack(fill=tk.BOTH, expand=True)
        
        # Panel izquierdo - Ahorcado
        left_panel = tk.Frame(game_frame, bg=self.COLORS['bg_secondary'], relief='sunken', bd=3)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # Canvas para dibujar ahorcado
        self.canvas = tk.Canvas(
            left_panel, 
            width=300, 
            height=250,
            bg=self.COLORS['bg_primary'],
            highlightthickness=0
        )
        self.canvas.pack(pady=20)
        
        # Panel derecho - Info del juego
        right_panel = tk.Frame(game_frame, bg=self.COLORS['bg_secondary'], relief='sunken', bd=3)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Palabra a adivinar
        palabra_frame = tk.Frame(right_panel, bg=self.COLORS['bg_secondary'])
        palabra_frame.pack(pady=20)
        
        tk.Label(
            palabra_frame,
            text="PALABRA:",
            font=self.pixel_font_medium,
            bg=self.COLORS['bg_secondary'],
            fg=self.COLORS['text_light']
        ).pack()
        
        self.palabra_label = tk.Label(
            palabra_frame,
            text="_ _ _ _ _ _ _ _",
            font=self.pixel_font_large,
            bg=self.COLORS['bg_secondary'],
            fg=self.COLORS['text_highlight']
        )
        self.palabra_label.pack(pady=10)
        
        # Etiqueta para mostrar cantidad de letras (pequeña y discreta)
        self.letras_count_label = tk.Label(
            palabra_frame,
            text="",
            font=self.pixel_font_mini,
            bg=self.COLORS['bg_secondary'],
            fg=self.COLORS['accent']
        )
        self.letras_count_label.pack()
        
        # Intentos restantes
        intentos_frame = tk.Frame(right_panel, bg=self.COLORS['bg_secondary'])
        intentos_frame.pack(pady=10)
        
        tk.Label(
            intentos_frame,
            text="INTENTOS:",
            font=self.pixel_font_medium,
            bg=self.COLORS['bg_secondary'],
            fg=self.COLORS['text_light']
        ).pack()
        
        self.intentos_label = tk.Label(
            intentos_frame,
            text="6",
            font=self.pixel_font_large,
            bg=self.COLORS['bg_secondary'],
            fg=self.COLORS['text_highlight']
        )
        self.intentos_label.pack()
        
        # Frame para el teclado
        keyboard_frame = tk.Frame(main_frame, bg=self.COLORS['bg_primary'])
        keyboard_frame.pack(fill=tk.X, pady=(20, 0))
        
        # Crear teclado virtual
        self.create_keyboard(keyboard_frame)
        
        # Botones de control
        control_frame = tk.Frame(main_frame, bg=self.COLORS['bg_primary'])
        control_frame.pack(fill=tk.X, pady=(20, 0))
        
        self.nuevo_juego_btn = tk.Button(
            control_frame,
            text="🎮 NUEVO JUEGO",
            font=self.pixel_font_medium,
            bg=self.COLORS['accent'],
            fg=self.COLORS['text_highlight'],
            activebackground=self.COLORS['button_hover'],
            activeforeground=self.COLORS['text_highlight'],
            relief='raised',
            bd=3,
            padx=20,
            pady=10,
            command=self.nuevo_juego
        )
        self.nuevo_juego_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        salir_btn = tk.Button(
            control_frame,
            text="❌ SALIR",
            font=self.pixel_font_medium,
            bg=self.COLORS['letter_incorrect'],
            fg=self.COLORS['text_highlight'],
            activebackground='#5c0f28',
            activeforeground=self.COLORS['text_highlight'],
            relief='raised',
            bd=3,
            padx=20,
            pady=10,
            command=self.root.quit
        )
        salir_btn.pack(side=tk.RIGHT)
        
        # Inicializar juego
        self.nuevo_juego()
    
    def create_keyboard(self, parent):
        """Crear teclado virtual"""
        self.letter_buttons = {}
        
        # Layout del teclado QWERTY
        rows = [
            ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
            ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Ñ'],
            ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
        ]
        
        for i, row in enumerate(rows):
            row_frame = tk.Frame(parent, bg=self.COLORS['bg_primary'])
            row_frame.pack(pady=5)
            
            for letter in row:
                btn = tk.Button(
                    row_frame,
                    text=letter,
                    font=self.pixel_font_small,
                    width=3,
                    height=1,
                    bg=self.COLORS['letter_unused'],
                    fg=self.COLORS['text_highlight'],
                    activebackground=self.COLORS['button_hover'],
                    activeforeground=self.COLORS['text_highlight'],
                    relief='raised',
                    bd=2,
                    command=lambda l=letter: self.jugar_letra(l)
                )
                btn.pack(side=tk.LEFT, padx=2)
                self.letter_buttons[letter.lower()] = btn
    
    def draw_hangman(self, intentos_restantes):
        """Dibujar el ahorcado según intentos restantes"""
        self.canvas.delete("all")
        
        # Color de líneas
        line_color = self.COLORS['text_light']
        line_width = 4
        
        # Base (siempre visible)
        self.canvas.create_rectangle(50, 220, 250, 240, fill=line_color, outline=line_color)
        
        if intentos_restantes <= 5:
            # Poste vertical
            self.canvas.create_rectangle(140, 50, 150, 220, fill=line_color, outline=line_color)
        
        if intentos_restantes <= 4:
            # Viga horizontal
            self.canvas.create_rectangle(140, 50, 200, 60, fill=line_color, outline=line_color)
        
        if intentos_restantes <= 3:
            # Cuerda
            self.canvas.create_rectangle(195, 60, 200, 90, fill=line_color, outline=line_color)
        
        if intentos_restantes <= 2:
            # Cabeza
            self.canvas.create_oval(180, 90, 215, 125, outline=line_color, width=line_width)
        
        if intentos_restantes <= 1:
            # Cuerpo
            self.canvas.create_rectangle(195, 125, 200, 180, fill=line_color, outline=line_color)
        
        if intentos_restantes <= 0:
            # Brazos
            self.canvas.create_line(197, 140, 170, 160, fill=line_color, width=line_width)
            self.canvas.create_line(197, 140, 225, 160, fill=line_color, width=line_width)
            # Piernas
            self.canvas.create_line(197, 180, 170, 210, fill=line_color, width=line_width)
            self.canvas.create_line(197, 180, 225, 210, fill=line_color, width=line_width)

            # Ojos en forma de 'X' al perder
            # Ojo izquierdo
            self.canvas.create_line(188, 100, 198, 110, fill=line_color, width=line_width)
            self.canvas.create_line(198, 100, 188, 110, fill=line_color, width=line_width)
            # Ojo derecho
            self.canvas.create_line(202, 100, 212, 110, fill=line_color, width=line_width)
            self.canvas.create_line(212, 100, 202, 110, fill=line_color, width=line_width)
    
    def nuevo_juego(self):
        """Iniciar un nuevo juego"""
        # Verificar si la palabra actual ya fue usada
        if hasattr(self, 'palabra_actual') and self.palabra_actual:
            self.palabras_usadas.add(self.palabra_actual)
        
        # Intentar obtener una nueva palabra que no haya sido usada
        intentos_busqueda = 0
        max_intentos = 50  # Evitar bucle infinito
        
        while intentos_busqueda < max_intentos:
            self.juego.iniciar_juego()
            palabra_nueva = ''.join([letra.dar_letra() for letra in self.juego.dar_palabra_actual().dar_letras()])
            
            if palabra_nueva not in self.palabras_usadas:
                self.palabra_actual = palabra_nueva
                break
            else:
                intentos_busqueda += 1
        
        # Si se agotaron todos los intentos, mostrar mensaje y limpiar el set
        if intentos_busqueda >= max_intentos:
            messagebox.showinfo("Palabras agotadas", "Has jugado con todas las palabras disponibles.\nReiniciando lista de palabras...")
            self.palabras_usadas.clear()
            self.juego.iniciar_juego()
            self.palabra_actual = ''.join([letra.dar_letra() for letra in self.juego.dar_palabra_actual().dar_letras()])
        
        self.actualizar_interfaz()
        
        # Mostrar cantidad de letras de manera discreta
        num_letras = len(self.palabra_actual)
        self.letras_count_label.configure(text=f"({num_letras} letras)")
        
        # Resetear colores de botones
        for btn in self.letter_buttons.values():
            btn.configure(
                bg=self.COLORS['letter_unused'],
                state=tk.NORMAL
            )
    
    def jugar_letra(self, letra_str):
        """Jugar una letra"""
        if self.juego.dar_estado() != Estado.JUGANDO:
            return
        
        letra = Letra(letra_str.lower())
        
        # Verificar si ya fue usada
        if self.juego.letra_utilizada(letra):
            messagebox.showwarning("Letra ya usada", f"Ya has usado la letra '{letra_str}'")
            return
        
        # Jugar la letra
        acierto = self.juego.jugar_letra(letra)
        
        # Cambiar color del botón
        btn = self.letter_buttons[letra_str.lower()]
        if acierto:
            btn.configure(bg=self.COLORS['letter_correct'])
        else:
            btn.configure(bg=self.COLORS['letter_incorrect'])
        
        btn.configure(state=tk.DISABLED)
        
        # Actualizar interfaz
        self.actualizar_interfaz()
        
        # Verificar fin del juego
        self.verificar_fin_juego()
    
    def actualizar_interfaz(self):
        """Actualizar toda la interfaz"""
        # Actualizar palabra
        if self.juego.dar_palabra_actual():
            ocurrencias = self.juego.dar_ocurrencias()
            palabra_mostrar = " ".join(str(letra) if letra != "_" else "_" for letra in ocurrencias)
            self.palabra_label.configure(text=palabra_mostrar)
        
        # Actualizar intentos
        intentos = self.juego.dar_intentos_disponibles()
        self.intentos_label.configure(text=str(intentos))
        
        # Dibujar ahorcado
        self.draw_hangman(intentos)
    
    def verificar_fin_juego(self):
        """Verificar si el juego ha terminado"""
        estado = self.juego.dar_estado()
        
        if estado == Estado.GANADOR:
            # Mostrar mensaje indicando si la palabra ya había sido usada
            mensaje = "¡Felicitaciones! Has adivinado la palabra."
            if self.palabra_actual in self.palabras_usadas:
                mensaje += "\n(Esta palabra ya había sido jugada anteriormente)"
            mensaje += "\n\n¿Quieres jugar otra vez?"
            
            messagebox.showinfo("¡GANASTE! 🎉", mensaje)
            self.deshabilitar_teclado()
            
        elif estado == Estado.AHORCADO:
            palabra_completa = ''.join([
                letra.dar_letra() 
                for letra in self.juego.dar_palabra_actual().dar_letras()
            ])
            
            # Mostrar mensaje indicando si la palabra ya había sido usada
            mensaje = f"¡Oh no! Has sido AHORCADO.\n\nLa palabra era: {palabra_completa.upper()}"
            if self.palabra_actual in self.palabras_usadas:
                mensaje += "\n(Esta palabra ya había sido jugada anteriormente)"
            mensaje += "\n\n¿Quieres jugar otra vez?"
            
            messagebox.showinfo("GAME OVER 💀", mensaje)
            self.deshabilitar_teclado()
    
    def deshabilitar_teclado(self):
        """Deshabilitar todos los botones del teclado"""
        for btn in self.letter_buttons.values():
            btn.configure(state=tk.DISABLED)
    
    def run(self):
        """Ejecutar la aplicación"""
        self.root.mainloop()

def main():
    """Función principal para ejecutar la GUI"""
    try:
        app = AhorcadoGUI()
        app.run()
    except Exception as e:
        print(f"Error al ejecutar la aplicación: {e}")
        messagebox.showerror("Error", f"Error al ejecutar la aplicación:\n{e}")

if __name__ == "__main__":
    main()

import random

def lancar_dados():
    dado1 = random.randint(1, 6) 
    dado2 = random.randint(1, 6)  
    resultado = dado1 + dado2    
    return resultado

print("Resultado dos dados:", lancar_dados())

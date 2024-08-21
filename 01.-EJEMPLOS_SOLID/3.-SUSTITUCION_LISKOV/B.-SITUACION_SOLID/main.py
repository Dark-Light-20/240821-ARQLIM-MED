from pinguino import Pinguino
from ave_voladora import AveVoladora

# Uso
if __name__ == "__main__":
    pinguino = Pinguino()
    golondrina = AveVoladora()
    
    # Uso polimórfico del método moverse
    print(f"Pingüino: {pinguino.moverse()}")
    print(f"Golondrina: {golondrina.moverse()}")
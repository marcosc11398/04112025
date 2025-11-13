import random

# 1. Tu lista de 12 personas
personas = [
    "Adrian", "Santiago", "Hector", "Diego", "Marco", "Sergio",
    "David", "Jorge", "Nerea", "Izaro", "Ginevra", "Ivan"
]

# 2. Mezclamos la lista aleatoriamente
random.shuffle(personas)

while personas:
    
    # Saca a las primeras 3 personas de la lista mezclada
    grupo = personas[0:3]
    print(grupo)
    personas = personas[3:]
def diviser_par_racine_carree(nombre):
    if nombre < 0:
        # Ici, on lève une erreur car on ne peut pas faire la racine d'un négatif
        raise ValueError("Le nombre ne peut pas être négatif !")
    
    return 10 / (nombre ** 0.5)

# Test
try:
    print(diviser_par_racine_carree(-5))
except ValueError as e:
    print(f"erreur attrape: {e}")
    
for i in range(10):
    if i % 2: continue
    print(i)
    if i % 10: break
else:
    print("error")

########################

camara = ["apa_minerala", "faina", "ciorba"]
tort = ["apa_minerala", "faina", "zahar", "fructe"]

lista_cumparaturi = []
print("/n")


def diferente(ing_camara, ing_tort):
    for ingrediente_tort in ing_tort:
        for ingrediente_camara in ing_camara:
            if ingrediente_tort != ingrediente_camara:
                lista_cumparaturi.append(ingrediente_tort)


numar_ingr_lipsa = len(lista_cumparaturi)
print(f"Lista de cumparaturi este de {numar_ingr_lipsa}, adica {lista_cumparaturi}")

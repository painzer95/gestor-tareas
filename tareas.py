def agregar_tarea(lista, tarea):
    lista.append(tarea)
    return lista


def listar_tareas(lista):
    if not lista:
        print("No hay tareas en la lista.")
    else:
        print("Lista de tareas:")
        for i, t in enumerate(lista):
            print(f"{i + 1}. {t}")

def eliminar_tarea(lista, indice):
    if not lista:
        print("No hay tareas para eliminar.")
    elif 0 <= indice < len(lista):
        del lista[indice]
        print("Tarea eliminada.")
        return lista
    else:
        print("Índice de tarea inválido.")
        return lista
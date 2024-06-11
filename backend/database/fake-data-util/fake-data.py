from faker import Faker

fake = Faker()


def create_fake_data():
    """
    Creamos documentos ficticios.

    **Estructura**
    - `titulo: str`
    - `contenido: str`
    :return: None
    """
    lista = []
    for i in range(50):
        titulo = fake.sentence()
        contenido = fake.text()
        lista.append({
            'titulo': titulo,
            'contenido': contenido
        })
    return lista


def generar_json():
    """
    Genera un archivo json con los datos ficticios
    :return: None
    """
    import json
    with open('out/fake-data.json', 'w') as f:
        json.dump(create_fake_data(), f)


if __name__ == '__main__':
    generar_json()

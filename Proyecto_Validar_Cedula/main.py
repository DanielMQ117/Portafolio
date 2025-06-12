"""Realizar un programa que valida cedulas de identidad de Nicaragua."""

import re
from typing import Union, List


def count_id(id: str = '') -> int:
    """Contar la cantidad de caracteres del ID"""
    return 0 if not id else len(id)


def split_id(id: str = '') -> list:
    """Dividir el ID en 4 partes"""
    if not id:
        return []

    result = id[:-1].split('-')
    result.append(id[-1])

    return result


def check_separator(id: str = '') -> bool:
    """Verificar que el ID tenga el separador correcto y en la posición correcta"""
    if not id:
        return False

    return id[3] == '-' and id[10] == '-' and id.count('-') == 2


def validate_id(parts: list = []) -> List[Union[bool, str]]:
    """Validar las 4 partes del ID"""
    if not parts or len(parts) != 4:
        return [False, 'Formato de ID incorrecto']

    message = '\t❌ Cedula invalida'
    result = parts[0].isdigit() and parts[1].isdigit(
    ) and parts[2].isdigit() and parts[3].isalpha()

    if result:
        message = '\t✔ Cedula valida'
    elif not parts[3].isalpha():
        message = message + '. El ultimo caracter debe ser una letra'

    return [result, message]


def advanced_validate_id(id: str = '') -> str:
    """Validar ID con expresiones regulares"""
    pattern = r'(\d{3})-(\d{6})-(\d{4}[A-z])'
    match = re.fullmatch(pattern=pattern, string=id)

    return '\t✔ Cedula valida' if match is not None else '\t❌ Cedula incorrecta'


if __name__ == '__main__':
    print('\n' + "=" * 80, end='\n\n')
    print("Validando cedula de identidad de Nicaragua".center(80))
    print('\n' + "=" * 80)

    for i in range(3):
        print(f"\n -> Intento {i + 1} de 3")
        id = input(" -> Ingrese cedula de identidad: ").strip()
        print("")
        if not id:
            print("\t❌ Cedula no puede estar vacia")
            continue

        if count_id(id) == 16:
            if check_separator(id):
                parts = split_id(id)
                valid, message = validate_id(parts)
                print(message)
            else:
                print(
                    "\t❌ Cedula debe tener 2 separadores '-' en las posiciones correctas")
        else:
            print("\t❌ Cedula debe tener 16 caracteres")

        print(advanced_validate_id(id))

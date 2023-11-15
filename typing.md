# Tipos de Datos en el Módulo `typing` de Python

El módulo `typing` en Python proporciona herramientas para trabajar con anotaciones de tipos, especialmente útiles en el desarrollo de programas más grandes y complejos. A continuación, se presentan algunos de los tipos de datos más comunes proporcionados por `typing`:

1. **`Any`**: Representa una variable de cualquier tipo. Se utiliza cuando no se conoce o no se quiere especificar el tipo exacto.

    ```python
    from typing import Any

    def ejemplo(valor: Any) -> None:
        print(valor)
    ```

2. **`List`**: Representa una lista de elementos de un tipo específico.

    ```python
    from typing import List

    def ejemplo(lista: List[int]) -> None:
        print(lista)
    ```

3. **`Tuple`**: Representa una tupla de elementos de tipos específicos.

    ```python
    from typing import Tuple

    def ejemplo(tupla: Tuple[int, str]) -> None:
        print(tupla)
    ```

4. **`Dict`**: Representa un diccionario con claves de un tipo y valores de otro tipo.

    ```python
    from typing import Dict

    def ejemplo(diccionario: Dict[str, int]) -> None:
        print(diccionario)
    ```

5. **`Set`**: Representa un conjunto de elementos de un tipo específico.

    ```python
    from typing import Set

    def ejemplo(conjunto: Set[float]) -> None:
        print(conjunto)
    ```

6. **`Union`**: Representa un tipo que puede ser uno de varios tipos. Puede ser útil cuando una variable puede tener diferentes tipos en diferentes situaciones.

    ```python
    from typing import Union

    def ejemplo(valor: Union[int, str]) -> None:
        print(valor)
    ```

7. **`Optional`**: Indica que un valor puede ser del tipo especificado o `None`.

    ```python
    from typing import Optional

    def ejemplo(valor: Optional[str]) -> None:
        print(valor)
    ```

8. **`Callable`**: Representa un objeto que se puede llamar como una función, con los tipos de argumentos y el tipo de retorno especificados.

    ```python
    from typing import Callable

    def ejemplo(funcion: Callable[[int, int], int]) -> None:
        print(funcion(3, 4))
    ```


# Apresentando doctests

> [!TIP]
> Você precisa ler e editar este arquivo para completar o exercício.
> Use a linha de comando abaixo para executar os testes até o primeiro
> que falhar. Siga corrigindo teste por teste, repetindo o comando até
> que o `doctest` não indique mais nenhum erro.
> Use a opção `-f` (*fail fast*) para que o `doctest` pare no primeiro
> erro, assim:

```shell
?> python3 -m doctest -f FIX_ME.md
```

## Sintaxe dos testes

O módulo `doctest` da biblioteca padrão do Python executa cada linha
marcada com `>>>` e verifica se o resultado é igual ao que aparece
nas linhas seguintes.

Por exemplo:

```python
>>> 1 + 1
2
>>> 2 + 2
4

```

> [!TIP]
> No código-fonte deste arquivo, as três crases ` ``` ` no início e
> palavra `python` fazem parte da sintaxe do Markdown para marcar
> um **bloco de código** a ser colorizado como Python.
> O que importa para o `doctest` é o texto entre o primeiro `>>>`
> e a linha em branco no final de cada bloco de código.

> [!WARNING]
> No final de cada bloco é preciso colocar uma linha em branco para
> indicar ao doctest que a saída esperada terminou, e ela não inclui
> o delimitador de blocos ` ``` ` do formato Markdown.

## Instruções de múltiplas linhas

Se for preciso usar instruções Python com várias linhas você
pode usar o sinal `...` no início da linha para indicar a continuação,
o mesmo que acontece automaticamente no console do Python.
Repare na indentação necessária:

```python
>>> for i in range(3):
...     print(i)
0
1
2

```

## Ignorar detalhes na saída

Algumas saídas geradas pelo Python podem conter detalhes irrelevantes
para o teste, tal como o endereço de uma função ou frações decimais
muito longas.

A forma mais fácil de evitar problemas é incluir a diretiva
`doctest: +ELLIPSIS` na expressão sob teste, e então usar `...`
na saída esperada para ignorar os detalhes:

```python
>>> def porcento(a, b):
...     return a * 100 / b
>>> porcento(1, 2)
50.0
>>> porcento(1, 3)  # doctest: +ELLIPSIS
33.33333...

```

Isso também é útil para abreviar saídas muito extensas.
Neste exemplo, coloque a diretiva `+ELLIPSIS` para que o teste passe:

```python
>>> list(range(100))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

```

Utilize a diretiva `+ELLIPSIS` e o sinal `...` para tornar este
teste mais robusto:

```python
>>> porcento(10, 100)
10.0

```

## Captura de exceções

Por padrão, o `doctest` ignora todas as linhas de um *traceback*
do Python, exceto a primeira e a última, então o teste a seguir
funciona mesmo sem usar `...`.

Mas a exceção e a mensagem de erro precisam ser exatamente
aquelas que o Python gera. Corrija este exemplo:

```python
>>> porcento(1, 0)
Traceback (most recent call last):
    ```
ZeroDivisionError: division by zero

```

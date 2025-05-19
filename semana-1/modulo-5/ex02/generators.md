# Explorando geradores

Isso é uma função geradora muito simples:

```python
>>> def gen_123():
...     yield 1
...     yield 2
...     yield 3

```

Execute este arquivo com `doctest -f` para explorar o funcionamento
desta função geradora.

python3 -m doctest generators.md -f -o ELLIPSIS

Corrija passo a passo os testes com os resultados observados por você.

```python3
>>> gen_123
<function gen_123 at ...>

>>> gen_123()
<generator object gen_123 at ...>

>>> for i in gen_123():
...     print(i + 10)
11
12
13

>>> list(gen_123())
[1, 2, 3]

>>> set(gen_123()) == {3, 2, 1}
True

```

> [!TIP]
> Note o truque do teste com `set`, para contornar o fato de que
> a ordem dos elementos do conjunto é imprevisível.
> A saída não necessariamente será na ordem `{1, 2, 3}`,
> mas a comparação será verdadeira se os elementos forem iguais
> nos dois conjuntos.

Agora vamos gerar alguns erros de propósito.
Sua tarefa é corrigir as saídas inclusive o 
texto correspondende de cada *traceback* para
documentar o comportamento do gerador.

```
>>> g = gen_123()
>>> next(g)
1

>>> next(g)
2

>>> next(g)
3

>>> a, b, c = gen_123()
>>> a, b, c
(1, 2, 3)

>>> a, b, c = gen_123()

>>> a, b, c = gen_123()

>>> a, *b = gen_123()
>>> a, b
(1, [2, 3])

```



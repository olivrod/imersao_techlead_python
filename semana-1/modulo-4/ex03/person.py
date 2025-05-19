class Person:
    '''Classe pessoa'''
    def __init__(self, name: str, age: int):
        '''Inicializacao da classe'''
        try:
            self.name = name
            self.age = age
        except Exception as e:
            raise e
        
    def birthday(self) -> str | None:
        '''Metodo de deixar mais velho'''
        try:
            self.age += 1
        except Exception as e:
            return(f'{type(e).__name__}: {e}')
        return None



# >>> python3
# >>> from person import Person
# >>> p = Person("Alice", 30)
# >>> p.name
# 'Alice'
# >>> p.age
# 30
# >>> p.birthday()
# >>> p.age
# 31
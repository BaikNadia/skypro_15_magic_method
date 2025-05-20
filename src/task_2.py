class StripChars:

    def __init__(self, chars):
        self.chars = chars


    def __call__(self, *args, **kwargs):
        return args[0].strip(self.chars)

st1 = StripChars('?')

res = st1('?Example?')

print(res)  # Example


class StripChars:
    """Класс, удаляющий определенные символы из строки"""
    def __init__(self, chars):
        """Инициализация символов для удаления"""
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        """Удаление символов из строки"""
        return args[0].strip(self.__chars)

# Cоздаем два экземпляра класса StripChars: st1 и st2
st1 = StripChars('!')
st2 = StripChars('_')

print(st1('!Attention!'))
print(st1('_Attention_'))
print(st2('_Attention_'))

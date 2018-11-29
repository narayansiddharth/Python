# Different Data Types in Python

noneWithoutTypeHint = None
print("Data Type of variable noneWithoutTypeHint : ", type(noneWithoutTypeHint))
noneWithTypeHint: None = None
print("Data Type of variable noneWithTypeHint : ", type(noneWithTypeHint))

booleanWithoutTypeHint = True
print("Data Type of variable noneWithoutTypeHint : ", type(booleanWithoutTypeHint))
booleanWithTypeHint: bool = False
print("Data Type of variable noneWithTypeHint : ", type(booleanWithTypeHint))

integerWithoutTypeHint = 5
print("Data Type of variable integerWithout : ", type(integerWithoutTypeHint))
integerWithTypeHint: int = 10
print("Data Type of variable integerWithTypeHint : ", type(integerWithTypeHint))

floatWithoutTypeHint = 5.0
print("Data Type of variable floatWithoutTypeHint : ", type(floatWithoutTypeHint))
floatWithTypeHint: float = 10.00
print("Data Type of variable floatWithTypeHint : ", type(floatWithTypeHint))
newNumber = integerWithoutTypeHint + floatWithTypeHint
print("Data Type of variable newNumber : ", type(newNumber))

stringWithoutTypeHint = "Python"
print("Data Type of variable stringWithoutTypeHint : ", type(stringWithoutTypeHint))
stringWithTypeHint: str = 'Python'
print("Data Type of variable stringWithTypeHint : ", type(stringWithTypeHint))

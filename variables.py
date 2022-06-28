# Types of variables in Python

# String
var1: str = "Hi world"

# Numeric
var2: int = 25
var3: float = 25.5
var4: complex = 25+5j

# Boolean
var5: bool = True
var6: bool = False

# Secuence
var7: tuple[int] = (0, 1, 2, 3)
var8: list[int] = [0, 1, 2, 3]
var9: set[int] = {0, 1, 2, 3}

list_names: list[str] = ["Jonathan", "Dario", "Gema", "Ivan", "Ramiro"]

jonathan_age: int = 25
def calculate_is_legal (age: int) -> bool:
    return age >= 18

is_jonathan_legal: bool = calculate_is_legal(age=jonathan_age)
print("is_jonathan_legal: ", is_jonathan_legal) # 
print(f"is_jonathan_legal: {is_jonathan_legal}") # Concatena 2 strings
# Crear conjuntos

tecnologias = {"Python", "JavaScript", "SQL"}

tecnologias.add("Java")
tecnologias.update(["Go", "Rust"])

print(tecnologias)

# Eliminar elementos

frutas = {"manzana", "naranja", "platano"}

frutas.remove("naranja")
frutas.discard("kiwi")

elem = frutas.pop()

print(elem)
print(frutas)

frutas.clear()

print(frutas)

# Subconjuntos y superconjuntos

pares = {2, 4, 6, 8}
nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}

print(pares.issubset(nums))
print(nums.issuperset(pares))

# Operaciones entre conjuntos

grupo_a = {"Ana", "Carlos", "Elena", "David"}
grupo_b = {"Carlos", "Elena", "Fernando"}

comunes = grupo_a.intersection(grupo_b)
todos = grupo_a.union(grupo_b)
solo_en_a = grupo_a.difference(grupo_b)
exclusivos = grupo_a.symmetric_difference(grupo_b)

print(comunes)
print(todos)
print(solo_en_a)
print(exclusivos)

vegetales = {"zanahoria", "pepino"}
frutas = {"manzana", "platano"}

print(vegetales.isdisjoint(frutas))

resultado = grupo_a.intersection(grupo_b).difference({"Elena"})

print(resultado)

# Operadores

u1 = {"acción", "comedia", "ciencia ficción", "aventura"}
u2 = {"drama", "comedia", "romance", "documental"}
u3 = {"acción", "aventura", "fantasía", "ciencia ficción"}

comunes_1_3 = u1 & u3
todos_1_2 = u1 | u2
solo_u1 = u1 - u2
excl_2_3 = u2 ^ u3

print(comunes_1_3)
print(todos_1_2)
print(solo_u1)
print(excl_2_3)

print(u3 <= u1)
print({2, 4} <= {1, 2, 3, 4, 5})
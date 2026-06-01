abc = {1,3,5}
xyz = {1,3,5}
print(abc is xyz)
abc = {1,4,5}
print(xyz is not abc)


xyz = 10293847561029384756
abc = 10293847561029384756
print(xyz is abc, "\n", xyz is not abc)

abc = "10293847561029384756"
xyz = "10293847561029384756"

print(xyz is abc, "\n", xyz is not abc)


abc = True
xyz = True
print(xyz is abc, "\n", xyz is not abc)
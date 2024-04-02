
import hashlib
mdp='RoadToRadiant'
result = hashlib.md5(mdp.encode())
print(result.hexdigest())

result2= hashlib.md5('2901'.encode())
print(result2.hexdigest())
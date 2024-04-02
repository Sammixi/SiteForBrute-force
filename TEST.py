
import hashlib
mdp='wikipedia'
result = hashlib.md5(mdp.encode())
print(result.hexdigest())
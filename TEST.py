
import hashlib
mdp='3816'
result = hashlib.md5(mdp.encode())
print(result.hexdigest())

result2= hashlib.md5('2901'.encode())
print(result2.hexdigest())

def hash2(mdp): 
    '''Fonction qui hash une chaine de caractère'''
    result = hashlib.md5(mdp.encode())
    return result.hexdigest()
    
def reduce(hash):
    '''Fonction qui réduit une chaine de caractère à ces 4 premiers caractères'''
    return hash[:4]
def cycle(mdp):
    '''Fonction qui effectue le cycle de hash et de réduction du mot de passe
    et ajoute le mdp initial et le hash final au dictionnaire qui nous sert de rainbow table'''
    for k in range(6):
        mdp_hash=hash2(mdp)
        print(f'{mdp_hash} + {k}')
        mdp=reduce(mdp_hash)
        print(f'{mdp} + {k}')
    mdp_hash=hash2(mdp)
    print(f'{mdp_hash}final')

cycle('wikipedia')
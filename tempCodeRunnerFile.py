liste_mdp=['wikipedia', 'google', 'quoicoubeh', 'apaignan', 'RoadToRadiant', 'SamAuSol', 'MarcNulBabyfoot']
dico_hashmdp={}
import hashlib
def hash2(mdp):
    result = hashlib.md5(mdp.encode())
    return result.hexdigest()
    
def reduce(hash):
    return hash[:4]

def cycle(mdp):
    mdpinitial=mdp
    for k in range(6):
        mdp_hash=hash2(mdp)
        mdp=reduce(mdp_hash)
    mdp_hash=hash2(mdp)
    dico_hashmdp[mdpinitial]=mdp_hash

def hash_table(liste):
    for k in liste:
        cycle(k)
    print(dico_hashmdp)
    return 0

def testhash(hash):
    hashinit=hash
    for k in dico_hashmdp:
        if dico_hashmdp[k]==hash:
            print(f'Le mot de passe est {k}')
    for k in range(6):
        mdp=reduce(hash)
        hash=hash2(mdp)
        for k in dico_hashmdp:
            if dico_hashmdp[k]==hash:
                print(f'Il faut chercher à partir de la réduction et du hash de {k}')
                search_mdp(hashinit, k)

def search_mdp(hash,mdpinitial):
    newhash=hash2(mdpinitial)
    while hash!=newhash:
        mdpinitial=reduce(newhash)
        newhash=hash2(mdpinitial)
    print(f'Le mot de passe est {mdpinitial}')

hash_table(liste_mdp)
testhash('a57e8915461b83adefb011530b711704')
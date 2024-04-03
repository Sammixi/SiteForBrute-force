liste_mdp=['wikipedia', 'google', 'instagram', 'snap', 'RoadToRadiant', 'MarcNulBabyfoot']
dico_hashmdp={}
import hashlib
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
    mdpinitial=mdp
    for k in range(6):
        mdp_hash=hash2(mdp)
        mdp=reduce(mdp_hash)
    mdp_hash=hash2(mdp)
    dico_hashmdp[mdpinitial]=mdp_hash

def hash_table(liste):
    '''Fonction qui hash tous les mots de passe de la liste'''
    for k in liste:
        cycle(k)
    return 0

def testhash(hash):
    '''Cette fonction vérifie si le hash en paramètre de notre fonction est dans notre rainbow table et si ce n'est pas le cas,
    le hash en paramètre effectue le même cycle que lors de la création de la rainbow table et si à un moment donné le hash correspond
    à un hash de la rainbow table. Alors, nous pouvons trouver le mot de passe lors du cycle de la rainbow table et nous utilisons donc
    la fonction search_mdp pour cela'''
    hashinit=hash
    for k in dico_hashmdp:
        if dico_hashmdp[k]==hash:
            print(f'Le mot de passe est {k}')
    for k in range(6):
        mdp=reduce(hash)
        hash=hash2(mdp)
        for k in dico_hashmdp:
            if dico_hashmdp[k]==hash:
                print(f'Il faut chercher à partir de la réduction et du hash du mot de passe {k} !')
                search_mdp(hashinit, k)

def search_mdp(hash,mdpinitial):
    '''Cette fonction a en paramètre le hash que l'on recherche et le mdp initial où l'on sait que lors de l'étape du cycle le hash
    est trouvé, on va donc refaire l'étape du cycle et lorsqu'on trouve le hash on regarde quelle est la chaine de caractère qui a mené
     a cette hash et donc nous connaissons le mot de passe'''
    newhash=hash2(mdpinitial)
    while hash!=newhash:
        mdpinitial=reduce(newhash)
        newhash=hash2(mdpinitial)
    print(f'Le mot de passe est {mdpinitial}')

hash_table(liste_mdp)
testhash('c911241d00294e8bb714eee2e83fa475')
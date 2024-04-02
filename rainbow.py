liste_mdp=['wikipedia', 'google', 'quoicoubeh', 'apaignan', 'RoadToRadiant', 'SamAuSol', 'MarcNulBabyfoot']
dico_hashmdp={}
import hashlib
str2hash = "password"
result = hashlib.md5(str2hash.encode())
print(result.hexdigest())
'''def hash(mdp):
    for k in liste_mdp:'''


def reduce(hash):
    newhash=''
    for k in range(4):
        newhash+=hash[k]
    print(newhash)
    return newhash



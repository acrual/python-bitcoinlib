import bitcoin.core
from bitcoin.rpc import RawProxy

# añadiendo branch acrualbranch para practicar con git

def esCoinbase(txid):
    raw = p.getrawtransaction(txid)
    tx = p.decoderawtransaction(raw)
    if 'coinbase' in list(tx['vin'][0]):
        return True

def obtenerVins(txid):
    if not esCoinbase(txid):
        raw = p.getrawtransaction(txid)
        tx = p.decoderawtransaction(raw)
        for i in range(len(tx['vin'])):
            txid = tx['vin'][i]['txid']
            n = tx['vin'][i]['vout']
            return obtenerVouts(txid, n)
    else:
        return "sorry, es que es coinbase"

def obtenerVouts(txid, numVout):
    cantidades = []
    direcciones = []
    raw = p.getrawtransaction(txid)
    tx = p.decoderawtransaction(raw)
    if numVout == 100000:
        for i in range(len(tx['vout'])):
            cantidades.append(str(tx['vout'][i]['value']))
            direcciones.append(str(tx['vout'][i]['scriptPubKey']['addresses'][0]))
    else:
        cantidades.append(str(tx['vout'][numVout]['value']))
        direcciones.append(str(tx['vout'][numVout]['scriptPubKey']['addresses'][0]))
    return cantidades, direcciones

def obtenerTransacciones(desde_que_bloque, hasta_que_bloque):
    amount = 0
    resultados = []
    for i in range(desde_que_bloque, hasta_que_bloque):
        bloque_actual = i
        info = p.getblockhash(i)
        bloque_explorado = p.getblock(info)
        for j in range(len(bloque_explorado['tx'])):
            raw = p.getrawtransaction(bloque_explorado['tx'][j])
            tx = p.decoderawtransaction(raw)
            print(i, j, tx['txid'])
    print(obtenerVins(tx['txid']))
    print(obtenerVins(tx['txid'])[1])
    for i in range(len(obtenerVins(tx['txid']))):
        print(obtenerVins(tx['txid'])[i][0])
    for i in range(len(obtenerVouts(tx['txid'], 100000))):
        print(obtenerVouts(tx['txid'], 100000)[0])

p = RawProxy()
info = p.getblockchaininfo()
hasta_que_bloque = info['blocks']
resultados = obtenerTransacciones(595770, 595771)


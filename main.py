import bitcoin.core
from bitcoin.rpc import RawProxy

<<<<<<< HEAD
# Txid es cada txid con sus inputs y sus outputs, sus fees de minería, etc...
class Txid(object):
    def __init__(self, txid):
        self.txid = txid

    def __str__(self):
        return " " + str(self.obtenerVins(self.txid)) + " " + str(self.obtenerVouts)

# Txlist es la lista de las transacciones que han afectado a una dirección hasta llegar al saldo actual
class Txlist(Txid):
    tx_list = []
    def __init__(self, tx_list):
        self.tx_list = tx_list

    def __str__(self):
        return self.tx_list

# Txlist es la clase del registro de la tabla1 que no son más que el saldo de las direcciones
class Registro(Txlist):
    def __init__(self, bloque_ultima_tx, Txid, direccion, saldo):
        self.bloque_ultima_tx = bloque_ultima_tx
        self.ultima_tx = ultima_tx
        self.direccion = direccion
        self.saldo = saldo

    def __str__(self):
        text = "Bloque: " + str(self.bloque_ultima_tx) + "ult_txid: " + str(self.ultima_tx) + "\n"
        return text + "Dirección: " + str(self.direccion) + "Saldo: " + str(self.saldo)


def esNullType(txid, numVout):
    raw = p.getrawtransaction(txid)
    tx = p.decoderawtransaction(raw)
    if tx['vout'][numVout]['scriptPubKey']['type'] == "nulldata":
        return True
    else:
        return False
=======
# añadiendo branch acrualbranch para practicar con git
# añadiendo segunda linea de comentarios git
>>>>>>> 9425985f5b658272dfe2a3c4f7d48a53bca9d1f3

def esCoinbase(txid):
    raw = p.getrawtransaction(txid)
    tx = p.decoderawtransaction(raw)
    if 'coinbase' in list(tx['vin'][0]):
        return True

def obtenerVins(txid, bloque):
    if not esCoinbase(txid):
        raw = p.getrawtransaction(txid)
        tx = p.decoderawtransaction(raw)
        for i in range(len(tx['vin'])):
            txid = tx['vin'][i]['txid']
            n = tx['vin'][i]['vout']
            return obtenerVouts(txid, n)
    else:
        return "sorry, es que es coinbase"

def obtenerVouts(txid, numVout, bloque):
    cantidades = []
    direcciones = []
    raw = p.getrawtransaction(txid)
    tx = p.decoderawtransaction(raw)
    if numVout == 100000:
        for i in range(len(tx['vout'])):
            if not esNullType(txid, i):
                cantidades.append(str(tx['vout'][i]['value']))
                direcciones.append(str(tx['vout'][i]['scriptPubKey']['addresses'][0]))
    else:
        if not esNullType(txid, numVout):
            cantidades.append(str(tx['vout'][numVout]['value']))
            direcciones.append(str(tx['vout'][numVout]['scriptPubKey']['addresses'][0]))
    # crear objeto de la clase Registro, pasándole (bloque, txid, dirección, saldo)
    # si es coinbase, debería sumar en vin al saldo
    return cantidades, direcciones

def obtenerTransacciones(bloque):
    amount = 0
    resultados = []
    info = p.getblockhash(bloque)
    bloque_explorado = p.getblock(info)
    for j in range(len(bloque_explorado['tx'])):
        raw = p.getrawtransaction(bloque_explorado['tx'][j])
        tx = p.decoderawtransaction(raw)
        print(i, j, tx['txid'])
    for i in range(len(obtenerVins(tx['txid']))):
        print("prueba1", obtenerVins(tx['txid'], bloque)[i][0])
    for i in range(len(obtenerVouts(tx['txid'], 100000))):
        print("prueba2", obtenerVouts(tx['txid'], 100000, bloque)[i])
    return obtenerVins(tx['txid'])[i][0], obtenerVouts(tx['txid'], 100000)[i]

p = RawProxy()
info = p.getblockchaininfo()
hasta_que_bloque = info['blocks']
for i in range(576000, 576001):
    resultados = obtenerTransacciones(i)


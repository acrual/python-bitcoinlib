# obtener los outputs e inputs de cada transacción, y estas de cada bloque
# en esos outputs e inputs hay dos opciones: si es output, se le resta al importe inicial y si es input se le suma
# en cualquiera de los dos casos, almacenamos el id de la tx para poder saber el histórico de ese output.
# si la dirección no estaba en la bbdd, entonces se le suma a cero (empieza desde cero)
# para hacerlo con clases, la clase es Dirección, cuyos atributos son address, saldo y txlist

import bitcoin.core
from bitcoin.rpc import RawProxy

class Direccion(object):
    txlist = []
    def __init__(self, address, saldo, txlist):
        self.address = address
        self.saldo = saldo
        self.txlist = txlist

    def __str__(self):
        return "La dirección " + str(self.address) + " tiene un saldo de " + str(self.saldo) + " bitcoins"

    def movimientoDetectado(self, input, amount, tx):
        self.input = input
        self.amount = amount
        self.txlist.append(tx)

    def cambiarSaldo(self):
        if self.input:
            self.saldo = self.saldo + self.amount
        else:
            self.saldo = self.saldo - self.amount

def obtenerTransacciones(desde_que_bloque, hasta_que_bloque):
    for i in range(desde_que_bloque, hasta_que_bloque):
        bloque_actual = i
        info = p.getblockhash(i)
        bloque_explorado = p.getblock(info)
        txs = bloque_explorado['tx'][0]
        raw = p.getrawtransactions(txs)
        txid = p.decoderawtransaction(raw)
        for j in range(len(txid['vout'])):
            amount = amount + txid['vout'][j]['value']
            resultados.append(bloque_actual, txid, amount, txid['vout'])
    return resultados


p = RawProxy()
info = p.getblockchaininfo()
hasta_que_bloque = info['blocks']
resultados = obtenerTransacciones(1, 10)
print(resultados)


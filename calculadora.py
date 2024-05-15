def calcular_nivel(vitorias, derrotas):
    saldo_vitorias = vitorias - derrotas
    nivel = ""
    
    if vitorias < 10:
        nivel = "Ferro"
    elif vitorias <= 20:
        nivel = "Bronze"
    elif vitorias <= 50:
        nivel = "Prata"
    elif vitorias <= 80:
        nivel = "Ouro"
    elif vitorias <= 90:
        nivel = "Diamante"
    elif vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"
    
    return f"O Herói tem saldo de {saldo_vitorias} está no nível de {nivel}"

# Exemplo de uso
vitorias = 95
derrotas = 20
print(calcular_nivel(vitorias, derrotas))

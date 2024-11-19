import numpy as np
from datetime import datetime

# 1.Leitura e preparação dos dados
my_data = np.genfromtxt('vendas.csv', delimiter=',', dtype=str, skip_header=1)

qtd_v = my_data[:, 3].astype(int)
produto_u = my_data[:, 4].astype(float)
valor_t = my_data[:, 5].astype(float)
prod = my_data[:, 2]
reg = my_data[:, 1]
datas = my_data[:, 0]

# 2.Análise Estatística:
# Média 
media_valor_t = np.mean(valor_t)
print(f"Média do Valor Total: {media_valor_t:.2f}")

# Mediana
mediana_valor_t = np.median(valor_t)
print(f"Mediana do Valor Total: {mediana_valor_t:.2f}")

#Desvio padrão
desvio_padrao_valor_t = np.std(valor_t)
print(f"Desvio Padrão do Valor Total: {desvio_padrao_valor_t:.2f}")

# Produto com a maior quantidade vendida  
prod_maior_qtd = prod[np.argmax(qtd_v)]
print(f"Produto com maior quantidade vendida: {prod_maior_qtd}")

# produto com o maior valor total de vendas
prod_maior_valor_t = prod[np.argmax(valor_t)]
print(f"Produto com maior valor total de vendas: {prod_maior_valor_t}")

# Valor total de vendas por região
regioes_unicas = np.unique(reg)
vendas_totais_por_reg = {
    regiao: np.sum(valor_t[reg == regiao]) for regiao in regioes_unicas
}
print("\nValor total de vendas por região:")
for regiao, valor in vendas_totais_por_reg.items():
    print(f"{regiao}: {valor:.2f}")

# Venda média por dia
datas_unicas = np.unique(datas)
media_vendas_por_dia = np.sum(valor_t) / len(datas_unicas)
print(f"\nVenda média por dia: {media_vendas_por_dia:.2f}")


#Análise Temporal
datas = my_data[:, 0]
valores_totais = valor_t

datas_datetime = np.array([datetime.strptime(data, "%Y-%m-%d") for data in datas])

dias_da_semana = [data.strftime("%A") for data in datas_datetime]
unicos, contagens = np.unique(dias_da_semana, return_counts=True)
dia_mais_vendas = unicos[np.argmax(contagens)]

ord = np.argsort(datas_datetime)
datas_ord = datas_datetime[ord]
valores_totais_ord = valores_totais[ord]

# Calcular diferenças entre dias consecutivos
variacao_diaria = np.diff(valores_totais_ord)

# Resultados
print(f"Dia da semana com maior número de vendas: {dia_mais_vendas}")

print("Variação diária no valor total de vendas:")

print(variacao_diaria)



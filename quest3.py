import json

# Carregar os dados do JSON
with open('dados.json') as file:
    dados = json.load(file)

valores = [dia['valor'] for dia in dados if dia['valor'] > 0]  # Ignorar dias com faturamento 0
menor_valor = min(valores)
maior_valor = max(valores)
media_mensal = sum(valores) / len(valores)


dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal)


print(f"Menor valor de faturamento: {menor_valor:.2f}")
print(f"Maior valor de faturamento: {maior_valor:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")

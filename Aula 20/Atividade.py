# -------------------------------------------------
# 1. LER OS DADOS DO ARQUIVO JSON
# -------------------------------------------------
import json 

# Abrir e ler o arquivo JSON usando with open
with open("Dados.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

lista_vendas = dados["vendas"]

print(f"\n✅ Dados carregados com sucesso!")
print(f"📊 Total de registros: {len(lista_vendas)}")




print("\n📋 LISTA COMPLETA DOS DADOS:\n")

print(
    f"{'Vendedor':<15} "
    f"{'Produto':<15} "
    f"{'Valor':>10} "
    f"{'Qtd':>5} "
    f"{'Meta':<15}"
)
print("-" * 65)

for registro in lista_vendas:
    status_meta = "✅ Atingida" if registro['meta_atingida'] else "❌ Não atingida"

    print(
        f"{registro['vendedor']:<15} "
        f"{registro['produto']:<15} "
        f"{registro['valor']:>10.2f} "
        f"{registro['quantidade']:>5} "
        f"{status_meta:<15}"
    )
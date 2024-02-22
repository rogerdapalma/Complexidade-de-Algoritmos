
import time  # Importa o módulo time para medir o tempo de execução
import itertools  # Importa o módulo itertools para gerar combinações de caracteres
import pandas as pd  # Importa o módulo pandas para manipulação de dados
import matplotlib.pyplot as plt  # Importa o módulo matplotlib.pyplot para visualização de dados

def break_password(password_to_break):
    # Define os caracteres possíveis na senha
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    start_time = time.time()  # Marca o início do tempo de execução
    found = False  # Inicializa a variável que indica se a senha foi encontrada

    # Loop que tenta senhas de tamanho 4 a 9 caracteres
    for i in range(4, 10):
        # Gera todas as combinações possíveis de caracteres para o tamanho atual i
        for combo in itertools.product(chars, repeat=i):
            password_attempt = ''.join(combo)  # Junta os caracteres para formar a tentativa de senha
            # Verifica se a tentativa de senha é igual à senha desejada
            if password_attempt == password_to_break:
                end_time = time.time()  # Marca o final do tempo de execução
                time_diff = (end_time - start_time) * 1000  # Calcula a diferença de tempo em milissegundos
                print(f"Senha encontrada: {password_attempt} ({time_diff:.2f} ms)")
                found = True  # Atualiza a variável para indicar que a senha foi encontrada
                return password_attempt, time_diff  # Retorna a senha e o tempo de execução
        if found:
            break  # Sai do loop se a senha foi encontrada

    # Caso a senha não seja encontrada após todas as tentativas
    if not found:
        end_time = time.time()  # Marca o final do tempo de execução
        time_diff = (end_time - start_time) * 1000  # Calcula a diferença de tempo em milissegundos
        print(f"Senha não encontrada após {time_diff:.2f} ms")
        return None, time_diff  # Retorna None e o tempo de execução

# Lista de senhas para testar
passwords_to_break = ["AbCd1","1234","AbC1","DcAb1"]

results = []  # Lista para armazenar os resultados

# Testa a quebra de cada senha e mede o tempo de execução
for password in passwords_to_break:
    result = break_password(password)
    results.append({"Password": password, "Execution Time (ms)": result[1]})

# Converte os resultados em um DataFrame para facilitar a manipulação e visualização
df = pd.DataFrame(results)

# Mostra os resultados em uma tabela
print("\nSenha | Tempo de Execução (ms)")
print("-" * 35)
for index, row in df.iterrows():
    print(f"{row['Password']} | {row['Execution Time (ms)']:.2f}")

# Configura e exibe um gráfico de barras com os tempos de execução
plt.figure(figsize=(10, 6))
plt.bar(df['Password'], df['Execution Time (ms)'], color='skyblue')
plt.xlabel('Password')
plt.ylabel('Execution Time (ms)')
plt.title('Password Cracking Execution Times')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

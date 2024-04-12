import tkinter as tk
from tkinter import messagebox
import subprocess

# Função para verificar o uso de recursos
def verificar_recursos():
    try:
        # Executa o script .sh e captura a saída
        saida = subprocess.check_output("monitoring.sh", shell=True).decode()
        
        # Analisa as informações coletadas
        info_recursos = {}
        for linha in saida.splitlines():
            chave, valor = linha.split('=')
            info_recursos[chave] = valor

        mensagem = f"Uso da CPU: {info_recursos['CPU_USAGE']}%\nUso de Memória: {info_recursos['MEM_USAGE']}%\nUso do Disco: {info_recursos['DISK_USAGE']}%"
        messagebox.showinfo("Resource Monitor", mensagem)
    except Exception as e:
        messagebox.showerror("Error", f"Ocorreu um erro: {str(e)}")

# Cria janela
janela = tk.Tk()
janela.title("Monitor de Recursos")

# Cria um botão para verificar recursos
botao_verificar = tk.Button(janela, text="Verificar Recursos", command=verificar_recursos)
botao_verificar.pack(padx=20, pady=10)

# Cria um botão de saída
botão_sair = tk.Button(janela, text="Sair", command=janela.quit)
botão_sair.pack(padx=20, pady=10)

# Inicia a interface
janela.mainloop()

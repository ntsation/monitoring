# Monitoramento de recursos do sistema

Este é um sistema de monitoramento de recursos do sistema que exibe informações sobre CPU, memória e uso de disco em uma interface gráfica.

## Requisitos

- Python 3.x
- Tkinter (Biblioteca para interface gráfica)
- Zenity (Para exibir caixas de diálogo no shell)

## Como usar

1. Clone o repositório para o seu sistema.

2. Verifique se você tem os requisitos listados instalados conforme mencionado acima.

3. Execute o script python:

 ```
python main.py
 ```

4. Isso abrirá a interface gráfica do sistema de monitoramento.

5. Clique no botão `Check Resources` para verificar o uso de recursos.Uma caixa de diálogo exibirá informações sobre CPU, memória e uso de disco.

6. Clique no botão `Exit` para fechar o aplicativo.

## Arquivos
1. **resource_monitor.py**: Script Python que cria a interface gráfica e chama os comandos do shell para monitorar os recursos.

2. **monitoring.sh**: Arquivo Shell contendo comandos de monitoramento de recursos.

## Customização
Você pode personalizar limites de alerta para uso de CPU, memória e disco editando o arquivo Monitoring.sh.Ajuste as variáveis CPU_LIMIT, MEM_LIMIT e DISK_LIMIT, conforme necessário.
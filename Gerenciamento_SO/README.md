# Gerenciamento de Sistema Operacional - Exercícios Python

Esta pasta contém uma série de exercícios práticos sobre monitoramento e gerenciamento de recursos do sistema operacional usando Python.

## 📋 Pré-requisitos

Python 3.7 ou superior instalado.

## 📦 Instalação de Bibliotecas

### ⚡ Método Rápido (Recomendado)

Abra o terminal (Ctrl + ~) na pasta do projeto e execute:

```bash
pip install -r requirements.txt
```

### Método Manual (Um por um)

#### Passo 1: Abrir o Terminal (PowerShell no Windows)

No VS Code:
1. Vá para **Terminal** > **New Terminal** (ou use `Ctrl + ~`)
2. Certifique-se de estar na pasta `Gerenciamento_SO`

#### Passo 2: Instalar a biblioteca `psutil`

```bash
pip install psutil
```

#### Passo 3: Instalar a biblioteca `py-cpuinfo` (usada no ex08)

```bash
pip install py-cpuinfo
```

### Verificar instalação

Para verificar se as bibliotecas foram instaladas corretamente:

```bash
pip list | findstr psutil
pip list | findstr cpuinfo
```

## 📄 Arquivo `requirements.txt`

O arquivo `requirements.txt` contém a lista de dependências:

```
psutil
py-cpuinfo
```

Isso garante que todos tenham as mesmas versões instaladas.

## 🚀 Como Executar os Exercícios

### No VS Code

1. Abra o arquivo do exercício desejado
2. Clique no botão ▶️ (Play) no canto superior direito, ou
3. Use o atalho `Ctrl + F5` (Run Python File in Terminal)

### Via Terminal (PowerShell)

```bash
python ex01_monitor_ram.py
python ex02_monitor_ram_alerta.py
# ... e assim por diante
```

## 📚 Lista de Exercícios

### **Ex01 - Monitor Simples de Memória RAM**
Mostra a quantidade total, usada e livre de RAM, atualizando a cada 2 segundos.

**Bibliotecas:** `psutil`, `time`  
**Conceitos:** Loop infinito, funções de monitoramento

---

### **Ex02 - Monitor de RAM com Alerta**
Estende o exercício 1 adicionando um limite de alerta definido pelo usuário.

**Bibliotecas:** `psutil`, `time`  
**Conceitos:** Entrada do usuário, condicionais, thresholds

---

### **Ex03 - Gerenciador de Espaço em Disco (Tabela)**
Lista todas as partições do disco com espaço total, usado, livre e percentual.

**Bibliotecas:** `psutil`  
**Conceitos:** Iteração, formatação de dados, tabelas

---

### **Ex04 - Alerta de Pouco Espaço em Disco**
Identifica e alerta sobre partições com espaço crítico (baseado no ex03).

**Bibliotecas:** `psutil`  
**Conceitos:** Reutilização de código, filtros, condicionais

---

### **Ex05 - Monitor de Tráfego de Rede**
Mostra taxa de download e upload em tempo real (KB/s).

**Bibliotecas:** `psutil`, `time`  
**Conceitos:** Cálculo de deltas, conversão de unidades

---

### **Ex06 - Monitor de Desempenho da CPU**
Exibe uso total da CPU e por núcleo, atualizado a cada segundo.

**Bibliotecas:** `psutil`  
**Conceitos:** Arrays/listas, formatação, monitoramento por core

---

### **Ex07 - Histórico de CPU (Logger)**
Registra uso da CPU em arquivo (`cpu_log.txt`) a cada 5 segundos.

**Bibliotecas:** `psutil`, `datetime`, `time`, `os`  
**Conceitos:** Manipulação de arquivos, timestamps, logging

---

### **Ex08 - Informações Detalhadas do Processador**
Mostra modelo, núcleos, frequência e tenta obter série (com aviso de limitações).

**Bibliotecas:** `psutil`, `platform`, `cpuinfo`  
**Conceitos:** Detecção de sistema, tratamento de exceções, dados de hardware

---

### **Ex09 - Listagem de Dispositivos de E/S**
Lista dispositivos de armazenamento e permite visualizar informações detalhadas.

**Bibliotecas:** `psutil`  
**Conceitos:** Menu interativo, reutilização de código, conceitos de E/S

---

### **Ex10 - Painel Integrado de Monitoramento**
Painel único que mostra RAM, CPU, disco e rede em tempo real.

**Bibliotecas:** `psutil`, `time`, `os`  
**Conceitos:** Integração de múltiplos monitoramentos, limpeza de tela, loops

---

## 🛠️ Estrutura e Boas Práticas

Cada arquivo contém:
- **Comentários explicativos** no início
- **Anotações inline** como se fosse um aluno deixando notas de estudo
- **Tratamento de erros** com `try/except` quando apropriado
- **Boas práticas** de organização e legibilidade

## ⚠️ Observações Importantes

### Windows vs Linux/macOS

- **Limpeza de tela:** Usa `os.system("cls")` no Windows e `os.system("clear")` em Linux/macOS
- **Caminhos:** Caminhos estão otimizados para Windows; adaptar conforme necessário

### Limitações Conhecidas

- **Número de série da CPU:** Não é possível obter de forma portável em todos os sistemas. O programa informará quando não estiver disponível.
- **Permissões:** Alguns dados de sistema podem exigir permissões elevadas.
- **Precisão:** As medições são aproximadas e dependem do intervalo de amostragem.

## 📞 Dúvidas Frequentes

**P: O programa reporta "modulo não encontrado"?**  
R: Execute `pip install psutil` e `pip install py-cpuinfo` no terminal.

**P: Como parar um programa em loop?**  
R: Pressione `Ctrl + C` no terminal.

**P: Por que a CPU nunca mostra 0%?**  
R: Porque o próprio Python está usando CPU para rodar o programa. É normal.

**P: Posso roditar vários programas de monitoramento ao mesmo tempo?**  
R: Sim! Abra múltiplos terminais no VS Code e execute cada um em um terminal diferente.

---

## 📝 Estrutura de Arquivos

```
Gerenciamento_SO/
├── README.md                    (este arquivo - Documentação)
├── requirements.txt             (Dependências do projeto)
├── ex01_monitor_ram.py
├── ex02_monitor_ram_alerta.py
├── ex03_gerenciador_disco.py
├── ex04_alerta_disco.py
├── ex05_monitor_rede.py
├── ex06_monitor_cpu.py
├── ex07_historico_cpu.py       (gera cpu_log.txt ao rodar)
├── ex08_info_processador.py
├── ex09_dispositivos_io.py
└── ex10_painel_integrado.py
```

---

**Última atualização:** 24/02/2026  
**Python version:** 3.7+

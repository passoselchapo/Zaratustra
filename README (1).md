# Projeto Zaratustra

Este projeto parece ser uma aplicação web baseada em FastAPI que interage com um agente de IA alimentado pela API do Google Gemini. Ele fornece uma interface para comunicação com o agente, provavelmente para propósitos de chat ou processamento de linguagem natural.

## Arquitetura

A arquitetura do projeto é baseada em:
-   **FastAPI**: Um framework web moderno e rápido para construir APIs com Python 3.7+.
-   **Agente de IA**: Implementado para processar mensagens de usuários, utilizando a API do Google Gemini para capacidades de geração de linguagem.
-   **Estrutura modular**: O código é organizado em módulos dentro do diretório `app/` para uma melhor separação de preocupações.

## Estrutura de Arquivos

-   `main.py`: O ponto de entrada principal da aplicação FastAPI. Ele inicia o servidor e provavelmente carrega as configurações e a lógica principal da API.
-   `requirements.txt`: Lista as dependências Python necessárias para o projeto, que devem ser instaladas para que a aplicação funcione corretamente.
-   `Untitled5.ipynb`: Um notebook Jupyter, possivelmente utilizado para testes, desenvolvimento exploratório ou exemplos de uso.
-   `app/`:
    -   `agent.py`: Provavelmente contém a lógica principal do agente de IA, incluindo a integração com a API do Google Gemini e o processamento das mensagens do usuário.
    -   `api.py`: Define os endpoints da API RESTful (como `/chat`) e lida com a roteamento das requisições e respostas.
    -   `db.py`: Sugere que há alguma interação com um banco de dados, possivelmente para persistir informações de conversas ou configurações do agente.
    -   `models.py`: Define os modelos de dados (e.g., classes Pydantic) usados para validação de requisições e serialização de respostas da API.
    -   `__init__.py`: Indica que `app` é um pacote Python.
    -   `__pycache__/`: Diretório gerado automaticamente pelo Python para armazenar arquivos bytecode compilados.

## Como Rodar o Projeto

### 1. Clonar o Repositório
```bash
!git clone https://github.com/passoselchapo/Zaratustra.git
```

### 2. Navegar para o Diretório do Projeto
```bash
!cd Zaratustra
```

### 3. Instalar Dependências
```bash
!pip install -r requirements.txt
```

### 4. Configurar a Chave da API do Google Gemini
O projeto requer uma chave da API do Google Gemini (`GOOGLE_API_KEY`). Você deve configurar esta variável de ambiente. **Substitua `SUA_API_KEY_DO_GEMINI` pela sua chave real.**

```python
import os
os.environ['GOOGLE_API_KEY'] = 'SUA_API_KEY_DO_GEMINI' # Substitua pela sua chave real
```

### 5. Iniciar o Servidor FastAPI em Segundo Plano
Para rodar o servidor sem bloquear o terminal do Colab, ele é iniciado em segundo plano. O comando também mata processos anteriores na porta 8000 e garante que a `GOOGLE_API_KEY` seja passada para o processo.

```bash
!kill $(lsof -t -i:8000) >/dev/null 2>&1 || true
!GOOGLE_API_KEY='SUA_API_KEY_DO_GEMINI' nohup python /content/Zaratustra/main.py > server_output.log 2>&1 &
```

### 6. Interagir com o Agente (Exemplo de Chat)
Para enviar uma mensagem ao agente, faça uma requisição POST para o endpoint `/chat`. A resposta será o `assistant_message`.

```bash
!curl -X POST "http://0.0.0.0:8000/chat" -H "Content-Type: application/json" -d '{"user_message": "Olá, agente! Isso é um teste."}'
```

### 7. Verificar a Saída do Servidor
Para verificar logs ou erros do servidor, você pode inspecionar o arquivo `server_output.log`.

```bash
!cat server_output.log
```

## Solução de Problemas Comuns

-   **`Error calling Gemini API: 404 models/gemini-pro is not found`**: Este erro indica que o nome do modelo Gemini configurado no `agent.py` pode estar incorreto, ou o modelo pode não estar disponível para sua conta/região. Verifique a documentação oficial da API do Google Gemini para os nomes de modelos mais recentes e compatíveis (`ListModels`). Pode ser necessário atualizar o `agent.py` com o nome de modelo correto (por exemplo, `gemini-pro-vision` se estiver usando visão, ou apenas `gemini-pro` se a disponibilidade ou a versão da API mudou).
-   **`Address already in use`**: Um processo do servidor anterior não foi encerrado corretamente. O comando de inicialização com `kill` deve resolver isso, mas se persistir, verifique manualmente os processos na porta 8000.

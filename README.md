# BOT-Python
WhatsApp Bot API

API para um bot do WhatsApp com integração à Whapi.Cloud, suportando envio e recebimento de mensagens, mídia, enquetes, geolocalização, webhooks, extração de contatos e captura de foto de perfil.

Pré-requisitos





Python 3.8+



Conta no Whapi.Cloud (obtenha o token em https://whapi.cloud)



URL de webhook (use Ngrok para testes locais)

Instalação





Clone o repositório:

git clone <repository_url>
cd whatsapp-bot-api



Crie um ambiente virtual:

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows



Instale as dependências:

pip install -r requirements.txt



Configure as variáveis de ambiente no arquivo .env:

WHAPI_TOKEN=seu_token_aqui
WEBHOOK_URL=sua_url_webhook_aqui



Inicie o servidor:

python src/main.py

Uso





Endpoints da API:





POST /api/send-message: Enviar mensagem de texto



POST /api/send-media: Enviar mídia (imagem, áudio, vídeo, PDF)



POST /api/send-poll: Enviar enquete



GET /api/group-contacts/{group_id}: Obter contatos de um grupo



GET /api/profile-picture/{phone}: Obter foto de perfil



Webhook: Configure o webhook na Whapi.Cloud para receber eventos em /webhook.

Notas





Para conexões ilimitadas, configure múltiplas instâncias com diferentes tokens ou números.



O suporte está disponível via Whapi.Cloud, de segunda a sexta, das 8h às 18h (verifique com o provedor).



Para grupos exclusivos no WhatsApp, contate o suporte da Whapi.Cloud.

Licença

MIT

Detalhes dos Arquivos

src/main.py: Inicializa o servidor FastAPI, configura rotas e o webhook.
src/config/config.py: Armazena configurações como a chave da API Whapi.Cloud e URLs.
src/routes/api.py: Define endpoints da API para envio/recebimento de mensagens, mídia, enquetes, etc.
src/services/whatsapp_service.py: Lógica para interagir com a API Whapi.Cloud (enviar/receber mensagens, gerenciar grupos, etc.).
src/services/webhook_service.py: Lógica para processar eventos recebidos via webhook.
src/utils/logger.py: Funções para logging de erros e eventos.
src/models/message.py: Estrutura para mensagens e contatos usando Pydantic.
.env: Armazena variáveis sensíveis, como a chave da API.
requirements.txt: Define dependências (FastAPI, httpx, python-dotenv, etc.).
README.md: Instruções para configurar e rodar o projeto.
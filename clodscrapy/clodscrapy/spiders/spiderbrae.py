import scrapy
import os
import json
import hashlib

class SpiderbraeSpider(scrapy.Spider):
    name = "spiderbrae"
    allowed_domains = ["sebrae.com.br"]
    start_urls = [
        "https://sebrae.com.br/sites/PortalSebrae/sebraeaz/6-passos-para-iniciar-bem-o-seu-novo-negocio,a28b5e24d0905410VgnVCM2000003c74010aRCRD"
    ]

    def parse(self, response):
        # Extração de dados da página inicial diretamente
        titulo = response.css('title::text').get() or "sem_titulo"
        conteudo = response.css(
            'div.sb-integra-conteudo__text::text'
        ).getall()

        if not conteudo:
            self.log("⚠️ Conteúdo vazio: Verifique o seletor CSS ou o HTML da página.")
            conteudo = ["Conteúdo não encontrado."]

        # Estruturar os dados
        dados = {
            'url': response.url,
            'titulo': titulo,
            'conteudo': ' '.join(conteudo).strip()
        }

        # Nome do arquivo baseado em um hash único da URL
        nome_arquivo = hashlib.md5(response.url.encode()).hexdigest() + ".json"

        # Criando um diretório para armazenar os arquivos
        diretorio = "C:/Users/Usuario/Desktop/ClodAI/src/utils/data/raw/"
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)

        # Salvando cada página em um arquivo separado
        caminho_completo = os.path.join(diretorio, nome_arquivo)
        try:
            with open(caminho_completo, 'w', encoding='utf-8') as f:
                json.dump(dados, f, ensure_ascii=False, indent=4)
            self.log(f"✅ Arquivo salvo com sucesso: {caminho_completo}")
        except Exception as e:
            self.log(f"❌ Erro ao salvar o arquivo: {e}")
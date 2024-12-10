# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import os


class ClodscrapyPipeline:
    def process_item(self, item, spider):
        #Nome do arquivo baseado na URL ou outra identificação
        titulo = item['titulo']
        nome_arquivo = f"saidas/{titulo.replace(' ', '_').lower()}.json"

        #Criar o diretório se não existir
        os.makedirs('saidas', exist_ok=True)

        #Salvar em JSON
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            json.dump(item, f, ensure_ascii=False, indent=4)
        return item
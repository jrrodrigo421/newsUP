import os
import json
from datetime import datetime, timedelta
import requests
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_wtf import CSRFProtect
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Carrega variáveis de ambientente
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'chave-dev-para-teste')
csrf = CSRFProtect(app)

# Adiciona processador de contexto para variáveis de templateeis de template
@app.context_processor
def injetar_ano():
    return {'current_year': datetime.now().year}

# Armazenamento em memória para MVP (usaria um banco de dados em produção)
ARTIGOS_SALVOS = []
PREFERENCIAS_USUARIO = {}

# Fontes de notícias
FONTES_NOTICIAS = {
    'tecnologia': [
        'https://techcrunch.com/',
        'https://www.theverge.com/',
        'https://www.wired.com/'
    ],
    'negocios': [
        'https://www.forbes.com/',
        'https://www.bloomberg.com/',
        'https://www.businessinsider.com/'
    ],
    'ciencia': [
        'https://www.scientificamerican.com/',
        'https://www.nature.com/news',
        'https://www.sciencemag.org/news'
    ],
    'saude': [
        'https://www.webmd.com/news',
        'https://www.medicalnewstoday.com/',
        'https://www.healthline.com/health-news'
    ],
    'entretenimento': [
        'https://variety.com/',
        'https://www.hollywoodreporter.com/',
        'https://deadline.com/'
    ]
}

# Cache para artigos de notu00edcias
CACHE_NOTICIAS = {}
DATA_ULTIMA_BUSCA = None

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/configurar', methods=['GET', 'POST'])
def configurar():
    if request.method == 'POST':
        topicos = request.form.getlist('topics')
        taxa_atualizacao = request.form.get('refresh_rate', 'diario')
        
        # Armazena preferu00eancias do usuu00e1rio
        session['topicos'] = topicos
        session['taxa_atualizacao'] = taxa_atualizacao
        
        # Redireciona para o feed de notu00edcias
        return redirect(url_for('feed_noticias'))
    
    return render_template('setup.html', categories=list(FONTES_NOTICIAS.keys()))

@app.route('/noticias')
def feed_noticias():
    topicos = session.get('topicos', [])
    if not topicos:
        return redirect(url_for('configurar'))
    
    artigos = buscar_noticias(topicos)
    return render_template('news_feed.html', articles=artigos, topics=topicos)

@app.route('/artigo/<int:artigo_id>')
def detalhe_artigo(artigo_id):
    # Em um app real, buscaru00edamos de um banco de dados
    # Para o MVP, usaremos o cache em memu00f3ria
    todos_artigos = []
    for artigos_topico in CACHE_NOTICIAS.values():
        todos_artigos.extend(artigos_topico)
    
    artigo = None
    for idx, art in enumerate(todos_artigos):
        if idx == artigo_id:
            artigo = art
            break
    
    if not artigo:
        return redirect(url_for('feed_noticias'))
    
    return render_template('article_detail.html', article=artigo, article_id=artigo_id)

@app.route('/salvar_artigo/<int:artigo_id>', methods=['POST'])
def salvar_artigo(artigo_id):
    todos_artigos = []
    for artigos_topico in CACHE_NOTICIAS.values():
        todos_artigos.extend(artigos_topico)
    
    artigo = None
    for idx, art in enumerate(todos_artigos):
        if idx == artigo_id:
            artigo = art
            break
    
    if artigo and artigo not in ARTIGOS_SALVOS:
        ARTIGOS_SALVOS.append(artigo)
    
    return redirect(url_for('artigos_salvos'))

@app.route('/salvos')
def artigos_salvos():
    return render_template('saved_articles.html', articles=ARTIGOS_SALVOS)

@app.route('/api/atualizar', methods=['POST'])
def atualizar_noticias():
    topicos = session.get('topicos', [])
    if not topicos:
        return jsonify({'erro': 'Nenhum tópico selecionado'}), 400
    
    # Força atualização limpando o cache
    for topico in topicos:
        if topico in CACHE_NOTICIAS:
            del CACHE_NOTICIAS[topico]
    
    artigos = buscar_noticias(topicos)
    return jsonify({'sucesso': True, 'quantidade_artigos': len(artigos)})

def buscar_noticias(topicos):
    global DATA_ULTIMA_BUSCA
    data_atual = datetime.now().date()
    
    # Verifica se precisamos atualizar o cache
    if DATA_ULTIMA_BUSCA != data_atual:
        # Limpa o cache se for um novo dia
        CACHE_NOTICIAS.clear()
        DATA_ULTIMA_BUSCA = data_atual
    
    todos_artigos = []
    
    for topico in topicos:
        # Usa resultados em cache se disponíveis
        if topico in CACHE_NOTICIAS:
            todos_artigos.extend(CACHE_NOTICIAS[topico])
            continue
        
        artigos_topico = []
        
        if topico in FONTES_NOTICIAS:
            for url_fonte in FONTES_NOTICIAS[topico]:
                try:
                    # Em um app real, usaríamos chaves de API e serviços adequados
                    # Para o MVP, vamos simular a busca com dados de exemplo
                    artigos = simular_busca_noticias(url_fonte, topico)
                    artigos_topico.extend(artigos)
                except Exception as e:
                    print(f"Erro ao buscar de {url_fonte}: {e}")
        
        # Armazena os resultados em cache
        CACHE_NOTICIAS[topico] = artigos_topico
        todos_artigos.extend(artigos_topico)
    
    return todos_artigos

def simular_busca_noticias(url_fonte, topico):
    """Simula a busca de artigos de notícias para fins de MVP"""
    # Em um app de produção, faríamos scraping ou usaríamos APIs
    # Para o MVP, retornaremos dados de exemplo
    dominio = url_fonte.split('//')[1].split('/')[0]
    
    artigos = []
    # Gera 3-5 artigos falsos por fonte
    import random
    num_artigos = random.randint(3, 5)
    
    # Mapeamento de tópicos para português
    topicos_pt = {
        'tecnologia': 'Tecnologia',
        'negocios': 'Negócios',
        'ciencia': 'Ciência',
        'saude': 'Saúde',
        'entretenimento': 'Entretenimento'
    }
    
    topico_pt = topicos_pt.get(topico, topico.capitalize())
    
    for i in range(num_artigos):
        data_publicacao = datetime.now() - timedelta(hours=random.randint(1, 24))
        
        artigo = {
            'title': f"Últimas notícias de {topico_pt} {i+1} de {dominio}",
            'description': f"Este é um artigo simulado sobre {topico_pt.lower()} de {dominio}. Em um app real, isso conteria conteúdo real extraído da fonte.",
            'url': f"{url_fonte}article-{i}",
            'source': dominio,
            'published': data_publicacao.strftime("%d/%m/%Y %H:%M"),
            'image_url': f"/static/img/placeholder-{random.randint(1, 3)}.jpg",
            'category': topico
        }
        artigos.append(artigo)
    
    return artigos


    

# In a real application, we would implement actual web scraping here
# For example:
# def scrape_news(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     articles = []
#     # Extract article data based on the website's structure
#     # ...
#     return articles

if __name__ == '__main__':
    app.run(debug=True)
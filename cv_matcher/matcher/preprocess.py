import pandas as pd
import numpy as np
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer
import PyPDF2
import spacy

nltk.download('punkt')
nltk.download('stopwords')
nlp = spacy.load('es_core_news_sm')

def limpiar_texto(texto):
    """
    Elimina todos los caracteres que no sean alfanuméricos (letras y números)
    """
    texto = texto.lower()
    return re.sub(r'[^a-zA-Z0-9] ', ' ', texto)

def tokenizar_espanol(texto):
    """
    Tokeniza texto en español usando NLTK
    """
    # Tokenizar en palabras
    tokens = word_tokenize(texto, language='spanish')
    
    return tokens

def quitar_stopwords(tokens):
    """
    Elimina las stop words en español de una lista de tokens
    """
    stop_words = set(stopwords.words('spanish'))
    tokens_filtrados = [token for token in tokens if token.lower() not in stop_words]
    return tokens_filtrados


def lematizar_spacy(texto):
    """
    Lematiza texto usando spaCy (más preciso que stemming)
    """
    texto = ' '.join(texto)
    doc = nlp(texto)
    lemas = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    texto_final = ' '.join(lemas)
    return texto_final

def tratamiento_texto(texto):
    texto = limpiar_texto(texto)
    texto = tokenizar_espanol(texto)
    texto = quitar_stopwords(texto)
    texto = lematizar_spacy(texto)
    return texto

def leer_pdf(ruta_archivo):
    """
    Lee el texto de un archivo PDF usando PyPDF2
    """
    texto_completo = ""
    
    with open(ruta_archivo, 'rb') as archivo:
        lector = PyPDF2.PdfReader(archivo)
        
        # Iterar por todas las páginas
        for pagina in lector.pages:
            texto_completo += pagina.extract_text() + "\n"
    
    return texto_completo
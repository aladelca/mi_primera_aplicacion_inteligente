from django.shortcuts import render, redirect
from .forms import DocumentForm
import pandas as pd
import numpy as np
from .models import Document
from .preprocess import *
import pickle
from sklearn.metrics.pairwise import cosine_similarity
# Create your views here.

def index(request):
    return render(request, "index.html")


def process_cv(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = DocumentForm()
    return render(request, 'process_cv.html', {"form": form})

def list_cv(request):
    df = pd.DataFrame(list(Document.objects.all().values()))
    if len(df)==0:
        df["id"] = np.nan
        df["document"] = np.nan
        df["uploaded_at"] = np.nan
    else:
        df = df[["id","document","uploaded_at"]]
    df["id"] = df["id"].astype(str)

    def add_url(data):
        output = "<a href="
        output = output + data + ">"
        output = output + data
        output = output + "</a>"
        return output
        
    df["id"] = df["id"].apply(add_url)
    html_table = df.to_html(
        escape = False,
        index = False,
        border = 1,
        classes = "table table-striped table-hover"
    )
    params = {"html_table":html_table}
    return render(request, 'list_cv.html', params)

def cv_specific(request, cv_id):
    # Cargar el cv

    filename = Document.objects.values_list('document', flat = True).get(id=cv_id)
    cv_raw = leer_pdf(filename)
    df_cv_raw = pd.DataFrame()
    df_cv_raw["texto"] = [cv_raw]

    # Cargar los archivos de puesto

    matriz_puestos = pd.read_pickle("matcher/static/data/puestos.pickle")

    # Cargar vectorizador ya entrenado

    with open('matcher/static/data/vectorizer.pickle', 'rb') as f:
        vect = pickle.load(f)

    # Limpiar

    vectores_cv = vect.transform(df_cv_raw["texto"].apply(tratamiento_texto))
    vectores_puestos = vect.transform(matriz_puestos['PUESTO'].apply(tratamiento_texto))

    # Calcular distancias de coseno

    serie_cv = pd.Series(cosine_similarity(vectores_puestos, vectores_cv)[:,0])
    
    # Obtener top 10

    valores = serie_cv.sort_values(ascending=False).head(10)
    indices = valores.index
    df_top = matriz_puestos.iloc[indices,:]
    df_top['ranking'] = valores

    html_match = df_top.to_html(
        formatters = {
            "ranking" : '{:,.2%}'.format
        },
        index = False,
        border = 1,
        escape = False,
        classes = 'table table-striped  table-hover'
    )

    params = {'html_match':html_match}
    return render(request, 'match.html', params)


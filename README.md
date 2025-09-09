# 🤖 AI JOBS - Sistema Inteligente de Matching CV-Empleos

Una aplicación web desarrollada con Django que utiliza **Inteligencia Artificial** y **Procesamiento de Lenguaje Natural (NLP)** para hacer matching entre CVs y ofertas de empleo, ayudando a los candidatos a encontrar los trabajos más compatibles con su perfil profesional.

## 🎯 Descripción del Proyecto

AI JOBS es un sistema inteligente que:
- **Procesa CVs en formato PDF** extrayendo y analizando el contenido
- **Utiliza técnicas de NLP** para limpiar y normalizar el texto
- **Aplica algoritmos de similitud** para encontrar los mejores matches
- **Presenta resultados ordenados** por compatibilidad con el perfil del candidato

## ✨ Características Principales

### 🧠 Inteligencia Artificial
- **Procesamiento de texto avanzado** con NLTK y spaCy
- **Lematización en español** para normalización de términos
- **Eliminación de stop words** específicas para contexto laboral
- **Vectorización con CountVectorizer** de scikit-learn

### 🎨 Interfaz Moderna
- **Diseño minimalista y elegante** con Bootstrap 5
- **Totalmente responsive** para dispositivos móviles y desktop
- **Animaciones suaves** y efectos hover
- **Experiencia de usuario intuitiva**

### 📊 Funcionalidades
- **Carga de CVs** mediante drag & drop o selector de archivos
- **Procesamiento automático** de documentos PDF
- **Análisis de compatibilidad** con base de datos de empleos
- **Ranking de resultados** ordenados por relevancia
- **Gestión de CVs** cargados previamente

## 🚀 Tecnologías Utilizadas

### Backend
- **Django 4.x** - Framework web de Python
- **Python 3.x** - Lenguaje principal
- **SQLite** - Base de datos

### Inteligencia Artificial & NLP
- **NLTK** - Tokenización y procesamiento de texto
- **spaCy** - Lematización avanzada en español
- **scikit-learn** - Vectorización y algoritmos de ML
- **pandas** - Manipulación de datos
- **PyPDF2/pdfplumber** - Extracción de texto de PDFs

### Frontend
- **HTML5 & CSS3** - Estructura y estilos
- **Bootstrap 5** - Framework CSS responsive
- **Font Awesome** - Iconografía
- **Google Fonts (Inter)** - Tipografía moderna
- **JavaScript** - Interactividad

## 📁 Estructura del Proyecto

```
mi_primera_aplicacion_inteligente/
├── cv_matcher/                    # Proyecto Django principal
│   ├── cv_matcher/               # Configuración del proyecto
│   │   ├── settings.py          # Configuraciones
│   │   ├── urls.py             # URLs principales
│   │   └── wsgi.py             # Configuración WSGI
│   ├── matcher/                 # Aplicación principal
│   │   ├── models.py           # Modelos de datos
│   │   ├── views.py            # Lógica de negocio
│   │   ├── forms.py            # Formularios
│   │   ├── urls.py             # URLs de la app
│   │   ├── templates/          # Plantillas HTML
│   │   │   ├── index.html      # Página principal
│   │   │   ├── process_cv.html # Carga de CV
│   │   │   ├── list_cv.html    # Lista de CVs
│   │   │   └── match.html      # Resultados
│   │   └── static/             # Archivos estáticos
│   │       ├── data/           # Datos serializados
│   │       └── images/         # Imágenes
│   ├── documents/              # CVs subidos
│   ├── notebook.ipynb          # Análisis y desarrollo
│   ├── manage.py              # Comando Django
│   └── db.sqlite3             # Base de datos
└── README.md                   # Este archivo
```

## ⚙️ Instalación y Configuración

### Prerequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git

### 1. Clonar el Repositorio
```bash
git clone https://github.com/aladelca/mi_primera_aplicacion_inteligente.git
cd mi_primera_aplicacion_inteligente
```

### 2. Crear Entorno Virtual
```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
```

### 3. Instalar Dependencias
```bash
pip install django pandas numpy nltk scikit-learn
pip install spacy pdfplumber PyPDF2
python -m spacy download es_core_news_sm
```

### 4. Configurar NLTK
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

### 5. Ejecutar Migraciones
```bash
cd cv_matcher
python manage.py migrate
```

### 6. Crear Superusuario (Opcional)
```bash
python manage.py createsuperuser
```

### 7. Ejecutar el Servidor
```bash
python manage.py runserver
```

La aplicación estará disponible en: `http://localhost:8000`

## 🔧 Uso de la Aplicación

### 1. Página Principal
- Accede a la página principal donde se presenta la aplicación
- Selecciona entre "Procesar CV" o "Ver CVs Cargados"

### 2. Procesar CV
- Sube un archivo PDF con tu currículum
- El sistema extraerá y procesará automáticamente el texto
- Recibirás una lista de empleos compatibles ordenados por relevancia

### 3. Ver Resultados
- Los resultados muestran los empleos más compatibles
- Cada resultado incluye el porcentaje de compatibilidad
- Puedes navegar de vuelta para procesar más CVs

## 🧪 Desarrollo y Análisis

El proyecto incluye un **Jupyter Notebook** (`notebook.ipynb`) con:
- Análisis exploratorio de datos de empleos
- Desarrollo del pipeline de procesamiento de texto
- Experimentos con diferentes algoritmos de NLP
- Visualizaciones y métricas de rendimiento

### Pipeline de Procesamiento de Texto
1. **Limpieza**: Eliminación de caracteres especiales
2. **Tokenización**: División en palabras individuales
3. **Eliminación de stop words**: Filtrado de palabras irrelevantes
4. **Lematización**: Normalización a forma base de las palabras
5. **Vectorización**: Conversión a representación numérica

## 🎨 Diseño y UX

### Paleta de Colores
- **Primario**: #6366f1 (Índigo)
- **Secundario**: #f8fafc (Gris claro)
- **Texto**: #1e293b (Gris oscuro)
- **Acentos**: Gradientes púrpura-azul

### Características de Diseño
- **Minimalista y moderno**
- **Responsive design**
- **Animaciones suaves**
- **Tipografía legible (Inter)**
- **Iconografía consistente**

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Próximas Mejoras

- [ ] Implementar más algoritmos de similitud (TF-IDF, Word2Vec)
- [ ] Agregar filtros por categoría de empleo
- [ ] Implementar sistema de puntuación más sofisticado
- [ ] Agregar exportación de resultados a PDF
- [ ] Implementar análisis de sentimientos
- [ ] Crear dashboard de métricas

## 📊 Métricas del Proyecto

- **Lenguajes**: Python (85%), HTML/CSS (10%), JavaScript (5%)
- **Líneas de código**: ~2000+
- **Archivos**: 15+ archivos principales
- **Dependencias**: 10+ librerías especializadas

## 👨‍💻 Autor

**Carlos Adrián Alarcón Delgado**
- Profesor de Cibertec
- Email: alarcon.adrianc@gmail.com

## 📄 Licencia

Este proyecto fue desarrollado como parte del curso de Inteligencia Artificial en Cibertec (2025).

---

**¡Desarrollado con ❤️ en Cibertec!**

> *"La inteligencia artificial no es solo sobre hacer que las máquinas piensen, sino sobre ayudar a las personas a encontrar mejores oportunidades."*

# Quotes and Authors App

## Descripción del Proyecto

El objetivo de este proyecto es desarrollar una aplicación web que permita visualizar citas y detalles de autores extraídos de la web [https://quotes.toscrape.com/](https://quotes.toscrape.com/). Este proyecto está diseñado para familiarizarse con técnicas de web scraping y el manejo de bases de datos NoSQL, en particular MongoDB.

### Briefing del Proyecto

La empresa XYZ Corp está buscando utilizar una frase que refleje sus valores y misión. Para ello, se ha desarrollado un programa en Python que realiza web scraping para extraer citas, el autor de cada cita, los tags asociados a cada cita, y la página "about" con información de los autores. Los datos extraídos se formatean y almacenan en una base de datos MongoDB.

**Objetivos del Proyecto:**

1. **Acceder a una Web Preparada para Ser Scrapeada**: La web contiene muchas frases junto con información relacionada.
2. **Extraer Información Relevante**: Utilizar técnicas de web scraping en Python para obtener todas las frases junto con la información adicional (autor, tags, about).
3. **Formatear los Datos**: Asegurar que los datos extraídos estén limpios y organizados de manera coherente.
4. **Almacenar los Datos en una Base de Datos**: Utilizar una base de datos NoSQL, específicamente MongoDB, para guardar la información extraída.

### Funcionalidades

- **Visualización de Citas**: Muestra una lista de citas junto con las etiquetas y el autor. Puedes expandir para ver la biografía del autor.
- **Visualización de Autores**: Muestra una lista de autores con sus detalles y citas asociadas.
- **Scraper**: Un script para extraer citas y detalles de autores de un sitio web y guardarlos en la base de datos MongoDB.

## Estructura del Proyecto

```
├── .gitignore
├── env/
├── requirements.txt
├── README.md
├── logs/
├── ├── scraper.log
│   └── database.log
├── scripts/
│   ├── scraper.py
│   └── database.py
└── tests/
    ├── test_scraper.py
    └── test_database.py
└── app.py
```

- `app.py`: Archivo principal de la aplicación Streamlit.
- `scraper.py`: Script para extraer datos del sitio web.
- `database.py`: Funciones para conectar y guardar datos en MongoDB.
- `requirements.txt`: Lista de dependencias del proyecto.
- `logs/`: Carpeta para almacenar archivos de registro (logs).
- `tests/`: Carpeta para pruebas unitarias.

## Requisitos

Para ejecutar este proyecto, necesitas tener instaladas las siguientes dependencias:

- Python 3.x
- MongoDB (local o en la nube)
- Las dependencias del proyecto listadas en `requirements.txt`

## Instalación

1. **Clona el repositorio**

   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio
   ```

2. **Configura un entorno virtual**

   ```bash
   python -m venv env
   source env/bin/activate  # En Windows: env\Scripts\activate
   ```

3. **Instala las dependencias**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configura MongoDB**

   Asegúrate de tener MongoDB en ejecución en `mongodb://localhost:27017/` o ajusta la URL de conexión en `database.py` según sea necesario.

## Ejecución

Para ejecutar la aplicación Streamlit, usa el siguiente comando:

```bash
streamlit run app.py
```

Esto abrirá la aplicación en tu navegador web por defecto.

## Uso del Scraper

Para ejecutar el scraper y poblar la base de datos con citas y detalles de autores, ejecuta el siguiente comando:

```bash
python scripts/scraper.py
```

Esto extraerá los datos del sitio web y los guardará en la base de datos MongoDB.


## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama para tu feature (`git checkout -b feature/mi-feature`).
3. Haz commit de tus cambios (`git commit -am 'Añadí nueva feature'`).
4. Empuja tu rama (`git push origin feature/mi-feature`).
5. Crea un nuevo Pull Request.



## ¡Gracias por usar la aplicación Quotes and Authors!


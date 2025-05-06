# Resultados-ChatGPT

Repositorio que incluye los resultados obtenidos del proyecto de Aplicación de la IA generativa en Herramientas de Gestión de Requisitos , correspondiente al Trabajo Fin de Máster de Francisco Hernández Garro.

## Estructura del catálogo

Este repositorio contiene los resultados de las dos herramientas desarrollados en este proyecto. En el subdirectorio _Catalogo de Requisitos_ se encuentran los resultados de la herramienta _RequiCreator_, encargada de crear un repositorio de requisitos de privacidad en base a una legislación. El subdirectorio _Seleccion de Requisitos_ contiene los resultados de _RequiSelector_, herramienta que selecciona una lista de requisitos en base a un catálogo de requisitos (opcional) y una legislación dada. En el tercer directorio, _Catalogo Incorrecto_, se encuentra un catálogo generado que incluye requisitos que inclumplen normas de la RGPD, para comprobar que ambas funcionalidades las detectan. El cuarto directorio, trata la validación de las salidas, por medio de _RequiValidator_. El quinto directorio, contiene las salidas correspondientes a la trazabilidad entre los requisitos y sus fuentes, realizada por medio de _RequiTrace_.

En el sexto directorio _Evaluación_, se trata la evaluación de los requisitos en base a su concordancia con las normas que referencian. Para ello se contiene un script de Python _comparar_bert_score.py_, que para ejecutarlo habrá que importar una serie de dependencias, que se encuentran en _requirements.txt_ con el siguiente comando:

```
pip install -r requirements.txt
```

También contiene las entradas a dicho script y los resultados, tanto rescalado como sin rescalado.

La estructura de subdirectorios es la siguiente:

```
Resultados-ChatGPT
|
+---1. Catalogo de Requisitos
|   +---Actualizacion
|   |       CatalogoPrivacidad_RequisitosDesfasados.pdf
|   |       CatalogoPrivacidad_Actualizado.pdf
|   |
|   +---Basico
|   |       CatalogoPrivacidad_Generado_ConConocimiento.pdf
|   |       CatalogoPrivacidad_Generado_SinConocimiento.pdf
|   |
|   +---Chain of Thought
|   |       Catalogo_ChainOfThought.pdf
|   |
|   \---Internacionalizacion
|           CatalogopPivacidad_Generado_CCPA_CPRA.pdf
|           CatalogoPrivacidad_Generado_Frances.pdf
|           CatalogoPrivacidad_Generado_Ingles.pdf
|
+---2. Seleccion de Requisitos
|   +---Basico
|   |       Requisitos_SaaS_HC_ConConocimiento (Con Catalogo).pdf
|   |       Requisitos_SaaS_HC_ConConocimiento (Sin Catalogo).pdf
|   |       Requisitos_SaaS_HC_SinConocimiento (Sin Catalogo).pdf
|   |
|   +---Chain of Thought
|   |       Seleccion_ChainOfThought.pdf
|   |
|   \---Internacionalizacion
|           Requisitos_SaaS_HC_CCPA_CPRA (Con Catalogo).pdf
|           Requisitos_SaaS_HC_Frances (Sin Catalogo).pdf
|           Requisitos_SaaS_HC_Ingles (Sin Catalogo).pdf
|
+---3. Catalogo Incorrecto
|      CatalogoPrivacidad_Incorrecto.pdf
|
+---4. Validación de salidas
|   +---4.1. Catalogo de Requisitos
|   |   +---Actualizacion
|   |   |       Validacion_CatalogoPrivacidad_Actualizado.xlsx
|   |   |
|   |   +---Basico
|   |   |       Validacion_CatalogoPrivacidad_Generado_ConConocimiento.xlsx
|   |   |       Validacion_CatalogoPrivacidad_Generado_SinConocimiento.xlsx
|   |   |
|   |   +---Chain of Thought
|   |   |       Validacion_Catalogo_ChainOfThought.xlsx
|   |   |
|   |   \---Internacionalizacion
|   |           Validacion_CatalogopPivacidad_Generado_CCPA_CPRA.xlsx
|   |           Validacion_CatalogoPrivacidad_Generado_Frances.xlsx
|   |           Validacion_CatalogoPrivacidad_Generado_Ingles.xlsx
|   |
|   +---4.2. Seleccion de Requisitos
|   |   +---Basico
|   |   |       Validacion_Requisitos_SaaS_HC_ConConocimiento (Con Catalogo).xlsx
|   |   |       Validacion_Requisitos_SaaS_HC_ConConocimiento (Sin Catalogo).xlsx
|   |   |       Validacion_Requisitos_SaaS_HC_SinConocimiento (Sin Catalogo).xlsx
|   |   |
|   |   +---Chain of Thought
|   |   |       Validacion_Seleccion_ChainOfThought.xlsx
|   |   |
|   |   \---Internacionalizacion
|   |           Validacion_Requisitos_SaaS_HC_CCPA_CPRA (Con Catalogo).xlsx
|   |           Validacion_Requisitos_SaaS_HC_Frances (Sin Catalogo).xlsx
|   |           Validacion_Requisitos_SaaS_HC_Ingles (Sin Catalogo).xlsx
|   |
|   \---4.3. Catalogo Incorrecto
|           Validacion_CatalogoPrivacidad_Incorrecto.xlsx
|
+---5. Trazabilidad de requisitos
|   +---Humano
|   |       Trazabilidad_TFG_FranMarquina_Junio_2019.xlsx
|   |
|   \---LLM
|           Trazabilidad_CatalogoPrivacidad_Generado_ConConocimiento.xlsx
|           Trazabilidad_Requisitos_SaaS_HC_ConConocimiento (Con Catalogo).xlsx
|           Trazabilidad_Requisitos_SaaS_HC_ConConocimiento (Sin Catalogo)l.xlsx
|           Trazabilidad_Seleccion_ChainOfThought.xlsx
|
\---6. Evaluación
    +---Código
    |       comparar_bert_score.py
    |       requirements.txt
    |
    +---Humano
    |   \---TFG FranMarquina Junio 2019
    |       |   Candidatos.xlsx
    |       |   Referencias.xlsx
    |       |   
    |       +---Resultados
    |       |       histograma_f1.png
    |       |       lineas_metricas.png
    |       |       resultados_bertscore.xlsx
    |       |       
    |       \---Resultados(Rescalado)
    |               histograma_f1.png
    |               lineas_metricas.png
    |               resultados_bertscore.xlsx
    |
    \---LLM
        +---CatalogoPrivacidad Generado ConConocimiento
        |   |   Candidatos.xlsx
        |   |   Referencias.xlsx
        |   |
        |   +---Resultados
        |   |       histograma_f1.png
        |   |       lineas_metricas.png
        |   |       resultados_bertscore.xlsx
        |   |
        |   \---Resultados(Rescalado)
        |           histograma_f1.png
        |           lineas_metricas.png
        |           resultados_bertscore.xlsx
        |
        +---Requisitos SaaS HC ConConocimiento (Con Catalogo)
        |   |   Candidatos.xlsx
        |   |   Referencias.xlsx
        |   |
        |   +---Resultados
        |   |       histograma_f1.png
        |   |       lineas_metricas.png
        |   |       resultados_bertscore.xlsx
        |   |
        |   \---Resultados(Rescalado)
        |           histograma_f1.png
        |           lineas_metricas.png
        |           resultados_bertscore.xlsx
        |
        +---Requisitos SaaS HC ConConocimiento (Sin Catalogo)
        |   |   Candidatos.xlsx
        |   |   Referencias.xlsx
        |   |
        |   +---Resultados
        |   |       histograma_f1.png
        |   |       lineas_metricas.png
        |   |       resultados_bertscore.xlsx
        |   |
        |   \---Resultados(Rescalado)
        |           histograma_f1.png
        |           lineas_metricas.png
        |           resultados_bertscore.xlsx
        |
        \---Seleccion ChainOfThought
            |   Candidatos.xlsx
            |   Referencias.xlsx
            |   
            +---Resultados
            |       histograma_f1.png
            |       lineas_metricas.png
            |       resultados_bertscore.xlsx
            |       
            \---Resultados(Rescalado)
                    histograma_f1.png
                    lineas_metricas.png
                    resultados_bertscore.xlsx
```

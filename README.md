# Resultados-ChatGPT
Repositorio que incluye los resultados obtenidos del proyecto de Aplicación de la IA generativa en Herramientas de Gestión de Requisitos , correspondiente al Trabajo Fin de Máster de Francisco Hernández Garro.

## Estructura del catálogo
Este repositorio contiene los resultados de las dos herramientas desarrollados en este proyecto. En el subdirectorio _Catalogo de Requisitos_ se encuentran los resultados de la herramienta _RequiCreator_, encargada de crear un repositorio de requisitos de privacidad en base a una legislación. El subdirectorio _Seleccion de Requisitos_ contiene los resultados de _RequiSelector_, herramienta que selecciona una lista de requisitos en base a un catálogo de requisitos (opcional) y una legislación dada. En el último directorio, _Catalogo Incorrecto_, se encuentra un catálogo generado que incluye requisitos que inclumplen normas de la RGPD, para comprobar que ambas funcionalidades las detectan.

La estructura de subdirectorios es la siguiente:

```
Resultados-ChatGPT
|   
+---1. Catalogo de Requisitos
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
\---3. Catalogo Incorrecto
        CatalogoPrivacidad_Incorrecto.pdf
```
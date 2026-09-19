# 🛒 Scraper y Monitor Automatizado de Precios de Competencia

Este proyecto es una solución en **Python** diseñada para automatizar la extracción, limpieza y monitoreo de precios e inventario de competidores en comercios de e-commerce.

## 💼 Problema de Negocio que Resuelve
Muchos comercios y revendedores pierden horas semanales relevando manualmente los sitios web de su competencia para ajustar sus estrategias de precios. 

Este script automatiza la recolección periódica, procesa la información y entrega un reporte listo para usar en Excel/CSV, identificando quiebres de stock y oportunidades de precio.

## 🛠️ Tecnologías Utilizadas
* **Python 3.10+**
* **Pandas:** Procesamiento, transformación de datos y exportación.
* **BeautifulSoup / Requests:** Extracción de datos web (Web Scraping).

## 🚀 Funcionalidades Clave
1. Extracción automatizada de catálogo de productos (Precios, Categorías, Stock).
2. Limpieza de datos e inclusión de marcas temporales (*timestamps*).
3. Clasificación automatizada de alertas de inventario.
4. Generación de reportes limpios listos para consumir en Excel o Power BI.

## 📊 Ejemplo de Salida (Output)
| ID | Producto | Categoría | Precio Competencia | Stock | Estado Alerta |
|---|---|---|---|---|---|
| PROD-01 | Teclado Mecánico RGB | Periféricos | $45,000 | True | Disponible |
| PROD-03 | Monitor 24 FHD 165Hz | Monitores | $185,000 | False | Sin Stock en Competencia |

---
✉️ **¿Necesitás automatizar la recolección de datos o reportes de tu negocio?**  
Contáctame por [LinkedIn](https://www.linkedin.com/in/marcelocharo) o por correo a marcelogcharo@gmail.com

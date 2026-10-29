# Pedido para Codex: colores de las galerías de tenis (TRIBALL)

Codex hace las imágenes y Claude las monta en la página después.

---

## Tu tarea

Eres diseñador de producto para el catálogo web de TRIBALL, una tienda de baloncesto y voleibol en Colombia.
Dentro de cada modelo de tenis hay una galería con todos sus colores. **Todas las fotos de la galería deben verse
iguales**: un solo tenis, de perfil, con la punta hacia la izquierda, sobre fondo transparente.
Hoy muchas son fotos viejas (con mano, caja, estatua, piso, varios pares o marcas de agua) y otras son renders
que miran hacia el otro lado o están de frente, de tres cuartos o desde arriba.

La lista está en `pendientes-codex/lista.json`, sección `galerias`. Cada modelo tiene:

- `posiciones`: colores con foto vieja. **Rehazlos todos.**
- `revisar`: colores que ya tienen render limpio. **Míralos uno por uno** y rehaz solo los que no cumplan
  las reglas (punta hacia la derecha, de frente, de tres cuartos, desde arriba, con texto o con número).
  Los que ya cumplen, déjalos quietos.

## Tandas (haz una, súbela y para)

| Prioridad | Qué es | Rehacer | Revisar |
|---|---|---|---|
| 1 | Los más vendidos: Ja 3, Sky Elite FF 3, Hyperset, Metarise, Court FF 3, Mizuno Wave Momentum, ST Flare, ST Charger | 46 | 12 |
| 2 | Resto de tenis de adulto (95 modelos) | 311 | 262 |
| 3 | Tenis de niños | 38 | 0 |
| 4 | Asics y Mizuno "más referencias" | 100 | 4 |

La prioridad 2 es grande: hazla por marca con `--marca`. Orden: `nike` (190 + 181), `jordan` (26 + 15),
`adidas` (44 + 11), `puma` (38 + 21), `under` (Under Armour, 10 + 23), y al final `asics`, `on` y `reebok` juntos.

```bash
python3 pendientes-codex/extraer_referencias.py --prioridad 2 --marca nike
```

Commit de cada marca: `Renders Codex: galerías prioridad 2 <marca>`.

Para sacar las fotos de referencia de una tanda, corre desde la raíz del repo:

```bash
python3 pendientes-codex/extraer_referencias.py --prioridad 1
```

Eso deja:
- `pendientes-codex/referencias/<slug>/<slug>-color-NN.jpg` → los que hay que rehacer.
- `pendientes-codex/referencias/<slug>/revisar/<slug>-color-NN.jpg` → los que hay que revisar.

## Reglas del render

1. **El mismo tenis y el mismo color que la foto de referencia.** Copia exactamente colores, materiales, logos y suela.
   No inventes colores ni combinaciones: es inventario real que se vende con esa foto.
2. **Un solo tenis**, aunque la foto tenga el par.
3. **De perfil, vista lateral exterior, con la punta mirando a la IZQUIERDA** y el talón a la derecha.
   Todos los colores del catálogo deben mirar hacia ese lado.
4. **Fondo transparente** (PNG con canal alfa). Sin piso, sin reflejos y sin sombras grandes.
5. Sin manos, cajas, estatuas, etiquetas colgando, texto, precios, números, marcas de agua ni el logo de TRIBALL.
6. Lienzo **1200 × 1200 px**. El tenis ocupa cerca del **90 % del ancho**, centrado y un poco por encima de la mitad.
7. No voltees la imagen como espejo si el tenis tiene letras o números (por ejemplo PUMA, SC, ON, ASICS):
   saldrían al revés. En ese caso haz el render de nuevo mirando a la izquierda.
8. Si la foto muestra dos colores distintos, está recortada o no se distingue el color o el modelo, **no lo inventes**:
   anótalo en `imagenes codex/no-se-pudo.txt` con el nombre del archivo y el motivo.

## Dónde guardar y cómo nombrar

```
imagenes codex/<slug>/<slug>-color-NN.png
```

El mismo nombre que la referencia, pero en .png y sin la carpeta `revisar`.
Ejemplo: `pendientes-codex/referencias/nike-ja-3/nike-ja-3-color-04.jpg` → `imagenes codex/nike-ja-3/nike-ja-3-color-04.png`.

## Lo que NO debes tocar

No edites `index.html`, ni las carpetas `c/`, `m/`, `p/`, `img/` o `assets/`. Solo agrega imágenes dentro de
`imagenes codex/`. Claude revisa cada render contra la foto original, monta solo los que coinciden, actualiza
las vistas previas de WhatsApp y publica.

## Al terminar cada tanda

Haz commit con el mensaje `Renders Codex: galerías prioridad N` y súbelo a la rama `main`.

---

## Portadas pendientes (aparte)

Quedan 4 portadas en la sección `portadas` de `lista.json`: tobillera, mangas de pierna, camiseta compresiva
manga larga y toalla Gatorade. No las hagas hasta que haya fotos nuevas del producto.

# Pedido para Codex: renders de producto para el catálogo TRIBALL

Copia este archivo completo en Codex. Codex hace las imágenes y Claude las monta en la página después.

---

## Tu tarea

Eres diseñador de producto para el catálogo web de TRIBALL (tienda de tenis de baloncesto y voleibol).
Tienes que crear **renders limpios de producto** para reemplazar fotos viejas del catálogo: fotos con manos,
cajas, una estatua de fondo, varios zapatos juntos, carteles con precio o marcas de agua.

La lista exacta está en `pendientes-codex/lista.json`. Para ver las fotos que tienes que rehacer, corre:

```bash
python3 pendientes-codex/extraer_referencias.py --prioridad 99   # solo saca las portadas
```

Eso deja cada foto actual en `pendientes-codex/referencias/<slug>/<slug>-color-NN.jpg`
(las portadas quedan en `pendientes-codex/referencias/_portadas/`).

## Orden de trabajo

**Desde el 29 de octubre Codex solo hace portadas** (la primera foto de cada producto).
Las galerías de colores se quedan con fotos reales del inventario: un render puede cambiar
detalles del zapato y el cliente debe ver exactamente lo que va a recibir.

Pendientes:

| Qué | Archivo |
|---|---|
| Portada de "Nike niños con velcro" (el render anterior salió como guayo con taches; es un tenis, sin taches) | `imagenes codex/_portadas/x-nike-ni-os-con-velcro.png` |

No hagas renders de galería (`imagenes codex/<slug>/<slug>-color-NN.png`) aunque aparezcan en `lista.json`.

## Reglas del render (tenis)

1. **El mismo zapato y el mismo color que la foto de referencia.** Copia exactamente los colores, los materiales,
   el logo y la suela. No inventes colores ni combinaciones: es inventario real que se vende con esa foto.
2. **Un solo zapato**, aunque la foto tenga el par.
3. **Vista lateral de perfil, con la punta mirando a la IZQUIERDA** y el talón a la derecha.
   Todo el catálogo mira hacia ese lado.
4. **Fondo transparente** (PNG con canal alfa). Sin sombras grandes, sin piso, sin reflejos.
5. Sin manos, cajas, etiquetas colgando, texto, precios, marcas de agua ni el logo de TRIBALL.
6. Lienzo **1200 × 1200 px**. El zapato ocupa cerca del **90 % del ancho**, centrado y un poco por encima de la mitad.
7. Si en la foto no se distingue bien el color o el modelo, **no lo inventes**: anótalo en
   `imagenes codex/no-se-pudo.txt` con el nombre del archivo y el motivo.

## Reglas para portadas de accesorios

Producto solo sobre fondo transparente, de frente, sin personas, sin texto y sin precios.
Si la foto es un cartel con varios productos, haz un render por producto y numéralos `-a`, `-b`, etc.

## Dónde guardar y cómo nombrar

```
imagenes codex/<slug>/<slug>-color-NN.png     ← mismo nombre que la referencia, pero en .png
imagenes codex/_portadas/<slug>.png
```

Ejemplo: la referencia `pendientes-codex/referencias/nike-ja-3/nike-ja-3-color-04.jpg`
se convierte en `imagenes codex/nike-ja-3/nike-ja-3-color-04.png`.

## Lo que NO debes tocar

No edites `index.html`, ni las carpetas `c/`, `m/`, `p/`, `img/` o `assets/`. Solo agrega imágenes dentro de
`imagenes codex/`. Claude se encarga de montarlas en la página, actualizar las vistas previas de WhatsApp
y publicar.

## Al terminar cada tanda

Haz commit con el mensaje `Renders Codex: portadas` y súbelo a la rama `main`.

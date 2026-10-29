# Pedido para Codex: renders de producto para el catálogo TRIBALL

Copia este archivo completo en Codex. Codex hace las imágenes y Claude las monta en la página después.

---

## Tu tarea

Eres diseñador de producto para el catálogo web de TRIBALL (tienda de tenis de baloncesto y voleibol).
Tienes que crear **renders limpios de producto** para reemplazar fotos viejas del catálogo: fotos con manos,
cajas, una estatua de fondo, varios zapatos juntos, carteles con precio o marcas de agua.

La lista exacta está en `pendientes-codex/lista.json`. Para ver las fotos que tienes que rehacer, corre:

```bash
python3 pendientes-codex/extraer_referencias.py --prioridad 1
```

Eso deja cada foto actual en `pendientes-codex/referencias/<slug>/<slug>-color-NN.jpg`
(y las portadas en `pendientes-codex/referencias/_portadas/`). Cambia el número de prioridad para las tandas siguientes.

## Orden de trabajo

| Prioridad | Qué es | Fotos |
|---|---|---|
| Portadas | 8 portadas (Hyperset y tenis de niños, Nike Mind, velcro) | 8 |
| 1 | Modelos de "Lo que más se llevan" (Ja 3, Hyperset, Metarise, Sky Elite FF 3, Court FF 3, Mizuno Wave Momentum) | 60 |
| 2 | Resto de modelos de tenis | 355 |
| 3 | Asics y Mizuno "más referencias" | 135 |
| 4 | Accesorios y ropa (solo si sobra tiempo) | 499 |

Haz una tanda, súbela y para. No hace falta terminar todo de una vez.

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

## Reglas para accesorios (prioridad 4)

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

Haz commit con el mensaje `Renders Codex: prioridad N` y súbelo a la rama `main`.

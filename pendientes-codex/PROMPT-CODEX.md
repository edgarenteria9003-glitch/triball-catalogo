# Pedido para Codex: portadas de producto para el catálogo TRIBALL

Codex hace las imágenes y Claude las monta en la página después.

---

## Tu tarea

Eres diseñador de producto para el catálogo web de TRIBALL, una tienda de baloncesto y voleibol en Colombia.
Tienes que crear **portadas limpias** (la primera foto de cada producto) para reemplazar fotos que tienen
personas, collages, varios productos juntos, empaques o una portada dañada.

**Solo portadas.** No hagas fotos de galería (`<slug>-color-NN`): las galerías se quedan con fotos reales del inventario.

La lista exacta, con el motivo de cada una, está en `pendientes-codex/lista.json` (sección `portadas`, 28 productos).
Para sacar la foto de referencia de cada producto, corre desde la raíz del repo:

```bash
python3 pendientes-codex/extraer_referencias.py
```

Eso deja cada portada actual en `pendientes-codex/referencias/_portadas/<slug>.jpg`.
Si la referencia no basta para ver bien el producto, mira también su galería en `m/<slug>.json`.

## Reglas para todas las portadas

1. **El mismo producto y el mismo color que la referencia.** No cambies colores, materiales, logos ni diseño.
   Si la referencia no tiene logo, no le pongas uno. Es inventario real que se vende con esa foto.
2. **Un solo producto**, salvo que la lista diga otra cosa (por ejemplo "el par" o "tres balacas en fila").
3. **Sin personas, manos, caras, jugadores famosos, maniquíes, empaques, cajas, etiquetas colgando, texto, precios,
   marcas de agua ni el logo de TRIBALL.**
4. **Fondo transparente** (PNG con canal alfa). Sin piso, sin reflejos y sin sombras grandes.
5. Lienzo **1200 × 1200 px**. El producto ocupa cerca del **85 % del lienzo**, centrado.
6. **Tenis:** vista lateral de perfil, con la punta mirando a la **IZQUIERDA**. Suela real del modelo (los tenis no llevan taches).
7. **Ropa:** de frente, extendida y sin arrugas fuertes, como foto de tienda.
8. **Accesorios:** de frente o en el ángulo que mejor muestre el producto.
9. Si no se distingue bien el producto o el color, **no lo inventes**: anótalo en
   `imagenes codex/no-se-pudo.txt` con el slug y el motivo.

## Dónde guardar y cómo nombrar

```
imagenes codex/_portadas/<slug>.png
```

Ejemplo: la referencia `pendientes-codex/referencias/_portadas/x-roller-foam.jpg`
se convierte en `imagenes codex/_portadas/x-roller-foam.png`.

## Lo que NO debes tocar

No edites `index.html`, ni las carpetas `c/`, `m/`, `p/`, `img/` o `assets/`. Solo agrega imágenes dentro de
`imagenes codex/`. Claude las revisa contra la foto original, las monta, actualiza las vistas previas de WhatsApp y publica.

## Al terminar

Haz commit con el mensaje `Renders Codex: portadas` y súbelo a la rama `main`.

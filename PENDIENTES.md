# Pendientes — Sitio CAABSA STEEL

Estado al 15 de agosto de 2026. Sitio publicado: **120 páginas**, español e inglés,
31 proyectos, 10 estados, 0 enlaces rotos.

---

## 1. Acción tuya (técnica) — 2 minutos

### Redesplegar el asistente IA
El chat en vivo sigue con información vieja (no conoce los 31 proyectos, las
4 regiones ni el sector Industrial). El código ya está actualizado en el repo:

```bash
cd ~/Downloads/claude/constructora-industrial/worker
npx wrangler deploy
```

No pide contraseña ni la API key.

### Rotar la API key de DeepSeek
Se compartió por chat durante la instalación. Generar una nueva en
platform.deepseek.com y luego `npx wrangler secret put DEEPSEEK_API_KEY`.

---

## 2. Preguntas para el cliente

| # | Tema | Detalle |
|---|------|---------|
| 1 | **Proyecto de Tlaxcala** | Hay 2 fotos pero sin nombre de cliente ni tipo de obra. La página del estado existe, sin proyecto. |
| 2 | **Grupo CIMSA — ubicación** | La presentación dice "Parque Industrial El Coecillo, **Estado de México**", pero El Coecillo está en León, **Guanajuato**. Se publicó como lo escribió el cliente. Confirmar cuál es. |
| 3 | **Cuatro proyectos sin foto** | Bardahl, Grupo CIMSA, Soriana e Interjet: las únicas imágenes de la presentación eran capturas de pantalla de Google Maps (con barra del navegador). No se publicaron por calidad y por derechos de imagen de Google. Se necesitan fotos propias. |
| 4 | **Cumplimiento normativo** | El texto publicado menciona REPSE vigente, normas de seguridad e higiene y fianzas de cumplimiento y calidad. **Confirmar la vigencia exacta del REPSE y qué tipo de fianzas manejan** antes de dejarlo definitivo (el propio documento del cliente lo pedía). |
| 5 | **Posible proyecto Irizar** | Entre las fotos sueltas de Querétaro aparece una nave con logotipo de Irizar. Hoy se usa solo como imagen de fondo. Si es obra de CAABSA, darle su página. |
| 6 | **Brochure en PDF** | El botón "Descargar brochure" funciona, pero no hay archivo que entregar. |
| 7 | **Sector de algunos proyectos** | Los que no encajaban en los 5 sectores del brief quedaron como "Industrial" (Metrocolor, Robin, Mixing, Polynt, Tecnosol, Bardahl, Soriana, Ferrostaal, Daewoo, Kimberly-Clark, Química Apollo, TST/TIMCO). Confirmar si alguno debe reclasificarse. |
| 8 | **Fotos por proyecto** | Varios proyectos nuevos tienen una sola foto. Si hay más, mejoran mucho las páginas. |

---

## 3. Ya aplicado del último lote

- **+400 proyectos entregados** en las cifras (junto a 45 años, 1,600,000 m², 80,000 ton).
- **Números del encabezado más grandes** y visibles sin hacer scroll.
- **Logo ISO más grande** (Bureau Veritas) en inicio y en Nosotros.
- **Carrusel de logos** de 23 marcas en banda infinita.
- **Reseñas reales** tomadas de las 6 cartas de recomendación.
- **Misión, visión y política de calidad** con la redacción del cliente.
- **Bloque de cumplimiento normativo** (REPSE, seguridad, fianzas).
- **Hero**: "grandes corporativos y empresas AAA y AA".
- **Dirección exacta** en contacto y en el mapa: Vicente Guerrero 2800, Col.
  Francisco I. Madero, 52172 Toluca de Lerdo.
- **31 proyectos** con m², ubicación y alcance reales de la presentación.

---

## 4. Antes de salir a producción (dominio propio)

1. **Formulario de contacto: hoy NO envía los datos a ningún lado.** Valida y
   confirma en pantalla, pero falta conectarlo a un correo o CRM. Es lo más
   importante para no perder prospectos.
2. **Dominio.** Todo el SEO (canonical, hreflang, sitemap) ya apunta a
   `https://caabsasteel.mx/`.
3. **Worker**: dejar en `ALLOWED_ORIGINS` únicamente el dominio final.
4. **Saldo de DeepSeek** para que el chat siga respondiendo.
5. **Google Search Console**: dar de alta el dominio y enviar `sitemap.xml`.

---

## Nota de mantenimiento

Las páginas se generan con `gen_site_i18n.py` (+ `projects_new.py`, `blog_en.py`).
Si se edita un HTML a mano, el siguiente cambio lo sobrescribe: los cambios se
hacen en el generador.

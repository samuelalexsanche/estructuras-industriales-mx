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
| 1 | ~~**Proyecto de Tlaxcala**~~ **RESUELTO** | Es **Vetrotex Saint-Gobain**, nave industrial en el Parque Industrial Xicohténcatl, Tlaxcala. Aparece en el CV de la empresa (no en el documento del blog). Ya tiene página propia con 3 fotos. Falta la superficie en m², que el CV no indica. |
| 2 | **Grupo CIMSA — ubicación** | La presentación **y el CV** dicen "P. Ind. El Coecillo, **Estado de México**" (36,000 m²), pero El Coecillo está en León, **Guanajuato**. Al repetirse en dos documentos, se publicó como ellos lo escriben. Confirmar de todos modos. |
| 3 | ~~**Tres proyectos sin foto**~~ **RESUELTO con reserva** | Bardahl, Grupo CIMSA y Soriana ya tienen fotografía. **Ojo:** las tres provienen de imagen aérea o Street View de Google, y la de Soriana conserva la marca de agua "©2015 Google" repetida sobre la imagen. Conviene sustituirlas por fotografía propia de obra cuando la tengan. |
| 4 | **Cumplimiento normativo** | El texto publicado menciona REPSE vigente, normas de seguridad e higiene y fianzas de cumplimiento y calidad. **Confirmar la vigencia exacta del REPSE y qué tipo de fianzas manejan** antes de dejarlo definitivo (el propio documento del cliente lo pedía). |
| 5 | ~~**Proyecto Irizar**~~ **RESUELTO** | Publicado como un solo proyecto de dos naves (9,144 m²), como lo pidió el cliente en el documento nuevo. **Corrección de mi parte:** antes anoté que había una foto con logotipo de Irizar entre las sueltas de Querétaro; al revisarlas una por una no la hay — el logotipo que vi era el de Metrocolor. Irizar se publica sin fotografía. |
| 6 | ~~**Brochure en PDF**~~ **RESUELTO** | El brochure 2026 ya está publicado y se entrega tras el registro. |
| 7 | **Sector de algunos proyectos** | Los que no encajaban en los 5 sectores del brief quedaron como "Industrial" (Metrocolor, Robin, Mixing, Polynt, Tecnosol, Bardahl, Soriana, Ferrostaal, Daewoo, Kimberly-Clark, Química Apollo, TST/TIMCO). Confirmar si alguno debe reclasificarse. |
| 8 | **Fotos por proyecto** | Varios proyectos nuevos tienen una sola foto. Si hay más, mejoran mucho las páginas. |
| 9 | **El CV documenta 74 proyectos; el sitio publica 43** | Van 43 publicados. El CV trae la lista completa con cliente, parque industrial, estado, superficie y alcance de cada obra (Mars, Kiekert, Brose, Hitachi, Ventramex, Fernández Editores, Grupo Modelo, Cargill, Warner Lambert, Sealy, Legrand, Firmenich y más). **Decidir con el cliente si se publican todos**: son páginas nuevas con SEO propio por estado y sector, pero la mayoría no tiene fotos. |
| 10 | **ThyssenKrupp: el documento nuevo dice que Metalúrgica es la de Xoxtla** | El documento "Obras en la web" lista **una sola** ThyssenKrupp: *"ThyssenKrupp, Metalúrgica — Parque Industrial Xoxtla — 18,600 m² — llave en mano"*. Hoy el sitio tiene esos datos en el proyecto **thyssenkrupp** y deja **thyssenkrupp Metalúrgica** sin cifras. Si Metalúrgica es la de Xoxtla, hay que mover los datos y decir qué es entonces la otra obra (la de las fotos con dron), que no aparece en ningún documento. |
| 10b | **Foto descartada de ThyssenKrupp** | El archivo `thyssenkrupp.jpg` de esa carpeta muestra un edificio cuyo letrero dice **"ThyssenKrupp Industrial Solutions (Australia) Pty Ltd"**. No se publicó por ser una instalación en Australia, no una obra de CAABSA. |
| 13 | ~~**Cuatro proyectos nuevos sin fotografía**~~ **RESUELTO** | La carpeta actualizada trae fotos de Irizar (2), Mann+Hummel (2), Rubau (1) y Vesta San Luis Potosí (1). |
| 14 | ~~**Euroquip**~~ **PUBLICADO** | La carpeta actualizada ya le hizo folder propio con sus 3 fotos. Datos del CV: 5,050 m², P. Ind. Bernardo Quintana, sector alimenticio. |
| 15 | **Cosmetic Colors: faltan datos** | La carpeta actualizada le hizo folder propio con una foto, pero no aparece en el CV, ni en la presentación, ni en la lista "Obras en la web". Se publicó solo con nombre, estado y sector. Faltan superficie, ubicación y alcance. |
| 11 | **Fotos de Brose y Baleros Mexicanos** | Las únicas que hay miden 420×221 y 415×166 px. Se publicaron a su tamaño real para no falsear la nitidez, pero se ven pequeñas. Si existen los originales, mejoran mucho. |
| 12 | ~~**Superficie de Vetrotex**~~ **RESUELTO** | El documento nuevo la da: 2,000 m², nave industrial de 3 niveles para producción. |

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

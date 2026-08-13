# Pendientes — Sitio CAABSA STEEL

Estado al 10 de agosto de 2026. El sitio está publicado y funcionando
(82 páginas, español e inglés, 0 enlaces rotos).

---

## 1. Acción tuya (técnica) — 2 minutos

### Redesplegar el asistente IA
**Verificado hoy: el chat en vivo todavía responde con información vieja.**
Al preguntarle "¿en qué estados tienen proyectos?" contesta solo Centro/Bajío/Sur,
sin Occidente, sin los estados reales y con las cifras anteriores.

El código ya está actualizado en el repo; solo falta publicarlo:

```bash
cd ~/Downloads/claude/constructora-industrial/worker
npx wrangler deploy
```

No pide contraseña ni la API key (ya están configuradas).

### Rotar la API key de DeepSeek
La key se compartió por chat durante la instalación, así que conviene cambiarla:
1. Generar una nueva en https://platform.deepseek.com y borrar la anterior.
2. `npx wrangler secret put DEEPSEEK_API_KEY` (pegar la nueva).

---

## 2. Información que falta del cliente

| # | Qué falta | Dónde impacta | Hoy muestra |
|---|-----------|---------------|-------------|
| 1 | **Reseñas reales** (nombre, puesto, empresa y texto de 3 clientes) | Sección "Lo que dicen nuestros clientes" en inicio | `[Nombre]`, `[Puesto]`, `[Empresa]` |
| 2 | **Misión y Visión** definitivas | Página Nosotros | Borradores marcados "[Pendiente de aprobación]" |
| 3 | **Brochure en PDF** | Botón "Descargar brochure" (inicio y Nosotros) | El formulario funciona, pero no hay archivo que descargar |
| 4 | **Proyecto de Tlaxcala**: nombre del cliente y qué se construyó | Página del estado de Tlaxcala | "0 proyectos documentados" (solo hay 2 fotos) |
| 5 | **Número total de proyectos entregados** | Bloque de cifras | Se sustituyó por "7 estados con obra ejecutada" (dato verificable) |
| 6 | **Dirección exacta** en Metepec | Mapa de la página de Contacto | El mapa apunta a "Metepec" en general |

### Datos que sí llegaron y ya están aplicados
- 45 años de experiencia · +1,600,000 m² construidos · +80,000 toneladas de acero
- Redes sociales reales (LinkedIn, Facebook, Instagram)
- Sello ISO 9001:2015 de Bureau Veritas
- Teléfono/WhatsApp 722 523 2020 · proyectos@caabsasteel.mx · Metepec, Edomex
- 15 proyectos con fotos, en 7 estados
- 3 artículos de blog

---

## 3. Detalles a confirmar con el cliente

1. **Superficies y alcance de 10 proyectos.** Solo 5 traían datos documentados
   (Gates 1,500 m² · Espejos Inteligentes 2,500 m² · Grupo Sánchez 25,000 m² ·
   Tecnosol 3,000 m² · Polynt 1,500 m²). Los otros 10 se describen sin cifras
   para no inventar nada.

2. **Ciudades por estado.** Solo se mencionan las que constan en su material
   (Cuernavaca, Cuautla, Guadalajara, Metepec). Si confirman más ciudades donde
   han trabajado, ayudan mucho al posicionamiento local.

3. **Sector de cada proyecto.** Se asignó el más defendible; 6 quedaron en
   "Industrial" (Mixing, Saint-Gobain, Metrocolor, Robin, Polynt, Tecnosol).

4. **Secciones sin proyectos todavía**, que hoy muestran una invitación a cotizar
   en lugar de obras:
   - Sector **Aeronáutico**
   - Región **Sur** (Oaxaca y Veracruz)

---

## 4. Antes de salir a producción (dominio propio)

1. **Dominio.** Todo el SEO (canonical, hreflang, sitemap) ya apunta a
   `https://caabsasteel.mx/`. Al publicar ahí, todo queda correcto sin cambios.
2. **Seguridad del asistente.** En `worker/worker.js`, dejar en `ALLOWED_ORIGINS`
   únicamente el dominio final y borrar el resto.
3. **Formulario de contacto.** Hoy valida y confirma en pantalla, pero **no envía
   los datos a ningún lado**. Falta conectarlo a un correo o CRM.
4. **Saldo de DeepSeek.** El chat responde mientras la cuenta tenga saldo.
5. **Google Search Console.** Dar de alta el dominio y enviar `sitemap.xml`.

---

## Nota de mantenimiento

Las páginas se generan con un script (`gen_site_i18n.py`). Si se edita un HTML a
mano, el siguiente cambio lo sobrescribe: los cambios se hacen en el generador.

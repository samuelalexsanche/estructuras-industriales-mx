#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera el sitio CAABSA STEEL en ESPAÑOL (raíz) e INGLÉS (/en/),
con hreflang, toggle de idioma y SEO por página.
"""
import os, shutil

ROOT = os.path.expanduser("~/Downloads/claude/constructora-industrial")
SITE_URL = "https://caabsasteel.mx/"

WA_NUM = "527225232020"
TEL = "722 523 2020"
EMAIL = "proyectos@caabsasteel.mx"

# Iconos de la sección de documentación
DOC_IC = ('<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.7" '
          'stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H7a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V7z"/>'
          '<path d="M14 2v5h5"/><path d="M9 13h6"/><path d="M9 17h4"/></svg>')
DL_IC  = ('<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" '
          'stroke-linecap="round" stroke-linejoin="round" style="margin-right:9px;vertical-align:-4px">'
          '<path d="M12 3v12"/><path d="m7 11 5 5 5-5"/><path d="M4 20h16"/></svg>')
WA_TXT = {
 "es": "Hola%2C%20quiero%20cotizar%20un%20proyecto%20industrial%20con%20CAABSA%20STEEL",
 "en": "Hello%2C%20I%27d%20like%20a%20quote%20for%20an%20industrial%20project%20with%20CAABSA%20STEEL",
}

for d in ["sectores","regiones","en","en/sectors","en/regions"]:
    os.makedirs(os.path.join(ROOT,d), exist_ok=True)

# ─────────────────────────────── DATA ───────────────────────────────
SECTORS = [
 dict(key="automotive", slug={"es":"automotriz","en":"automotive"},
   name={"es":"Automotriz","en":"Automotive"}, chip="chip--auto",
   photo="images/proyectos/gates/01.jpg",
   h1={"es":"Construcción industrial para el sector automotriz",
       "en":"Industrial construction for the automotive sector"},
   meta={"es":"Naves y plantas industriales para la cadena de suministro automotriz en Querétaro, Guanajuato, San Luis Potosí y Aguascalientes. Certificación ISO 9001:2015.",
         "en":"Industrial buildings and plants for the automotive supply chain in Querétaro, Guanajuato, San Luis Potosí and Aguascalientes. ISO 9001:2015 certified."},
   summary={"es":"Plantas y naves para la cadena de suministro automotriz del Bajío.",
            "en":"Plants and buildings for the automotive supply chain in the Bajío region."},
   copy={"es":"El sector automotriz exige tiempos de entrega precisos, especificaciones técnicas exactas y cero margen de error. En CAABSA STEEL diseñamos y construimos naves y plantas para armadoras y proveedores Tier 1 y Tier 2 en el Bajío, cumpliendo con los estándares de calidad que este sector requiere.",
         "en":"The automotive sector demands precise delivery schedules, exact technical specifications and zero margin for error. At CAABSA STEEL we design and build industrial facilities and plants for OEMs and Tier 1 and Tier 2 suppliers across the Bajío region, meeting the quality standards this industry requires."},
   build={"es":["Naves de manufactura","Centros de almacenamiento de partes","Áreas de ensamble","Oficinas administrativas anexas"],
          "en":["Manufacturing facilities","Parts warehousing centers","Assembly areas","Adjoining administrative offices"]},
   proj=("images/proyectos/martinrea-honsel/01.jpg","Martinrea Honsel",
         {"es":"Planta de autopartes con edificio administrativo · Bajío",
          "en":"Auto-parts plant with administrative building · Bajío region"})),

 dict(key="food", slug={"es":"alimenticio","en":"food-beverage"},
   name={"es":"Alimenticio","en":"Food & Beverage"}, chip="chip--food",
   photo="images/proyectos/jugos-del-valle/01.jpg",
   h1={"es":"Construcción industrial para el sector alimenticio",
       "en":"Industrial construction for the food and beverage sector"},
   meta={"es":"Naves industriales para plantas de alimentos y bebidas, con cumplimiento de normas sanitarias, en el centro de México y el Bajío.",
         "en":"Industrial buildings for food and beverage plants, compliant with sanitary regulations, in Central Mexico and the Bajío region."},
   summary={"es":"Instalaciones que cumplen normas sanitarias e industriales.",
            "en":"Facilities that meet sanitary and industrial standards."},
   copy={"es":"Las plantas de alimentos y bebidas requieren materiales, acabados y sistemas que cumplan con normativas sanitarias estrictas. Construimos instalaciones pensadas para procesos de producción alimentaria, con atención especial a superficies, ventilación y flujo de materiales.",
         "en":"Food and beverage plants require materials, finishes and systems that comply with strict sanitary regulations. We build facilities designed around food production processes, with particular attention to surfaces, ventilation and material flow."},
   build={"es":["Plantas de producción","Almacenes refrigerados","Áreas de empaque","Oficinas de control de calidad"],
          "en":["Production plants","Refrigerated warehouses","Packaging areas","Quality control offices"]},
   proj=("images/proyectos/jugos-del-valle/01.jpg","Jugos del Valle",
         {"es":"Planta de bebidas · nave de proceso y almacén",
          "en":"Beverage plant · process building and warehouse"})),

 dict(key="logistics", slug={"es":"logistico","en":"logistics"},
   name={"es":"Logístico","en":"Logistics"}, chip="chip--log",
   photo="images/proyectos/andenes/01.jpg",
   h1={"es":"Construcción de naves y centros de distribución logística",
       "en":"Construction of warehouses and logistics distribution centers"},
   meta={"es":"Centros de distribución y naves logísticas de alto rendimiento en el Estado de México, CDMX y Puebla.",
         "en":"High-performance distribution centers and logistics warehouses in the State of Mexico, Mexico City and Puebla."},
   summary={"es":"Centros de distribución de alto rendimiento.",
            "en":"High-performance distribution centers."},
   copy={"es":"Un centro de distribución bien diseñado reduce tiempos operativos y costos a largo plazo. Construimos naves logísticas con alturas libres optimizadas, andenes de carga eficientes y circulación pensada para el movimiento constante de mercancía.",
         "en":"A well-designed distribution center reduces operating times and long-term costs. We build logistics warehouses with optimized clear heights, efficient loading docks and circulation designed for the constant movement of goods."},
   build={"es":["Centros de distribución","Cross-dock","Naves de almacenamiento","Patios de maniobras"],
          "en":["Distribution centers","Cross-dock facilities","Storage warehouses","Truck maneuvering yards"]},
   proj=("images/proyectos/la-moderna/01.jpg","La Moderna",
         {"es":"Centro de distribución de gran claro con andenes de carga",
          "en":"Long-span distribution center with loading docks"})),

 dict(key="corporate", slug={"es":"corporativo","en":"corporate"},
   name={"es":"Corporativo","en":"Corporate"}, chip="chip--corp",
   photo="images/proyectos/tintas-sanchez/01.jpg",
   h1={"es":"Construcción de espacios corporativos industriales",
       "en":"Construction of industrial corporate spaces"},
   meta={"es":"Oficinas corporativas y espacios administrativos integrados a complejos industriales en el centro de México.",
         "en":"Corporate offices and administrative spaces integrated into industrial complexes in Central Mexico."},
   summary={"es":"Oficinas y espacios que representan tu marca.",
            "en":"Offices and spaces that represent your brand."},
   copy={"es":"Tus oficinas también son la cara de tu empresa. Diseñamos espacios corporativos funcionales y representativos, integrados a tu operación industrial, sin sacrificar estética ni comodidad para tus equipos de trabajo.",
         "en":"Your offices are also the face of your company. We design functional, representative corporate spaces integrated into your industrial operation, without compromising on aesthetics or comfort for your teams."},
   build={"es":["Oficinas corporativas","Salas de juntas","Recepciones","Áreas comunes en complejos industriales"],
          "en":["Corporate offices","Meeting rooms","Reception areas","Common areas within industrial complexes"]},
   proj=("images/proyectos/tintas-sanchez/01.jpg","Grupo Sánchez",
         {"es":"Complejo llave en mano de 25,000 m² con edificio corporativo",
          "en":"25,000 m² turnkey complex with corporate building"})),

 dict(key="pharma", slug={"es":"farmaceutico","en":"pharmaceutical"},
   name={"es":"Farmacéutico","en":"Pharmaceutical"}, chip="chip--pharma",
   photo="images/proyectos/aventis-pharma/01.jpg",
   h1={"es":"Construcción industrial para el sector farmacéutico",
       "en":"Industrial construction for the pharmaceutical sector"},
   meta={"es":"Plantas farmacéuticas, cuartos limpios y naves con control de contaminación en el Estado de México y el centro del país. Certificación ISO 9001:2015.",
         "en":"Pharmaceutical plants, cleanrooms and facilities with contamination control in the State of Mexico and Central Mexico. ISO 9001:2015 certified."},
   summary={"es":"Plantas y naves con los controles que exige la industria farmacéutica.",
            "en":"Plants and facilities with the controls the pharmaceutical industry demands."},
   copy={"es":"La industria farmacéutica trabaja bajo normas estrictas de higiene, control de contaminación y trazabilidad. Construimos plantas, áreas de proceso y almacenes con los acabados, materiales e instalaciones que estos procesos exigen, bajo nuestro sistema de gestión de calidad certificado ISO 9001:2015.",
         "en":"The pharmaceutical industry works under strict hygiene, contamination-control and traceability standards. We build plants, process areas and warehouses with the finishes, materials and installations these processes demand, under our ISO 9001:2015 certified quality management system."},
   build={"es":["Plantas de proceso farmacéutico","Cuartos limpios","Almacenes con control ambiental","Áreas de laboratorio y control de calidad"],
          "en":["Pharmaceutical process plants","Cleanrooms","Environmentally controlled warehouses","Laboratory and quality control areas"]},
   proj=None),

 dict(key="industrial", slug={"es":"industrial","en":"industrial"},
   name={"es":"Industrial","en":"Industrial"}, chip="chip--ind",
   photo="images/proyectos/metrocolor/01.jpg",
   h1={"es":"Construcción de naves y plantas industriales",
       "en":"Construction of industrial facilities and plants"},
   meta={"es":"Naves industriales, plantas de proceso y ampliaciones para la industria química, de impresión, materiales y manufactura en el centro de México, el Bajío y el occidente.",
         "en":"Industrial facilities, process plants and expansions for the chemical, printing, materials and manufacturing industries in Central Mexico, the Bajío and Western Mexico."},
   summary={"es":"Naves de proceso, ampliaciones y obra para plantas de manufactura.",
            "en":"Process facilities, expansions and works for manufacturing plants."},
   copy={"es":"No toda la industria encaja en una sola categoría. Construimos naves de proceso, almacenes y ampliaciones para plantas químicas, de impresión, de materiales y de manufactura en general. Buena parte de estas obras se ejecutan con la planta en operación, lo que exige una coordinación milimétrica para no interrumpir la producción de nuestro cliente.",
         "en":"Not every industry fits into a single category. We build process facilities, warehouses and expansions for chemical, printing, materials and general manufacturing plants. Many of these projects are carried out while the plant is running, which demands precise coordination so our client's production is never interrupted."},
   build={"es":["Naves de proceso","Ampliaciones sobre operación","Almacenes industriales","Bases para tanques y equipo","Vialidades internas","Obra civil y laminación"],
          "en":["Process facilities","Expansions over live operations","Industrial warehouses","Tank and equipment foundations","Internal roadways","Civil works, roofing and cladding"]},
   proj=("images/proyectos/tecnosol/01.jpg","Tecnosol",
         {"es":"Ampliación de almacén en planta en producción · 3,000 m²",
          "en":"Warehouse expansion at an operating plant · 3,000 m²"})),

 dict(key="aerospace", slug={"es":"aeronautico","en":"aerospace"},
   name={"es":"Aeronáutico","en":"Aerospace"}, chip="chip--aero",
   photo="images/proyectos/espejos-inteligentes/01.jpg",
   h1={"es":"Construcción industrial para el sector aeronáutico",
       "en":"Industrial construction for the aerospace sector"},
   meta={"es":"Infraestructura de precisión para la industria aeroespacial en Querétaro y el Bajío. Certificación ISO 9001:2015.",
         "en":"Precision infrastructure for the aerospace industry in Querétaro and the Bajío region. ISO 9001:2015 certified."},
   summary={"es":"Infraestructura de precisión para la industria aeroespacial.",
            "en":"Precision infrastructure for the aerospace industry."},
   copy={"es":"La industria aeroespacial exige tolerancias mínimas y procesos de construcción sumamente controlados. En CAABSA STEEL aplicamos nuestros procesos certificados ISO 9001:2015 para entregar infraestructura que cumple con las exigencias técnicas de este sector en el corredor aeroespacial del Bajío.",
         "en":"The aerospace industry demands minimal tolerances and tightly controlled construction processes. At CAABSA STEEL we apply our ISO 9001:2015 certified processes to deliver infrastructure that meets the technical requirements of this sector across the Bajío aerospace corridor."},
   build={"es":["Hangares","Plantas de manufactura de componentes","Áreas de ensamble de precisión"],
          "en":["Hangars","Component manufacturing plants","Precision assembly areas"]},
   proj=None),
]

REGIONS = [
 dict(key="central", slug={"es":"centro","en":"central-mexico"},
   name={"es":"Centro del país","en":"Central Mexico"},
   photo="images/proyectos/la-moderna/01.jpg",
   h1={"es":"Construcción industrial en el centro de México",
       "en":"Industrial construction in Central Mexico"},
   meta={"es":"Constructora industrial AAA y AA en Estado de México, CDMX y Puebla. Naves, centros logísticos y espacios corporativos.",
         "en":"Industrial construction company for AAA and AA clients in the State of Mexico, Mexico City and Puebla. Warehouses, logistics centers and corporate spaces."},
   summary={"es":"Estado de México, CDMX y Puebla.","en":"State of Mexico, Mexico City and Puebla."},
   copy={"es":"Desde nuestra base en Metepec, Estado de México, atendemos proyectos industriales en todo el centro del país. Esta región concentra gran parte de la actividad logística y corporativa de México, y hemos construido naves, centros de distribución y espacios administrativos para empresas que operan aquí.",
         "en":"From our base in Metepec, State of Mexico, we serve industrial projects throughout Central Mexico. This region concentrates much of the country's logistics and corporate activity, and we have built industrial facilities, distribution centers and administrative spaces for companies operating here."},
   states={"es":"Estado de México, Ciudad de México, Puebla","en":"State of Mexico, Mexico City, Puebla"},
   focus={"es":"logístico, corporativo","en":"logistics, corporate"},
   proj=("images/proyectos/la-moderna/01.jpg","La Moderna",
         {"es":"Centro de distribución · Estado de México","en":"Distribution center · State of Mexico"})),

 dict(key="bajio", slug={"es":"bajio","en":"bajio"},
   name={"es":"Bajío","en":"Bajío Region"},
   photo="images/proyectos/martinrea-honsel/01.jpg",
   h1={"es":"Construcción industrial en el Bajío",
       "en":"Industrial construction in the Bajío region"},
   meta={"es":"Naves industriales para los sectores automotriz y aeroespacial en Querétaro, Guanajuato, San Luis Potosí y Aguascalientes.",
         "en":"Industrial buildings for the automotive and aerospace sectors in Querétaro, Guanajuato, San Luis Potosí and Aguascalientes."},
   summary={"es":"Querétaro, Guanajuato, San Luis Potosí y Aguascalientes.",
            "en":"Querétaro, Guanajuato, San Luis Potosí and Aguascalientes."},
   copy={"es":"El Bajío es uno de los corredores industriales más dinámicos de México, con un fuerte clúster automotriz y aeroespacial. Construimos naves y plantas para proveedores y armadoras que buscan calidad certificada y tiempos de entrega confiables en esta región.",
         "en":"The Bajío is one of Mexico's most dynamic industrial corridors, with a strong automotive and aerospace cluster. We build facilities and plants for suppliers and OEMs seeking certified quality and reliable delivery schedules in this region."},
   states={"es":"Querétaro, Guanajuato, San Luis Potosí, Aguascalientes","en":"Querétaro, Guanajuato, San Luis Potosí, Aguascalientes"},
   focus={"es":"automotriz, aeronáutico","en":"automotive, aerospace"},
   proj=("images/proyectos/martinrea-honsel/01.jpg","Martinrea Honsel",
         {"es":"Planta de autopartes · Bajío","en":"Auto-parts plant · Bajío region"})),

 dict(key="occidente", slug={"es":"occidente","en":"western-mexico"},
   name={"es":"Occidente","en":"Western Mexico"},
   photo="images/proyectos/jugos-del-valle/01.jpg",
   h1={"es":"Construcción industrial en el occidente de México",
       "en":"Industrial construction in Western Mexico"},
   meta={"es":"Constructora industrial en Jalisco y el occidente de México. Naves industriales, plantas de proceso y estructura de acero en Guadalajara y su zona metropolitana.",
         "en":"Industrial construction company in Jalisco and Western Mexico. Industrial facilities, process plants and structural steel in Guadalajara and its metropolitan area."},
   summary={"es":"Jalisco y la zona metropolitana de Guadalajara.",
            "en":"Jalisco and the Guadalajara metropolitan area."},
   copy={"es":"El occidente de México concentra una fuerte industria de alimentos y bebidas, manufactura y tecnología alrededor de Guadalajara. Construimos naves de proceso, almacenes y espacios industriales para empresas que operan en esta región, con la misma calidad certificada de nuestras obras en el centro del país y el Bajío.",
         "en":"Western Mexico concentrates a strong food and beverage, manufacturing and technology industry around Guadalajara. We build process facilities, warehouses and industrial spaces for companies operating in this region, with the same certified quality as our projects in Central Mexico and the Bajío."},
   states={"es":"Jalisco","en":"Jalisco"},
   focus={"es":"alimenticio","en":"food and beverage"},
   proj=("images/proyectos/jugos-del-valle/01.jpg","Jugos del Valle",
         {"es":"Nave industrial de procesos · Guadalajara, Jalisco",
          "en":"Process facility · Guadalajara, Jalisco"})),

 dict(key="south", slug={"es":"otros-estados","en":"other-states"},
   name={"es":"Otros estados","en":"Other states"},
   photo="images/proyectos/jugos-del-valle/01.jpg",
   h1={"es":"Construcción industrial en otros estados de México",
       "en":"Industrial construction in other Mexican states"},
   meta={"es":"Constructora industrial con obra en Veracruz y otros estados de México. Naves, plantas y proyectos ejecutivos con calidad certificada ISO 9001:2015.",
         "en":"Industrial construction company with projects in Veracruz and other Mexican states. Facilities, plants and executive projects with ISO 9001:2015 certified quality."},
   summary={"es":"Veracruz y otros estados donde nos ha llevado la obra.","en":"Veracruz and other states our projects have taken us to."},
   copy={"es":"Nuestra obra no se limita a una sola región: acompañamos a nuestros clientes donde tengan su operación. Aquí reunimos los proyectos ejecutados fuera del centro, el Bajío y el occidente, incluida la zona sur y el Golfo, impulsada hoy por el nearshoring y el Corredor Interoceánico.",
         "en":"Our work is not limited to a single region: we follow our clients wherever their operations are. Here we bring together the projects delivered outside Central Mexico, the Bajío and the west, including the south and the Gulf, driven today by nearshoring and the Interoceanic Corridor."},
   states={"es":"Veracruz (y disponibles para el resto del país)","en":"Veracruz (and available across the rest of the country)"},
   focus={"es":"","en":""},
   proj=None),
]

# ─────────────────────────────── UI STRINGS ───────────────────────────────
UI = {
 "es": dict(
   nav_sectors="Sectores", nav_regions="Regiones", nav_projects="Proyectos",
   nav_about="Nosotros", nav_contact="Contacto", nav_quote="Cotizar", nav_blog="Blog", nav_states="Estados",
   home="Inicio",
   foot_desc="Construcción industrial y estructura de acero para empresas AAA y AA. 45 años de experiencia · ISO 9001:2015.",
   foot_sectors="Sectores", foot_regions="Regiones", foot_contact="Contacto",
   foot_rights="Todos los derechos reservados.", foot_tag="Construcción industrial · ISO 9001:2015",
   foot_cv="Descargar CV de la empresa (PDF)",
   phone_lbl="Tel / WhatsApp", address="Metepec, Estado de México",
   wa_aria="Escríbenos por WhatsApp", wa_label="¿Cotizamos tu proyecto?",
   ai_open="Abrir asistente con inteligencia artificial", ai_title="Asistente IA",
   ai_status="En línea · responde sobre la empresa", ai_close="Cerrar asistente",
   ai_chip1="¿Qué sectores atienden?", ai_chip2="¿En qué regiones trabajan?", ai_chip3="¿Cómo cotizo un proyecto?",
   ai_ph="Escribe tu pregunta…", ai_send="Enviar",
   ai_note='Respuestas generadas por <b>IA</b> · pueden contener imprecisiones',
   # contacto
   c_kicker="Cotiza tu proyecto", c_title="¿Tienes un proyecto industrial en puerta?",
   c_lead="Te asesoramos sin costo ni compromiso. Cuéntanos qué necesitas y te contactamos en menos de 24 horas.",
   c_b1="Respuesta de un ingeniero en menos de 24 h", c_b2="Visita técnica y anteproyecto sin costo",
   c_b3="Procesos certificados ISO 9001:2015",
   c_wa="Escríbenos por WhatsApp", c_mail="Correo",
   f_name="Nombre completo", f_name_ph="Tu nombre", f_company="Empresa", f_company_ph="Nombre de la empresa",
   f_phone="Teléfono / WhatsApp", f_email="Correo electrónico", f_sector="Tipo de proyecto (sector)",
   f_select="Selecciona…", f_other="Otro", f_msg="Cuéntanos de tu proyecto",
   f_msg_ph="Ubicación, tipo de obra, superficie, fechas objetivo…", f_submit="Solicitar cotización",
   seg_client="Cliente", seg_supplier="Proveedor", seg_job="Trabaja con nosotros",
   # secciones
   s_portfolio="Portafolio del sector", s_featured="Proyecto destacado",
   s_build="Qué construimos",
   s_states="Estados que cubrimos", s_focus="Sectores con más presencia",
   s_noproj_kicker="Portafolio en crecimiento",
   s_noproj_title="¿Tienes un proyecto de este tipo?",
   s_noproj_sub="Contamos con la ingeniería y el equipo para tu obra. Cuéntanos qué necesitas y te preparamos un anteproyecto sin costo.",
   s_noproj_btn="Cotizar mi proyecto",
   sector_pre="Sector", coverage_pre="Cobertura",
 ),
 "en": dict(
   nav_sectors="Industries", nav_regions="Regions", nav_projects="Projects",
   nav_about="About us", nav_contact="Contact", nav_quote="Get a quote", nav_blog="Blog", nav_states="States",
   home="Home",
   foot_desc="Industrial construction and structural steel for AAA and AA companies. 45 years of experience · ISO 9001:2015.",
   foot_sectors="Industries", foot_regions="Regions", foot_contact="Contact",
   foot_rights="All rights reserved.", foot_tag="Industrial construction · ISO 9001:2015",
   foot_cv="Download company CV (PDF)",
   phone_lbl="Phone / WhatsApp", address="Metepec, State of Mexico",
   wa_aria="Message us on WhatsApp", wa_label="Shall we quote your project?",
   ai_open="Open the AI assistant", ai_title="AI Assistant",
   ai_status="Online · answers about the company", ai_close="Close assistant",
   ai_chip1="Which industries do you serve?", ai_chip2="Which regions do you cover?", ai_chip3="How do I request a quote?",
   ai_ph="Type your question…", ai_send="Send",
   ai_note='Answers generated by <b>AI</b> · may contain inaccuracies',
   c_kicker="Request a quote", c_title="Do you have an industrial project coming up?",
   c_lead="We advise you at no cost and with no commitment. Tell us what you need and we'll get back to you within 24 hours.",
   c_b1="A reply from an engineer within 24 hours", c_b2="Site visit and preliminary design at no cost",
   c_b3="ISO 9001:2015 certified processes",
   c_wa="Message us on WhatsApp", c_mail="Email",
   f_name="Full name", f_name_ph="Your name", f_company="Company", f_company_ph="Company name",
   f_phone="Phone / WhatsApp", f_email="Email address", f_sector="Project type (industry)",
   f_select="Select…", f_other="Other", f_msg="Tell us about your project",
   f_msg_ph="Location, type of facility, area, target dates…", f_submit="Request a quote",
   seg_client="Client", seg_supplier="Supplier", seg_job="Work with us",
   s_portfolio="Industry portfolio", s_featured="Featured project",
   s_build="What we build",
   s_states="States we cover", s_focus="Industries with the strongest presence",
   s_noproj_kicker="Growing portfolio",
   s_noproj_title="Do you have a project like this?",
   s_noproj_sub="We have the engineering and the team for your build. Tell us what you need and we'll prepare a preliminary design at no cost.",
   s_noproj_btn="Request a quote",
   sector_pre="Industry", coverage_pre="Coverage",
 ),
}

# rutas desde la raíz del sitio, por página y por idioma
def path_of(kind, lang, slug=None):
    if lang == "es":
        return {"home":"index.html","about":"nosotros.html","contact":"contacto.html","blog":"blog.html",
                "sector":f"sectores/{slug}.html","region":f"regiones/{slug}.html"}[kind]
    return {"home":"en/index.html","about":"en/about.html","contact":"en/contact.html","blog":"en/blog.html",
            "sector":f"en/sectors/{slug}.html","region":f"en/regions/{slug}.html"}[kind]

def head(lang, title, desc, base, self_path, alt_path):
    other = "en" if lang == "es" else "es"
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <link rel="canonical" href="{SITE_URL}{self_path}" />
  <link rel="alternate" hreflang="{lang}" href="{SITE_URL}{self_path}" />
  <link rel="alternate" hreflang="{other}" href="{SITE_URL}{alt_path}" />
  <link rel="alternate" hreflang="x-default" href="{SITE_URL}{self_path if lang=='es' else alt_path}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:type" content="website" />
  <meta property="og:locale" content="{'es_MX' if lang=='es' else 'en_US'}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap" />
  <link rel="stylesheet" href="{base}css/styles.css?v=12" />
  <link rel="icon" href="{base}assets/favicon.svg" type="image/svg+xml" />
</head>
<body>'''

def nav(lang, base, alt_path):
    u = UI[lang]
    L = lambda p: base + p
    return f'''  <header class="nav" id="nav">
    <div class="nav__inner container">
      <a href="{L(path_of("home",lang))}" class="brand" aria-label="CAABSA STEEL — {u["home"]}"><img class="brand__logo brand__logo--light" src="{base}assets/logo-grupo-white.png" alt="Grupo CAABSA Steel" width="207" height="46" /><img class="brand__logo brand__logo--dark" src="{base}assets/logo-grupo-dark.png" alt="Grupo CAABSA Steel" width="207" height="46" /></a>
      <nav class="nav__links" id="navLinks">
        <a href="{L(path_of("home",lang))}#sectores">{u["nav_sectors"]}</a>
        <a href="{L(path_of("home",lang))}#regiones">{u["nav_regions"]}</a>
        <a href="{base}{"proyectos/index.html" if lang=="es" else "en/projects/index.html"}">{u["nav_projects"]}</a>
        <a href="{base}{"estados/index.html" if lang=="es" else "en/states/index.html"}">{u["nav_states"]}</a>
        <a href="{L(path_of("blog",lang))}">{u["nav_blog"]}</a>
        <a href="{L(path_of("about",lang))}">{u["nav_about"]}</a>
        <a href="{L(path_of("contact",lang))}">{u["nav_contact"]}</a>
        <a class="langtoggle" href="{base}{alt_path}" hreflang="{'en' if lang=='es' else 'es'}" aria-label="{'View this page in English' if lang=='es' else 'Ver esta página en español'}"><span class="langtoggle__on">{'ES' if lang=='es' else 'EN'}</span><span class="langtoggle__off">{'EN' if lang=='es' else 'ES'}</span></a>
        <a href="{L(path_of("contact",lang))}" class="btn btn--sm btn--primary">{u["nav_quote"]}</a>
      </nav>
      <button class="nav__toggle" id="navToggle" aria-label="{'Abrir menú' if lang=='es' else 'Open menu'}" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </header>'''

def footer(lang, base):
    u = UI[lang]; L = lambda p: base + p
    li='<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M4.98 3.5A2.5 2.5 0 1 1 5 8.5a2.5 2.5 0 0 1 0-5zM3 9h4v12H3zM9 9h3.8v1.7h.05c.53-.95 1.83-1.95 3.75-1.95 4 0 4.75 2.6 4.75 6V21h-4v-5.1c0-1.2-.02-2.75-1.7-2.75s-1.95 1.3-1.95 2.65V21H9z"/></svg>'
    fb='<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M14 9h3V6h-3c-2.2 0-4 1.8-4 4v2H7v3h3v6h3v-6h3l.5-3H13v-2c0-.6.4-1 1-1z"/></svg>'
    ig='<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg>'
    sec = "".join(f'<a href="{L(path_of("sector",lang,s["slug"][lang]))}">{s["name"][lang]}</a>' for s in SECTORS)
    reg = "".join(f'<a href="{L(path_of("region",lang,r["slug"][lang]))}">{r["name"][lang]}</a>' for r in REGIONS)
    return f'''  <footer class="footer">
    <div class="container footer__grid">
      <div>
        <a href="{L(path_of("home",lang))}" class="brand brand--footer"><img class="brand__logo brand__logo--light" src="{base}assets/logo-grupo-white.png" alt="Grupo CAABSA Steel" width="216" height="48" /></a>
        <p class="footer__desc">{u["foot_desc"]}</p>
        <div class="footer__social">
          <a href="https://www.linkedin.com/in/grupo-caabsa-steel-m%C3%A9xico-089055197/" target="_blank" rel="noopener" aria-label="LinkedIn">{li}</a><a href="https://www.facebook.com/caabsasteel/" target="_blank" rel="noopener" aria-label="Facebook">{fb}</a><a href="https://www.instagram.com/caabsasteelmex/" target="_blank" rel="noopener" aria-label="Instagram">{ig}</a>
        </div>
      </div>
      <div class="footer__col"><h4>{u["foot_sectors"]}</h4>{sec}</div>
      <div class="footer__col"><h4>{u["foot_regions"]}</h4>{reg}<a href="{L(path_of("about",lang))}">{u["nav_about"]}</a><a href="{L(path_of("blog",lang))}">{u["nav_blog"]}</a><a href="{base}{"proyectos/index.html" if lang=="es" else "en/projects/index.html"}">{u["nav_projects"]}</a><a href="{base}{"estados/index.html" if lang=="es" else "en/states/index.html"}">{u["nav_states"]}</a></div>
      <div class="footer__col"><h4>{u["foot_contact"]}</h4>
        <a href="tel:+52{WA_NUM[2:]}">{u["phone_lbl"]}: {TEL}</a>
        <a href="mailto:{EMAIL}">{EMAIL}</a>
        <span>{u["address"]}</span>
        <a href="{base}assets/docs/cv-caabsa-steel.pdf" download>{u["foot_cv"]}</a>
      </div>
    </div>
    <div class="footer__bottom container">
      <span>© <span id="year"></span> CAABSA STEEL. {u["foot_rights"]}</span>
      <span>{u["foot_tag"]}</span>
    </div>
  </footer>'''

def wa(lang):
    u = UI[lang]
    return f'''  <a class="wa" href="https://wa.me/{WA_NUM}?text={WA_TXT[lang]}" target="_blank" rel="noopener" aria-label="{u["wa_aria"]}">
    <span class="wa__pulse"></span>
    <svg viewBox="0 0 32 32" width="30" height="30" fill="currentColor"><path d="M16 3C9.4 3 4 8.4 4 15c0 2.1.6 4.1 1.6 5.9L4 29l8.3-1.6C14 28.4 15 28.6 16 28.6 22.6 28.6 28 23.2 28 16.6 28 8.4 22.6 3 16 3zm0 23.3c-1 0-2-.2-2.9-.6l-.4-.2-4.9 1 1-4.8-.3-.4C7.6 19 7.1 17 7.1 15 7.1 10 11 6.1 16 6.1S24.9 10 24.9 15 21 26.3 16 26.3zm5-7.7c-.3-.1-1.7-.8-1.9-.9-.3-.1-.5-.1-.7.1-.2.3-.7.9-.9 1.1-.2.2-.3.2-.6.1-1.6-.8-2.6-1.4-3.7-3.2-.3-.5.3-.5.8-1.5.1-.2 0-.4 0-.5 0-.1-.7-1.6-.9-2.2-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.3 5.2 4.6 2 .8 2.7.9 3.6.8.6-.1 1.7-.7 1.9-1.4.2-.7.2-1.2.2-1.4-.1-.1-.3-.2-.6-.3z"/></svg>
    <span class="wa__label">{u["wa_label"]}</span>
  </a>'''

def chat(lang):
    u = UI[lang]
    return f'''  <button class="ai-fab" id="aiFab" aria-label="{u["ai_open"]}">
    <span class="ai-fab__mark" aria-hidden="true"><svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l1.6 3.9L17.5 8l-3.9 1.6L12 13l-1.6-3.4L6.5 8l3.9-1.1z"/><path d="M18.5 13.5l.8 1.9 1.9.8-1.9.8-.8 1.9-.8-1.9-1.9-.8 1.9-.8z"/></svg></span>
    <span class="ai-fab__dot" aria-hidden="true"></span>
    <span class="ai-fab__label">{'Pregúntale a la IA' if lang=='es' else 'Ask the AI'}</span>
  </button>
  <section class="ai-panel" id="aiPanel" role="dialog" aria-modal="false" aria-label="{u["ai_title"]} CAABSA STEEL" hidden>
    <header class="ai-head">
      <div class="ai-head__avatar" aria-hidden="true"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l1.6 3.9L17.5 8l-3.9 1.6L12 13l-1.6-3.4L6.5 8l3.9-1.1z"/></svg></div>
      <div class="ai-head__meta"><b>{u["ai_title"]}</b><span>{u["ai_status"]}</span></div>
      <button class="ai-head__close" id="aiClose" aria-label="{u["ai_close"]}"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg></button>
    </header>
    <div class="ai-body" id="aiBody" aria-live="polite"></div>
    <div class="ai-chips" id="aiChips">
      <button class="ai-chip">{u["ai_chip1"]}</button>
      <button class="ai-chip">{u["ai_chip2"]}</button>
      <button class="ai-chip">{u["ai_chip3"]}</button>
    </div>
    <footer class="ai-foot">
      <form class="ai-inputwrap" id="aiForm">
        <textarea class="ai-input" id="aiInput" rows="1" maxlength="2000" placeholder="{u["ai_ph"]}" autocomplete="off"></textarea>
        <button type="submit" class="ai-send" id="aiSend" aria-label="{u["ai_send"]}"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12l16-8-6 16-2.5-6.5z"/></svg></button>
      </form>
      <p class="ai-foot__note">{u["ai_note"]}</p>
    </footer>
  </section>'''

def scripts(base):
    return f'''  <script src="{base}js/main.js?v=12"></script>
  <script src="{base}js/chat.js?v=12"></script>
</body>
</html>
'''

def form(lang, sector_default="", simple=True):
    u = UI[lang]
    seg = "" if simple else f'''
        <div class="seg" role="radiogroup" aria-label="{u["c_kicker"]}">
          <input type="radio" name="intent" id="int-cliente" value="cliente" checked /><label for="int-cliente">{u["seg_client"]}</label>
          <input type="radio" name="intent" id="int-proveedor" value="proveedor" /><label for="int-proveedor">{u["seg_supplier"]}</label>
          <input type="radio" name="intent" id="int-empleo" value="empleo" /><label for="int-empleo">{u["seg_job"]}</label>
        </div>'''
    opts = "".join(f'<option{" selected" if sector_default==s["name"][lang] else ""}>{s["name"][lang]}</option>' for s in SECTORS)
    return f'''      <form class="contacto__form reveal" id="leadForm" novalidate>{seg}
        <div class="field"><label for="nombre">{u["f_name"]}</label><input id="nombre" name="nombre" type="text" placeholder="{u["f_name_ph"]}" required /><small class="err"></small></div>
        <div class="field field--half">
          <div><label for="empresa" id="lblEmpresa">{u["f_company"]}</label><input id="empresa" name="empresa" type="text" placeholder="{u["f_company_ph"]}" /><small class="err"></small></div>
          <div><label for="telefono">{u["f_phone"]}</label><input id="telefono" name="telefono" type="tel" placeholder="55 0000 0000" required /><small class="err"></small></div>
        </div>
        <div class="field"><label for="email">{u["f_email"]}</label><input id="email" name="email" type="email" placeholder="you@company.com" required /><small class="err"></small></div>
        <div class="field"><label for="sector">{u["f_sector"]}</label>
          <select id="sector" name="sector"><option value="" disabled {"" if sector_default else "selected"}>{u["f_select"]}</option>{opts}<option>{u["f_other"]}</option></select>
        </div>
        <div class="field"><label for="mensaje" id="lblMensaje">{u["f_msg"]}</label><textarea id="mensaje" name="mensaje" rows="3" placeholder="{u["f_msg_ph"]}"></textarea></div>
        <button type="submit" class="btn btn--primary btn--lg btn--block" id="formSubmit">{u["f_submit"]}</button>
        <p class="form-note" id="formNote" role="status"></p>
      </form>'''

def contact_section(lang, base, sector_default="", simple=True, alt=False):
    u = UI[lang]
    return f'''  <section class="section contacto{'' if not alt else ' section--alt'}" id="contacto">
    <div class="container contacto__grid">
      <div class="contacto__intro reveal">
        <div class="kicker">{u["c_kicker"]}</div>
        <h2 class="h2">{u["c_title"]}</h2>
        <p class="lead">{u["c_lead"]}</p>
        <ul class="contacto__list">
          <li><span class="ci"></span> {u["c_b1"]}</li>
          <li><span class="ci"></span> {u["c_b2"]}</li>
          <li><span class="ci"></span> {u["c_b3"]}</li>
        </ul>
        <div class="contacto__direct">
          <a href="tel:+52{WA_NUM[2:]}" class="direct"><b>{u["phone_lbl"]}</b>{TEL}</a>
          <a href="mailto:{EMAIL}" class="direct"><b>{u["c_mail"]}</b>{EMAIL}</a>
        </div>
        <div style="margin-top:18px"><a href="https://wa.me/{WA_NUM}?text={WA_TXT[lang]}" target="_blank" rel="noopener" class="btn btn--accent">{u["c_wa"]}</a></div>
      </div>
{form(lang, sector_default, simple)}
    </div>
  </section>'''

def page(lang, base, title, desc, self_path, alt_path, body):
    return (head(lang,title,desc,base,self_path,alt_path) + "\n" + nav(lang,base,alt_path) + "\n" +
            body + "\n" + footer(lang,base) + "\n" + wa(lang) + "\n" + chat(lang) + "\n" + scripts(base))

def proj_block(lang, base, proj, alt=False):
    if not proj: return ""
    img, name, meta = proj
    u = UI[lang]
    return f'''  <section class="section{' section--alt' if alt else ''}">
    <div class="container">
      <div class="section-head reveal"><div class="kicker">{u["s_featured"]}</div><h2 class="h2">{name}</h2></div>
      <div class="proyectos__grid" style="grid-template-columns:1fr">
        <article class="proj reveal" style="min-height:420px">
          <div class="proj__media"><img src="{base}{img}" alt="{name}" loading="lazy" /></div>
          <div class="proj__info"><h3>{name}</h3><p>{meta[lang]}</p></div>
        </article>
      </div>
    </div>
  </section>'''

def sector_projects_block(lang, base, sector_key):
    """Lista todos los proyectos del sector; si no hay, muestra el CTA."""
    pu = UI[lang]
    projs = [p for p in PROJECTS if p["sector"] == sector_key]
    if not projs:
        return noproj_block(lang, base)
    cards = "\n".join(f'''        <article class="proj reveal">
          {pmedia(p, base, lang)}
          <div class="proj__info"><span class="chip {CHIP[p["sector"]]}">{STATES[p["state"]]["name"][lang]}</span><h3>{p["client"]}</h3>
          <p>{p["kind"][lang]}{" · "+p["m2"] if p["m2"] else ""}</p>
          <a class="post__more" href="{base}{proj_path(p["slug"],lang)}">{"Ver proyecto →" if lang=="es" else "View project →"}</a></div>
        </article>''' for p in projs)
    n = len(projs)
    title = (f"{n} proyecto{'s' if n>1 else ''} en este sector" if lang=="es"
             else f"{n} project{'s' if n>1 else ''} in this industry")
    return f'''  <section class="section section--alt">
    <div class="container">
      <div class="section-head reveal"><div class="kicker">{pu["s_portfolio"]}</div><h2 class="h2">{title}</h2></div>
      <div class="proyectos__grid">
{cards}
      </div>
    </div>
  </section>'''

def region_projects_block(lang, base, region_key):
    """Lista todos los proyectos de la región (vía sus estados) + enlaces a estados."""
    u = UI[lang]; pu = PUI[lang]
    skeys = [k for k,v in STATES.items() if v["region"] == region_key]
    projs = [p for p in PROJECTS if p["state"] in skeys]
    if not projs:
        return noproj_block(lang, base)
    cards = "\n".join(f'''        <article class="proj reveal">
          {pmedia(p, base, lang)}
          <div class="proj__info"><span class="chip {CHIP[p["sector"]]}">{STATES[p["state"]]["name"][lang]}</span><h3>{p["client"]}</h3>
          <p>{p["kind"][lang]}{" · "+p["m2"] if p["m2"] else ""}</p>
          <a class="post__more" href="{base}{proj_path(p["slug"],lang)}">{"Ver proyecto →" if lang=="es" else "View project →"}</a></div>
        </article>''' for p in projs)
    links = " · ".join(f'<a href="{base}{state_path(k,lang)}">{STATES[k]["name"][lang]}</a>' for k in skeys)
    n = len(projs)
    title = (f"{n} proyecto{'s' if n>1 else ''} en esta región" if lang=="es"
             else f"{n} project{'s' if n>1 else ''} in this region")
    lbl = ("Páginas por estado" if lang=="es" else "Pages by state")
    return f'''  <section class="section section--alt">
    <div class="container">
      <div class="section-head reveal"><div class="kicker">{u["s_portfolio"]}</div><h2 class="h2">{title}</h2>
        <p class="section-head__sub"><b>{lbl}:</b> {links}</p></div>
      <div class="proyectos__grid">
{cards}
      </div>
    </div>
  </section>'''

def noproj_block(lang, base):
    u = UI[lang]
    return f'''  <section class="section section--alt">
    <div class="container center">
      <div class="section-head center reveal"><div class="kicker">{u["s_noproj_kicker"]}</div><h2 class="h2">{u["s_noproj_title"]}</h2><p class="section-head__sub">{u["s_noproj_sub"]}</p></div>
      <div class="reveal"><a href="{base}{path_of("contact",lang)}" class="btn btn--primary btn--lg">{u["s_noproj_btn"]}</a></div>
    </div>
  </section>'''

# ─────────────────────────────── BUILD ───────────────────────────────
def build_lang(lang):
    u = UI[lang]
    depth_sub = 2 if lang == "en" else 1     # sectores/regiones
    depth_root = 1 if lang == "en" else 0    # index/about/contact
    base_sub = "../" * depth_sub
    base_root = "../" * depth_root
    other = "en" if lang == "es" else "es"

    # SECTORES
    for s in SECTORS:
        self_p = path_of("sector", lang, s["slug"][lang])
        alt_p  = path_of("sector", other, s["slug"][other])
        body = f'''  <section class="subhead">
    <div class="subhead__photo" style="background-image:url('{base_sub}{s["photo"]}')"></div>
    <div class="subhead__scrim"></div><div class="subhead__bg"></div>
    <div class="container">
      <div class="breadcrumb"><a href="{base_sub}{path_of("home",lang)}">{u["home"]}</a><span class="sep">/</span><a href="{base_sub}{path_of("home",lang)}#sectores">{u["nav_sectors"]}</a><span class="sep">/</span> {s["name"][lang]}</div>
      <div class="kicker">{u["sector_pre"]} · {s["name"][lang]}</div>
      <h1>{s["h1"][lang]}</h1>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="prose reveal">
        <p style="font-size:1.1rem;color:var(--text)">{s["copy"][lang]}</p>
        <h2>{u["s_build"]}</h2>
        <ul>{"".join(f"<li>{b}</li>" for b in s["build"][lang])}</ul>
      </div>
    </div>
  </section>
{sector_projects_block(lang, base_sub, s["key"])}
{cta_band(lang, base_sub, sector_band_photo(s["key"]), (f"Construimos para el sector {s['name'][lang].lower()}" if lang=="es" else f"We build for the {s['name'][lang].lower()} sector"))}
{contact_section(lang, base_sub, s["name"][lang], simple=True, alt=False)}'''
        html = page(lang, base_sub, f'{s["h1"][lang]} | CAABSA STEEL', s["meta"][lang], self_p, alt_p, body)
        open(os.path.join(ROOT, self_p), "w", encoding="utf-8").write(html)

    # REGIONES
    for r in REGIONS:
        self_p = path_of("region", lang, r["slug"][lang])
        alt_p  = path_of("region", other, r["slug"][other])
        focus = f'<p><b>{u["s_focus"]}:</b> {r["focus"][lang]}.</p>' if r["focus"][lang] else ""
        body = f'''  <section class="subhead">
    <div class="subhead__photo" style="background-image:url('{base_sub}{r["photo"]}')"></div>
    <div class="subhead__scrim"></div><div class="subhead__bg"></div>
    <div class="container">
      <div class="breadcrumb"><a href="{base_sub}{path_of("home",lang)}">{u["home"]}</a><span class="sep">/</span><a href="{base_sub}{path_of("home",lang)}#regiones">{u["nav_regions"]}</a><span class="sep">/</span> {r["name"][lang]}</div>
      <div class="kicker">{u["coverage_pre"]} · {r["name"][lang]}</div>
      <h1>{r["h1"][lang]}</h1>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="prose reveal">
        <p style="font-size:1.1rem;color:var(--text)">{r["copy"][lang]}</p>
        <p><b>{u["s_states"]}:</b> {r["states"][lang]}.</p>
        {focus}
      </div>
    </div>
  </section>
{region_projects_block(lang, base_sub, r["key"])}
{design_band(lang, base_sub, DESIGN_REGION[r["key"]],
   (UI[lang]["coverage_pre"]+" · "+r["name"][lang]),
   ("Construimos donde opera tu industria" if lang=="es" else "We build where your industry operates"),
   ("Naves, plantas y espacios corporativos en "+r["states"][lang]+", con procesos certificados ISO 9001:2015."
    if lang=="es" else
    "Facilities, plants and corporate spaces in "+r["states"][lang]+", under ISO 9001:2015 certified processes.")) if r["key"] in DESIGN_REGION else ""}
{contact_section(lang, base_sub, "", simple=True, alt=False)}'''
        html = page(lang, base_sub, f'{r["h1"][lang]} | CAABSA STEEL', r["meta"][lang], self_p, alt_p, body)
        open(os.path.join(ROOT, self_p), "w", encoding="utf-8").write(html)

    # NOSOTROS / ABOUT
    self_p = path_of("about", lang); alt_p = path_of("about", other)
    A = {"es":dict(
            crumb="Nosotros", kicker="Quiénes somos", h1="45 años construyendo la industria de México",
            intro="CAABSA STEEL es una empresa constructora especializada en obra industrial, con presencia en el centro del país, el Bajío, el occidente y el sur de México. Con 45 años de experiencia, trabajamos con empresas AAA y AA que exigen procesos certificados, cumplimiento de tiempos y calidad constructiva de principio a fin.",
            mision_t="Misión", mision="Somos un equipo de profesionales expertos en la construcción de naves, plantas industriales y edificios comerciales, con presencia sólida en el mercado nacional. Respaldamos a nuestros clientes en costo, tiempo, calidad e innovación — certificados en ISO 9001:2015, asegurando la rentabilidad y el crecimiento a través de la mejora continua.",
            vision_t="Visión", vision="Ser líderes en la construcción de proyectos industriales sustentables, reconocidos por la excelencia, calidad e innovación — superando las expectativas de los inversionistas que confían en nosotros para el desarrollo de México, bajo un modelo de excelencia operativa que nos diferencia en valor, productividad y eficiencia.",
            pol_t="Política de calidad",
            pol="Lograr un crecimiento sostenido en la rentabilidad de cada proyecto, mediante el manejo eficiente de los recursos, la calidad en la ejecución y la mejora continua de nuestro Sistema de Gestión de la Calidad ISO 9001:2015.",
            norm_t="Una empresa confiable, dentro y fuera de la obra",
            norm="Más allá de la calidad constructiva, cumplimos con los requisitos que los grandes corporativos y las empresas AAA y AA exigen a sus proveedores: contamos con registro REPSE vigente, cumplimos con las normas de seguridad e higiene aplicables a obra industrial y respaldamos nuestros proyectos con fianzas que garantizan cumplimiento y calidad. Junto con nuestra certificación ISO 9001:2015, esto permite procesos transparentes y auditables en cada etapa del proyecto.",
            cert_t="Calidad certificada en cada proyecto",
            cert_p="Nuestra certificación ISO 9001:2015 garantiza procesos documentados, control de calidad en cada etapa y mejora continua — el estándar que exigen las empresas AAA y AA.",
            vid_k="Video institucional", vid_t="Conoce cómo trabajamos",
            vid_p="Un recorrido por nuestras obras: fabricación en taller, izaje y montaje de estructura de acero.",
            vid_btn="Ver con sonido", vid_hint="Se reproduce en silencio automáticamente",
            br_k="Documentación", br_t="Nuestra documentación técnica",
            br_s="Todo nuestro historial de obra y nuestras capacidades, listos para tu área de compras o licitaciones.",
            br_btn="Descargar brochure",
            br_role="Puesto o posición", br_role_ph="Ej. Director de Operaciones",
            br_mail="Correo electrónico empresarial", br_mail_hint="Usa el correo de tu empresa; no aceptamos correos personales (gmail, hotmail, etc.).",
            cv_tag="PDF · 54 páginas", cv_t="Currículum de obra",
            cv_p="45 años de trayectoria documentados: cada proyecto con su cliente, ubicación, superficie y alcance, con fotografías de obra. Es el documento que solicitan las áreas de compras y los comités de licitación.",
            cv_l1="Más de 400 proyectos entregados, por sector",
            cv_l2="Clientes AAA y AA: Bosch, Ford, Bridgestone, Coca-Cola FEMSA y más",
            cv_l3="Superficies, tonelajes y alcance de cada obra",
            cv_l4="Certificación ISO 9001:2015 y registros vigentes",
            cv_link="Descargar CV de la empresa",
            cv_note="Descarga directa · 15 MB · sin registro",
            br_tag="PDF · 5 páginas", br_t2="Brochure corporativo",
            br_p="Presentación breve de la empresa, sectores de especialización y capacidades técnicas. Ideal para una primera revisión.",
            title="Nosotros — 45 años de construcción industrial | CAABSA STEEL",
            desc="CAABSA STEEL: 45 años construyendo obra industrial para empresas AAA y AA en el centro, Bajío, occidente y sur de México. Certificación ISO 9001:2015."),
         "en":dict(
            crumb="About us", kicker="Who we are", h1="45 years building Mexico's industry",
            intro="CAABSA STEEL is a construction company specialized in industrial projects, with presence in Central Mexico, the Bajío region, Western Mexico and Southern Mexico. With 45 years of experience, we work with AAA and AA companies that demand certified processes, on-time delivery and construction quality from start to finish.",
            mision_t="Mission", mision="We are a team of professionals specialized in building industrial facilities, plants and commercial buildings, with a solid presence in the national market. We back our clients on cost, schedule, quality and innovation — ISO 9001:2015 certified, securing profitability and growth through continuous improvement.",
            vision_t="Vision", vision="To lead the construction of sustainable industrial projects, recognised for excellence, quality and innovation — exceeding the expectations of the investors who trust us with Mexico's development, under a model of operational excellence that sets us apart in value, productivity and efficiency.",
            pol_t="Quality policy",
            pol="To achieve sustained growth in the profitability of every project through efficient use of resources, quality in execution and continuous improvement of our ISO 9001:2015 Quality Management System.",
            norm_t="A dependable company, on site and off it",
            norm="Beyond construction quality, we meet the requirements major corporations and AAA and AA companies demand of their suppliers: we hold a current REPSE registration, comply with the health and safety standards applicable to industrial construction, and back our projects with bonds guaranteeing performance and quality. Together with our ISO 9001:2015 certification, this allows for transparent, auditable processes at every stage of the project.",
            cert_t="Certified quality on every project",
            cert_p="Our ISO 9001:2015 certification guarantees documented processes, quality control at every stage and continuous improvement — the standard AAA and AA companies require.",
            vid_k="Company video", vid_t="See how we work",
            vid_p="A walkthrough of our projects: shop fabrication, lifting and steel erection on site.",
            vid_btn="Watch with sound", vid_hint="Plays muted automatically",
            br_k="Documentation", br_t="Our technical documentation",
            br_s="Our full project record and capabilities, ready for your procurement or tender team.",
            br_btn="Download brochure",
            br_role="Role or position", br_role_ph="e.g. Operations Director",
            br_mail="Business email address", br_mail_hint="Please use your company email; personal addresses (gmail, hotmail, etc.) are not accepted.",
            cv_tag="PDF · 54 pages", cv_t="Company project record (CV)",
            cv_p="45 years documented: every project with its client, location, floor area and scope, with photographs from site. This is the document procurement departments and tender committees ask for.",
            cv_l1="Over 400 delivered projects, broken down by industry",
            cv_l2="AAA and AA clients: Bosch, Ford, Bridgestone, Coca-Cola FEMSA and more",
            cv_l3="Floor areas, tonnage and scope for each project",
            cv_l4="ISO 9001:2015 certification and current registrations",
            cv_link="Download the company CV",
            cv_note="Direct download · 15 MB · no registration",
            br_tag="PDF · 5 pages", br_t2="Corporate brochure",
            br_p="A short company presentation with our areas of specialization and technical capabilities. Ideal for a first review.",
            title="About us — 45 years of industrial construction | CAABSA STEEL",
            desc="CAABSA STEEL: 45 years building industrial projects for AAA and AA companies in Central Mexico, the Bajío, the west and the south. ISO 9001:2015 certified.")}[lang]
    body = f'''  <section class="subhead">
    <div class="subhead__photo" style="background-image:url('{base_root}images/proyectos/gates/01.jpg')"></div>
    <div class="subhead__scrim"></div><div class="subhead__bg"></div>
    <div class="container">
      <div class="breadcrumb"><a href="{base_root}{path_of("home",lang)}">{u["home"]}</a><span class="sep">/</span> {A["crumb"]}</div>
      <div class="kicker">{A["kicker"]}</div>
      <h1>{A["h1"]}</h1>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="prose reveal">
        <p style="font-size:1.12rem;color:var(--text)">{A["intro"]}</p>
        <h2>{A["mision_t"]}</h2><p>{A["mision"]}</p>
        <h2>{A["vision_t"]}</h2><p>{A["vision"]}</p>
      </div>
      <div class="cert reveal" style="margin-top:36px">
        <img class="cert__seal-img" src="{base_root}assets/iso-9001-bv.png" alt="Certificado ISO 9001:2015 · Bureau Veritas" width="300" height="120" loading="lazy" />
        <div class="cert__txt"><b>{A["cert_t"]}</b><p>{A["cert_p"]}</p></div>
      </div>
      <div class="prose reveal" style="margin-top:36px">
        <h2>{A["pol_t"]}</h2><p>{A["pol"]}</p>
        <h2>{A["norm_t"]}</h2><p>{A["norm"]}</p>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="section-head center reveal">
        <div class="kicker">{"El equipo" if lang=="es" else "The team"}</div>
        <h2 class="h2">{"Detrás de cada obra hay un equipo" if lang=="es" else "Behind every project there is a team"}</h2>
        <p class="section-head__sub">{"Ingeniería, taller y obra trabajando bajo un mismo sistema de calidad." if lang=="es" else "Engineering, workshop and site teams working under a single quality system."}</p>
      </div>
      <img class="reveal" src="{base_root}{TEAM_PHOTO}" alt="{"Equipo de CAABSA STEEL" if lang=="es" else "The CAABSA STEEL team"}" loading="lazy" style="width:100%;border-radius:var(--radius);box-shadow:var(--shadow)" />
    </div>
  </section>

  <div class="videoband" id="video">
    <video class="videoband__media" id="corpVideo" autoplay muted loop playsinline preload="metadata" poster="{base_root}assets/video/poster.jpg"><source src="{base_root}assets/video/caabsa-corporativo.mp4" type="video/mp4" /></video>
    <div class="videoband__overlay"></div>
    <div class="videoband__content reveal">
      <div class="kicker">{A["vid_k"]}</div><h2 class="h2">{A["vid_t"]}</h2><p>{A["vid_p"]}</p>
      <div class="videoband__cta"><button class="btn btn--primary" id="videoSound" type="button"><svg class="videoband__sound-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 5 6 9H2v6h4l5 4z"/><path d="M15.5 8.5a5 5 0 0 1 0 7"/><path d="M18.5 5.5a9 9 0 0 1 0 13"/></svg> {A["vid_btn"]}</button><span class="videoband__hint">{A["vid_hint"]}</span></div>
    </div>
  </div>

  <section class="section section--alt" id="documentos">
    <div class="container">
      <div class="section-head center reveal"><div class="kicker">{A["br_k"]}</div><h2 class="h2">{A["br_t"]}</h2><p class="section-head__sub">{A["br_s"]}</p></div>
      <div class="docs__grid">

        <article class="doccard doccard--feat reveal">
          <div class="doccard__top">
            <span class="doccard__ic">{DOC_IC}</span>
            <span class="doccard__tag doccard__tag--feat">{A["cv_tag"]}</span>
          </div>
          <h3 class="doccard__t">{A["cv_t"]}</h3>
          <p class="doccard__p">{A["cv_p"]}</p>
          <ul class="doccard__list">
            <li>{A["cv_l1"]}</li><li>{A["cv_l2"]}</li><li>{A["cv_l3"]}</li><li>{A["cv_l4"]}</li>
          </ul>
          <a class="btn btn--primary btn--lg btn--block doccard__btn" href="{base_root}assets/docs/cv-caabsa-steel.pdf" download>{DL_IC}{A["cv_link"]}</a>
          <p class="doccard__note">{A["cv_note"]}</p>
        </article>

        <article class="doccard reveal reveal-d1">
          <div class="doccard__top">
            <span class="doccard__ic doccard__ic--soft">{DOC_IC}</span>
            <span class="doccard__tag">{A["br_tag"]}</span>
          </div>
          <h3 class="doccard__t">{A["br_t2"]}</h3>
          <p class="doccard__p">{A["br_p"]}</p>
          <form class="contacto__form" id="brochureForm" novalidate data-file="{base_root}assets/docs/brochure-caabsa-steel-2026.pdf">
            <div class="field"><label for="bnombre">{u["f_name"]}</label><input id="bnombre" name="nombre" type="text" placeholder="{u["f_name_ph"]}" required /><small class="err"></small></div>
            <div class="field"><label for="bempresa">{u["f_company"]}</label><input id="bempresa" name="empresa" type="text" placeholder="{u["f_company_ph"]}" required /><small class="err"></small></div>
            <div class="field"><label for="bpuesto">{A["br_role"]}</label><input id="bpuesto" name="puesto" type="text" placeholder="{A["br_role_ph"]}" required /><small class="err"></small></div>
            <div class="field"><label for="bemail">{A["br_mail"]}</label><input id="bemail" name="email" type="email" placeholder="nombre@empresa.com" required /><small class="err"></small>
              <small class="field__hint">{A["br_mail_hint"]}</small></div>
            <button type="submit" class="btn btn--ghost btn--block" id="brochureSubmit">{A["br_btn"]}</button>
            <p class="form-note" id="brochureNote" role="status"></p>
          </form>
        </article>

      </div>
    </div>
  </section>'''
    open(os.path.join(ROOT, self_p),"w",encoding="utf-8").write(
        page(lang, base_root, A["title"], A["desc"], self_p, alt_p, body))

    # CONTACTO / CONTACT
    self_p = path_of("contact", lang); alt_p = path_of("contact", other)
    C = {"es":dict(crumb="Contacto", h1="Hablemos de tu próximo proyecto",
            lead="Te asesoramos en tu próximo proyecto industrial sin costo ni compromiso. Cuéntanos qué necesitas y te ayudamos a definirlo.",
            k="Datos de contacto", t="Estamos en Metepec, operamos en el centro, Bajío, occidente y sur",
            addr_lbl="Dirección", addr="Vicente Guerrero 2800, Col. Francisco I. Madero, 52172 Toluca de Lerdo, Estado de México",
            title="Contacto — Cotiza tu proyecto industrial | CAABSA STEEL",
            desc="Contacta a CAABSA STEEL para tu proyecto de construcción industrial. Asesoría sin costo. Metepec, Estado de México. Tel/WhatsApp 722 523 2020."),
         "en":dict(crumb="Contact", h1="Let's talk about your next project",
            lead="We advise you on your next industrial project at no cost and with no commitment. Tell us what you need and we'll help you define it.",
            k="Contact details", t="Based in Metepec, serving Central Mexico, the Bajío, the west and the south",
            addr_lbl="Address", addr="Vicente Guerrero 2800, Col. Francisco I. Madero, 52172 Toluca de Lerdo, State of Mexico",
            title="Contact — Request a quote for your industrial project | CAABSA STEEL",
            desc="Contact CAABSA STEEL for your industrial construction project. Free consultation. Metepec, State of Mexico. Phone/WhatsApp +52 722 523 2020.")}[lang]
    body = f'''  <section class="subhead">
    <div class="subhead__bg"></div>
    <div class="container">
      <div class="breadcrumb"><a href="{base_root}{path_of("home",lang)}">{u["home"]}</a><span class="sep">/</span> {C["crumb"]}</div>
      <div class="kicker">{C["crumb"]}</div>
      <h1>{C["h1"]}</h1>
      <p class="lead">{C["lead"]}</p>
    </div>
  </section>

  <section class="section contacto">
    <div class="container contacto__grid">
      <div class="contacto__intro reveal">
        <div class="kicker">{C["k"]}</div>
        <h2 class="h2">{C["t"]}</h2>
        <ul class="contacto__list">
          <li><span class="ci"></span> {u["c_b1"]}</li>
          <li><span class="ci"></span> {u["c_b2"]}</li>
          <li><span class="ci"></span> {u["c_b3"]}</li>
        </ul>
        <div class="contacto__direct">
          <a href="tel:+52{WA_NUM[2:]}" class="direct"><b>{u["phone_lbl"]}</b>{TEL}</a>
          <a href="mailto:{EMAIL}" class="direct"><b>{u["c_mail"]}</b>{EMAIL}</a>
          <span class="direct"><b>{C["addr_lbl"]}</b>{C["addr"]}</span>
        </div>
        <div style="margin-top:16px"><a href="https://wa.me/{WA_NUM}?text={WA_TXT[lang]}" target="_blank" rel="noopener" class="btn btn--accent">{u["c_wa"]}</a></div>
        <iframe class="map-embed" style="margin-top:22px" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="CAABSA STEEL — Metepec" src="https://www.google.com/maps?q=Vicente+Guerrero+2800%2C+Madero%2C+52172+Toluca+de+Lerdo%2C+M%C3%A9x.&output=embed"></iframe>
      </div>
{form(lang, "", simple=False)}
    </div>
  </section>'''
    open(os.path.join(ROOT, self_p),"w",encoding="utf-8").write(
        page(lang, base_root, C["title"], C["desc"], self_p, alt_p, body))

    # HOME
    self_p = path_of("home", lang); alt_p = path_of("home", other)
    H = {"es":dict(
            eyebrow="Construcción industrial &middot; ISO 9001:2015",
            h1='Construcción Industrial para Corporativos y Empresas <span class="grad">AAA y AA</span>',
            sub="Naves industriales, plantas y edificios comerciales en el centro de México, el Bajío, el occidente y el sur. Respaldamos a nuestros clientes en costo, tiempo, calidad e innovación. Certificados ISO 9001:2015.",
            cta1="Solicita una cotización", cta2="Descarga nuestro brochure",
            m1="años de experiencia", m2="m² construidos", m3="toneladas de acero", m4="proyectos entregados",
            cert_t="Calidad certificada en cada proyecto",
            cert_p="Contamos con certificación ISO 9001:2015: procesos documentados, control de calidad en cada etapa y cumplimiento con los estándares que exigen las empresas AAA y AA.",
            sec_k="Sectores", sec_t="Construimos para la industria que mueve México",
            sec_s="Cada sector exige normas, tiempos y acabados distintos. Los dominamos.",
            badges=["ISO 9001:2015","Registro REPSE vigente","Fianzas de cumplimiento y calidad","Normas de seguridad e higiene en obra"],
            reg_k="Cobertura", reg_t="Presencia en el centro del país, el Bajío, el occidente y el sur",
            reg_s="Nos encuentran desde cualquier estado donde operen. Estas son las regiones que atendemos.",
            reg_cta="Ver proyectos en la región →",
            st_k="Nuestro respaldo", st_t="Cifras que sostienen cada proyecto",
            st1="de experiencia", st2="m² construidos", st3="toneladas de acero", st4="proyectos entregados",
            pr_k="Portafolio", pr_t="Últimos proyectos",
            band_k="De la cimentación al último tornillo", band_t="45 años construyendo la industria de México",
            band_p="Naves, plantas y espacios corporativos en acero, con calidad certificada ISO 9001:2015 para empresas AAA y AA.",
            band_btn="Cotiza tu proyecto",
            rv_k="Lo que dicen nuestros clientes", rv_t="Cartas de recomendación de quienes ya construyeron con nosotros",
            cvb_k="Currículum de obra", cvb_t="45 años de obra industrial, en un solo documento",
            cvb_p="Nuestro currículum reúne más de 400 proyectos entregados: cada uno con su cliente, ubicación, superficie y alcance, con fotografías de obra. Es el documento que piden las áreas de compras y los comités de licitación.",
            cvb_btn="Descargar CV de la empresa",
            cvb_meta="PDF · 54 páginas · descarga directa, sin registro",
            cvb_alt="Ver también el brochure corporativo",
            vid_k="Video corporativo", vid_t="CAABSA STEEL en movimiento",
            vid_p="Un recorrido por nuestras obras: fabricación en taller, izaje y montaje de estructura de acero.",
            vid_btn="Ver con sonido", vid_hint="Se reproduce en silencio automáticamente",
            sector_more="Ver más →",
            title="CAABSA STEEL — Construcción industrial para empresas AAA y AA | Centro, Bajío, Occidente y Sur",
            desc="Constructora industrial con 45 años de experiencia. Naves, plantas y espacios corporativos para empresas AAA y AA en el centro de México, Bajío, occidente y sur. ISO 9001:2015."),
         "en":dict(
            eyebrow="Industrial construction &middot; ISO 9001:2015",
            h1='Industrial Construction for Corporations and <span class="grad">AAA and AA</span> Companies',
            sub="Industrial facilities, plants and commercial buildings across Central Mexico, the Bajío, the west and the south. We back our clients on cost, schedule, quality and innovation. ISO 9001:2015 certified.",
            cta1="Request a quote", cta2="Download our brochure",
            m1="years of experience", m2="m² built", m3="tons of steel", m4="projects delivered",
            cert_t="Certified quality on every project",
            cert_p="We hold ISO 9001:2015 certification: documented processes, quality control at every stage and compliance with the standards AAA and AA companies require.",
            sec_k="Industries", sec_t="We build for the industries that move Mexico",
            sec_s="Every industry demands different standards, schedules and finishes. We know them all.",
            badges=["ISO 9001:2015","Current REPSE registration","Performance and quality bonds","On-site health and safety standards"],
            reg_k="Coverage", reg_t="Presence in Central Mexico, the Bajío, the west and the south",
            reg_s="Reach us from any state where you operate. These are the regions we serve.",
            reg_cta="View projects in this region →",
            st_k="Our track record", st_t="The numbers behind every project",
            st1="of experience", st2="m² built", st3="tons of steel", st4="projects delivered",
            pr_k="Portfolio", pr_t="Latest projects",
            band_k="From the foundation to the last bolt", band_t="45 years building Mexico's industry",
            band_p="Steel facilities, plants and corporate spaces, with ISO 9001:2015 certified quality for AAA and AA companies.",
            band_btn="Request a quote",
            rv_k="What our clients say", rv_t="Recommendation letters from companies that have built with us",
            cvb_k="Project record", cvb_t="45 years of industrial construction, in a single document",
            cvb_p="Our company CV brings together more than 400 delivered projects: each one with its client, location, floor area and scope, with photographs from site. This is the document procurement departments and tender committees ask for.",
            cvb_btn="Download the company CV",
            cvb_meta="PDF · 54 pages · direct download, no registration",
            cvb_alt="See the corporate brochure as well",
            vid_k="Company video", vid_t="CAABSA STEEL in motion",
            vid_p="A walkthrough of our projects: shop fabrication, lifting and steel erection on site.",
            vid_btn="Watch with sound", vid_hint="Plays muted automatically",
            sector_more="Learn more →",
            title="CAABSA STEEL — Industrial construction for AAA and AA companies | Central Mexico, Bajío, West & South",
            desc="Industrial construction company with 45 years of experience. Facilities, plants and corporate spaces for AAA and AA companies in Central Mexico, the Bajío, the west and the south. ISO 9001:2015.")}[lang]

    ICONS = {
     "automotive":'<svg viewBox="0 0 48 48"><path d="M6 30l4-11a5 5 0 0 1 4.7-3.4h18.6A5 5 0 0 1 38 19l4 11" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M6 30h36v6a2 2 0 0 1-2 2h-3a2 2 0 0 1-2-2v-2H13v2a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2z" fill="none" stroke="currentColor" stroke-width="2.2"/><circle cx="14" cy="30" r="2.5" fill="var(--accent)"/><circle cx="34" cy="30" r="2.5" fill="var(--accent)"/></svg>',
     "food":'<svg viewBox="0 0 48 48"><path d="M14 6v14a4 4 0 0 0 8 0V6M18 6v36" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M34 6c-4 0-6 4-6 10s2 8 6 8v18" fill="none" stroke="currentColor" stroke-width="2.2"/><circle cx="18" cy="26" r="2" fill="var(--accent)"/></svg>',
     "logistics":'<svg viewBox="0 0 48 48"><path d="M6 34V16l12-6 12 6v18" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M6 34h36V22l-8-4" fill="none" stroke="currentColor" stroke-width="2.2"/><rect x="14" y="24" width="8" height="10" fill="none" stroke="var(--accent)" stroke-width="2.2"/></svg>',
     "corporate":'<svg viewBox="0 0 48 48"><rect x="10" y="6" width="20" height="36" rx="2" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M30 18h8v24h-8" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M16 14h8M16 22h8M16 30h8" stroke="var(--accent)" stroke-width="2.2"/></svg>',
     "pharma":'<svg viewBox="0 0 48 48"><rect x="19" y="6" width="10" height="13" rx="2" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M24 19v7m-7 0h14l4 12a2 2 0 0 1-2 2.6H15a2 2 0 0 1-2-2.6z" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M20 33h8" stroke="var(--accent)" stroke-width="2.6"/></svg>',
     "industrial":'<svg viewBox="0 0 48 48"><path d="M6 40V22l10 6V22l10 6V14l16 10v16z" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/><path d="M6 40h36" stroke="currentColor" stroke-width="2.2"/><rect x="30" y="30" width="6" height="10" fill="var(--accent)"/></svg>',
     "aerospace":'<svg viewBox="0 0 48 48"><path d="M4 26l40-12-8 16-10-2-6 10-3-8z" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/><circle cx="34" cy="18" r="2" fill="var(--accent)"/></svg>',
    }
    sect_cards = "\n".join(f'''        <a class="sector reveal" href="{base_root}{path_of("sector",lang,s["slug"][lang])}">
          <div class="sector__icon">{ICONS[s["key"]]}</div>
          <h3>{s["name"][lang]}</h3><p>{s["summary"][lang]}</p>
          <span class="sector__arrow">{H["sector_more"]}</span>
        </a>''' for s in SECTORS)
    reg_cards = "\n".join(f'''        <a class="region-card reveal" href="{base_root}{path_of("region",lang,r["slug"][lang])}">
          <h3>{r["name"][lang]}</h3><p>{r["summary"][lang]}</p>
          <span class="region-card__states">{H["reg_cta"]}</span>
        </a>''' for r in REGIONS)

    PROJ = [
     ("images/proyectos/martinrea-honsel/01.jpg","chip--auto","automotive","Martinrea Honsel",
      {"es":"Planta de autopartes · edificio administrativo","en":"Auto-parts plant · administrative building"}),
     ("images/proyectos/gates/01.jpg","chip--auto","automotive","Gates",
      {"es":"Ampliación de nave en producción · 1,500 m²","en":"Expansion of an operating facility · 1,500 m²"}),
     ("images/proyectos/la-moderna/01.jpg","chip--log","logistics","La Moderna",
      {"es":"Centro de distribución · gran claro y andenes","en":"Distribution center · long-span with loading docks"}),
     ("images/proyectos/jugos-del-valle/01.jpg","chip--food","food","Jugos del Valle",
      {"es":"Planta de bebidas · nave de proceso","en":"Beverage plant · process building"}),
     ("images/proyectos/tintas-sanchez/01.jpg","chip--corp","corporate","Grupo Sánchez",
      {"es":"Complejo llave en mano · 25,000 m² con oficinas","en":"Turnkey complex · 25,000 m² with offices"}),
     ("images/proyectos/espejos-inteligentes/01.jpg","chip--auto","automotive","Espejos Inteligentes",
      {"es":"Ampliación de nave y almacén · 2,500 m²","en":"Facility and warehouse expansion · 2,500 m²"}),
    ]
    name_of = {s["key"]: s["name"][lang] for s in SECTORS}
    proj_cards = "\n".join(f'''        <article class="proj reveal">
          <div class="proj__media"><img src="{base_root}{p[0]}" alt="{p[3]}" loading="lazy" /></div>
          <div class="proj__info"><span class="chip {p[1]}">{name_of[p[2]]}</span><h3>{p[3]}</h3><p>{p[4][lang]}</p></div>
        </article>''' for p in PROJ)

    def initials(nm):
        parts=[x for x in nm.replace("Ing.","").replace("Lic.","").replace("C.P.","").split() if x]
        return (parts[0][0]+ (parts[1][0] if len(parts)>1 else "")).upper()
    rev_cards = "\n".join(f'''        <div class="review reveal"><div class="review__stars">★★★★★</div>
          <p class="review__text">"{r["text"][lang]}"</p>
          <div class="review__who"><div class="review__ava">{initials(r["who"])}</div><div><b>{r["who"]}</b><span>{r["role"][lang]} · {r["client"]}</span></div></div>
        </div>''' for r in REVIEWS_REAL)

    body = f'''  <section class="hero" id="inicio">
    <div class="hero__bg" aria-hidden="true">
      <div class="hero__photo" data-parallax="0.14" style="background-image:url('{base_root}images/proyectos/gates/01.jpg')"></div>
      <div class="grid-layer" data-parallax="0.22"></div>
      <div class="blueprint-layer" data-parallax="0.3"><svg class="blueprint" viewBox="0 0 1440 900" preserveAspectRatio="xMidYMid slice">
        <defs><linearGradient id="beam" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="var(--primary-2)" stop-opacity="0.9"/><stop offset="1" stop-color="var(--primary-2)" stop-opacity="0.15"/></linearGradient></defs>
        <g class="wire" stroke="url(#beam)" fill="none" stroke-width="1.4">
          <path class="draw" d="M120 780 L120 380 L720 140 L1320 380 L1320 780"/>
          <path class="draw" d="M260 780 L260 430 L720 235 L1180 430 L1180 780"/>
          <path class="draw" d="M120 380 L1320 380"/><path class="draw" d="M260 430 L1180 430"/>
          <path class="draw" d="M120 560 L1320 560"/><path class="draw" d="M120 700 L1320 700"/>
          <path class="draw" d="M420 780 L420 300"/><path class="draw" d="M620 780 L620 210"/>
          <path class="draw" d="M820 780 L820 210"/><path class="draw" d="M1020 780 L1020 300"/>
          <path class="draw thin" d="M260 560 L420 430 M420 560 L620 430 M620 560 L820 430 M820 560 L1020 430 M1020 560 L1180 430"/>
        </g>
        <g class="nodes" fill="var(--accent)"><circle cx="720" cy="140" r="4"/><circle cx="120" cy="380" r="3"/><circle cx="1320" cy="380" r="3"/><circle cx="420" cy="430" r="2.5"/><circle cx="820" cy="430" r="2.5"/></g>
      </svg></div>
      <div class="hero__scrim"></div>
    </div>
    <div class="hero__content container">
      <div class="eyebrow reveal"><span class="pulse"></span> {H["eyebrow"]}</div>
      <h1 class="hero__title reveal">{H["h1"]}</h1>
      <p class="hero__sub reveal">{H["sub"]}</p>
      <div class="hero__cta reveal">
        <a href="{base_root}{path_of("contact",lang)}" class="btn btn--primary btn--lg">{H["cta1"]}</a>
        <a href="{base_root}{path_of("about",lang)}#brochure" class="btn btn--on-dark btn--lg">{H["cta2"]}</a>
      </div>
      <div class="hero__mini reveal">
        <div><b>45</b><span>{H["m1"]}</span></div><div class="sep"></div>
        <div><b>+1.6M</b><span>{H["m2"]}</span></div><div class="sep"></div>
        <div><b>+80k</b><span>{H["m3"]}</span></div><div class="sep"></div>
        <div><b>+400</b><span>{H["m4"]}</span></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="cert reveal">
        <img class="cert__seal-img" src="{base_root}assets/iso-9001-bv.png" alt="Certificado ISO 9001:2015 · Bureau Veritas" width="300" height="120" loading="lazy" />
        <div class="cert__txt"><b>{H["cert_t"]}</b><p>{H["cert_p"]}</p></div>
      </div>
    </div>
  </section>

{clients_marquee(lang, base_root)}

  <section class="section section--alt" id="sectores">
    <div class="container">
      <div class="section-head center reveal"><div class="kicker">{H["sec_k"]}</div><h2 class="h2">{H["sec_t"]}</h2><p class="section-head__sub">{H["sec_s"]}</p>
        <div class="badges">{"".join(f'<span class="badge">{b}</span>' for b in H["badges"])}</div>
      </div>
      <div class="sectores__grid">
{sect_cards}
      </div>
    </div>
  </section>

  <section class="section" id="regiones">
    <div class="container">
      <div class="section-head center reveal"><div class="kicker">{H["reg_k"]}</div><h2 class="h2">{H["reg_t"]}</h2><p class="section-head__sub">{H["reg_s"]}</p></div>
      <div class="regions__grid">
{reg_cards}
      </div>
    </div>
  </section>

  <section class="section stats pbg" id="cifras" style="background-image:url('{base_root}images/proyectos/la-moderna/01.jpg')">
    <div class="container">
      <div class="section-head center reveal"><div class="kicker">{H["st_k"]}</div><h2 class="h2">{H["st_t"]}</h2></div>
      <div class="stats__grid">
        <div class="stat reveal"><div class="stat__num" data-count="45" data-suffix="{' años' if lang=='es' else ' yrs'}">0</div><div class="stat__label">{H["st1"]}</div><div class="stat__bar"><i></i></div></div>
        <div class="stat reveal"><div class="stat__num" data-count="1600000" data-suffix="+">0</div><div class="stat__label">{H["st2"]}</div><div class="stat__bar"><i></i></div></div>
        <div class="stat reveal"><div class="stat__num" data-count="80000" data-suffix="+">0</div><div class="stat__label">{H["st3"]}</div><div class="stat__bar"><i></i></div></div>
        <div class="stat reveal"><div class="stat__num" data-count="400" data-suffix="+">0</div><div class="stat__label">{H["st4"]}</div><div class="stat__bar"><i></i></div></div>
      </div>
    </div>
  </section>

  <section class="section section--alt" id="proyectos">
    <div class="container">
      <div class="section-head reveal"><div class="kicker">{H["pr_k"]}</div><h2 class="h2">{H["pr_t"]}</h2></div>
      <div class="proyectos__grid">
{proj_cards}
      </div>
    </div>
  </section>

  <div class="pband" style="background-image:url('{base_root}images/proyectos/espejos-inteligentes/01.jpg')">
    <div class="pband__content">
      <div class="kicker">{H["band_k"]}</div>
      <h2 class="h2">{H["band_t"]}</h2>
      <p>{H["band_p"]}</p>
      <a href="{base_root}{path_of("contact",lang)}" class="btn btn--primary btn--lg">{H["band_btn"]}</a>
    </div>
  </div>

  <section class="section" id="resenas">
    <div class="container">
      <div class="section-head center reveal"><div class="kicker">{H["rv_k"]}</div><h2 class="h2">{H["rv_t"]}</h2></div>
      <div class="reviews__grid">
{rev_cards}
      </div>
    </div>
  </section>

  <section class="section cvband" id="cv">
    <div class="container">
      <div class="cvband__box reveal">
        <div class="cvband__main">
          <div class="kicker">{H["cvb_k"]}</div>
          <h2 class="h2">{H["cvb_t"]}</h2>
          <p class="cvband__p">{H["cvb_p"]}</p>
        </div>
        <div class="cvband__side">
          <a class="btn btn--primary btn--lg cvband__btn" href="{base_root}assets/docs/cv-caabsa-steel.pdf" download>{DL_IC}{H["cvb_btn"]}</a>
          <span class="cvband__meta">{H["cvb_meta"]}</span>
          <a class="cvband__alt" href="{base_root}{path_of("about",lang)}#documentos">{H["cvb_alt"]} &rarr;</a>
        </div>
      </div>
    </div>
  </section>

  <div class="videoband" id="video">
    <video class="videoband__media" id="corpVideo" autoplay muted loop playsinline preload="metadata" poster="{base_root}assets/video/poster.jpg"><source src="{base_root}assets/video/caabsa-corporativo.mp4" type="video/mp4" /></video>
    <div class="videoband__overlay"></div>
    <div class="videoband__content reveal">
      <div class="kicker">{H["vid_k"]}</div><h2 class="h2">{H["vid_t"]}</h2><p>{H["vid_p"]}</p>
      <div class="videoband__cta"><button class="btn btn--primary" id="videoSound" type="button"><svg class="videoband__sound-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 5 6 9H2v6h4l5 4z"/><path d="M15.5 8.5a5 5 0 0 1 0 7"/><path d="M18.5 5.5a9 9 0 0 1 0 13"/></svg> {H["vid_btn"]}</button><span class="videoband__hint">{H["vid_hint"]}</span></div>
    </div>
  </div>

{contact_section(lang, base_root, "", simple=True, alt=False)}'''
    open(os.path.join(ROOT, self_p),"w",encoding="utf-8").write(
        page(lang, base_root, H["title"], H["desc"], self_p, alt_p, body))

import json as _json, importlib.util as _ilu
_SD = os.path.dirname(os.path.abspath(__file__))
ART_ES = _json.load(open(os.path.join(_SD,"blog_es.json"), encoding="utf-8"))
_spec = _ilu.spec_from_file_location("blog_en", os.path.join(_SD,"blog_en.py"))
BEN = _ilu.module_from_spec(_spec); _spec.loader.exec_module(BEN)

import re as _re2
def fix_colon(t):
    """Corrige dos puntos sin espacio del documento original (respeta ISO 9001:2015)."""
    return _re2.sub(r'(?<=[a-záéíóúñ]):(?=[A-ZÁÉÍÓÚÑ])', ': ', t)

def art_title(key, lang):
    return fix_colon((ART_ES[key] if lang=="es" else BEN.EN[key])[0])

def art_path(key, lang):
    return (f'blog/{BEN.META[key]["slug"]["es"]}.html' if lang=="es"
            else f'en/blog/{BEN.META[key]["slug"]["en"]}.html')

def build_articles(lang):
    """Páginas de artículo con el texto real del documento del cliente."""
    u = UI[lang]; other = "en" if lang=="es" else "es"
    base = "../" if lang=="es" else "../../"
    os.makedirs(os.path.join(ROOT, "blog" if lang=="es" else "en/blog"), exist_ok=True)
    for key in BEN.ORDER:
        M = BEN.META[key]; st = BEN.STRUCT[key]
        paras = [fix_colon(t) for t in (ART_ES[key] if lang=="es" else BEN.EN[key])]
        title = paras[0]
        blocks, buf = [], []
        def flush():
            if buf: blocks.append("<ul>" + "".join(f"<li>{x}</li>" for x in buf) + "</ul>"); buf.clear()
        for i, t in enumerate(paras):
            if i == 0 or i in st["drop"] or not t.strip(): continue
            if i in st["h2"]: flush(); blocks.append(f"<h2>{t}</h2>")
            elif i in st["li"]: buf.append(t)
            else: flush(); blocks.append(f"<p>{t}</p>")
        flush()
        article = "\n        ".join(blocks)
        self_p = art_path(key, lang); alt_p = art_path(key, other)
        gimgs = M.get("gallery") or []
        gal = ("" if not gimgs else
          '<div class="artgal">' + "".join(
            f'<img src="{base}images/proyectos/{g}" alt="{title}" loading="lazy" />' for g in gimgs) + "</div>")
        back = ("Volver al blog" if lang=="es" else "Back to the blog")
        body = f'''  <section class="subhead">
    <div class="subhead__photo" style="background-image:url(\'{base}{M["photo"]}\')"></div>
    <div class="subhead__scrim"></div><div class="subhead__bg"></div>
    <div class="container">
      <div class="breadcrumb"><a href="{base}{path_of("home",lang)}">{u["home"]}</a><span class="sep">/</span><a href="{base}{path_of("blog",lang)}">{u["nav_blog"]}</a><span class="sep">/</span> {M["cat"][lang]}</div>
      <div class="kicker">{M["cat"][lang]} · {M["meta_lbl"][lang]}</div>
      <h1>{title}</h1>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="prose reveal">
        {article}
      </div>
      {gal}
      <p style="margin-top:30px"><a class="post__more" href="{base}{path_of("blog",lang)}">← {back}</a></p>
    </div>
  </section>

{cta_band(lang, base, M.get("photo"))}
{contact_section(lang, base, "", simple=True, alt=True)}
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":"{title}","description":"{M["desc"][lang]}","inLanguage":"{lang}","author":{{"@type":"Organization","name":"CAABSA STEEL"}},"publisher":{{"@type":"Organization","name":"CAABSA STEEL"}}}}</script>'''
        open(os.path.join(ROOT, self_p), "w", encoding="utf-8").write(
            page(lang, base, f"{title} | CAABSA STEEL", M["desc"][lang], self_p, alt_p, body))

POSTS = [
 ("images/proyectos/martinrea-honsel/03.jpg","chip--auto","automotive",
  {"es":"Cuernavaca, Morelos","en":"Cuernavaca, Morelos"},
  {"es":"Ingeniería subterránea al servicio de una llantera",
   "en":"Underground engineering for a tire manufacturing plant"},
  {"es":"Edificio industrial de 5 niveles con 3 sótanos, muros milán y grúa viajera para una planta de fabricación de llantas.",
   "en":"A five-level industrial building with three basement levels, diaphragm walls and an overhead traveling crane for a tire plant."}),
 ("images/proyectos/la-moderna/02.jpg","chip--log","logistics",
  {"es":"Calidad certificada ISO 9001:2015","en":"ISO 9001:2015 certified quality"},
  {"es":"Centros logísticos de alto rendimiento",
   "en":"High-performance logistics centers"},
  {"es":"Planeación, precisión y calidad en la construcción de naves de distribución que operan como un reloj desde el día uno.",
   "en":"Planning, precision and quality in distribution facilities that run like clockwork from day one."}),
 ("images/proyectos/tintas-sanchez/03.jpg","chip--corp","corporate",
  {"es":"Proyecto llave en mano","en":"Turnkey project"},
  {"es":"Complejo industrial de 25,000 m² para Grupo Sánchez",
   "en":"25,000 m² industrial complex for Grupo Sánchez"},
  {"es":"Producción, almacén, oficinas, silos y básculas integrados en un solo desarrollo llave en mano.",
   "en":"Production, warehousing, offices, silos and truck scales integrated into a single turnkey development."}),
 ("images/proyectos/gates/05.jpg","chip--auto","automotive",
  {"es":"Obra sobre operación","en":"Construction over live operations"},
  {"es":"Ampliar una nave sin detener la producción",
   "en":"Expanding a facility without stopping production"},
  {"es":"Incremento de altura y refuerzo estructural de una nave de 1,500 m² con la planta en operación.",
   "en":"Height increase and structural reinforcement of a 1,500 m² facility with the plant still running."}),
 ("images/proyectos/espejos-inteligentes/02.jpg","chip--auto","automotive",
  {"es":"2,500 m²","en":"2,500 m²"},
  {"es":"Ampliación de nave y almacén para autopartes",
   "en":"Facility and warehouse expansion for auto parts"},
  {"es":"Terracerías, cimentación, laminación y estructura metálica para una nueva zona de almacenaje.",
   "en":"Earthworks, foundations, roofing and cladding, and structural steel for a new storage area."}),
 ("images/proyectos/mixing/01.jpg","chip--corp","corporate",
  {"es":"Procesos productivos","en":"Production processes"},
  {"es":"Naves industriales pensadas para producir",
   "en":"Industrial facilities designed to produce"},
  {"es":"Estructuras de gran claro y pisos de alto desempeño diseñados para el flujo de materiales y la maquinaria.",
   "en":"Long-span structures and high-performance floors designed around material flow and machinery."}),
]

def build_blog(lang):
    u = UI[lang]; other = "en" if lang=="es" else "es"
    base = "../" if lang=="en" else ""
    self_p = path_of("blog", lang); alt_p = path_of("blog", other)
    name_of = {s["key"]: s["name"][lang] for s in SECTORS}
    cards = "\n".join(f'''        <a class="post reveal" href="{base}{art_path(k,lang)}">
          <div class="post__media"><img src="{base}{BEN.META[k]["photo"]}" alt="{art_title(k,lang)}" loading="lazy" />
            <span class="chip {BEN.META[k]["chip"]} post__cat">{BEN.META[k]["cat"][lang]}</span>
          </div>
          <div class="post__body">
            <div class="post__meta">{BEN.META[k]["meta_lbl"][lang]}</div>
            <h3>{art_title(k,lang)}</h3>
            <p>{BEN.META[k]["desc"][lang]}</p>
            <span class="post__more">{'Leer artículo →' if lang=='es' else 'Read article →'}</span>
          </div>
        </a>''' for k in BEN.ORDER)
    t = {"es":("Blog","Ideas y obra","Blog de CAABSA STEEL",
               "Notas técnicas y casos reales de construcción industrial y montaje de estructura de acero.",
               "Blog | CAABSA STEEL","Blog de CAABSA STEEL: casos reales y notas técnicas de construcción industrial en México."),
         "en":("Blog","Insights & projects","CAABSA STEEL Blog",
               "Technical notes and real cases from industrial construction and steel erection.",
               "Blog | CAABSA STEEL","CAABSA STEEL blog: real cases and technical notes on industrial construction in Mexico.")}[lang]
    body = f'''  <section class="subhead">
    <div class="subhead__bg"></div>
    <div class="container">
      <div class="breadcrumb"><a href="{base}{path_of("home",lang)}">{u["home"]}</a><span class="sep">/</span> {t[0]}</div>
      <div class="kicker">{t[1]}</div>
      <h1>{t[2]}</h1>
      <p class="lead">{t[3]}</p>
    </div>
  </section>

  <section class="section blog">
    <div class="container">
      <div class="blog__grid">
{cards}
      </div>
    </div>
  </section>'''
    open(os.path.join(ROOT, self_p),"w",encoding="utf-8").write(
        page(lang, base, t[4], t[5], self_p, alt_p, body))

# ══════════════════════════ PROYECTOS Y ESTADOS ══════════════════════════
STATES = {
 "estado-de-mexico": dict(name={"es":"Estado de México","en":"State of Mexico"}, region="central",
    cities={"es":"Metepec y el corredor industrial del Estado de México","en":"Metepec and the State of Mexico industrial corridor"}),
 "morelos": dict(name={"es":"Morelos","en":"Morelos"}, region="central",
    cities={"es":"Cuernavaca y Cuautla","en":"Cuernavaca and Cuautla"}),
 "hidalgo": dict(name={"es":"Hidalgo","en":"Hidalgo"}, region="central",
    cities={"es":"el corredor industrial de Hidalgo","en":"the Hidalgo industrial corridor"}),
 "puebla": dict(name={"es":"Puebla","en":"Puebla"}, region="central",
    cities={"es":"Puebla y su clúster automotriz","en":"Puebla and its automotive cluster"}),
 "tlaxcala": dict(name={"es":"Tlaxcala","en":"Tlaxcala"}, region="central",
    cities={"es":"el corredor industrial de Tlaxcala","en":"the Tlaxcala industrial corridor"}),
 "queretaro": dict(name={"es":"Querétaro","en":"Querétaro"}, region="bajio",
    cities={"es":"Querétaro y su corredor industrial","en":"Querétaro and its industrial corridor"}),
 "jalisco": dict(name={"es":"Jalisco","en":"Jalisco"}, region="occidente",
    cities={"es":"Guadalajara y su zona metropolitana","en":"Guadalajara and its metropolitan area"}),
}

_spec2 = _ilu.spec_from_file_location("projects_new", os.path.join(_SD,"projects_new.py"))
PN = _ilu.module_from_spec(_spec2); _spec2.loader.exec_module(PN)

def P(slug, client, state, sector, photos, kind, m2=None, scope=None, about=None, city=None, article=None):
    return dict(slug=slug, client=client, state=state, sector=sector, photos=photos,
                kind=kind, m2=m2, scope=scope or {}, about=about or {}, city=city or {}, article=article)

PROJECTS = PN.PROJECTS
STATES.update(PN.EXTRA_STATES)
REVIEWS_REAL = PN.REVIEWS

# Fotos sueltas del cliente (fuera de carpetas de proyecto) usadas como DISEÑO
DESIGN = {
 "queretaro":       dict(hero="images/proyectos/queretaro-general/01.jpg", band="images/proyectos/queretaro-general/03.jpg"),
 "estado-de-mexico":dict(hero="images/proyectos/edomex-general/01.jpg",    band="images/proyectos/edomex-general/02.jpg"),
 "tlaxcala":        dict(hero="images/proyectos/tlaxcala/01.jpg",          band="images/proyectos/tlaxcala/02.jpg"),
}
DESIGN_REGION = {
 "bajio":     "images/proyectos/queretaro-general/02.jpg",
 "central":   "images/proyectos/andenes/01.jpg",
 "occidente": "images/proyectos/jugos-del-valle/02.jpg",
}
TEAM_PHOTO = "images/equipo/01.jpg"

CTA_BAND = {
 "es": dict(k="CAABSA STEEL", t="Construimos donde opera tu industria",
            p="45 años construyendo naves, plantas y espacios corporativos para empresas AAA y AA, con procesos certificados ISO 9001:2015."),
 "en": dict(k="CAABSA STEEL", t="We build where your industry operates",
            p="45 years building facilities, plants and corporate spaces for AAA and AA companies, under ISO 9001:2015 certified processes."),
}
def sector_band_photo(sector_key):
    """Una foto real de un proyecto del sector, para la banda de cierre."""
    for pr in PROJECTS:
        if pr["sector"] == sector_key and pr["photos"] >= 2:
            return f'images/proyectos/{pr["slug"]}/02.jpg'
    for pr in PROJECTS:
        if pr["sector"] == sector_key and pr["photos"] >= 1:
            return f'images/proyectos/{pr["slug"]}/01.jpg'
    return None

def cta_band(lang, base, photo, title=None):
    """Banda parallax de cierre; va al final de cada página, antes del contacto."""
    if not photo: return ""
    c = CTA_BAND[lang]
    return design_band(lang, base, photo, c["k"], title or c["t"], c["p"])

def design_band(lang, base, photo, kicker, title, text):
    """Banda parallax de ancho completo con foto real del cliente."""
    return f'''  <div class="pband" style="background-image:url(\'{base}{photo}\')">
    <div class="pband__content">
      <div class="kicker">{kicker}</div>
      <h2 class="h2">{title}</h2>
      <p>{text}</p>
      <a href="{base}{path_of("contact",lang)}" class="btn btn--primary btn--lg">{UI[lang]["nav_quote"]}</a>
    </div>
  </div>'''

# Logos de clientes extraídos de la presentación del cliente
CLIENT_LOGOS = [
 ("bosch","Bosch"),("ford","Ford"),("bridgestone","Bridgestone"),("kimberly-clark","Kimberly-Clark"),
 ("saint-gobain","Saint-Gobain"),("femsa","Coca-Cola FEMSA"),("soriana","Soriana"),("lear","Lear Corporation"),
 ("martinrea","Martinrea Honsel"),("thyssenkrupp","thyssenkrupp"),("la-moderna","La Moderna"),
 ("jugos-del-valle","Jugos del Valle"),("interjet","Interjet"),("vesta","Vesta"),("finsa","FINSA"),
 ("daewoo","Daewoo"),("bardahl","Bardahl"),("grupo-sanchez","Grupo Sánchez"),("ferrostaal","Ferrostaal"),
 ("quimica-apollo","Química Apollo"),("tst-timco","TST Inc · TIMCO"),("cimsa","Grupo CIMSA"),
 ("dalton-honda","Dalton Honda"),
 # añadidos del currículum de obra
 ("gates","Gates"),("brose","Brose"),("dart","Dart de México"),("irizar","Irizar"),
 ("euroquip","Euroquip"),("rubau","Rubau"),("metrocolor","Metrocolor"),("polynt","Polynt"),
 ("tecnosol","Tecnosol"),("vetrotex","Vetrotex"),("aventis","Aventis Pharma"),
 ("baleros-mexicanos","Baleros Mexicanos"),("espejos-inteligentes","Espejos Inteligentes"),
]

def _logo_w(slug, h=46):
    """Ancho real del logo a la altura de la banda; si se declara mal, el track
    cambia de tamaño al cargar la imagen y la animación da un salto."""
    try:
        from PIL import Image
        im = Image.open(os.path.join(ROOT, "images", "logos", slug + ".png"))
        return max(1, round(im.width * h / im.height))
    except Exception:
        return 150

def clients_marquee(lang, base):
    """Banda infinita con los logos de las empresas que han construido con CAABSA."""
    mid = (len(CLIENT_LOGOS)+1)//2
    def band(items, rev=False):
        imgs = "".join(
          f'<img class="mq__logo" src="{base}images/logos/{sl}.png" alt="{nm}" width="{_logo_w(sl)}" height="46" decoding="async" />'
          for sl,nm in items*2)
        return f'<div class="mq"><div class="mq__track{" mq__track--rev" if rev else ""}">{imgs}</div></div>'
    t = ({"kicker":"Confianza","h2":"Empresas que han construido con nosotros",
          "p":"Grandes corporativos y empresas AAA y AA que han confiado sus proyectos a CAABSA STEEL."}
         if lang=="es" else
         {"kicker":"Trusted by","h2":"Companies that have built with us",
          "p":"Major corporations and AAA and AA companies that have trusted their projects to CAABSA STEEL."})
    return f'''  <section class="clients" id="clientes">
    <div class="container clients__head reveal">
      <div class="kicker">{t["kicker"]}</div>
      <h2>{t["h2"]}</h2>
      <p>{t["p"]}</p>
    </div>
    {band(CLIENT_LOGOS[:mid])}
    {band(CLIENT_LOGOS[mid:], rev=True)}
  </section>'''

FALLBACK_PHOTO = "images/proyectos/edomex-general/01.jpg"

def pphoto(p, idx=1):
    """Foto propia del proyecto, o None si el cliente aún no la envía."""
    return f'images/proyectos/{p["slug"]}/{idx:02d}.jpg' if p["photos"] >= idx else None

def phero(p):
    """Foto del encabezado: la que el proyecto declare, o la primera."""
    return pphoto(p, p.get("hero") or 1)

def pband_photo(p):
    """Foto para la banda de cierre: una del propio proyecto si le sobran,
    si no la del estado o la de la región, para no repetir la de la galería."""
    if p["photos"] >= 3:
        h = p.get("hero") or 1
        for i in range(p["photos"], 0, -1):
            if i != h and i != p.get("banner"): return pphoto(p, i)
    st = STATES.get(p["state"], {})
    return (DESIGN.get(p["state"],{}).get("band")
            or DESIGN_REGION.get(st.get("region"))
            or FALLBACK_PHOTO)

def pmain(p):
    """Imagen para contextos de estado o región, donde no se atribuye a un proyecto."""
    return pphoto(p) or DESIGN.get(p["state"],{}).get("hero") or FALLBACK_PHOTO

# Marca para los proyectos sin fotografía: nunca se usa la foto de otra obra,
# porque en la tarjeta quedaría atribuida a este cliente.
BLANK_MARK = ('<svg class="proj__blankmark" viewBox="0 0 64 40" fill="none" stroke="currentColor" '
  'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
  '<path d="M2 38h60"/><path d="M6 38V16l14-8 14 8v22"/><path d="M34 38V22h24v16"/>'
  '<path d="M13 38v-9h7v9"/><path d="M41 29h4M50 29h4"/><path d="M6 16l14 8 14-8"/></svg>')

def pmedia(p, base, lang, alt=None):
    """Bloque de imagen de una tarjeta de proyecto."""
    alt = alt or f'{p["client"]} — {p["kind"][lang]}'
    ph = pphoto(p)
    if ph:
        return f'<div class="proj__media"><img src="{base}{ph}" alt="{alt}" loading="lazy" /></div>'
    lbl = "Fotografía pendiente" if lang == "es" else "Photograph pending"
    return (f'<div class="proj__media proj__media--blank" role="img" aria-label="{alt} — {lbl}">'
            f'{BLANK_MARK}<span class="proj__blanktxt">{lbl}</span></div>')

SECTOR_BY_KEY = {s["key"]: s for s in SECTORS}
REGION_BY_KEY = {r["key"]: r for r in REGIONS}
CHIP = {"automotive":"chip--auto","food":"chip--food","logistics":"chip--log",
        "corporate":"chip--corp","aerospace":"chip--aero","industrial":"chip--ind","pharma":"chip--pharma"}
SECTOR_LABEL = {"industrial":{"es":"Industrial","en":"Industrial"}}
def sector_label(k, lang):
    if k in SECTOR_BY_KEY: return SECTOR_BY_KEY[k]["name"][lang]
    return SECTOR_LABEL[k][lang]

def proj_path(slug, lang):
    return f"proyectos/{slug}.html" if lang=="es" else f"en/projects/{slug}.html"
def state_path(skey, lang):
    return f"estados/{skey}.html" if lang=="es" else f"en/states/{skey}.html"

PUI = {
 "es": dict(projects="Proyectos", states="Estados", crumb_proj="Proyectos",
   scope="Alcance de la obra", about="Sobre el proyecto", gallery="Galería del proyecto",
   location="Ubicación", surface="Superficie", sector="Sector", state="Estado", client="Cliente",
   more_state="Ver más proyectos en", back_projects="Ver todos los proyectos",
   in_state="Proyectos en", states_title="Estados donde construimos",
   states_sub="Construcción industrial y estructura de acero con presencia comprobada en estos estados.",
   region_lbl="Región", cities="Zonas donde operamos", nproj="proyectos documentados",
   proj_kicker="Proyecto"),
 "en": dict(projects="Projects", states="States", crumb_proj="Projects",
   scope="Scope of work", about="About the project", gallery="Project gallery",
   location="Location", surface="Area", sector="Industry", state="State", client="Client",
   more_state="See more projects in", back_projects="View all projects",
   in_state="Projects in", states_title="States where we build",
   states_sub="Industrial construction and structural steel with a proven track record in these states.",
   region_lbl="Region", cities="Areas we serve", nproj="documented projects",
   proj_kicker="Project"),
}

def build_projects(lang):
    u = UI[lang]; pu = PUI[lang]; other = "en" if lang=="es" else "es"
    os.makedirs(os.path.join(ROOT, "proyectos" if lang=="es" else "en/projects"), exist_ok=True)
    base = "../" if lang=="es" else "../../"
    for p in PROJECTS:
        st = STATES[p["state"]]
        stname = st["name"][lang]
        city = p["city"].get(lang, "") if p["city"] else ""
        loc = f"{city}, {stname}" if city else stname
        self_p = proj_path(p["slug"], lang); alt_p = proj_path(p["slug"], other)
        sec = sector_label(p["sector"], lang)
        m2txt = f' · {p["m2"]}' if p["m2"] else ""
        title = (f'{p["client"]} — {p["kind"][lang]} en {loc} | CAABSA STEEL' if lang=="es"
                 else f'{p["client"]} — {p["kind"][lang]} in {loc} | CAABSA STEEL')
        desc = (f'{p["kind"][lang]} para {p["client"]} en {loc}{m2txt}. Construcción industrial y estructura de acero por CAABSA STEEL, certificación ISO 9001:2015.'
                if lang=="es" else
                f'{p["kind"][lang]} for {p["client"]} in {loc}{m2txt}. Industrial construction and structural steel by CAABSA STEEL, ISO 9001:2015 certified.')
        bidx = p.get("banner")
        gallery = "\n".join(f'''        <img src="{base}images/proyectos/{p["slug"]}/{i:02d}.jpg" alt="{p["client"]} — {p["kind"][lang]} ({loc}) {i}" loading="lazy" />'''
                            for i in range(1, p["photos"]+1) if i != bidx)
        bandphoto = pband_photo(p) or DESIGN.get(p["state"],{}).get("band")
        band = (f'''  <div class="photoband reveal" role="img" aria-label="{p["client"]} — {p["kind"][lang]} ({loc})"
       style="background-image:url(\'{base}images/proyectos/{p["slug"]}/{bidx:02d}.jpg\')"></div>''' if bidx else "")
        ngal = p["photos"] - (1 if bidx else 0)
        scope = "".join(f"<li>{s}</li>" for s in p["scope"][lang])
        facts = f'''<div class="build-list">
          <span><b>{pu["client"]}:</b> {p["client"]}</span>
          <span><b>{pu["sector"]}:</b> {f'<a href="{base}{path_of("sector",lang,SECTOR_BY_KEY[p["sector"]]["slug"][lang])}">{sec}</a>' if p["sector"] in SECTOR_BY_KEY else sec}</span>
          <span><b>{pu["location"]}:</b> {loc}</span>
          {f'<span><b>{pu["surface"]}:</b> {p["m2"]}</span>' if p["m2"] else ''}
        </div>'''
        reg = REGION_BY_KEY.get(st["region"]) if st["region"] else None
        reglink = (f'<a href="{base}{path_of("region",lang,reg["slug"][lang])}">{reg["name"][lang]}</a>' if reg else "—")
        jsonld = f'''<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Project","name":"{p["client"]} — {p["kind"][lang]}","description":"{p["kind"][lang]} · {loc}","location":{{"@type":"Place","address":{{"@type":"PostalAddress","addressRegion":"{stname}","addressCountry":"MX"}}}},"provider":{{"@type":"Organization","name":"CAABSA STEEL","url":"{SITE_URL}"}}}}</script>'''
        body = f'''  <section class="subhead">
    {f'<div class="subhead__photo" style="background-image:url({chr(39)}{base}{phero(p)}{chr(39)})"></div>' if phero(p) else ''}
    <div class="subhead__scrim"></div><div class="subhead__bg"></div>
    <div class="container">
      <div class="breadcrumb"><a href="{base}{path_of("home",lang)}">{u["home"]}</a><span class="sep">/</span><a href="{base}{state_path(p["state"],lang)}">{stname}</a><span class="sep">/</span> {p["client"]}</div>
      <div class="kicker">{pu["proj_kicker"]} · {sec} · {loc}</div>
      <h1>{p["client"]} — {p["kind"][lang]}</h1>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="prose reveal">
        <p style="font-size:1.1rem;color:var(--text)">{p["about"][lang]}</p>
        {facts}
        <h2>{pu["scope"]}</h2>
        <ul>{scope}</ul>
        {f'<p style="margin-top:18px"><b>{"Artículo relacionado" if lang=="es" else "Related article"}:</b> <a href="{base}{art_path(p["article"],lang)}">{art_title(p["article"],lang)}</a></p>' if p.get("article") else ""}
        <p style="margin-top:18px"><b>{pu["region_lbl"]}:</b> {reglink} &nbsp;·&nbsp; <a href="{base}{state_path(p["state"],lang)}">{pu["more_state"]} {stname} →</a></p>
      </div>
    </div>
  </section>

{band}

{f'''  <section class="section section--alt">
    <div class="container">
      <div class="section-head reveal"><div class="kicker">{pu["gallery"]}</div><h2 class="h2">{p["client"]}</h2></div>
      <div class="pgal reveal">
{gallery}
      </div>
    </div>
  </section>''' if ngal > 0 else ""}

{cta_band(lang, base, bandphoto, ("¿Tienes un proyecto así?" if lang=="es" else "Have a project like this?"))}
{contact_section(lang, base, sec if p["sector"] in SECTOR_BY_KEY else "", simple=True, alt=False)}
  {jsonld}'''
        open(os.path.join(ROOT,self_p),"w",encoding="utf-8").write(
            page(lang, base, title, desc, self_p, alt_p, body))

def build_states(lang):
    u = UI[lang]; pu = PUI[lang]; other = "en" if lang=="es" else "es"
    os.makedirs(os.path.join(ROOT, "estados" if lang=="es" else "en/states"), exist_ok=True)
    base = "../" if lang=="es" else "../../"
    for skey, st in STATES.items():
        stname = st["name"][lang]
        projs = [p for p in PROJECTS if p["state"]==skey]
        self_p = state_path(skey, lang); alt_p = state_path(skey, other)
        title = (f'Construcción industrial en {stname} — Naves y estructura de acero | CAABSA STEEL' if lang=="es"
                 else f'Industrial construction in {stname} — Facilities and structural steel | CAABSA STEEL')
        desc = (f'Constructora industrial en {stname}: naves industriales, plantas y estructura de acero. {len(projs)} proyectos documentados en {st["cities"][lang]}. ISO 9001:2015.'
                if lang=="es" else
                f'Industrial construction company in {stname}: industrial facilities, plants and structural steel. {len(projs)} documented projects in {st["cities"][lang]}. ISO 9001:2015 certified.')
        intro = (f'Construimos naves industriales, plantas y espacios corporativos en {stname}, con obra ejecutada en {st["cities"][lang]}. Cada proyecto se entrega bajo procesos certificados ISO 9001:2015.'
                 if lang=="es" else
                 f'We build industrial facilities, plants and corporate spaces in {stname}, with projects delivered in {st["cities"][lang]}. Every project is completed under ISO 9001:2015 certified processes.')
        cards = "\n".join(f'''        <article class="proj reveal">
          {pmedia(p, base, lang)}
          <div class="proj__info"><span class="chip {CHIP[p["sector"]]}">{sector_label(p["sector"],lang)}</span><h3>{p["client"]}</h3><p>{p["kind"][lang]}{" · "+p["m2"] if p["m2"] else ""}</p>
          <a class="post__more" href="{base}{proj_path(p["slug"],lang)}">{"Ver proyecto →" if lang=="es" else "View project →"}</a></div>
        </article>''' for p in projs)
        reg = REGION_BY_KEY.get(st["region"]) if st["region"] else None
        regline = (f'<p><b>{pu["region_lbl"]}:</b> <a href="{base}{path_of("region",lang,reg["slug"][lang])}">{reg["name"][lang]}</a></p>' if reg else "")
        gal = ""
        if not projs:
            extra = {"tlaxcala":2}.get(skey,0)
            if extra:
                gal = '<div class="proyectos__grid">' + "".join(
                  f'<article class="proj reveal"><div class="proj__media"><img src="{base}images/proyectos/{skey}/{i:02d}.jpg" alt="{stname} {i}" loading="lazy" /></div></article>'
                  for i in range(1,extra+1)) + '</div>'
        body = f'''  <section class="subhead">
    <div class="subhead__photo" style="background-image:url('{base}{DESIGN.get(skey,{}).get("hero") or next((pphoto(x) for x in projs if pphoto(x)), None) or FALLBACK_PHOTO}')"></div>
    <div class="subhead__scrim"></div><div class="subhead__bg"></div>
    <div class="container">
      <div class="breadcrumb"><a href="{base}{path_of("home",lang)}">{u["home"]}</a><span class="sep">/</span><a href="{base}{('estados/index.html' if lang=='es' else 'en/states/index.html')}">{pu["states"]}</a><span class="sep">/</span> {stname}</div>
      <div class="kicker">{pu["state"]} · {stname}</div>
      <h1>{"Construcción industrial en" if lang=="es" else "Industrial construction in"} {stname}</h1>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="prose reveal">
        <p style="font-size:1.1rem;color:var(--text)">{intro}</p>
        <p><b>{pu["cities"]}:</b> {st["cities"][lang]}.</p>
        {regline}
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="section-head reveal"><div class="kicker">{pu["in_state"]} {stname}</div><h2 class="h2">{len(projs)} {pu["nproj"]}</h2></div>
      <div class="proyectos__grid">
{cards}
      </div>
      {gal}
    </div>
  </section>

{design_band(lang, base, DESIGN[skey]["band"],
   (u["coverage_pre"]+" · "+stname),
   ("Obra industrial en "+stname if lang=="es" else "Industrial construction in "+stname),
   ("Estructura de acero, naves y ampliaciones ejecutadas en "+st["cities"][lang]+", con calidad certificada ISO 9001:2015."
    if lang=="es" else
    "Structural steel, industrial facilities and expansions delivered in "+st["cities"][lang]+", with ISO 9001:2015 certified quality.")) if skey in DESIGN else ""}

{contact_section(lang, base, "", simple=True, alt=False)}'''
        open(os.path.join(ROOT,self_p),"w",encoding="utf-8").write(
            page(lang, base, title, desc, self_p, alt_p, body))

    # índice de estados
    self_p = ("estados/index.html" if lang=="es" else "en/states/index.html")
    alt_p  = ("en/states/index.html" if lang=="es" else "estados/index.html")
    cards = "\n".join(f'''        <a class="region-card reveal" href="{base}{state_path(k,lang)}">
          <h3>{st["name"][lang]}</h3><p>{st["cities"][lang]}</p>
          <span class="region-card__states">{len([p for p in PROJECTS if p["state"]==k])} {pu["nproj"]} →</span>
        </a>''' for k,st in STATES.items())
    body = f'''  <section class="subhead">
    <div class="subhead__bg"></div>
    <div class="container">
      <div class="breadcrumb"><a href="{base}{path_of("home",lang)}">{u["home"]}</a><span class="sep">/</span> {pu["states"]}</div>
      <div class="kicker">{u["coverage_pre"]}</div>
      <h1>{pu["states_title"]}</h1>
      <p class="lead">{pu["states_sub"]}</p>
    </div>
  </section>
  <section class="section">
    <div class="container"><div class="regions__grid">
{cards}
    </div></div>
  </section>
{contact_section(lang, base, "", simple=True, alt=True)}'''
    open(os.path.join(ROOT,self_p),"w",encoding="utf-8").write(
        page(lang, base, ("Estados donde construimos | CAABSA STEEL" if lang=="es" else "States where we build | CAABSA STEEL"),
             ("Construcción industrial por estado: Estado de México, Morelos, Hidalgo, Puebla, Tlaxcala, Querétaro y Jalisco. Naves y estructura de acero." if lang=="es"
              else "Industrial construction by state: State of Mexico, Morelos, Hidalgo, Puebla, Tlaxcala, Querétaro and Jalisco. Facilities and structural steel."),
             self_p, alt_p, body))

    # índice de proyectos
    self_p = ("proyectos/index.html" if lang=="es" else "en/projects/index.html")
    alt_p  = ("en/projects/index.html" if lang=="es" else "proyectos/index.html")
    cards = "\n".join(f'''        <article class="proj reveal">
          {pmedia(p, base, lang, p["client"])}
          <div class="proj__info"><span class="chip {CHIP[p["sector"]]}">{sector_label(p["sector"],lang)}</span><h3>{p["client"]}</h3>
          <p>{p["kind"][lang]} · {STATES[p["state"]]["name"][lang]}</p>
          <a class="post__more" href="{base}{proj_path(p["slug"],lang)}">{"Ver proyecto →" if lang=="es" else "View project →"}</a></div>
        </article>''' for p in PROJECTS)
    body = f'''  <section class="subhead">
    <div class="subhead__photo" style="background-image:url('{base}images/proyectos/martinrea-honsel/01.jpg')"></div>
    <div class="subhead__scrim"></div><div class="subhead__bg"></div>
    <div class="container">
      <div class="breadcrumb"><a href="{base}{path_of("home",lang)}">{u["home"]}</a><span class="sep">/</span> {pu["projects"]}</div>
      <div class="kicker">{"Portafolio" if lang=="es" else "Portfolio"}</div>
      <h1>{"Proyectos de construcción industrial" if lang=="es" else "Industrial construction projects"}</h1>
      <p class="lead">{"Obras ejecutadas en 7 estados de México para empresas AAA y AA." if lang=="es" else "Projects delivered across 7 Mexican states for AAA and AA companies."}</p>
    </div>
  </section>
  <section class="section">
    <div class="container"><div class="proyectos__grid">
{cards}
    </div></div>
  </section>
{contact_section(lang, base, "", simple=True, alt=True)}'''
    open(os.path.join(ROOT,self_p),"w",encoding="utf-8").write(
        page(lang, base, ("Proyectos — Portafolio de construcción industrial | CAABSA STEEL" if lang=="es" else "Projects — Industrial construction portfolio | CAABSA STEEL"),
             ("Portafolio de CAABSA STEEL: 15 proyectos de construcción industrial y estructura de acero en 7 estados de México." if lang=="es"
              else "CAABSA STEEL portfolio: 15 industrial construction and structural steel projects across 7 Mexican states."),
             self_p, alt_p, body))

for lg in ("es","en"):
    build_lang(lg); build_blog(lg); build_articles(lg)
    build_projects(lg); build_states(lg)
    print("built:", lg)

# sitemap
urls = []
for lg in ("es","en"):
    urls.append(path_of("home",lg)); urls.append(path_of("about",lg)); urls.append(path_of("contact",lg))
    for s in SECTORS: urls.append(path_of("sector",lg,s["slug"][lg]))
    for r in REGIONS: urls.append(path_of("region",lg,r["slug"][lg]))
    urls.append("proyectos/index.html" if lg=="es" else "en/projects/index.html")
    urls.append("estados/index.html" if lg=="es" else "en/states/index.html")
    for pr in PROJECTS: urls.append(proj_path(pr["slug"],lg))
    for sk in STATES: urls.append(state_path(sk,lg))
    urls.append(path_of("blog",lg))
    for _k in BEN.ORDER: urls.append(art_path(_k,lg))
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
sm += "".join(f"  <url><loc>{SITE_URL}{u}</loc></url>\n" for u in urls)
sm += "</urlset>\n"
open(os.path.join(ROOT,"sitemap.xml"),"w",encoding="utf-8").write(sm)
print("sitemap:", len(urls), "urls")
print("DONE")

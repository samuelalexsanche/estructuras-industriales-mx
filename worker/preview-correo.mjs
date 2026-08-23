import { readFileSync, writeFileSync } from 'fs';
let src = readFileSync(new URL('./worker.js', import.meta.url), 'utf8');
// aislar solo las funciones de la plantilla para poder ejecutarlas fuera del Worker
const desde = src.indexOf('const LEAD_LABELS');
const hasta = src.indexOf('async function handleLead');
const mod = src.slice(desde, hasta) + '\nexport { leadHtml, leadText };\n';
writeFileSync('/tmp/tpl.mjs', mod);
const { leadHtml, leadText } = await import('/tmp/tpl.mjs');

const site = 'http://localhost:8099';
const contacto = leadHtml({
  titulo: 'Nuevo contacto · Cliente', intent: 'cliente', esBrochure: false,
  rows: [['Nombre','Ana Ruiz'],['Empresa','Industrias Prueba S.A. de C.V.'],
         ['Teléfono','722 523 2020'],['Correo','ana@industriasprueba.com'],
         ['Sector','Alimenticio'],['Página de origen','/sectores/alimenticio.html']],
  mensaje: 'Necesitamos una nave de 4,000 m² en el corredor industrial de Querétaro, con andenes de carga y oficinas anexas. ¿Podrían darnos un anteproyecto?',
  email: 'ana@industriasprueba.com', telefono: '722 523 2020', siteUrl: site,
});
const brochure = leadHtml({
  titulo: 'Descarga del brochure', intent: '', esBrochure: true,
  rows: [['Nombre','Luis Herrera'],['Empresa','Constructora XYZ'],
         ['Puesto','Director de Compras'],['Correo','luis@constructoraxyz.com'],
         ['Página de origen','/nosotros.html']],
  mensaje: '', email: 'luis@constructoraxyz.com', telefono: '', siteUrl: site,
});
writeFileSync('../_mail_contacto.html', contacto);
writeFileSync('../_mail_brochure.html', brochure);
console.log(leadText({ titulo:'Nuevo contacto · Cliente',
  rows:[['Nombre','Ana Ruiz'],['Empresa','Industrias Prueba']], mensaje:'Necesitamos una nave…' }));

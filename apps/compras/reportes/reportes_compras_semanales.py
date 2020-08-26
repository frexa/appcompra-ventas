from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, TA_CENTER
from reportlab.lib.units import inch, mm
from reportlab.lib import colors
from reportlab.platypus import (Paragraph,
								Table,
								SimpleDocTemplate,
								Spacer,
								TableStyle)
from apps.compras.models import LineaDeCompra

class ReporteComprasSemanales(object):
	"""docstring for ReporteComprasSemanales"""
	def __init__(self):
		self.buf = BytesIO()

	def run(self):
		self.doc = SimpleDocTemplate(self.buf)
		self.story=[]
		self.encabezado()
		self.creartabla()
		self.doc.build(self.story,
						onFirstPage=self.numeropagina,
						onLaterPages=self.numeropagina)
		pdf = self.buf.getvalue()
		self.buf.close()
		return pdf

	def encabezado(self):
		p = Paragraph("Compras realizadas durante la semana",self.estiloPC())
		self.story.append(p)
		self.story.append(Spacer(1,0.5*inch))

	def creartabla(self):
		data = [["Ingrediente", "Precio Unitario","Cantidad","Total pagado","Total peso"]]\
				+[[c.ingrediente, c.ingrediente.precio_unit,c.cantidad,c.total,c.total_peso]
					for c in LineaDeCompra.objects.all()]
		
		styles = TableStyle([('GRID',(0,0),(-1,-1), 0.25,colors.black),
								('ALIGN',(0,0),(-1,-1),'CENTER'),
								('VALIGN',(0,0),(-1,-1),'MIDDLE')])
		t = Table(data)
		#t.setStyles(style)
		self.story.append(t)

	def estiloPC(self):
		return ParagraphStyle(name='centrado', alignment=TA_CENTER)

	def numeropagina(self, canvas, doc):
		num = canvas.getPageNumber()
		text= 'Pagina %s' % num
		#canvas.drawRigthString(200*mm, 20*mm, text)
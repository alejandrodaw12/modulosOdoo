# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class proyectos(models.Model):
#     _name = 'proyectos.proyectos'
#     _description = 'proyectos.proyectos'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
from odoo import models , fields, api

class departamento(models.Model):
	_name = 'proyectos.departamento'
	_description = 'Define los atributos de un departamento'

	#atributos
	nombreDpto = fields.Char(string='Nombre departamento', required=True)

	#Relacion entre tablas
	empleado_id = fields.One2many('proyectos.empleado','departamento_id', string='Departamento')

class empleado(models.Model):
	_name = 'proyectos.empleado'
	_description = 'Define los atributos de un empleado'

	#atributos
	dniEmpleado = fields.Char(string='DNI', required=True)
	nombreEmpleado = fields.Char(string='Nombre', required=True)
	fechaNacimiento = fields.Date(string='Fecha Nacimiento', required=True, default = fields.date.today())
	direccionEmpleado = fields.Char(string='Direccion', required=True)
	telefonoEmpleado = fields.Char(string='Telefono')

	@api.depends('fechaNacimiento')
	def _getEdad(self):
		hoy = date.today()
		for empleado in self:
			empleado.edad = relativedelta(hoy, empleado.fechaNacimiento).years

	@api.constrains('dniEmpleado')
	def _checkDNI(self):
		for empleado in self:
			if (len(empleado.dniEmpleado) > 9 ):
				raise exceptions.ValidationError("El DNI no puede ser superior a 9 caracteres")
			if (len(empleado.dniEmpleado) < 9 ):
				raise exceptions.ValidationError("El DNI no puede tener menos de 9 caracteres")	

	#Relacion entre tablas
	departamento_id = fields.Many2one('proyeto.departamento', string='Empleados')
	proyecto_id = fields.Many2one('proyectos.proyecto', string='Proyectos')

class proyecto(models.Model):
	_name = 'proyectos.proyecto'
	_description = 'Atributos de un proyecto'

	#atributos
	nombreProyecto = fields.Char(string='Nombre Proyecto', required=True)
	tipoProyecto = fields.Selection(string='Tipo de Proyecto', selection=[('f','Front-End'),('b','Back-End')], help='Tipo de proyecto al que esta destinado')
	ciudadProyecto = fields.Char(string='Ciudad')
	descriptionProyecto = fields.Text('Descripcion Proyecto')
	fechaInicio = fields.Date('Fecha de inicio', required=True)
	fechaFinal = fields.Date('Fecha de final', required=True)


	@api.depends('fechaInicio')
	def _checkFechaInicio(self):
		hoy = date.today()
		for proyecto in self:
			proyecto.fechaInicio
			dias = relativedelta(hoy, proyecto.fechaInicio).days
			if (dias < 0):
				raise exceptions.ValidationError("La fecha no puede ser anterior a hoy")
	
	@api.depends('fechaFinal')
	def _checkFechaFinal(self):
		hoy = date.today()
		for proyecto in self:
			if relativedelta(hoy, proyecto,fechaFinal).days > 0:
				raise exceptions.ValidationError("La fehca no puede ser anterior a la fecha de inicio")

	#Relacion entre tablas
	empleado_id = fields.Many2many('proyectos_empleado', string='Empleados')
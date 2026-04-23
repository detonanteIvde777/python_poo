from persona import Persona

juan = Persona("Juan","castellanos" ,15)
juan.mostrarpersona()

leidy = Persona("Leidy","alvarez" ,18)
leidy.mostrarpersona()

leidy.apellido = "perez"
leidy.mostrarpersona()

juan = leidy

juan.mostrarpersona()
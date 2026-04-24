from persona import persona

juan = persona("elbergon", "castrillon",15)
juan.mostrarpersona()

laura = persona("laura", "gomez", 18)
laura.mostrarpersona()

laura = persona("laura", "perez", 20)
laura.mostrarpersona()

juan = laura

juan.mostrarpersona()
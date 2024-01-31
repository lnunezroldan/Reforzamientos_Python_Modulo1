cursos = ["Cálculo", "Investigación de Operaciones", "Petrología", "Mineralogía",
          "Planeamiento de Minas", "Geoestadística"]

cursos.append("PerVol")
cursos.append("Economia Minera")
cursos.append("Costos")
cursos.append("Cierre de Minas")

print("La lista de cursos ampliada es: {}".format(cursos))

cursos.remove("Costos")
cursos.remove("Economia Minera")

print("La lista de cursos reducida es: {}".format(cursos))
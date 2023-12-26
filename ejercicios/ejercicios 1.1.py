#otros cursos duracion
otros_cursos_min=2.5
otros_cursos_max=7
otros_cursos_prom=4
dalto_curso=1.5
crudo_promedio=5
crudo_dalto=3.5

#diferencias de duracion

diferencias_con_min = 100 - dalto_curso/otros_cursos_min * 100

diferencias_con_max = 100 - dalto_curso *1000 //otros_cursos_max / 10

diferencias_con_prom = 100 - dalto_curso/otros_cursos_prom * 100


tiempo_vacio_promedio = 100 - otros_cursos_prom * 1000 // crudo_promedio / 10

tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10
#diferencias de porcentajes
print(f'el curso de dalto dura un {diferencias_con_min}% menos que el mas rapido')

print(f'el curso de dalto dura un {diferencias_con_max}% menos que el mas lento')

print(f'el curso de dalto dura un {diferencias_con_prom}% menos que el promedio')
print("-----------")
#tiempo vacio promedio
print(f'un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio')
print(f'el curso de dalto elimina un {tiempo_vacio_dalto}% de tiempo vacio')
print("-----------")
#diferencias del curso de 10 horas
print(f'ver 10 horas de este curso equivale a ver {otros_cursos_prom *100 // dalto_curso /10 } horas de otro curso')
print(f'ver 10 horas de otros curso equivale a ver {dalto_curso *100 // otros_cursos_prom /10 } horas de este curso')


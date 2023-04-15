import random

diccionario = {
    "sustantivos": ["hundo", "kato", "domo", "arbo", "tablo", "knabo", "knabino", "pomo", "libro", "komputilo", "floro", "aĉulo", "pano", "teo", "kafao"],
    "adjetivos": ["granda", "bela", "flava", "blua", "malvarma", "varma", "nova", "malnova", "dika", "malgrasa", "molasa", "malseka", "dolĉa", "akra", "dumtempa"],
    "verbos": ["manĝi", "kuri", "danci", "kanti", "lerni", "paroli", "fali", "stari", "veni", "iri", "legi", "skribi", "dormi", "vivi", "pafi"],
    "adverbios": ["hodiaŭ", "jam", "tre", "nun", "baldaŭ", "tuj", "ĉiam", "ofte", "jam ne", "ne plu", "ĉiutage", "foje", "preskaŭ neniam", "vere"],
    "preposiciones": ["je", "en", "sur", "sub", "antaŭ", "post", "ĉe", "tra", "pro", "per", "sen", "dum"],
    "pronombres": ["mi", "vi", "li", "ŝi", "ĝi", "ni", "ili", "oni", "si", "ĉiu", "neniu", "iu", "io", "nenio", "tiu", "tio", "neniu"],
    "conjunciones": ["kaj", "aŭ", "sed", "do", "kvankam", "ĉar", "se", "anstataŭ", "malgraŭ", "tamen"],
    "interjecciones": ["ha", "ho", "nu", "ve", "jen"]
}


def generar_frase_simple(diccionario):
    sujeto = random.choice(diccionario["pronombres"])
    verbo = random.choice(diccionario["verbos"])
    return f"{sujeto} {verbo}."

def generar_frase_con_objeto(diccionario):
    sujeto = random.choice(diccionario["pronombres"])
    verbo = random.choice(diccionario["verbos"])
    objeto = random.choice(diccionario["sustantivos"])
    return f"{sujeto} {verbo} la {objeto}."

def generar_frase_con_adjetivo(diccionario):
    sujeto = random.choice(diccionario["pronombres"])
    verbo = random.choice(diccionario["verbos"])
    objeto = random.choice(diccionario["sustantivos"])
    adjetivo = random.choice(diccionario["adjetivos"])
    return f"{sujeto} {verbo} la {adjetivo} {objeto}."

def generar_frase_con_adverbio(diccionario):
    sujeto = random.choice(diccionario["pronombres"])
    verbo = random.choice(diccionario["verbos"])
    adverbio = random.choice(diccionario["adverbios"])
    return f"{sujeto} {verbo} {adverbio}."

def generar_frase_compleja(diccionario):
    sujeto1 = random.choice(diccionario["pronombres"])
    verbo1 = random.choice(diccionario["verbos"])
    sujeto2 = random.choice(diccionario["pronombres"])
    verbo2 = random.choice(diccionario["verbos"])
    objeto = random.choice(diccionario["sustantivos"])
    preposicion = random.choice(diccionario["preposiciones"])
    return f"{sujeto1} {verbo1} la {objeto}, {preposicion} {sujeto2} {verbo2}."
  
  def generar_frase_con_interjeccion(diccionario):
    interjeccion = random.choice(diccionario["interjecciones"])
    sujeto = random.choice(diccionario["pronombres"])
    verbo = random.choice(diccionario["verbos"])
    objeto = random.choice(diccionario["sustantivos"])
    return f"{interjeccion}! {sujeto} {verbo} la {objeto}."

def generar_frase_con_conjuncion(diccionario):
    sujeto1 = random.choice(diccionario["pronombres"])
    verbo1 = random.choice(diccionario["verbos"])
    sujeto2 = random.choice(diccionario["pronombres"])
    verbo2 = random.choice(diccionario["verbos"])
    objeto = random.choice(diccionario["sustantivos"])
    conjuncion = random.choice(diccionario["conjunciones"])
    return f"{sujeto1} {verbo1} la {objeto}, {conjuncion} {sujeto2} {verbo2}."


opciones = [
    generar_frase_simple, 
    generar_frase_con_objeto, 
    generar_frase_con_adjetivo, 
    generar_frase_con_adverbio, 
    generar_frase_compleja,
    generar_frase_con_interjeccion,
    generar_frase_con_conjuncion
]

frase_generada = random.choice(opciones)(diccionario)
print(frase_generada)

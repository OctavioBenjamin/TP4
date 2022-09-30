

class Proyecto:
    def __init__(self, usuario, repo, descri, fecha, leng, likes, tags, url):
        self.usuario = usuario
        self.repo = repo
        self.descri = descri
        self.fecha = fecha
        self.leng = leng
        self.likes = likes
        self.tags = tags
        self.url = url

    def __str__(self):
        linea = ""
        linea += '{:<30}'.format(self.usuario)
        linea += ' '
        linea += '{:<35}'.format(self.repo)
        linea += ' '
        linea += '{:<5}'.format(self.descri)
        linea += ' '
        linea += '{:<12}'.format(self.fecha)
        linea += ' '
        linea += '{:<18}'.format(self.leng)
        linea += ' '
        linea += '{:<7}'.format(self.likes)
        linea += ' '
        linea += '{:<220}'.format(self.tags)
        linea += ' '
        linea += '{:<25}'.format(self.url)
        return linea

def to_string(proyecto):
    return f"{proyecto.usuario}|{proyecto.repo}|{proyecto.descri}|{proyecto.fecha}|{proyecto.leng}|{proyecto.likes}|{proyecto.tags}|{proyecto.url}\n"
    

def to_proyecto(linea, lista_leng):
    r = linea.split("|")
    usuario = r[0]
    repo = r[1]
    descri = "  "
    fecha = r[3]
    leng = r[4]
    lista_leng.append(leng)
    likes = r[5]
    ch = 'k'
    likes = likes.rstrip(ch)
    #likes = likes[:-1]
    tags = r[6]
    url = r[7]
    proyecto = Proyecto(usuario, repo, descri, fecha, leng, likes, tags, url)
    return proyecto, lista_leng



class ElementoDeMatriz:
    def __init__(self, mes, tipo, proyectos):
        self.mes = mes
        self.tipo = tipo
        self.proyectos = proyectos

    def __str__(self):
        linea = ' '
        linea += '{:<11}'.format(self.mes)
        linea += ' '
        linea += '{:<10}'.format(self.tipo)
        linea += ' '
        linea += '{:<10}'. format(self.proyectos)
        linea += ' '
        return linea


    
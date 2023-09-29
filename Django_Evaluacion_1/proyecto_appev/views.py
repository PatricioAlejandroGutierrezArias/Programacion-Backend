from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'proyecto_appev/index.html')

def Viento(request):
    data = {    "titulo": "Viento",
                "categoria" :"viento",
                "producto1" :"Flauta",
                "producto2" :"Tuba",
                "producto3" :"Clarinete",
                "foto1":"viento1.jpg",
                "foto2":"viento2.jpg",
                "foto3":"viento3.jpg"
                }
    return render(request, 'proyecto_appev/producto.html',data)

def Cuerda(request):
    data = {    "titulo": "Cuerda",
                "categoria" :"cuerda",
                "producto1" :"Guitarra",
                "producto2" :"Violin",
                "producto3" :"Violonchelo",
                "foto1":"cuerda1.jpg",
                "foto2":"cuerda2.jpg",
                "foto3":"cuerda3.jpg"
                }
    return render(request, 'proyecto_appev/producto.html',data)

def Percusion(request):
    data = {    "titulo": "Percusion",
                "categoria" :"percusion",
                "producto1" :"Bateria",
                "producto2" :"Tambor",
                "producto3" :"Pandero",
                "foto1":"percusion1.jpg",
                "foto2":"percusion2.jpg",
                "foto3":"percusion3.jpg"
                }
    return render(request, 'proyecto_appev/producto.html',data)

def Usuario(request):
    data = {    "titulo": "Usuario",
                "ID" :"123",
                "nombre" :"Patricio Alejandro",
                "apellido" :"Gutiérrez Arias",
                "email" :"patricio.gutierrez@inacapmail.cl",
                "foto1":"usuario1.jpg"
                }
    return render(request, 'proyecto_appev/usuario.html',data)



def Descripcion(request,categoria,producto):
    descripciones = {
        "viento":{"Flauta":"Una flauta es un instrumento musical de viento que se caracteriza por su diseño alargado y estrecho. Por lo general, está hecha de metal, madera o plástico y consta de un tubo con agujeros a lo largo de su cuerpo. Para producir sonido, el intérprete sopla aire a través de una embocadura en un extremo del tubo y utiliza los dedos para abrir y cerrar los agujeros, lo que modifica la longitud efectiva del tubo y, por lo tanto, la altura del sonido producido. Las flautas se han utilizado en diversas culturas y géneros musicales a lo largo de la historia y pueden generar melodías suaves y expresivas gracias a su capacidad para controlar la afinación y el volumen con precisión.",
                     "Tuba":"Una tuba es un instrumento musical de viento-metal que se destaca por su gran tamaño y su forma curva. Por lo general, está hecha de latón y consta de un largo tubo enrollado en forma de espiral con una campana ancha en el extremo opuesto. La tuba se toca soplando aire a través de una boquilla en la parte superior del tubo y utilizando las manos para presionar y liberar válvulas que cambian la longitud efectiva del tubo, lo que permite al músico producir una variedad de notas y tonos. La tuba es conocida por su poderoso sonido grave y su papel fundamental en las secciones de viento-metal de las orquestas y bandas, proporcionando una base sólida y resonante en la música. Su timbre profundo y su capacidad para generar notas bajas hacen de la tuba un instrumento fundamental en la música clásica, así como en géneros como el jazz y la música de banda.",
                     "Clarinete":"El clarinete es un instrumento musical de viento-madera reconocido por su diseño elegante y sonido melódico. Construido principalmente de granadillo o plástico, consta de un cuerpo alargado con llaves y agujeros que permiten al músico, al soplar a través de una boquilla en la parte superior, generar una amplia gama de notas y tonos. Su tono suave y cálido lo hace ideal para una variedad de géneros musicales, desde la música clásica hasta el jazz y la música popular. Es un componente esencial en orquestas, bandas y grupos de cámara, apreciado por su versatilidad y capacidad para expresar emociones musicales sutiles y expresivas."},
        "cuerda":{  "Guitarra":"Una guitarra es un instrumento musical de cuerda que consta de un cuerpo alargado con una caja de resonancia y un mástil con trastes. Por lo general, tiene seis cuerdas que se tocan al puntearlas o rasguearlas con los dedos o una púa. Las vibraciones de las cuerdas generan sonido que se amplifica a través de la caja de resonancia, produciendo una amplia variedad de tonos y notas. La guitarra es uno de los instrumentos más populares y versátiles del mundo, utilizado en una amplia gama de géneros musicales, desde el rock y el pop hasta la música clásica y el folk.",
                    "Violin":"El violín es un instrumento musical de cuerda frotada que se caracteriza por su forma elegante y su sonido expresivo. Consiste en un cuerpo con forma de reloj de arena, cuatro cuerdas afinadas en quintas y un mástil sobre el que se colocan los dedos para cambiar la afinación. Se toca pasando un arco con cerdas sobre las cuerdas o mediante técnicas de pizzicato (pulsando las cuerdas con los dedos). El violín es conocido por su capacidad para producir melodías emotivas y es ampliamente utilizado en la música clásica, así como en géneros como el jazz y la música folclórica. Su sonido rico y versátil lo convierte en uno de los instrumentos más icónicos y apreciados en todo el mundo.",
                    "Violonchelo":"El violonchelo es un instrumento musical de cuerda frotada que destaca por su tamaño y su sonido profundo y resonante. Tiene una forma alargada con un cuerpo hueco, cuatro cuerdas afinadas en quintas y se toca sosteniéndolo entre las piernas y utilizando un arco con cerdas para producir sonido al frotar las cuerdas. El violonchelo es parte fundamental de la sección de cuerdas de una orquesta y es apreciado por su capacidad para expresar melodías emotivas y graves. Su versatilidad lo hace apto para una variedad de géneros musicales, desde la música clásica hasta la música contemporánea y el jazz."},
        "percusion":{   "Bateria":"La batería musical es un conjunto de instrumentos de percusión agrupados en un kit que incluye tambores, platillos y pedales. Los componentes esenciales de una batería suelen ser una caja, un bombo, varios tambores llamados toms y platillos como el hi-hat, el ride y el crash. Se toca utilizando baquetas o mazos, y el baterista coordina golpes en diferentes partes de la batería para crear ritmos y patrones rítmicos. La batería es fundamental en una amplia variedad de géneros musicales, desde el rock y el jazz hasta el pop y el funk, y aporta energía y ritmo a la música. Su versatilidad y capacidad para marcar el pulso hacen de la batería un elemento esencial en muchas bandas y grupos musicales.",
                        "Tambor":"El tambor es un instrumento de percusión simple pero poderoso. Consiste en un cilindro hueco cubierto con una membrana llamada parche, que se estira sobre uno o ambos extremos del cilindro. Se toca golpeando la membrana con las manos o con baquetas. El tambor puede variar en tamaño y forma, desde tambores pequeños y portátiles como el tambor de mano hasta tambores grandes y profundos como el bombo de una batería. Su sonido puede ser agudo o grave dependiendo del tamaño y la afinación del tambor. El tambor ha sido utilizado en diversas culturas y géneros musicales de todo el mundo y es esencial para la creación de ritmos y patrones rítmicos en la música.",
                        "Pandero":"El pandero es un instrumento de percusión de forma circular y relativamente pequeño, con una estructura de marco y una membrana estirada sobre una de sus caras. Esta membrana se golpea con los dedos o con la mano, mientras que la otra mano sostiene y agita el instrumento para producir un sonido característico de cascabeleo. El pandero suele tener pequeñas placas de metal llamadas platillos incrustadas en su marco, lo que agrega un tintineo adicional a su sonido. Es comúnmente utilizada en música folclórica, música tradicional y en una variedad de géneros musicales para aportar ritmo y textura. El pandero es conocida por su versatilidad y su capacidad para agregar un toque festivo y animado a la música."}
    }
    
    descripcion = descripciones.get(categoria, {}).get(producto, "descripcion no encontrada")

    
    data = {    "titulo": "Descripcion",
                "categoria" : categoria,
                "producto" : producto,
                "descripcion" : descripcion
                
                
                }
    return render(request, 'proyecto_appev/descripcion.html',data)
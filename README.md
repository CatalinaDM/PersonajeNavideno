
# Evaluación de la Unidad III --Personaje Navideño - Principios de IoT
## Nombre del personaje
Jack .El extraño mundo de Jack.

# Integrantes
| Asingación | Información |
|--|--|
| Alumno 1 | Delgado Manzano Carmen Catalina |
| Número de control | 1223100422 |
| Gupo | GDS0643 |

| Asingación | Información |
|--|--|
| Alumno 2 | Rodriguez Guerrero Juan Francisco |
| Número de control | 1223100422 |
| Gupo | GDS0643 |


## Índice
1. [Dibujo del prototipo](#dibujo-del-prototipo-a-desarrollar)
2. [Imagenes del proyecto final](#imagenes-del-proyecto-final)
3. [Codigo fuente](/codigo_fuente)
4. [Funcionalidades tecnicas](#funcionalidades-técnicas)
5. [Curso de JavaScript en NetAcad](#curso-javascript-en-netacad)
6. [TikTok](#video-tiktok)

---
# Dibujo del prototipo a desarrollar
- Coloca el dibujo a mano de la propuesta de prototipo a realizar.
<img src="https://github.com/user-attachments/assets/79cad305-b6c0-4b67-8c7d-225b1b2fdd36"/>

# Imagenes del proyecto final 
<img src="https://github.com/user-attachments/assets/73fc9bc0-eb24-4543-8c12-bb2069dbe7ed"/>
<img src="https://github.com/user-attachments/assets/13a845b7-500b-4803-92c6-59ffb3bdcfd2"/>
<img src="https://github.com/user-attachments/assets/dfc90555-fc38-4ebd-a52c-c09b6c4fef31"/>
<img src="https://github.com/user-attachments/assets/e8cff29d-e3ba-4b2a-bdea-2c0650179485"/>

# Funcionalidades técnicas 

### LUZ

- **¿En que se utilizaron?**:Encendido de la matriz, RGB en serie y LEDs para encender sus ojos.

                                                                                   
           -    **Descripción**:
                                 1.- El árbol de Navidad se decoró con luces RGB en serie, creando el efecto de una cascada. Al completar cada ciclo de luces, los colores cambiaban, y cada nivel de la cascada tenía colores diferentes, simulando un flujo 
                                 dinámico y colorido de una cascada en movimiento.


                                2.- La matriz se enciende con un mensaje que se controla con comunicación en NodeRed, este mensaje puede estar cambiando.


                                3.- Los LEDs en los ojos también se encienden y apagan, esos son de color blanco. 


  
- **Video de demostración**: [Enlace al video de demostración](https://drive.google.com/file/d/1h1Dn3R6HkuR31hK5Mm-WmFRk2f9UYmPS/view?usp=sharing)

---



### SONIDO


- **¿En que se utilizaron?**: Buzzer Pasivo
   
           -    **Descripción**: Al buzzer se le agrego código con melodias con una canción navideña que igualmente se controla para que encienda y apague con el NodeRed par que no este todo el tiempo la música. 

- - ** Video demostrativo**: [Enlace al video demostrativo](https://drive.google.com/file/d/1h5HTg_13BnU8y5nMm-cLB09lj92ETHKJ/view?usp=drive_link)

---

### MOVIMIENTO
- **¿En que se utilizaron?**: Servos 
   
           -    **Descripción**: El personaje de Jack tiene en sus manos una ramo de flores de noche buena, lo que hace es subirla y bajarlas, cuando las personas se acercan sube su brazo para entregarlas, cuando ya no detecta a nadie cerca las vuelve a                                    bajar.

- - ** Video demostrativo**: [Enlace al video demostrativo](https://drive.google.com/file/d/1hK7oSyW46Eggr1rBekW867unL8vVyHMt/view?usp=drive_link)

### SENSORES
- **¿En que se utilizaron?**: Sensor de distancia
   
           -    **Descripción**:  Para el proyecto, se está creando una representación del personaje Jack de la película El extraño mundo de Jack con varias funciones interactivas. Este muñeco navideño utiliza un sensor de distancia para detectar         
                                  personas. Cuando alguien se acerca en un rango de 1 metro, Jack moverá las manos y simulara entregar un ramo de flores de noche buena al público que este cerca,si la persona se aleja, las manos regresan a una posición 
                               neutral es decir bajara su mano. 

- - ** Video demostrativo**: [Enlace al video demostrativo](https://drive.google.com/file/d/1hK7oSyW46Eggr1rBekW867unL8vVyHMt/view?usp=drive_link)
  - 
---
### COMUNICACIÒN Node-RED y MQTT.

- **¿En que se utilizaron?**: Para encender y apagar las luces de los ojos de Jack, Para encender y apagar la música y para cambiar el mensaje a uno personalizado en la matriz. 
   
           -    **Descripción**:
                                  1.- Jack en sus ojos tiene unos LEDS de color blanco, estos pueden encenderse y apagarse mediante la comunicación con NodeRed, ya que se tiene un switch para activarlo o desactivarlos.

                                  2.- Para la música se encuentra un buzzer y al saber que todos los proyectos tendriían sonidos, decidimos controlar el encendido y apagado de la música mediante NodeRed.

                                  3.- Igualmente tenemos una matriz, donde se estaran mostrando mensajes de buenos decesos con tematica de navidad, pero en NodeRed puedes cambiar el mensaje para que diga lo que quieras, esta uno predeterminado pero puede                                        cambiar. 

- - ** Video demostrativo**: [Enlace al video demostrativo](https://drive.google.com/file/d/1hK7oSyW46Eggr1rBekW867unL8vVyHMt/view?usp=drive_link)
  - 

- **Carpeta**: [`Conexiones Node-Red`](conexiones_NodeRed)

### DISEÑO 
De fondo se encuentra un escenario de la la tematica de la pelicula "El extraño mundo de Jack" donde se ve la luna muy grande y ya que es el mundo de Jack suele ser muy oscuro se seleccionaron esos colores. 
Por otro lado tenemos la base que la decoramos con algodon para simular cuando Jack va al mundo de la navidad y esta repleto de nieve. 
Agregamos el árbol de navidad con mucha decoración e iluminación que va en cascada hasta llegar a la punta del árbol donde se enciende la estrella. 
Las orillas se decoro con escarchas para que le diera un toque más navideño. 
El muñeco de Jack se dejo con la vestimenta tradicional que lo caracteriza, ya que en unas escenas sale de Santa Claus, pero nosotros lo dejamos asi ya que es la escencia de la pelicula y por ello le dimos el escenario navideño ya que es algo que conocio e incorporo a su propio mundo, por ello solo se le agrega un gorro de navidad. 
En la esquina superioro derecha se agregaron decoraciones navideñas. 


|<img src="https://github.com/user-attachments/assets/e8cff29d-e3ba-4b2a-bdea-2c0650179485" width="230" height="300" />|<img src="https://github.com/user-attachments/assets/987af168-68b5-4b57-9382-c505a39e69e0" width="230" height="300" />  | <img src="https://github.com/user-attachments/assets/3222eafa-d5be-458a-9fe8-f374e4064ca0" width="230" height="300" /> | <img src="https://github.com/user-attachments/assets/d5562e59-e852-4174-b167-8382eb2e82df" width="230" height="300" /> | <img src="https://github.com/user-attachments/assets/d1c55dfc-d8a5-4d94-8fdc-fbb10b4ec686" width="230" height="300" />|


### Curso JavaScript en NetAcad

Avance documentado en el curso de JavaScript en NetAcad.
## Módulo 1 
<img src="https://github.com/user-attachments/assets/27251d98-d34f-45e6-b9a4-b1ff27fab61a"/>

## Módulo 2
<img src="!https://github.com/user-attachments/assets/cbcdc447-dd0f-4a4f-95fd-3c28ffd45249"/>

## Módulo 3
<img src="https://github.com/user-attachments/assets/9af782bb-866f-4748-a501-4509df9e3a5f"/>

## Módulo 4
<img src="https://github.com/user-attachments/assets/f1c5b10a-7760-4677-9fce-7e2efe55568b"/>

## Módulo 5
<img src="https://github.com/user-attachments/assets/b5e22c13-8ba1-456e-8c60-1fac41e756b9"/>

## Módulo 6
<img src="https://github.com/user-attachments/assets/fa1b8b44-e372-476c-b532-9649d03dbdac"/>

## Examen final del Curso
<img src="https://github.com/user-attachments/assets/56455999-6546-4f45-a830-713782b4ce3b"/>

## Porcentaje  de evaluaciones finales del Módulo 1 a  Módulo 4 y examen Final del Curso
<img src="https://github.com/user-attachments/assets/dbde5e37-0b8a-4655-bdeb-ddae64065694"/>

---

### Video TikTok

**Video de demostración**: [Enlace al video de demostración](https://vm.tiktok.com/ZMkeNUwAq/)


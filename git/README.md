# Git       
En la acutalidad, cuando se programa se suele almacenar os programas na "nube". Porque xeralmente na creación habera implicadas varias personas para controlar todo isto empregase un sistema de control de version. É como unha especie de nube pero leva un rexistro dos cambios, ten opcion dde traballar en paralelo e ferramentas especificos.
Para usar git hay que instalalo no ordenador e deberiamos en principio establecer o noso usuario e o noso email:

- `git config --user.name "nombre"`

- `git config --user.email "correo"`

Deberemos crear un cartafol onde vai o repositorio e dentro del inicializar o repositorio con *git init*.
### GIT ten tres etapas:
1. Zona de traballo: cando estamos cambiando o codigo dos archivos.

2. Área de preparacion: transicion entre zona de traballo e repositorio.

3. Repositorio: é o acumulado dos cambios.

Si queremos pillar o codigo do repositorio para traballar temos que facer un checkout, pero para subir o código modificado ao repositorio hai que facelo en duas fases: unha primeira de *stage* (preparación), onde se rexistra a información dos cambios, e despois facemos un commit, que é modificar o repositorio con estes cambios rexistrados. Esto chamase **ciclo de traballo en git**.


from guizero import App , Text, PushButton,yesno, warn, info, MenuBar, Picture
app = App(title="trashbot ", height = 500, width = 700, bgcolor = "black")

#Bienvenida al programa "Trashbot"
join_the_trashbot= yesno("Welcome", "Do you want to join trashbot?")

if join_the_trashbot == True:
  info("Welcome", "Thank you!")
else:
  app.destroy()

message = Text(app, text="Join trashbot", color = "red")

def push ():
  print("start")
  
boton  = PushButton(app, command= push, icon= "ASIMO.gif")

def edit_function():
    print("Edit option")
def file_function():
    print("File option")

def edit_function():
    print("Edit option")

#app = App()
menubar = MenuBar(app,
                  toplevel=["Robot", "Contaminacion en el mundo", "ventajas del Trashbot","como podemos fomentar esto"],
                  options=[
                      [ ["mecanismo", file_function], ["electronica y programacion", file_function] ],
                      [ ["cuanto afecta", edit_function], ["tipos de contaminacion", edit_function] ],
                      [ ["Analiza y separa la basura", file_function], ["mantiene limpio el entorno", file_function] ],
                      [ ["metodos de educacion ambiental", edit_function], ["En redes sociales ya que tienen demasiado impacto mundial", edit_function] ]
                  ])



app.display()

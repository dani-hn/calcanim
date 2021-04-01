from sys import float_repr_style
from manimlib.imports import *

############################################################
################ coordenadas polares y cartesianas #########
############################################################
#Aparece en excel como Campos lineales, sin embargo el vídeo se dividirá en dos partes para que no sea tan largo


class Polares_y_Cartesianas(Scene):

    def parte1 (self):
        titulo=TextMobject('''Coordenadas polares y \n
                                cartesianas''').scale(2)
        text1=TextMobject('''En el curso de Cálculo Vectorial Integral \n
                             se suele trabajar en espacios tipo $\\mathbb{R}^{n}$,\n
                              así que siempre tendremos una base con la cual trabajar \n
                               y con ello un sistema de coordenadas.''')
        text2=TextMobject('''En diversas ocasiones es más práctico optar por \n
                             unas coordenadas que por otras, \n
                             así que es importante dominar los cambios de \n
                             coordenadas.''')
        text3=TextMobject("Veamos el caso de $\\mathbb{R}^{2}$.").move_to(3*UP)
        text4=TextMobject('''Las coordenadas usuales en este espacio son \n
                                las polares ''','''y cartesianas.''').move_to(3*UP)
        text5=TextMobject('''Podemos definir una función que transforme un \n
                            vector de unas coordenadas a otras.''').move_to(3*UP)
        text6=TextMobject('''Tómate un segundo para pensar en la función \n
                                que transforme un vector en coordenadas polares \n
                                a cartesianas.''').move_to(2.5*UP) 


        linea1=Arrow([-4,0,0],[4,0,0])
        linea2=Arrow([0,-3,0],[0,3,0])
        lineas=VGroup(linea1,linea2).move_to(1*DOWN)
        linea1_1=Arrow([-4,0,0],[4,0,0])
        linea2_1=Arrow([0,-3,0],[0,3,0])
        Plano1=VGroup(linea1_1,linea2_1).scale(0.7)
        Plano1.move_to(1*DOWN+3*LEFT)
        linea1_2=Arrow([-4,0,0],[4,0,0])
        linea2_2=Arrow([0,-3,0],[0,3,0])
        Plano2=VGroup(linea1_2,linea2_2).move_to(1*DOWN-3*LEFT).scale(0.7)

        #Es posible moficar los siguientes parametros para mostrar un vector diferente
        a=1
        b=1.2
        #########
        ap=np.cos(a)/2
        bp=np.sin(b)/2
        vector1=Arrow([0,-1,0],[a,b,0],color=BLUE_E,buff=0)
        r=TextMobject("r").next_to(vector1,LEFT,buff=-0.3)
        angulo=Arc(fill_opacity=0,stroke_opacity=1, angle=np.arctan(b/a),radius=a/2,arc_center=[0,-1,0],buff=0)
        angulo_l=TextMobject("$\\theta$").next_to(angulo,UP+RIGHT,buff=0.2)
        angs=VGroup(angulo,angulo_l)

        #cartesianas
        brazox=Brace(vector1,RIGHT)
        x=TexMobject(r"x").next_to(brazox,RIGHT,buff=0.1)
        xs=VGroup(brazox,x)
        brazoy=Brace(vector1,UP)
        y=TexMobject(r"y").next_to(brazoy,UP,buff=0.1)
        ys=VGroup(y,brazoy)
        
        #Para la funcion
        vector1_1=Arrow([0,0,0],[a,b,0],color=BLUE_E,buff=0).scale(0.7).move_to((1-b*0.7/2)*DOWN+(3-a*0.7/2)*LEFT)
        r_1=TextMobject("r").next_to(vector1_1,LEFT,buff=-0.3)
        angulo_1=Arc(fill_opacity=0,stroke_opacity=1, angle=np.arctan(b/a),radius=a/2,arc_center=1*DOWN+3*LEFT).scale(0.7)
        angulo_l1=TextMobject("$\\theta$").next_to(angulo_1,0.2*UP+RIGHT,buff=0.2)
        Grupo1=VGroup(angulo_1,angulo_l1,vector1_1,r_1)

        #flabel
        f=TextMobject("$f$")
        farrow=Arrow([-0.5,0,0],[0.5,0,0],buff=0)
        f.next_to(farrow,UP,buff=0.3)

        #cartesianas        
        vector1_2=Arrow([0,0,0],[a,b,0],color=BLUE_E,buff=0).scale(0.7).move_to((1-b*0.7/2)*DOWN+(-3-a*0.7/2)*LEFT)
        brazox_1=Brace(vector1_2,RIGHT)
        x_1=TexMobject(r"x").next_to(brazox_1,RIGHT,buff=0.1)
        brazoy_1=Brace(vector1_2,UP)
        y_1=TexMobject(r"y").next_to(brazoy_1,UP,buff=0.1)
        Grupo2=VGroup(vector1_2,y_1,brazoy_1,x_1,brazox_1)

        D=Dot(color=RED).move_to(1*DOWN-3*LEFT)
        D2=Dot(color=RED).move_to(1*DOWN+3*LEFT)

        Grupo3=VGroup(Grupo1,Grupo2,Plano1,Plano2,f,farrow)





        self.play(Write(titulo))
        self.wait(3.5)
        self.play(FadeOut(titulo))
        self.play(Write(text1))
        self.wait(14)
        self.play(FadeOut(text1))
        self.play(Write(text2))
        self.wait(11)
        self.play(FadeOut(text2))
        self.wait()
        self.play(Write(text3))
        self.wait(4)
        self.play(Write(lineas))
        self.play(FadeOut(text3))
        self.play(Write(text4[0]))
        self.play(Write(vector1))
        self.play(Write(r),ShowCreation(angulo),Write(angulo_l))
        self.wait(5)
        self.play(Write(text4[1]))
        self.wait(3)
        self.play(ReplacementTransform(r,ys),ReplacementTransform(angs,xs))
        self.play(FadeOut(text4))
        self.play(Write(text5),FadeOut(lineas),FadeOut(ys),FadeOut(xs),FadeOut(vector1))
        self.play(ShowCreation(Plano1),ShowCreation(Plano2))
        self.play(ShowCreation(Grupo1))
        self.play(ShowCreation(f))
        self.play(ShowCreation(farrow))
        self.play(ShowCreation(Grupo2))
        self.wait(7)
        self.play(FadeOut(text5))
        self.play(Write(text6))
        self.wait(9)
        self.play(FadeOut(text6),FadeOut(Grupo3))
    def parte2 (self):
        #se puede modificar r y a
        r=2
        a=4
        #####
        theta=np.pi/a
        ## se puede modificar r1 y a1
        r1=1
        a1=1
        ####
        theta1=np.pi/a1



        text7=TextMobject('''Considera un vector en coordenadas polares ($\\vec{\\rho}=(r,\\theta)$),\n
                             por ejemplo $\\vec{\\rho}=($'''+str(r)+''',$\\pi/$'''+str(a)+''').''')
        text8=TextMobject("Veamos cómo se ve el vector en coordenadas cartesianas.").move_to(3*UP)
        text9=TextMobject("Notemos que $x=2\\cos(\\pi/4)$ y $y=2\\sin(\\pi/4)$.").move_to(3*UP)
        text10=TextMobject('''Entonces podemos definir la función que nos de el \n
                            cambio de coordenadas (de polares a cartesianas) como:
                             $$f:\\vec{\\rho}(r,\\theta)\\rightarrow\\vec{x}(x,y)$$  
                             $$f(\\vec{\\rho})=(r\\cos\\theta,r\\sin\\theta) $$''')
        text11=TextMobject('''Sin embargo, hay que tener cuidado con \n
                                el dominio de la función.''')
        text12=TextMobject('''Podemos entonces restringir el dominio \n
                         para que los ángulos queden unívocamente \n
                             determinados, $$\\theta \\in [0,2\\pi). $$''')
        text13=TextMobject('''Nota que si $0\\leq r$, entonces el vector cero \n
                            tiene muchas etiquetas en coordenadas polares, \n
                            a saber, $(0,\\theta)$.''').move_to(3*UP)
        text14=TextMobject('''De ahí que consideramos que el origen no tiene \n
                                    un ángulo asociado.''').move_to(3*UP)
        
        
        
        linea1=Arrow([-4,0,0],[4,0,0])
        linea2=Arrow([0,-3,0],[0,3,0])
        Plano=VGroup(linea1,linea2).move_to(1*DOWN)

        #Polares
        vector=Arrow([0,-1,0],[r*np.cos(theta),-1+(r*np.sin(theta)),0],buff=0,color=BLUE_C)
        radio=TexMobject(r"r="+str(r)).next_to(vector,LEFT,buff=-0.3)
        angulo=Arc(fill_opacity=0,stroke_opacity=1, angle=theta,radius=(r/2),arc_center=[0,-1,0],buff=0)
        angulo_l=TexMobject(r"\theta=\pi/"+str(a)).next_to(angulo,0*UP+RIGHT,buff=0.2)
        polares=VGroup(radio,angulo,angulo_l)
        #Cartesianas
        b_x=Brace(vector,RIGHT)
        x=TexMobject(r"x="+str(r)+r"\cos(\pi/"+str(a)+r")").next_to(b_x,RIGHT,buff=0.1)
        b_y=Brace(vector,UP)
        y=TexMobject(r"y="+str(r)+r"\sin(\pi/"+str(a)+r")").next_to(b_y,UP,buff=0.1)
        cartesianas=VGroup(y,x,b_y,b_x)
        
        vector_0=Dot(color=RED,radius=0.2).move_to(1*DOWN)

        vector1=Arrow([0,-1,0],[r*np.cos(theta),-1+(r*np.sin(theta)),0],buff=0,color=BLUE_C)

        


        self.play(Write(text7))
        self.wait(5)
        self.play(text7.shift,3*UP,runtime=6)
        self.play(ShowCreation(Plano))
        self.play(ShowCreation(vector))
        self.play(Write(polares))
        self.wait(6)
        self.play(FadeOut(text7),FadeOut(polares))
        self.play(Write(text8))
        self.play(Write(cartesianas))
        self.wait(8)
        self.play(FadeOut(text8))
        self.play(Write(text9))
        self.wait(10)
        self.play(FadeOut(Plano),FadeOut(text9),FadeOut(cartesianas),FadeOut(vector))
        self.play(Write(text10))
        self.wait(15)
        self.play(FadeOut(text10))
        self.play(Write(text11))
        self.wait(8)
        self.play(FadeOut(text11))
        self.play(Write(text12))
        self.wait(10)
        self.play(FadeOut(text12))
        self.play(Write(text13))
        self.play(ShowCreation(Plano))
        self.play(ShowCreation(vector_0))       
        self.wait(11)
        self.play(FadeOut(text13)) 
        self.play(Write(text14))
        self.wait(8)
        self.play(FadeOut(text14),FadeOut(Plano),FadeOut(vector_0))

    def parte3 (self):
        
        text15=TextMobject('''Si no restringimos el ángulo, tenemos por ejemplo \n
                            $(1,\\pi)$''','''$\\rightarrow(-1,0)$ ''','''\n 
                            $(1,3\\pi)$''','''$\\rightarrow(-1,0).$''').move_to(2.5*UP)
        #Ejes
        linea1_1=Arrow([-4,0,0],[4,0,0])
        linea2_1=Arrow([0,-3,0],[0,3,0])
        Plano1=VGroup(linea1_1,linea2_1).scale(0.7)
        Plano1.move_to(1*DOWN+3*LEFT)
        linea1_2=Arrow([-4,0,0],[4,0,0])
        linea2_2=Arrow([0,-3,0],[0,3,0])
        Plano2=VGroup(linea1_2,linea2_2).move_to(1*DOWN-3*LEFT).scale(0.7)
        

        #se pueden moficar los siguientes parámetros
        a=-1
        b=0
        r=1
        theta=np.pi
        ############


        #flabel
        f=TextMobject("$f$")
        farrow=Arrow([-0.5,0,0],[0.5,0,0],buff=0)
        f.next_to(farrow,UP,buff=0.3)
        fs=VGroup(f,farrow)

        #vectores 1
        vector1_1=Arrow([0,0,0],[a,b,0],color=RED,buff=0).scale(0.7).move_to((1-b*0.7/2)*DOWN+(3-a*0.7/2)*LEFT)
        r_1=TextMobject(r"r="+str(r)).next_to(vector1_1,LEFT+UP,buff=0.3)
        angulo_1=Arc(fill_opacity=0,stroke_opacity=1, angle=-theta,radius=a/2,arc_center=1*DOWN+3*LEFT).scale(0.7)
        angulo_l1=TexMobject(r"\theta=\pi").next_to(angulo_1,UP,buff=0.5)
        Grupo1=VGroup(angulo_1,angulo_l1,vector1_1,r_1)

        #en cartesianas #Cartesianas
        vector1_2=Arrow([0,0,0],[a,b,0],color=RED,buff=0).scale(0.7).move_to(((1-b*0.7/2))*DOWN+(3+a*0.7/2)*RIGHT)#(1-b*0.7/2)*DOWN+(3-a*0.7/2)*RIGHT)
        b_x=Brace(vector1_2,RIGHT)
        x=TexMobject(r"x="+str(r)+r"\cos(\pi)").next_to(b_x,RIGHT+DOWN,buff=0.1)
        b_y=Brace(vector1_2,UP)
        y=TexMobject(r"y="+str(r)+r"\sin(\pi)").next_to(b_y,UP,buff=0.1)
        cartesianas=VGroup(y,x,b_y,b_x)
        
        #segundo ejemplo
        r_3=TextMobject(r"r="+str(r)).next_to(vector1_1,LEFT+UP,buff=0.3)
        angulo_3=Arc(fill_opacity=0,stroke_opacity=1, angle=-theta-2*np.pi,radius=a/2,arc_center=1*DOWN+3*LEFT).scale(0.7)
        angulo_l3=TexMobject(r"\theta=3\pi").next_to(angulo_1,UP,buff=0.5)
        Grupo2=VGroup(angulo_3,angulo_l3,vector1_1,r_3)

        #en cartesianas #Cartesianas
        x2=TexMobject(r"x="+str(r)+r"\cos(3\pi)").next_to(b_x,RIGHT+DOWN,buff=0.1)
        y2=TexMobject(r"y="+str(r)+r"\sin(3\pi)").next_to(b_y,UP,buff=0.1)
        cartesianas1=VGroup(y2,x2,b_y,b_x,vector1_2)

        self.play(ShowCreation(Plano1),ShowCreation(Plano2))
        self.play(Write(text15[0]))
        self.play(ShowCreation(Grupo1))
        self.play(Write(text15[1]))
        self.play(ShowCreation(fs))
        self.play(ShowCreation(vector1_2))
        self.play(ShowCreation(cartesianas))
        self.play(FadeOut(cartesianas),FadeOut(fs),FadeOut(Grupo1))
        self.wait(7)
        self.play(Write(text15[2]))
        self.play(ShowCreation(Grupo2))
        self.play(ShowCreation(text15[3]))
        self.play(ShowCreation(fs))
        self.play(ShowCreation(cartesianas1))
        self.wait()
        self.wait(7)
        self.play(FadeOut(cartesianas1),FadeOut(Grupo2),FadeOut(fs),
                FadeOut(Plano1),FadeOut(Plano2),FadeOut(text15))    

    def parte4 (self):
        #se pueden modificar los siguientes parámetros para usar como ejemplo otro vector
        x=2
        y=1
        ##########3

        text16=TextMobject('''Para el cambio de coordenadas de cartesianas a \n
                                polares, considera $\\vec{x}=($'''+str(x)+''','''+str(y)+''')''')
        text17=TextMobject('''Puedes notar que \n  
                            $r=\\sqrt{2^2+1^2} \ \ \ y \ \ \ \\theta=\\tan^{-1}\\left(\\frac{1}{2}\\right).$''').move_to(3*UP)
        text18=TextMobject('''Por lo que podríamos pensar que la función \n
                                de cambio de coordenadas es 
                                $$g(\\vec{x})=\\left(\\sqrt{x^2+y^2},\\tan^{-1}\\left(\\frac{y}{x}\\right)\\right)$$''','''\n
                                Y casi...''')
        text19=TextMobject('''Debemos hacer un pequeño ajuste en la función \n
                                 previamente definida.''').move_to(3*UP)#,'''\n
        text19_1=TextMobject('''Ya que nuestra función no considera muchos \n
                                vectores, entre ellos $(0,0)$ y $(r,\\pi/2)$.''').move_to(2.5*UP)
        text20=TextMobject('''Si tomamos  $h(x)=(\\sqrt{x^2+y^2},\\theta)$ \n
                                            Donde''').move_to(3*UP)
        #Objetos para definir el texto de theta
        text21_m=TexMobject(r'''{\begin{matrix} 
                                \tan^{-1}\left(\frac{y}{x}\right) & si & x>0 \ \ \text{y} \ \ y \geq0\\
                                                                &        &  \\
                                \frac{\pi}{2} & \text{si} & x=0  \ \ \text{y} \ \ y >0\\
                                &        &  \\
                                \tan^{-1}\left(\frac{y}{x}\right)+\pi & \text{si} & x<0 \\
                                &        &  \\
                                \frac{3\pi}{2} & \text{si} & x=0 \ \ \text{y} \ \ y <0\\
                                &        &  \\
                                \tan^{-1}\left(\frac{y}{x}\right)+2\pi & \text{si} & x>0 \ \  \text{y} \ \ y<0 \end{matrix}}''').move_to(0.5*RIGHT+0.8*DOWN)
        text21_b=Brace(text21_m,LEFT)#.next_to(text20,LEFT,buff=0.5)
        text21_t=TexMobject(r"\theta=").next_to(text21_b,LEFT,buff=0.1)    
        text21=VGroup(text21_m,text21_b,text21_t)       

        text22=TextMobject('''Así podemos pasar de coordenadas polares a cartesianas,\n
                                 sin ningún problema. ''')
        text23=TextMobject('''¡Ya conocemos las funciones que nos permiten \n
                            pasar de coordenadas cartesianas a polares y viceversa.!''')

        
        #Un solo eje
        linea1=Arrow([-4,0,0],[4,0,0])
        linea2=Arrow([0,-3,0],[0,3,0])
        Plano=VGroup(linea1,linea2).move_to(1*DOWN)
        vector=Arrow([0,-1,0],[x,-1+y,0],buff=0,color=BLUE_C)

        #labels catersianas
        x_b=Brace(vector,RIGHT)
        x_l=TexMobject(r"x="+str(x)).next_to(x_b,RIGHT,buff=0.1)
        y_b=Brace(vector,UP)
        y_l=TexMobject(r"y="+str(y)).next_to(y_b,UP,buff=0.1)
        cartesianas=VGroup(y_b,x_b,y_l,x_l)     
        xs=VGroup(x_b,x_l)
        ys=VGroup(y_b,y_l)

        #labels en polares
        r=(x**2+y**2)**(1/2)
        r_1=DecimalNumber(r, num_decimal_places=1).move_to(vector.get_center()+(x/4)*LEFT+0.1*UP)#next_to(vector,LEFT,buff=0.2)#move_to((x/80)*LEFT+(y/28)*UP)
        radio=TexMobject(r"r=").next_to(r_1,LEFT,buff=0.5)          
        rs=VGroup(r_1,radio)

        if x>0 and y!=0:
            theta=np.arctan(y/x)
        if x==0 and y>0:
            theta=np.pi/2
        if x<0:
            theta=np.arctan(y/x)+np.pi
        if x==0 and y<0:
            theta=np.arctan(y/x)+2*np.pi
        
        angulo=Arc(fill_opacity=0,stroke_opacity=1, angle=theta,radius=(r/2),arc_center=[0,-1,0],buff=0)
        ###
        angulo_l=TexMobject(r"\theta=").move_to(angulo.get_center()+(x/4+0.1)*RIGHT)#next_to(angulo,RIGHT+0*UP,buff=0.3)#next_to(angulo,(r/30*np.sin(theta/2))*UP+RIGHT,buff=0.3)
        theta_1=DecimalNumber(theta, num_decimal_places=1).next_to(angulo_l,(x/((x**2)**(1/2)))*RIGHT,buff=0.1)
        thetas=VGroup(theta_1,angulo_l,angulo)
        polares=VGroup(radio,r_1,angulo,angulo_l,theta_1)
        

        y2=ValueTracker(0.8)
        vector_1=Arrow([0,-1,0],[0,-1,0],color=BLUE_C,buff=0)      #  t1_2f=0.3  
        def mov_vector (obj):
            y = y2.get_value()
            vector_1.become(Arrow([0,-1,0],[0,y-1,0],color=BLUE_C,buff=0))

        vector_1.add_updater(mov_vector)


        vector_0=Dot(color=RED,radius=0.2).move_to(1*DOWN)
            

        self.play(Write(text16))
        self.wait()
        self.play(text16.shift,3*UP,runtime=6)
        self.play(ShowCreation(Plano))
        self.play(ShowCreation(vector),ShowCreation(cartesianas))
        self.wait(8)
        self.play(FadeOut(text16))
        self.play(Write(text17))
        self.play(ReplacementTransform(xs,rs),ReplacementTransform(ys,thetas))
        self.wait(8)
        self.play(FadeOut(vector),FadeOut(Plano),FadeOut(cartesianas),FadeOut(polares),
                    FadeOut(text17))
        self.play(Write(text18[0]))
        self.wait(10)
        self.play(Write(text18[1]))
        self.wait(5)
        self.play(FadeOut(text18))
        self.play(ShowCreation(Plano))
        self.play(ShowCreation(text19))
        self.wait(8)
        self.play(FadeOut(text19))
        self.play(Write(text19_1))
        self.play(ShowCreation(vector_0))
        self.play(ReplacementTransform(vector_0,vector_1))
        self.play(y2.set_value, 2,run_time=10)
        self.wait(5)
        self.play(FadeOut(text19_1))
        self.play(FadeOut(Plano),FadeOut(vector_1))
        self.play(Write(text20))
        self.play(Write(text21))
        self.wait(20)
        self.play(FadeOut(text21),FadeOut(text20))
        self.play(Write(text22))
        self.wait(8)
        self.play(FadeOut(text22))
        self.play(Write(text23))
        self.wait(9)
        self.play(FadeOut(text23))

    def construct(self):
        self.parte1()
        self.parte2()
        self.parte3()
        self.parte4()





##########################################################################
############## Funciones de R^2 en R^3: superficies parametrizadas ########
############################################################################

###PARA ESTA CLASE ES NECESARIO APLICAR LA SOLUCION A LOS VECTORES 3D, TAL COMO EN LA SIGUIENTE LIGA ###
###https://github.com/3b1b/manim/issues/774###
class superficies_parametrizadas (ThreeDScene, Scene):
    def setup(self):
        Scene.setup(self)
        ThreeDScene.setup(self)
    def FadeOutWrite3D(self,objeto1,objeto2):
        self.play(FadeOut(objeto1))
        self.acomodar_textos(objeto2)
    def acomodar_textos(self,objeto):
        self.add_fixed_in_frame_mobjects(objeto)
        self.play(Write(objeto))
    def superficie(self):
        superficie = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                2*math.exp(-1*(u**2+v**2))
            ]),v_min=-3,v_max=3,u_min=-3,u_max=3,fill_color=PURPLE_E,fill_opacity=0.75,
            resolution=(30, 30))
        return superficie
    def punto3D(self):
        bola = ParametricSurface(
            lambda u, v: np.array([
                0.075*np.cos(v) * np.sin(u),
            0.075*np.sin(v) * np.sin(u),
            0.075*np.cos(u)
            ]),v_min=0,v_max=TAU,u_min=0.001,u_max=PI-0.001,
            resolution=(24,24),fill_opacity=1,stroke_color=RED,fill_color=RED)
        return bola
    def PrimeraEscena(self):
        texto_1 = TextMobject('''Sea $\\sigma$ la parametrización de una superficie, \n
                                definida de la siguiente forma''').move_to(1*UP)
        texto_2_1 = TexMobject(r"\sigma=(\sigma_1,\sigma_2,\sigma_3):[-3,3]\times[-3,3]\in\mathbb{R}^2\to\mathbb{R}^3").next_to(texto_1,1*DOWN)
        texto_2_2 = TexMobject(r"\sigma(x,y)=(x,y,2e^{-(x^2+y^2)})").next_to(texto_2_1,DOWN)
        texto_2 = VGroup(texto_2_1,texto_2_2)
        
        #EJES
        axes = ThreeDAxes(x_min=-3.5,x_max=3.5,y_min=-3.5,y_max=3.5,z_min=-1,z_max=3,num_axis_pieces= 30)
        #Superficie
        superficie = self.superficie()

        self.play(Write(texto_1))
        self.wait(5)
        self.play(Write(texto_2))
        self.wait(5)
        self.play(FadeOut(texto_1))
        self.play(
            texto_2.shift,3.5*UP
        )
        self.add_fixed_in_frame_mobjects(texto_2)
        self.wait(0.5)
        self.move_camera(phi=70 * DEGREES,theta=-30*DEGREES,frame_center=(0,0,1))
        self.play(ShowCreation(axes))
        self.play(ShowCreation(superficie))
        self.wait(4)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.move_camera(phi=0,theta=-90*DEGREES,frame_center=(0,0,0))
    def SegundaEscena(self):
        texto_1 = TextMobject('''Consideremos la matriz jacobiana o derivada \n
                                    de $\\sigma$, definida como''').move_to(3*UP)
        texto_2 = TexMobject(r"""D\sigma(\hat{x}_0)=\begin{pmatrix} \dfrac{\partial \sigma_1}{\partial x}(\hat{x}_0) &  \dfrac{\partial \sigma_1}{\partial y}(\hat{x}_0)  \\ \dfrac{\partial \sigma_2}{\partial x}(\hat{x}_0) & \dfrac{\partial \sigma_2}{\partial y}(\hat{x}_0) \\ \dfrac{\partial \sigma_3}{\partial x}(\hat{x}_0) & \dfrac{\partial \sigma_3}{\partial y}(\hat{x}_0)\end{pmatrix}""")
        texto_3 = TextMobject("En el ejemplo, tomemos $\\hat{x}_0=(0.2,0.2)$").move_to(3*UP)
        texto_4 = TexMobject(r"""\text{Entonces, } D\sigma(\hat{x}_0)=\begin{pmatrix} 1 & 0 \\ 0 & 1 \\ -0.74 & -0.74  \end{pmatrix}""").move_to(2.5*UP)
        texto_5 = TextMobject(''' A partir de la matriz $D\\sigma(\\hat{x}_0)$, es posible\n
                                calcular las derivadas parciales de $\\sigma$ en $\\hat{x}_0$ ''').move_to(3*UP)
        texto_6 = TexMobject(r"""\dfrac{\partial \sigma}{\partial x}(\hat{x}_0)=\begin{pmatrix} 1 & 0 \\ 0 & 1 \\ -0.74 & -0.74  \end{pmatrix}\begin{pmatrix} 1 \\ 0 \end{pmatrix}=\begin{pmatrix} 1 \\ 0 \\ -0.74 \end{pmatrix}""").move_to(2.5*UP)
        texto_7 = TexMobject(r"""\dfrac{\partial \sigma}{\partial y}(\hat{x}_0)=\begin{pmatrix} 1 & 0 \\ 0 & 1 \\ -0.74 & -0.74  \end{pmatrix}\begin{pmatrix} 0 \\ 1 \end{pmatrix}=\begin{pmatrix} 0 \\ 1 \\ -0.74 \end{pmatrix} """).move_to(2.5*UP)
        texto_8 = TextMobject(''' Los vectores $\\dfrac{\\partial \\sigma}{\\partial x}(\\hat{x}_0)$ y $\\dfrac{\\partial \\sigma}{\\partial y}(\\hat{x}_0)$ son vectores tangentes\n
                                a la superficie en el punto $\\sigma(\\hat{x}_0)$''').move_to(3*UP)
        texto_9 = TextMobject(''' Definimos $\\dfrac{\\partial \\sigma}{\\partial x}(\\hat{x}_0) \\times \\dfrac{\\partial \\sigma}{\\partial y}(\\hat{x}_0)$ como el vector normal a la\n
                                superficie en $\\sigma(\\hat{x}_0)$, inducida por la parametrización $\\sigma$ ''').move_to(3*UP)
        texto_10 = TextMobject(''' Este vector genera un plano tangente a la superficie en $\\sigma(\\hat{x}_0)$ ''').move_to(3*UP)
        texto_11 = TextMobject(''' Si $\\hat{x}_0$ corresponde a un punto crítico de $\\sigma$, puede ocurrir que\n
                                $\\dfrac{\\partial \\sigma}{\\partial x}(\\hat{x}_0) =\\vec{0}= \\dfrac{\\partial \\sigma}{\\partial y}(\\hat{x}_0)$ y entonces la superficie no tiene\n
                                plano tangente definido en el punto. ''').move_to(2.5*UP)
        texto_12 = TextMobject('''Lo mismo ocurre si las parciales son linealmente dependientes.\n
Nuestro ejemplo no tiene puntos críticos.''').move_to(3*UP)
        etiqueta_1 = TexMobject(r"""\dfrac{\partial \sigma}{\partial x}(\hat{x}_0)=\begin{pmatrix} 1 \\ 0 \\ -0.74 \end{pmatrix} """).scale(0.75).set_color(PINK).move_to(4*RIGHT)
        etiqueta_2 = TexMobject(r"""\dfrac{\partial \sigma}{\partial y}(\hat{x}_0)=\begin{pmatrix} 0 \\ 1 \\ -0.74 \end{pmatrix} """).scale(0.75).set_color(YELLOW_E).next_to(etiqueta_1,DOWN)
        #EJES
        axes = ThreeDAxes(x_min=-3.5,x_max=3.5,y_min=-3.5,y_max=3.5,z_min=-1,z_max=3,num_axis_pieces= 30)
        #Superficies
        superficie = self.superficie()
        punto = self.punto3D().move_to((0.2,0.2,1.846))
        punto_critico = self.punto3D().move_to((0,0,2))

        dot = Dot().move_to(0.2).move_to(0.2*RIGHT+0.2*UP)
        linea = DashedLine((0.2,0.2,0),(0.2,0.2,1.846))

        plano = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                2.15 - 0.74*(u+v)
            ]),v_min=-0.5,v_max=1,u_min=-0.5,u_max=1,fill_color=GREEN,fill_opacity=1,checkerboard_colors=[GREEN,GREEN],
            resolution=(1, 1))

        #Vectores
        parcial_x = Arrow(start=(0.2,0.2,1.846), end=(1.2,0.2,1.106)).set_color(PINK)
        parcial_y_1 = Arrow(start=(0.2,0.2,1.846), end=(0.2,1.2,1.106)).set_color(YELLOW_E)
        parcial_y_arrow_tip = ArrowTip().set_color(YELLOW_E).scale(0.45).rotate_in_place(155*DEGREES).move_to(2.4*LEFT+0.65*DOWN)
        parcial_y = VGroup(parcial_y_1,parcial_y_arrow_tip)

        vector_normal_1 =Arrow(start=(0.2,0.2,1.846), end=(0.94,0.94,2.846))
        vector_normal_arrow_tip = ArrowTip().set_color(WHITE).scale(0.65).rotate_in_place(-15*DEGREES).move_to(2.27*LEFT+0.23*UP)
        vector_normal = VGroup(vector_normal_1,vector_normal_arrow_tip)
        
        #Animaciones
        self.play(Write(texto_1))
        self.wait(5.7)
        self.play(Write(texto_2))
        self.wait(3)
        self.play(FadeOut(texto_1),FadeOut(texto_2))
        self.acomodar_textos(texto_3)
        self.wait()
        self.move_camera(phi=70 * DEGREES,theta=-30*DEGREES,frame_center=(-3,2,3),distance=1000)
        self.play(ShowCreation(axes))
        self.play(FadeIn(dot))
        self.wait()
        self.play(ShowCreation(linea))
        self.wait(0.4)
        self.play(FadeIn(punto))
        self.play(ShowCreation(superficie))
        self.play(FadeOut(linea),FadeOut(dot))
        self.FadeOutWrite3D(texto_3,texto_4)
        self.wait(3)
        self.FadeOutWrite3D(texto_4,texto_5)
        self.wait(8)
        self.FadeOutWrite3D(texto_5,texto_6)
        self.wait(3)
        self.play(ReplacementTransform(texto_6,etiqueta_1))
        self.add_fixed_in_frame_mobjects(etiqueta_1)
        self.play(FadeIn(parcial_x))
        self.wait()
        self.FadeOutWrite3D(texto_6,texto_7)
        self.wait(3)
        self.play(ReplacementTransform(texto_7,etiqueta_2))
        self.add_fixed_in_frame_mobjects(etiqueta_2)
        self.add_fixed_in_frame_mobjects(parcial_y_arrow_tip)
        self.play(FadeIn(parcial_y_arrow_tip),FadeIn(parcial_y_1))
        self.wait(3)
        self.acomodar_textos(texto_8)
        self.wait(7)
        self.FadeOutWrite3D(texto_8,texto_9)
        self.wait(7)
        self.add_fixed_in_frame_mobjects(vector_normal_arrow_tip)
        self.play(FadeIn(vector_normal_arrow_tip),FadeIn(vector_normal_1))
        self.wait()
        self.FadeOutWrite3D(texto_9,texto_10)
        self.wait(5)
        self.play(ShowCreation(plano))
        self.bring_to_front(plano) #NO PUEDO HACER QUE EL PLANO PASE A "PRIMER PLANO"
        self.wait(3)
        self.play(FadeOut(vector_normal),FadeOut(parcial_y),FadeOut(parcial_x),FadeOut(etiqueta_1),FadeOut(etiqueta_2))
        self.play(FadeOut(plano),FadeOut(punto))
        self.FadeOutWrite3D(texto_10,texto_11)
        self.play(FadeIn(punto_critico))
        self.wait(11)
        self.FadeOutWrite3D(texto_11, texto_12)
        self.wait(5.6)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.move_camera(phi=0,theta=-90*DEGREES,frame_center=(0,0,0))
    def TerceraEscena(self):
        texto_1 = TextMobject(''' Ahora veamos ejemplos de \n
                                    superficies parametrizadas ''')
        texto_2_1 = TextMobject("$\\sigma(x,y)=(\\cos{(x)}\\sin{(y)},\\sin{(x)}\\sin{(y)},\\cos{(y)})$").move_to(3*UP)
        texto_2_2 = TextMobject("con $(x,y)\\in [0,2\\pi]\\times[0,\\pi]$").next_to(texto_2_1,DOWN)
        texto_2_3 = TextMobject("Esfera Unitaria").set_color(PINK).move_to(4*LEFT+0.5*UP)
        texto_2 = VGroup(texto_2_1,texto_2_2)
        texto_3_1 = TextMobject("$\\sigma(x,y)=((R+r\\cos{(y)})\\cos{(x)},(R+r\\cos{(y)})\\sin{(x)},r\\sin{(y)})$").move_to(3*UP)
        texto_3_2 = TextMobject("con $(x,y)\\in [0,2\\pi]\\times[0,2\\pi]$").next_to(texto_3_1,DOWN)
        texto_3_3 = TextMobject("Toro").set_color(PINK).move_to(4*LEFT+0.5*UP)
        texto_3 = VGroup(texto_3_1,texto_3_2)
        texto_4_1 = TextMobject("$\\sigma(x,y)=((2+y\\cos{(x/2)})\\cos{(x)},(2+y\\cos{(x/2)})\\sin{(x)},y\\sin{(x/2)})$").move_to(3*UP).scale(0.9)
        texto_4_2 = TextMobject("con $(x,y)\\in[0,2\\pi]\\times[-1,1]$").next_to(texto_4_1,DOWN)
        texto_4_3 = TextMobject("Banda de Möbius").set_color(PINK).move_to(4*LEFT+0.5*UP)
        texto_4 = VGroup(texto_4_1,texto_4_2)
        #Ejes
        axes = ThreeDAxes(x_min=-3.5,x_max=3.5,y_min=-3.5,y_max=3.5,z_min=-2.5,z_max=3,num_axis_pieces= 30)
        #Otros Objetos
        toro_R = DashedLine((0,0,0),(-1.41,1.41,0))
        etiqueta_R = TextMobject("$R$").move_to(1.1*RIGHT+0.95*DOWN).scale(0.7)
        toro_r = DashedLine((-1.41,1.41,0),(-1.41,1.41,0.5))
        etiqueta_r = TextMobject("$r$").move_to(2*RIGHT+0.9*DOWN).scale(0.7)

        #Superficies
        esfera = ParametricSurface(
            lambda u, v: np.array([
                np.cos(v) * np.sin(u),
                np.sin(v) * np.sin(u),
                np.cos(u)
            ]),v_min=0.0001,v_max=2*PI-0.0001,u_min=0.0001,u_max=PI-0.0001,fill_color=GOLD_E,fill_opacity=1,checkerboard_colors=[PINK,LIGHT_PINK],
            resolution=(20, 30))
        
        toro = ParametricSurface(
            lambda u, v: np.array([
                (2 + 0.5*np.cos(v))*np.cos(u),
                (2 + 0.5*np.cos(v))*np.sin(u),
                0.5*np.sin(v)
            ]),v_min=0.0001,v_max=2*PI-0.0001,u_min=0.0001,u_max=2*PI-0.0001,fill_color=GOLD_E,fill_opacity=1,checkerboard_colors=[PINK,LIGHT_PINK],
            resolution=(20, 30))
        
        parte_toro = ParametricSurface(
            lambda u,v: np.array([
                -1.41-0.5*0.7*np.sin(u),
                1.41+0.5*0.7*np.sin(u),
                0.5*np.cos(u)
            ]),u_min=0.0001,u_max=2*PI-0.0001,fill_color=GOLD_E,fill_opacity=1,checkerboard_colors=[GOLD_E,GOLD_D],
            resolution=(20, 30))

        moebius = ParametricSurface(
            lambda u, v: np.array([
                (2+v*np.cos(u/2))*np.cos(u),
                (2+v*np.cos(u/2))*np.sin(u),
                v*np.sin(u/2)
            ]),u_min=0.0001,u_max=2*PI-0.0001,v_min=-1,v_max=1,fill_color=PINK,fill_opacity=1,checkerboard_colors=[PINK,LIGHT_PINK],
            resolution=(20, 30))

        #Animaciones
        self.play(Write(texto_1))
        self.wait(3)
        self.play(FadeOut(texto_1))
        self.move_camera(phi=70 * DEGREES,theta=-30*DEGREES,frame_center=(0,0,1.5))
        self.play(ShowCreation(axes))
        self.acomodar_textos(texto_2)
        self.acomodar_textos(texto_2_3)
        self.wait()
        self.play(ShowCreation(esfera))
        self.begin_ambient_camera_rotation(rate=0.25)
        self.wait(4)
        self.stop_ambient_camera_rotation()
        self.play(FadeOut(esfera),FadeOut(texto_2_3))
        self.FadeOutWrite3D(texto_2,texto_3)
        self.acomodar_textos(texto_3_3)
        self.wait()
        self.play(ShowCreation(toro_R))
        self.acomodar_textos(etiqueta_R)
        self.wait()
        self.play(ShowCreation(toro_r))
        self.acomodar_textos(etiqueta_r)
        self.wait()
        self.play(ShowCreation(parte_toro))
        self.wait()
        self.play(FadeOut(toro_R),FadeOut(toro_r),FadeOut(etiqueta_R),FadeOut(etiqueta_r))
        self.play(ShowCreation(toro))
        self.play(FadeOut(parte_toro))
        self.begin_ambient_camera_rotation(rate=0.25)
        self.wait(4)
        self.stop_ambient_camera_rotation()
        self.play(FadeOut(toro),FadeOut(texto_3_3))
        self.FadeOutWrite3D(texto_3,texto_4)
        self.acomodar_textos(texto_4_3)
        self.wait()
        self.play(ShowCreation(moebius))
        self.wait()
        self.begin_ambient_camera_rotation(rate=0.25)
        self.wait(10)
        self.stop_ambient_camera_rotation()
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
    def construct(self):
        titulo = TextMobject('''Funciones de $\\mathbb{R}^2$ en $\\mathbb{R}^3$\n
                             Superficies Parametrizadas''').scale(1.5)
        #Animaciones
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))
        self.PrimeraEscena()
        self.SegundaEscena()
        self.TerceraEscena()
        

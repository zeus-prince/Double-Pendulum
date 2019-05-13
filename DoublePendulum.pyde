l1 = 150
l2 = 150
m1 = 30
m2 = 30
q1,q2 = random(TWO_PI),random(TWO_PI) 
v1,v2 = 0.1,0.2
g = 0.981
px2 = 0
py2 = 0
damping = 0.9999


def setup():
    size(800,600)
    #fullScreen(P2D)
    width,height = 800,600
    global canvas,cx,cy
    cx = width*0.5
    cy = height*0.5
    canvas = createGraphics(width,height)
    canvas.beginDraw()
    canvas.background(0)
    canvas.endDraw()
    
def draw():
    global q1,q2,v1,v2,px2,py2
    image(canvas,0,0)
    strokeWeight(2)
    translate(cx,cy)
    x1 = l1*sin(q1)
    y1 = l1*cos(q1)
    x2 = x1 + (l2*sin(q2))
    y2 = y1 + (l2*cos(q2))
    arm(x1,x2,y1,y2,m1,m2)
    
    #Defining the ODEs
    num1 = -g*(2*m1 + m2)*sin(q1)
    num2 = -m2*g*sin(q1 - (2*q2))
    num3 = -2*sin(q1-q2)*m2*((v2*v2*l2)+(v1*v1*l1*cos(q1-q2)))
    den = ((2*m1) + m2 -(m2*cos((2*q1)-(2*q2))))
    a1 = (num1+num2+num3)/(l1*den)
    num1 = 2*sin(q1-q2)
    num2 = v1*v1*l1*(m1 + m2)
    num3 = g*(m1+m2)*cos(q1)
    num4 = v2*v2*l2*m2*cos(q1-q2)
    a2 = (num1*(num2 + num3 + num4))/(l2*den)    
    v1+=a1
    v2+=a2
    q1+=v1
    q2+=v2
    v1 *= damping
    v2 *= damping
    canvas.beginDraw()
    canvas.translate(cx,cy)
    canvas.strokeWeight(4);
    canvas.stroke(57,255,20)
    if frameCount > 1 :
        canvas.line(px2,py2,x2,y2)
    canvas.endDraw()
    px2 = x2
    py2 = y2    

#Rendering the pendulum    
def arm(x1,x2,y1,y2,m1,m2):
    strokeWeight(6)
    stroke(0,0,255)
    line(0,0,x1,y1)
    line(x1,y1,x2,y2)
    strokeWeight(2)
    fill(255)
    ellipse(x1,y1,m1,m1)
    ellipse(x2,y2,m2,m2)
    fill(255,0,0)
    rect(-15,-15,30,30)

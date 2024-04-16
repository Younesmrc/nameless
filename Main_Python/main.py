from model.constante import *
from model.obstacle import Obstacle
from controller.strategies import Avancer,Tourner_D,Tourner_G,Sequentiel,Boucle
from controller.controleur import Controleur
from irl.robotadaptateur import RobotAdaptateur
from model.simulation import Simulation
from model.reel import Reel
from model.environnement import Environnement
from model.robot import Robot
try :
    from irl.RobotReel import Robot2IN013
except ImportError:
    from irl.mockup import Robot2I013Mockup
	
#test
graphique=True
environnement = Environnement(largeur_environnement, hauteur_environnement)
robot_version = 1 # 1 : simulation 2 : robot reel autre : robot mockup

if robot_version == 1:
    robot = Robot(robot_x, robot_y, robot_longueur, robot_largeur, direction_x, direction_y,environnement,robot_rayon)
elif robot_version == 2: 
    graphique=False     
    robot_reel = Robot2IN013()
    robot = RobotAdaptateur(robot_reel,robot_x,robot_y, direction_x, direction_y,environnement)
else :
     graphique=False
     robot_mockup = Robot2I013Mockup()
     robot = RobotAdaptateur(robot_mockup,robot_x,robot_y, direction_x, direction_y,environnement)

#ajout robot et obstacle
environnement.robot = robot
environnement.ajoute_object(robot) #ajout en premier dans la liste
obstacle = Obstacle(350, 350, 50, 50)
environnement.ajoute_object(obstacle)

#

#definition controleur
controleur = Controleur()
avancer=Avancer(robot,environnement,100)
tourner = Tourner_D(robot,environnement,90)
faire_carrer = Sequentiel()
faire_carrer.strategies=[avancer,tourner]*4
controleur.add_strategie(faire_carrer)



simulation = Simulation(controleur,robot,environnement,graphique)
reel = Reel(controleur,robot)

if robot_version == 1 :
    simulation.run_simulation()
else :
    reel.run_reel()
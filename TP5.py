class Voiture(object):

    def __init__(self,marque,couleur):
        
        self.marque=marque
        self.couleur=couleur
        self.conducteur='personne'
        self.vitesse=0

    def choisirConducteur(self,nom):
        self.conducteur=nom

    def affiche_infos(self):
        print(self.marque,self.couleur,self.conducteur,self.vitesse)

    def accelerer(self,taux,duree):
        self.vitesse=self.vitesse + taux*duree
        
        
        

    


mavoiture=Voiture('ford','rouge')
tavoiture=Voiture('hyudai', 'blanche')
savoiture=Voiture('suzuki', 'bleue')

mavoiture.choisirConducteur('Hassan')
mavoiture.accelerer(10,60)

mavoiture.affiche_infos()
        
     

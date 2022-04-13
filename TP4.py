class compteBancaire(object):
    
    def __init__(self,nomTitulaire,solde):
             self.nomTitulaire=nomTitulaire
             self.solde=solde
            

        
    def deposer(self,montant):
            self.solde=self.solde + montant
            


    def retrait(self,montant):
           self.solde=self.solde - montant

    def affiche_infos(self):
            print(self.nomTitulaire, self.solde)
    
    
    
    



           
compte1=compteBancaire("Al",10000)

compte1.deposer(2500)
compte1.retrait(3000)
compte1.retrait(7000)
compte1.deposer(1500)
compte1.affiche_infos()



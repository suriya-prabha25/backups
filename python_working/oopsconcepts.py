# Methods
class bag:            
    note = ""
    pen = 0
    bottle = 0
    def bagcontainer(self): #using self keyword in method
        print(self.note)

bag2 = bag()     #object creation
bag2.note = "english"
bag2.pen = 1
bag2.bottle = 1
bag2.bagcontainer()   #if need to print the self.note , we have to call a method here like this.

bag3 = bag()
bag3.note = "Tamil"
bag3.pen = 3
bag3.bottle = 2
bag3.bagcontainer()

# Constructor Function
class department:
    # constructor function
    def __init__(self, dep_name = "", secession = "", rank = 0):
        self.result = dep_name, secession, rank
        print(self.result)

department_values = department("MCA","A",1)

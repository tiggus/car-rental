class Criteria:
    def __init__(self):
        self.__cost_criteria = None
        self.__from_date_criteria = None
        self.__to_date_criteria = None
        
    def cost_criteria(self, cost):
        self.__cost_criteria = cost
    
    def get_cost_criteria(self):
        return self.__cost_criteria

    def from_date_criteria(self, from_date):
        self.__from_date_criteria = from_date

    def to_date_criteria(self, to_date):
        self.__to_date_criteria = to_date

    def get_from_date_criteria(self):
        return self.__from_date_criteria
    
    def get_to_date_criteria(self):
        return self.__to_date_criteria
        
    def __str__(self):
        return "cost_criteria: " + str(self.__cost_criteria) + " from_date_criteria: " + str(self.__from_date_criteria) + " to_date_criteria: " + str(self.__to_date_criteria)
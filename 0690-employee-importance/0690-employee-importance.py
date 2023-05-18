"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def get_importance(id, employees):
            if id not in employees:
                return 0
            total_importance = employees[id].importance
            for subordinate_id in employees[id].subordinates:
                total_importance += get_importance(subordinate_id, employees)
            return total_importance
        def get_total_importance(employees, id):
            employee_dict = {}
            for employee in employees:
                employee_dict[employee.id] = employee
            return get_importance(id, employee_dict)
        
        return get_total_importance(employees,id)
    
 
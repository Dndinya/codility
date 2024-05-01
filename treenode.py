class EmployeeNode:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.left = None
        self.right = None

class OrganizationChart:
    def __init__(self):
        self.root = None

    def insert_employee(self, employee_id, name):
        if not self.root:
            self.root = EmployeeNode(employee_id, name)
        else:
            self._insert_employee(self.root, employee_id, name)

    def _insert_employee(self, current_node, employee_id, name):
        if employee_id < current_node.employee_id:
            if current_node.left:
                self._insert_employee(current_node.left, employee_id, name)
            else:
                current_node.left = EmployeeNode(employee_id, name)
        else:
            if current_node.right:
                self._insert_employee(current_node.right, employee_id, name)
            else:
                current_node.right = EmployeeNode(employee_id, name)

    def search_employee(self, employee_id):
        return self._search_employee(self.root, employee_id)

    def _search_employee(self, current_node, employee_id):
        if not current_node:
            return None
        if current_node.employee_id == employee_id:
            return current_node
        elif employee_id < current_node.employee_id:
            return self._search_employee(current_node.left, employee_id)
        else:
            return self._search_employee(current_node.right, employee_id)

    def delete_employee(self, employee_id):
        self.root = self._delete_employee(self.root, employee_id)

    def _delete_employee(self, current_node, employee_id):
        if not current_node:
            return current_node
        if employee_id < current_node.employee_id:
            current_node.left = self._delete_employee(current_node.left, employee_id)
        elif employee_id > current_node.employee_id:
            current_node.right = self._delete_employee(current_node.right, employee_id)
        else:
            if not current_node.left:
                return current_node.right
            elif not current_node.right:
                return current_node.left
            else:
                temp = self._min_value_node(current_node.right)
                current_node.employee_id = temp.employee_id
                current_node.name = temp.name
                current_node.right = self._delete_employee(current_node.right, temp.employee_id)
        return current_node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def print_organization_chart(self):
        self._print_organization_chart(self.root, 0)

    def _print_organization_chart(self, node, depth):
        if node:
            self._print_organization_chart(node.right, depth + 1)
            print(' ' * depth + '|--', f"ID: {node.employee_id}, Name: {node.name}")
            self._print_organization_chart(node.left, depth + 1)


org_chart = OrganizationChart()


org_chart.insert_employee(101, "Derrick")
org_chart.insert_employee(202, "Alila")
org_chart.insert_employee(303, "Charlo")
org_chart.insert_employee(404, "Davie")
org_chart.insert_employee(505, "Ericko")

print("Organization Chart:")
org_chart.print_organization_chart()

employee = org_chart.search_employee(303)
if employee:
    print(f"Employee found: ID {employee.employee_id}, Name {employee.name}")
else:
    print("Employee not found")

org_chart.delete_employee(303)

# Print organization chart after deletion
print("\nOrganization Chart after deletion:")
org_chart.print_organization_chart()
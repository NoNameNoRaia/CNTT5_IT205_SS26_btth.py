from abc import ABC, abstractmethod
class Employee(ABC):
    
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        
    def display_info(self):
        emp_type = "Full-time"
        if isinstance(self, PartTimeEmployee):
            emp_type = "Part-time"
        elif isinstance(self, InternEmployee):
            emp_type = "Intern"
            
        print(f"Mã NV: {self.employee_id} | Họ tên: {self.name} | Loại: {emp_type}")
        
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    
    def __init__(self, employee_id, name, base_salary, bonus):
        super().__init__(employee_id, name)
        self.base_salary = base_salary
        self.bonus = bonus
        
    def calculate_salary(self):
        return self.base_salary + self.bonus


class PartTimeEmployee(Employee):
    
    def __init__(self, employee_id, name, working_hours, hourly_rate):
        super().__init__(employee_id, name)
        self.working_hours = working_hours
        self.hourly_rate = hourly_rate
        
    def calculate_salary(self):
        return self.working_hours * self.hourly_rate


class InternEmployee(Employee):
    
    def __init__(self, employee_id, name, allowance):
        super().__init__(employee_id, name)
        self.allowance = allowance
        
    def calculate_salary(self):
        return self.allowance

employees = [
    FullTimeEmployee("E001", "Nguyen Van A", 15000000, 3000000),
    PartTimeEmployee("E002", "Tran Thi B", 80, 50000),
    InternEmployee("E003", "Le Van C", 3000000)
]
def display_employees(employee_list):
    """Chức năng 1: Xem danh sách nhân viên"""
    print("\n--- DANH SÁCH NHÂN VIÊN ---")
    for employee in employee_list:
        employee.display_info()


def display_salaries(employee_list):
    """Chức năng 2: Tính lương toàn bộ nhân viên (Sử dụng Tính Đa Hình)"""
    print("\n--- BẢNG LƯƠNG NHÂN VIÊN ---")
    for employee in employee_list:
        salary = employee.calculate_salary()
        salary_formatted = f"{salary:,.0f} VND"
        print(f"{employee.employee_id} | {employee.name} | Lương: {salary_formatted}")
def main():
    while True:
        print("\n=== EMPLOYEE SALARY MANAGER ===")
        print("1. Xem danh sách nhân viên")
        print("2. Tính lương toàn bộ nhân viên")
        print("3. Thoát chương trình")
        choice = input("Chọn chức năng (1-3): ").strip()
        
        if choice == "1":
            display_employees(employees)
        elif choice == "2":
            display_salaries(employees)
        elif choice == "3":
            print("\nCảm ơn bạn đã sử dụng Employee Salary Manager!")
            break
        else:
            print("\nLựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()
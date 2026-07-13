from typing import Optional
import random

id_pool = set()

class Employee:
    __company_name: str = ""  # 类属性company_name（公司名称，所有员工共享）

    def __init__(self, name: Optional[str] = None,
                 age: Optional[int] = None,
                 employee_id: Optional[str] = None):
        """
        构造函数，初始化实例属性
        :param name: 姓名
        :param age: 年龄
        :param employee_id: 员工ID
        """
        self.name = name  # 实例属性：姓名
        if age is not None and age < 0:
            raise ValueError("年龄不能为负数！")
        self.age = age  # 实例属性：年龄

        # 如果未提供employee_id，则自动生成
        if employee_id is None:
            self.employee_id = Employee.generate_employee_id()
        else:
            self.employee_id = employee_id

    # ---------- 实例方法，用于打印员工的个人信息和公司名称。 ----------

    def introduce(self):
        """打印员工的个人信息和公司名称。"""
        company_name = Employee._Employee__company_name  # 访问私有类属性
        print(f"公司:{company_name} 员工姓名：{self.name}, 年龄:{self.age}, 员工ID:{self.employee_id}")

    def get_bonus(self):
        return self.__calculate_bonus()

    # ----------私有方法：计算员工的奖金（此处为模拟，可以固定返回一个值或根据实际需求设计）。 ----------
    def __calculate_bonus(self):
        """计算员工奖金（模拟）"""
        # 根据年龄或职位简单计算奖金
        if self.age and self.age > 30:
            return 30000
        return 20000

    # ---------- 类方法：设置公司名称 ----------
    @classmethod
    def set_company_name(cls, name: Optional[str] = None):
        cls.__company_name = name

    # ---------- 类方法：获取公司名称 ----------
    @classmethod
    def get_company_name(cls):
        return cls.__company_name

    # ----------静态方法：生成唯一的员工编号（此处为模拟，可以返回递增的整数或根据实际需求设计，例：全局变量+递增）。 ----------
    @staticmethod
    def generate_employee_id(id: Optional[str] = None):
        while True:
            new_id = str(random.randint(10000, 99999))
            if new_id not in id_pool:
                id_pool.add(new_id)
                return new_id


class Manager(Employee):
    def __init__(self, name: Optional[str] = None,
                 age: Optional[int] = None,
                 employee_id: Optional[str] = None,
                 department: Optional[str] = None):
        """
        构造函数，初始化实例属性
        :param name: 姓名
        :param age: 年龄
        :param employee_id: 员工ID
        :param department:  部门
        """
        super().__init__(name, age, employee_id)  #调用父函数构造函数进行构造
        self.department = department  # 实例属性：部门
        self.__salary = 8000   # 私有属性： 薪资，默认为8000

    # ---------- 实例方法，用于打印员工的个人信息和公司名称。 ----------

    def introduce(self):
        """打印员工的个人信息和公司名称。"""
        company_name = Employee._Employee__company_name  # 访问私有类属性
        print(f"公司:{company_name} 员工姓名：{self.name}, 年龄:{self.age}, "
              f"员工ID:{self.employee_id}, 部门:{self.department}, 薪资:{self.__salary}")

    def set_salary(self, salary: Optional[float] = None):
        """公共方法，设置员工的薪资（通过访问私有属性__salary）"""
        if salary is not None and salary >= 0:
            self.__salary = salary
        else:
            raise ValueError("薪资不能为负数！")

    def get_salary(self):
        """公共方法，返回员工的薪资（通过访问私有属性_salary）"""
        return self.__salary

    def promote(self, percentage: Optional[float] = None):
        """
        接受一个薪资增长的百分比作为参数，并更新薪资。
        :param percentage: 增长百分比，例如 10 表示增长10%
        :return: 更新后的薪资
        """
        if percentage is None:
            return self.__salary
        elif percentage < 0:
            raise ValueError("增长百分比不能为负数！")
        else:
            self.__salary *= (100 + percentage) / 100
            return self.__salary

    # ----------静态方法：计算员工的年收入（薪资 + 奖金，奖金有默认值） ----------
    @staticmethod
    def calculate_annual_income(salary: Optional[float] = 0 , bonus: Optional[float] = 0):
        """
        接收月薪和奖金作为参数，并计算年薪
        :param salary:  月薪
        :param bonus:  奖金
        :return:  年薪 = 月薪 * 12 + 奖金
        """
        return salary * 12 + bonus


# ==================== 测试实例 ====================
if __name__ == '__main__':
    print("=" * 60)
    print("员工信息管理系统测试")
    print("=" * 60)

    # 1. 测试类方法：设置公司名称
    print("\n1. 设置公司名称")
    Employee.set_company_name("科技未来有限公司")
    print(f"公司名称已设置为: {Employee.get_company_name()}")

    # 2. 创建 Employee 对象
    print("\n2. 创建普通员工")
    emp1 = Employee("张三", 25)
    emp2 = Employee("李四", 35, "EMP001")  # 手动指定ID
    emp3 = Employee("王五", 28)

    # 打印员工信息
    print("--- 员工信息展示 ---")
    emp1.introduce()
    emp2.introduce()
    emp3.introduce()

    # 3. 创建 Manager 对象
    print("\n3. 创建经理对象")
    mgr1 = Manager("赵经理", 40, department="技术部")
    mgr2 = Manager("孙经理", 38, employee_id="MGR001", department="市场部")
    mgr3 = Manager("周经理", 45, department="人力资源部")  # 使用默认薪资8000

    # 手动设置月薪
    mgr1.set_salary(salary=12000)
    mgr2.set_salary(salary=10000)

    print("--- 经理信息展示 ---")
    mgr1.introduce()
    mgr2.introduce()
    mgr3.introduce()

    # 4. 测试静态方法生成员工ID
    print("\n4. 测试自动生成员工ID")
    emp4 = Employee("赵六", 30)  # 不指定ID，自动生成
    emp5 = Employee("钱七", 32)
    print("自动生成的ID示例：")
    print(f"  {emp4.name}: {emp4.employee_id}")
    print(f"  {emp5.name}: {emp5.employee_id}")

    # 5. 测试 Manager 特有方法
    print("\n5. 测试经理特有能力")
    print(f"  {mgr1.name} 当前薪资: {mgr1.get_salary():.2f}")

    # 测试升职加薪
    mgr1.promote(10)  # 加薪10%
    print(f"  {mgr1.name} 加薪10%后薪资: {mgr1.get_salary():.2f}")

    mgr1.promote(5)  # 再加薪5%
    print(f"  {mgr1.name} 再加薪5%后薪资: {mgr1.get_salary():.2f}")

    # 6. 测试静态方法：计算年收入
    print("\n6. 测试年收入计算")
    mgr1_bonus = mgr1.get_bonus()  # 调用私有方法（模拟）
    annual_income = Manager.calculate_annual_income(mgr1.get_salary(), mgr1_bonus)
    print(f"  {mgr1.name} 的月薪: {mgr1.get_salary()}, 奖金: {mgr1_bonus:.2f}")
    print(f"  {mgr1.name} 的年收入: {annual_income:.2f} 元")


from MyPackage.module1 import main as fun1
from MyPackage.module2 import main as fun2
from MyPackage.module3 import main as fun3
from MyPackage.submodule.module4 import main as fun4
from MyPackage.submodule.module5 import main as fun5


wynik= fun1([1,20,20,7,7,7,3,5])
print(wynik)

wynik= fun1([1,20,20,7,7,2,3,5])
print(wynik)

wynik= fun2(5)
print(wynik)

wynik= fun3("a,b,c")
print(wynik)

wynik= fun4((1,2,3))
print(wynik)

wynik= fun5((12,1,8888,1000000))
print(wynik)
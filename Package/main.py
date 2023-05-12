from MyPackage.module1 import m1 as fun1
from MyPackage.module2 import m2 as fun2
from MyPackage.module3 import m3 as fun3
from MyPackage.submodule.module4 import m4 as fun4
from MyPackage.submodule.module5 import m5 as fun5


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
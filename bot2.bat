set /a num=%random% %%1 + 2
set num=^"%num%^ 
FOR /L %%i IN (1,1,1) DO (
  
    
   python Bins.py bins%random%.py ""%num%"""
   python Bin.py bin%random%.py  ""%num%"""
)
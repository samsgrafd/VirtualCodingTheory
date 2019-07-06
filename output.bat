FOR /L %%i IN (1,1,25) DO (
    python bridge.py 0 0 0 
    parameters.bat  >>out.csv	
)


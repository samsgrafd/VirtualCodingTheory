FOR /L %%i IN (1,1,1) DO (
   python static/UserBin.py >>static/outBin.txt
   python static/UserBins.py >>static/outBins.txt
  )
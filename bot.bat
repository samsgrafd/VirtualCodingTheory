FOR /L %%i IN (1,1,1) DO (
   python static/Bins.py static/UserBins.py """0""">>static/outBins.txt
   python static/Bin.py static/UserBin.py """0""">>static/outBin.txt
   python static/UserBins.py
  )
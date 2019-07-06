FOR /L %%i IN (1,1,1) DO (
   python Bins.py UPLOADS/UserBins.py """0""">>UPLOADS/outBins.txt
   python Bin.py UPLOADS/UserBin.py """0""">>UPLOADS/outBin.txt
   python UPLOADS/UserBin.py
  )
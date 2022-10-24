import os
os.system('cmd /k "scp -rv postgresql-2022-10-07_000000.log root@172.16.16.75:/var/log/postgresql/"')
#For backend process
#os.system('cmd /c "scp -rv postgresql-2022-09-22_000000.log Monday_postgresql-2022-09-26_224215.log root@172.16.16.75:/var/log/postgresql/"')

print("Done")

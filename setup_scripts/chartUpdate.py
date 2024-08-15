import shutil 
import sys


APP_VERSION = sys.argv[1]

shutil.copy('geoapp/Chart.yaml', 'geoapp/chart_bk.yaml')

def chartModif(chart_version):
    with open("geoapp/Chart.yaml", 'r') as f:
        content = f.readlines()
        
    with open("geoapp/Chart.yaml" , 'w')  as f1:
        for line in content:
            if 'version:' in line:
                f1.write(f'version: {chart_version}\n')
            elif 'appVersion:' in line:
                f1.write(f'appVersion: {chart_version}\n')
            else:
                f1.write(line)
     
chartModif(APP_VERSION)    
         
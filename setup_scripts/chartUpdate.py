import shutil 
import sys


APP_VERSION = sys.argv[1]

def takeBackup():
    shutil.copy('geoapp/Chart.yaml', 'geoapp/chart_bk.yaml')

def chartModif(chart_version):
    
    try:
        with open("geoapp/Chart.yaml", 'r') as f:
            content = f.readlines()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(99)
    else:
                
        with open("geoapp/Chart.yaml" , 'w')  as f1:
            for line in content:
                if 'version:' in line:
                    f1.write(f'version: {chart_version}\n')
                elif 'appVersion:' in line:
                    f1.write(f'appVersion: {chart_version}\n')
                else:
                    f1.write(line)

def main():
    takeBackup()     
    chartModif(APP_VERSION)    

if __name__== "__main__":
    main()        
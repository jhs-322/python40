import pandas as pd 
import folium, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
df = pd.read_excel('학교주소좌표.xlsx',engine='openpyxl', header=None)
df.columns = ['학교이름', '주소', 'x', 'y']

name_list = df['학교이름'].to_list()
addr_list = df['주소'].to_list()
position_x_list = df['x'].to_list()
position_y_list = df['y'].to_list()

map = folium.Map(location=[37, 127], zoom_start = 7) #7배 줌

for i in range(len(name_list)): #마킹
    if position_x_list[i] != 0:
        marker = folium.Marker([position_y_list[i], position_x_list[i]],
                               popup=name_list[i],
                               icon = folium.Icon(color='blue'))
        marker.add_to(map)
map.save('univ_map.html')

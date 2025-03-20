import folium, os

map = folium.Map(location=[37,127],zoom_start=7)

marker = folium.Marker([37.341435483, 126.733026596],
                    popup='한국공학대학교', 
                    icon = folium.Icon(color='blue'))

marker.add_to(map) 

os.chdir(os.path.dirname(os.path.abspath(__file__)))
map.save('uni_map.html')

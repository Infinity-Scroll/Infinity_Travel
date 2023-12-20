import googlemaps
from datetime import datetime

# API 키와 라이브러리를 통해 객체 구성
gmaps = googlemaps.Client(key='AIzaSyBPRAME5ZhySmydx9zsgIZwPkTD6MclT1Y')

'''
# 주소를 받아 지오코딩하는 예
geocode_result = gmaps.geocode('도쿄 센소지')
'''

# 주소를 입력받아 지오코딩 수행
def get_coordinates(address):
    geocode_result = gmaps.geocode(address)

    # 결과가 있다면 첫 번째 결과의 좌표를 반환
    if geocode_result:
        location = geocode_result[0]['geometry']['location']
        return location['lat'], location['lng']
    else:
        print(f"{address}에 대한 좌표를 찾을 수 없습니다.")
        return None
import requests

def get_coordinates_from_address(address):
    # Google Maps Geocoding API의 엔드포인트와 API 키를 설정
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    api_key = "AIzaSyCUzWM4L4iAj-krLKiEx3MkD-j0HrqlNrs"

    # 주소를 이용하여 API에 요청을 보냄
    params = {"address": address, "key": api_key}
    response = requests.get(base_url, params=params)
    data = response.json()

    print(data["status"] + " 테스트용 좌표 0 ")
    
    # API 응답에서 좌표값 추출
    if data["status"] == "OK":
        location = data["results"][0]["geometry"]["location"]
        print(location["lat"] + " 테스트용 좌표 1 ")
        print(location["lng"] + " 테스트용 좌표 2 ")
        latitude = location["lat"]
        longitude = location["lng"]
        return latitude, longitude
    else:
        return None

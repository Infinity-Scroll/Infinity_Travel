# Infinity_Travel

-   **Infinity_Travel**은 사용자들이 자신의 여행 지역, 후기, 별점을 공유하며 **새로운 여행 파티**를 찾을 수 있는 서비스입니다.

다른 사용자들과 만남을 통해 만들어지는 이야기가 여행의 끝이 어디인지 알 수 없는 무한한 여행의 시작입니다.

## 프로젝트 기간

> 2023.12.08 ~ 2023.12.28

## 📌 팀원 소개

|                                                                     김창환🚩                                                                      |                                            남정식                                            |                                                                      심주용                                                                       |                                           윤여범                                            |
| :-----------------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------: |
| <img src="https://github.com/Infinity-Scroll/Infinity_Travel_BE/assets/138690980/7039dd11-5647-44d8-9a18-d2caea2f5a39" width="200" height="230" > | <img src="https://avatars.githubusercontent.com/u/109896609?v=4"  width="200" height="230"/> | <img src="https://github.com/Infinity-Scroll/Infinity_Travel_BE/assets/138690980/a7a1ee18-27b9-4d09-846e-ef11b121aa2c" width="200" height="230"/> | <img src="https://avatars.githubusercontent.com/u/147234803?v=4" width="200" height="230"/> |
|                                    <a href="https://github.com/Blood-donation-day"> 🌱 Blood-donation-day</a>                                     |                      <a href="https://github.com/sk7556">🌱 sk7556</a>                       |                                             <a href="https://github.com/SimJuyong1">🌱 SimJuyong1</a>                                             |                     <a href="https://github.com/yabdove">🌱 yabdove</a>                     |

## 목차

[1. 프로젝트 목표](#1-목표)<br>
[2. 개발 환경 및 배포 URL](#2-개발-환경-및-배포-url)<br>
[3. 프로젝트 구조](#3-프로젝트-구조와-개발-일정)<br>
[4. 구성도와 데이터베이스 모델링(ERD)](#4-데이터베이스-모델링erd)<br>
[5. API 명세서](#5-api-명세)<br>
[7. 메인기능](#7-메인기능)<br>
[8. 추가기능](#7-추가기능)<br>
[9. 개발중 경험한 문제점과 해결방법](#8-개발과정과-느낀점)<br>
[10. 프로젝트 후기](#8-개발과정과-느낀점)<br>

## 1. 목표

-   함께 여행하는 파트너를 모집하는 서비스

-   나만의 일정을 만들고 공유하는 서비스

-   여행자간 실시간 채팅을 통해 정보를 공유하는 서비스

#### FlowChart

<img src=https://github.com/Infinity-Scroll/Infinity_Travel_BE/assets/138690980/6278f543-6e02-4ec7-b191-df9cf5906a94>

## 2. 개발 환경 및 배포 URL

#### [FrontEnd]

<div>
    <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
    <img src="https://img.shields.io/badge/css3-1572B6?style=for-the-badge&logo=css3&logoColor=white">
    <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=white">
    <img src="https://img.shields.io/badge/Tailwind-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white">
    
</div>

#### [BackEnd]

<div>
    <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
    <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">
</div>

#### [DataBase]

<img src="https://img.shields.io/badge/postgresql-4169E1?style=for-the-badge&logo=postgresql&logoColor=white">

### 2-2. 배포 URL

<details>
  <summary> 테스트계정</summary>
  
```
ID: test123@test123.com
PW: test123

채팅테스트 2번 ID
ID: test1@test1.com
PW: test123

```

</details>

프론트엔드 페이지
https://www.infinity-travel.shop/front/pages/

백엔드
https://www.infinity-travel.shop/

## 3. 프로젝트 구조와 개발 일정

### 3.1프로젝트 구조

```

📦Infinity_Travel_BE
┣ 📂.github
┃ ┗ 📂workflows
┃ ┃ ┗ 📜main.yml
┣ 📂accounts
┃ ┣ 📂migrations
┃ ┣ 📜admin.py
┃ ┣ 📜apps.py
┃ ┣ 📜models.py
┃ ┣ 📜serializers.py
┃ ┣ 📜tests.py
┃ ┣ 📜urls.py
┃ ┣ 📜utils.py
┃ ┣ 📜views.py
┃ ┗ 📜**init**.py
┣ 📂chat
┃ ┣ 📂migrations
┃ ┣ 📜admin.py
┃ ┣ 📜apps.py
┃ ┣ 📜chatting2.html
┃ ┣ 📜consumers.py
┃ ┣ 📜models.py
┃ ┣ 📜routing.py
┃ ┣ 📜serializers.py
┃ ┣ 📜tests.py
┃ ┣ 📜urls.py
┃ ┣ 📜utils.py
┃ ┣ 📜views.py
┃ ┗ 📜**init**.py
┣ 📂companion
┃ ┣ 📂migrations
┃ ┣ 📜admin.py
┃ ┣ 📜apps.py
┃ ┣ 📜models.py
┃ ┣ 📜serializers.py
┃ ┣ 📜tests.py
┃ ┣ 📜urls.py
┃ ┣ 📜views.py
┃ ┗ 📜**init**.py
┣ 📂core
┃ ┣ 📜models.py
┃ ┗ 📜permissions.py
┣ 📂infinity_travel
┃ ┣ 📜asgi.py
┃ ┣ 📜settings.py
┃ ┣ 📜urls.py
┃ ┣ 📜wsgi.py
┃ ┗ 📜**init**.py
┣ 📂place
┃ ┣ 📂migrations
┃ ┣ 📜admin.py
┃ ┣ 📜apps.py
┃ ┣ 📜geoCode.py
┃ ┣ 📜models.py
┃ ┣ 📜serializers.py
┃ ┣ 📜tests.py
┃ ┣ 📜urls.py
┃ ┣ 📜views.py
┃ ┗ 📜**init**.py
┣ 📂schedule
┃ ┣ 📂migrations
┃ ┣ 📜admin.py
┃ ┣ 📜apps.py
┃ ┣ 📜models.py
┃ ┣ 📜serializers.py
┃ ┣ 📜tests.py
┃ ┣ 📜urls.py
┃ ┣ 📜views.py
┃ ┗ 📜**init**.py
┣ 📜.DS_Store
┣ 📜.gitignore
┣ 📜manage.py
┣ 📜README.md
┗ 📜requirements.txt

```

### 3-2 개발일정

[개발일정 바로가기](https://github.com/orgs/Infinity-Scroll/projects/1/views/3)
<img src="https://github.com/Infinity-Scroll/Infinity_Travel_BE/assets/138690980/281333c3-242b-409e-8490-2595b7d7bc8d" />

## 4.구성도와 데이터베이스 모델링

### 4-1 아키텍쳐 구성도

<img src=https://github.com/Infinity-Scroll/Infinity_Travel_BE/assets/138690980/06172cbc-aa63-44bb-aedb-af65e9d60962>

### 4-2 데이터베이스-모델링 ERD

<img src="https://github.com/Infinity-Scroll/Infinity_Travel_BE/assets/138690980/847a351c-0284-4cde-abb2-5a49dbde16c6" />

## 5.api 명세

|  accounts  | Method |       내용        | 로그인 권한 | 작성자 권한 |
| :--------: | :----: | :---------------: | :---------: | :---------: |
| 'create/'  |  POST  |     회원가입      |             |             |
|  'login/'  |  POST  | 로그인(토큰 발급) |             |             |
| 'refresh/' |  POST  | 엑세스토큰 재발급 |     ✅      |             |
|     ''     |  GET   |    프로필 조회    |     ✅      |     ✅      |
|     ''     | PATCH  |    프로필 수정    |     ✅      |     ✅      |
|     ''     | DELETE |     회원 탈퇴     |     ✅      |     ✅      |

<br>

|              chat               | Method |        내용        | 로그인 권한 | 작성자 권한 |
| :-----------------------------: | :----: | :----------------: | :---------: | :---------: |
|          'roomcreate/'          |  POST  |    채팅방 생성     |     ✅      |     ✅      |
|           'roomlist/'           |  GET   |   내 채팅방 조회   |     ✅      |     ✅      |
|       '<str:room_name>/'        |  GET   | 채팅방 메세지 조회 |     ✅      |     ✅      |
| 'roominvisible/<str:room_name>' |  GET   |    채팅방 숨김     |     ✅      |     ✅      |

<br>

|     companion      | Method |      내용      | 로그인 권한 | 작성자 권한 |
| :----------------: | :----: | :------------: | :---------: | :---------: |
|      'list/'       |  GET   | 동행 목록조회  |             |             |
|      'list/'       |  POST  |  동행 글 작성  |     ✅      |             |
|  'list/<int:pk>'   |  GET   |  동행 글 상세  |             |             |
|  'list/<int:pk>'   |  PUT   |  동행 글 수정  |     ✅      |     ✅      |
|  'list/<int:pk>'   | DELETE |  동행 글 삭제  |     ✅      |     ✅      |
|     'comment/'     |  POST  | 동행 댓글 작성 |     ✅      |     ✅      |
| 'comment/<int:pk>' | PATCH  | 동행 댓글 수정 |     ✅      |     ✅      |
| 'comment/<int:pk>' | DELETE | 동행 댓글 삭제 |     ✅      |     ✅      |

<br>

|         planner         | Method |      내용      | 로그인 권한 | 작성자 권한 |
| :---------------------: | :----: | :------------: | :---------: | :---------: |
|     'api/planners/'     |  POST  |   일정 생성    |     ✅      |             |
|     'api/planners/'     |  GET   | 일정 목록 조회 |             |             |
| 'api/planners/<int:pk>' |  GET   | 일정 상세 조회 |             |             |
| 'api/planners/<int:pk>' | PATCH  |   일정 수정    |     ✅      |     ✅      |
| 'api/planners/<int:pk>' | DELETE |   일정 삭제    |     ✅      |     ✅      |

<br>

|             place             | Method |      내용      | 로그인 권한 | 작성자 권한 |
| :---------------------------: | :----: | :------------: | :---------: | :---------: |
|         'api/places/'         |  POST  |   장소 생성    |     ✅      |             |
|         'api/places/'         |  GET   | 장소 목록 조회 |             |             |
| 'api/places/<int:comment_id>' |  GET   | 장소 상세 조회 |             |             |
| 'api/places/<int:comment_id>' | PATCH  |   장소 수정    |     ✅      |     ✅      |
| 'api/places/<int:comment_id>' | DELETE |   장소 삭제    |     ✅      |     ✅      |

## 6.메인기능<br>

<img src=https://github.com/Infinity-Scroll/Infinity_Travel_BE/assets/138690980/e2adc15e-6487-48d0-bb8e-ae111cf0c250>회원가입 

<img src=https://github.com/Infinity-Scroll/Infinity_Travel_BE/assets/138690980/73f3a8cb-96a9-45e2-bf69-10b0d281af2f>이메일 인증 및 로그인

<img src=https://github.com/Infinity-Scroll/Infinity_Travel_BE/assets/138690980/13e4fd35-f3bf-443d-8999-16b05ff9c5c4>내 프로필


<div><img src=https://github.com/Infinity-Scroll/Infinity_Travel_BE/assets/138690980/0c9f5432-1d62-4cb9-bf11-61d814379d00></div>
프로필 변경




메인페이지,
동행, 일정

## 7.추가기능<br>

프로필(변경), 내동행, 내일정
채팅

<img src=https://github.com/Infinity-Scroll/Infinity_Travel_BE/assets/138690980/e4098055-fd11-498d-8921-c1d214c10532>



<img src=https://github.com/Infinity-Scroll/Infinity_Travel_BE/assets/138690980/7e952857-1593-4a83-97d3-5894be168e62>
채팅하기

<img src=https://github.com/Infinity-Scroll/Infinity_Travel_BE/assets/138690980/3d8ad921-b06c-4184-a400-8fb929b18d21>
스크롤 올려 메세지 더 불러오기 및 나가기

## 8.개발중 경험한 문제점과 해결방법

### 8-1 유저 인증 구현

이전 프로젝트에서는 다른 도메인 간 쿠키를 사용한 인증이 실패한 적이 있습니다. 쿠키의 값을 읽을 수 없어, 로그인 시 응답에 토큰값을 보내주고 그걸 로컬스토리지에 저장 후 다음 요청시 보내는 방식이였습니다.

이번 프로젝트에서는 해당 문제를 극복하기 위해 도전했고, 이번에는 쿠키에 포함된 access_token 값을 활용하여 사용자를 인증하고 있습니다.

<img src=https://github.com/Infinity-Scroll/Infinity_Travel_BE/assets/138690980/df43f7dc-ba28-476b-94c7-297bc1f5d2a0>[지난 프로젝트 도메인 차이]

<img src=https://github.com/Infinity-Scroll/Infinity_Travel_BE/assets/138690980/efb166d6-91b9-4b43-bdb6-653f2d4e149a>[현재 도메인]

사용자 인증 시, 기본적으로 제공되는 restframework.authentication대신 새로운 인증방식을 구현해야 했습니다. 새로운 권한(permission)을 추가해야 했기 때문에, 쿠키에서 access 토큰을 검증하는 JWTCookieAuthenticated권한을 기본 인증방식으로 설정하였습니다.

```python
class JWTCookieAuthenticated(BasePermission):
    def has_permission(self, request, view):
        cookie = request.COOKIES.get("access_token")
        if not cookie:
            return False
        try:
            access_token = AccessToken(cookie)
        except:
            return False

        return True
```


[쿠키에서 access_token값을 가져와 기간, 유효성을 검증하는 permission]
<br>

덕분에 쿠키의 값을 자바스크립트로 읽어들이는 XSS(크로스 사이트 스크립팅) 공격 등의 보안 취약점을 방지하여, 보안성이 강화된 사용자 인증이 가능해졌습니다.

### 8-2 채팅 구현중 문제점

같이 여행갈 동료을 모집하며 서로 채팅을 할 수 있는 기능을 추가하고자 하였습니다. 사용자간 채팅을 하는데 필요한 조건을 다음과 같이 정리하였습니다.

-   채팅방을 생성하고, 목록을 불러올 수 있어야한다.
-   채팅방의 메세지를 생성하고 불러올 수 있어야한다.
-   메세지는 DB에 저장되어 다음 채팅을 이어갈 때 불러올 수 있어야한다.
-   1:1 채팅방에는 보낸 사람과 받는사람만이 메세지를 읽을 수 있다.
-   둘 중 한명이 나간다면 남는 사람만 기존 메세지를 확인가능.
-   남은사람이 메세지를 보냈다면 나간사람은 다시 기존 메세지를 불러올 수 있어야한다.

조건을 만족하기 위한 초기모델링을 다음과 같이 작성하였습니다.

<details>
  <summary>Room</summary>

```python
class Room(TimestampedModel):
    member = models.ManyToManyField(User, related_name="member")
    room_name = models.CharField(max_length=50)
    invisible = models.ManyToManyField(User, "room_invisible")
    lastest_text = models.TextField("마지막 대화")
```

-   member에서 채팅방에 어느 유저가 있는지 중계테이블을 생성하였습니다.
-   invisible에 해당하는 user가 추가되면 방 목록에서 보이지 않게 됩니다.
-   채팅방의 마지막 메세지를 저장하여 방 목록을 조회할 때 같이 보이도록 하였습니다.

그러나 member와 invisible의 중계테이블을 만드는 과정이 중복되었고, 채팅방에 모든 유저가 나갈 시
대화 목록을 불러올 방법이 없는 문제가 생겨 모델을 수정하였습니다.

```python
class Rooms(TimestampedModel):
    room_name = models.CharField(max_length=50)
    lastest_text = models.TextField("마지막 대화")


class Room_members(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="member")
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, related_name="visibility")
    is_visibled = models.BooleanField(default=True)

```

모델을 나눠 사용자와 채팅방 숨김여부를 확인하는 모델을 만들었습니다. 중계테이블이 중복되는 문제를 해결하였고, 채팅방을 숨겨도 메세지를 불러올 수 있게되었습니다.

</details>

#### 비동기 컨텍스트에서 데이터베이스에서 유저를 가져오는 쿼리를 수행하지 못하는 문제

<details>
  <summary> error</summary>

```
asyncio.py", line 24, in inner
raise SynchronousOnlyOperation(message)
django.core.exceptions.SynchronousOnlyOperation: You cannot call this from an async context - use a thread or sync_to_async.
```

</details>
토큰에있는 유저의 pk값을 이용하여 사용자를 검증하려고 하였는데 비동기적인 함수의 실행과정에서 데이터베이스 접근하려고하니 해당 문제가 발생하였습니다.

```python
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
       ...
       try:
            token = self.scope["cookies"]["access_token"]
            user_id = AccessToken(token)["user_id"]
            user = await User.objects.get(pk=user_id)
            print(user)
        ...
```

원인은 장고의 ORM은 기본적으로 동기적인 환경에서 사용되도록 설계되었기 때문에, 위와 같은 비동기 함수 안에서 동기적인 ORM메서드를 직접 호출하였기 때문입니다. 따라서 비동기적인 환경에서 백그라운드 스레드를 사용하는 channels.db모듈의 database_sync_to_async를 사용하여 문제를 해결하였습니다.

```python
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        user = await get_user_from_cookie(self)
        room_name = self.scope["url_route"]["kwargs"]["room_name"]
        room = await get_room(room_name)
        ...
```

<details>
  <summary>get_user_from_cookie</summary>

```python
async def get_user_from_cookie(self):
    try:
        token = self.scope["cookies"]["access_token"]
        user_id = AccessToken(token)["user_id"]
        user = await get_user(user_id)
        return user

    except TokenError:
        await self.close()
        return Response({"error": "토큰만료"}, status=401)
```

스코프에서 쿠키의 엑세스토큰 값에서 user_id를 가져와 get_user()호출

</details>
<details>
<summary>get_user</summary>

```python
@database_sync_to_async
def get_user(user_id):
    return User.objects.get(pk=user_id)
```

</details>

#### 채팅방을 숨기면 상대방도 채팅방이 보이지 않는 문제

```python
class RoomListAPIView(generics.ListAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        user_id = get_user_id(self.request)
        queryset = (
            Rooms.objects.filter(visibility__user=user_id)
            .exclude(visibility__is_visibled=False)
            .order_by("-updated_at")
        )
        return queryset
```

```python

class Rooms(TimestampedModel):
    room_name = models.CharField(max_length=50)
    lastest_text = models.TextField("마지막 대화")


class Room_members(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="member")
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, related_name="visibility")
    is_visibled = models.BooleanField(default=True)
```


초기 채팅방을 불러오는 뷰를 위와같이 작성했습니다. 해당 사용자의 id가 있는 Rooms중 is_visibled=False것은 제외하고 리스트를 제공합니다.

그러나 채팅방에서 한 유저가 채팅방을 삭제하면 다른 모든 유저들은 해당채팅방의 목록을 조회할 수 없는 문제가 있었습니다. 우선 ORM에서 쿼리를 어떻게 생성하는지 살펴봤습니다.

<details>
<summary>query</summary>
SELECT "chat_rooms"."id", "chat_rooms"."created_at", "chat_rooms"."updated_at", "chat_rooms"."room_name", "chat_rooms"."lastest_text" FROM "chat_rooms" INNER JOIN "chat_room_members" ON ("chat_rooms"."id" = "chat_room_members"."room_id") WHERE ("chat_room_members"."user_id" = 3 AND NOT (EXISTS(SELECT 1 AS "a" FROM "chat_room_members" U1 WHERE (NOT U1."is_visibled" AND U1."room_id" = ("chat_rooms"."id")) LIMIT 1))) ORDER BY "chat_rooms"."updated_at" DESC
</details>

EXISTS... Rooms에 is_visibled가 False인 경우가 하나라도 있는지 확인하고 있으면 조회가 되지 않는 문제였고 아래와 같이 수정하여 문제를 해결했습니다.

```python
class RoomListAPIView(generics.ListAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        user_id = get_user_id(self.request)
        room_ids = Room_members.objects.filter(
            user=user_id, is_visibled=True
        ).values_list("room", flat=True)
        queryset = Rooms.objects.filter(id__in=room_ids)
        return queryset
```

<details>
<summary>query</summary>

1번쿼리
SELECT "chat_room_members"."room_id" FROM "chat_room_members" WHERE ("chat_room_members"."is_visibled" AND "chat_room_members"."user_id" = 1)

2번쿼리
SELECT "chat_rooms"."id", "chat_rooms"."created_at", "chat_rooms"."updated_at", "chat_rooms"."room_name", "chat_rooms"."lastest_text" FROM "chat_rooms" WHERE "chat_rooms"."id" IN (SELECT U0."room_id" FROM "chat_room_members" U0 WHERE (U0."is_visibled" AND U0."user_id" = 1)) ORDER BY "chat_rooms"."created_at" DESC, "chat_rooms"."updated_at" DESC

</details>

[최종 채팅]
<img src=https://github.com/Infinity-Scroll/Infinity_Travel_BE/assets/138690980/e4098055-fd11-498d-8921-c1d214c10532>



## 9.프로젝트 후기(배운점 & 느낀점)

### 김창환

모두 프로젝트 기간동안 고생하셨습니다. 첫 팀 프로젝트에서 팀장 역할을 맡아 팀을 이끌었지만 부족한 모습만 팀원분들에게 보여준것 같아 죄송합니다. 그래도 끝까지 따라와주시고 노력해주셔서 감사합니다. 팀으로써 협업을통해 할수있는 경험들을 얻게되었습니다. 프로젝트를 진행하며 재미있는 경험, 아쉬운 경험도 있었고 저에게 큰 자극이 되어 성장하는 계기가 된것같아 만족하고 있습니다. 프로젝트 기간동안 좋은 경험을 얻게 해주신 정식님,주용님,여범님에게 감사 인사를 드립니다. 앞으로도 이 경험을 기억하며 더 노력하는 개발자가 되도록 하겠습니다.

### 남정식

프로젝트의 전체 스펙을 파악하지 못해 필요한 업무 목록, 업무 분배에 문제를 겪었습니다
본인의 역량이나 행동력에 대해 정량적으로 알 수 있는 기회였고, 여러 번의 프로젝트 경험을 통해 구체화 할 수 있었다
기존 있던 프로젝트를 참고 함으로서 현재 서비스 되는 프로젝트들의 스펙을 확인하는 경험을 했다

### 심주용

처음 접해본 팀 프로젝트의 진행 상황 및 과정에 대해 기대에 부응하는 부분과 기대와 어긋나는 부분 등에 확실한 경험을 하게 되어 기쁩니다.
프로젝트의 경험으로 문제해결에 대한 고민할 시간이 많았으며, 이에 대해 조금씩 공부하는 느낌을 받았습니다.
스스로의 개발 속도에 대해 알아볼 수 있었으며, 자가발전을 위한 방향성을 찾을 수 있었습니다.



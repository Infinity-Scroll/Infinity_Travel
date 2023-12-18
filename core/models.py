from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at", "-updated_at"]


class AreaModel(models.Model):
    AREA_CHOICES = [
        # 대륙 목록
        ('동아시아', '동아시아'),
        ('동남아시아', '동남아시아'),
        ('중앙아시아', '중앙아시아'),
        ('서남아시아', '서남아시아'),
        ('유럽', '유럽'),
        ('오세아니아', '오세아니아'),
        ('아프리카', '아프리카'),
        ('북아메리카', '북아메리카'),
        ('남아메리카', '남아메리카'),

        # 동아시아 국가 목록
        ('한국', '한국'),
        ('몽골', '몽골'),
        ('중국', '중국'),
        ('대만', '대만'),
        ('마카오', '마카오'),
        ('홍콩', '홍콩'),
        ('일본', '일본'),
        # 동남아시아 국가 목록
        ('인도네시아', '인도네시아'),
        ('태국', '태국'),
        ('베트남', '베트남'),
        ('싱가포르', '싱가포르'),
        ('말레이시아', '말레이시아'),
        ('필리핀', '필리핀'),
        ('미얀마', '미얀마'),
        ('캄보디아', '캄보디아'),
        ('라오스', '라오스'),
        ('동티모르', '동티모르'),
        ('브루나이', '브루나이'),
        # 중앙아시아 국가 목록
        ('아제르바이잔', '아제르바이잔'),
        ('부탄', '부탄'),
        ('아프가니스탄', '아프가니스탄'),
        ('타지키스탄', '타지키스탄'),
        ('키르기스스탄', '키르기스스탄'),
        ('카자흐스탄', '카자흐스탄'),
        ('투르크메니스탄', '투르크메니스탄'),
        ('우즈베키스탄', '우즈베키스탄'),
        ('방글라데시', '방글라데시'),
        ('티베트', '티베트'),
        # 서남아시아 국가 목록
        ('아르메니아', '아르메니아'),
        ('카타르', '카타르'),
        ('이스라엘', '이스라엘'),
        ('네팔', '네팔'),
        ('인도', '인도'),
        ('오만', '오만'),
        ('아랍에미리트', '아랍에미리트'),
        ('몰디브', '몰디브'),
        ('스리랑카', '스리랑카'),
        ('키프로스', '키프로스'),
        ('파키스탄', '파키스탄'),
        ('이란', '이란'),
        ('시리아', '시리아'),
        ('예멘', '예멘'),
        ('요르단', '요르단'),
        ('바레인', '바레인'),
        ('이라크', '이라크'),
        ('팔레스타인', '팔레스타인'),
        ('쿠웨이트', '쿠웨이트'),
        ('사우디아라비아', '사우디아라비아'),
        ('레바논', '레바논'),
        # 유럽 국가 목록
        ('크로아티아', '크로아티아'),
        ('우크라이나', '우크라이나'),
        ('에스토니아', '에스토니아'),
        ('알바니아', '알바니아'),
        ('안도라', '안도라'),
        ('슬로바키아', '슬로바키아'),
        ('세르비아', '세르비아'),
        ('산마리노', '산마리노'),
        ('불가리아', '불가리아'),
        ('보스니아헤르체고비나', '보스니아헤르체고비나'),
        ('조지아', '조지아'),
        ('벨라루스', '벨라루스'),
        ('스웨덴', '스웨덴'),
        ('핀란드', '핀란드'),
        ('아이슬란드', '아이슬란드'),
        ('폴란드', '폴란드'),
        ('포르투갈', '포르투갈'),
        ('스위스', '스위스'),
        ('독일', '독일'),
        ('네덜란드', '네덜란드'),
        ('오스트리아', '오스트리아'),
        ('영국', '영국'),
        ('노르웨이', '노르웨이'),
        ('덴마크', '덴마크'),
        ('슬로베니아', '슬로베니아'),
        ('체코', '체코'),
        ('벨기에', '벨기에'),
        ('헝가리', '헝가리'),
        ('아일랜드', '아일랜드'),
        ('러시아', '러시아'),
        ('그리스', '그리스'),
        ('스페인', '스페인'),
        ('터키', '터키'),
        ('이탈리아', '이탈리아'),
        ('프랑스', '프랑스'),
        ('바티칸', '바티칸'),
        ('몰타', '몰타'),
        ('몰도바', '몰도바'),
        ('몬테네그로', '몬테네그로'),
        ('모나코', '모나코'),
        ('마케도니아', '마케도니아'),
        ('리히텐슈타인', '리히텐슈타인'),
        ('리투아니아', '리투아니아'),
        ('룩셈부르크', '룩셈부르크'),
        ('루마니아', '루마니아'),
        ('라트비아', '라트비아'),
        # 오세아니아 국가 목록
        ('나우루', '나우루'),
        ('마셜제도', '마셜제도'),
        ('피지', '피지'),
        ('팔라우', '팔라우'),
        ('파푸아뉴기니', '파푸아뉴기니'),
        ('통가', '통가'),
        ('키리바시', '키리바시'),
        ('솔로몬제도', '솔로몬제도'),
        ('사모아', '사모아'),
        ('바누아투', '바누아투'),
        ('미크로네시아', '미크로네시아'),
        ('뉴질랜드', '뉴질랜드'),
        ('호주', '호주'),
        # 아프리카 국가 목록
        ('르완다', '르완다'),
        ('레소토', '레소토'),
        ('라이베리아', '라이베리아'),
        ('니제르', '니제르'),
        ('남수단', '남수단'),
        ('나이지리아', '나이지리아'),
        ('기니비사우', '기니비사우'),
        ('기니', '기니'),
        ('감비아', '감비아'),
        ('가봉', '가봉'),
        ('가나', '가나'),
        ('리비아', '리비아'),
        ('튀니지', '튀니지'),
        ('토고', '토고'),
        ('콩고민주공화국', '콩고민주공화국'),
        ('콩고공화국', '콩고공화국'),
        ('코트디부아르', '코트디부아르'),
        ('코모로', '코모로'),
        ('카보베르데', '카보베르데'),
        ('카메룬', '카메룬'),
        ('차드', '차드'),
        ('짐바브웨', '짐바브웨'),
        ('지부티', '지부티'),
        ('중앙아프리카공화국', '중앙아프리카공화국'),
        ('적도기니', '적도기니'),
        ('상투메프린시페', '상투메프린시페'),
        ('부르키나파소', '부르키나파소'),
        ('부룬디', '부룬디'),
        ('보츠와나', '보츠와나'),
        ('베냉', '베냉'),
        ('모잠비크', '모잠비크'),
        ('모리타니', '모리타니'),
        ('모리셔스', '모리셔스'),
        ('말리', '말리'),
        ('말라위', '말라위'),
        ('서사하라', '서사하라'),
        ('세네갈', '세네갈'),
        ('잠비아', '잠비아'),
        ('우간다', '우간다'),
        ('에리트레아', '에리트레아'),
        ('앙골라', '앙골라'),
        ('알제리', '알제리'),
        ('시에라리온', '시에라리온'),
        ('에스와티니', '에스와티니'),
        ('수단', '수단'),
        ('소말리아', '소말리아'),
        ('세이셸', '세이셸'),
        ('마다가스카르', '마다가스카르'),
        ('나미비아', '나미비아'),
        ('케냐', '케냐'),
        ('에티오피아', '에티오피아'),
        ('탄자니아', '탄자니아'),
        ('남아프리카공화국', '남아프리카공화국'),
        ('이집트', '이집트'),
        ('모로코', '모로코'),
        # 북아메리카 국가 목록
        ('가이아나', '가이아나'),
        ('파나마', '파나마'),
        ('트리니다드토바고', '트리니다드토바고'),
        ('코스타리카', '코스타리카'),
        ('자메이카', '자메이카'),
        ('온두라스', '온두라스'),
        ('엘살바도르', '엘살바도르'),
        ('과테말라', '과테말라'),
        ('니카라과', '니카라과'),
        ('엔티가바부다', '엔티가바부다'),
        ('아이티', '아이티'),
        ('세인트키츠 네비스', '세인트키츠 네비스'),
        ('세인트빈센트그레나딘', '세인트빈센트그레나딘'),
        ('세인트루시아', '세인트루시아'),
        ('벨리즈', '벨리즈'),
        ('바하마', '바하마'),
        ('도미니카연방', '도미니카연방'),
        ('도미니카공화국', '도미니카공화국'),
        ('멕시코', '멕시코'),
        ('캐나다', '캐나다'),
        ('미국', '미국'),
        ('쿠바', '쿠바'),
        # 남아메리카 국가 목록
        ('콜롬비아', '콜롬비아'),
        ('우루과이', '우루과이'),
        ('에콰도르', '에콰도르'),
        ('수리남', '수리남'),
        ('브라질', '브라질'),
        ('베네수엘라', '베네수엘라'),
        ('파라과이', '파라과이'),
        ('그린란드', '그린란드'),
        ('그레나다', '그레나다'),
        ('바베이도스', '바베이도스'),
        ('페루', '페루'),
        ('볼리비아', '볼리비아'),
        ('아르헨티나', '아르헨티나'),
        ('칠레', '칠레'),

        # 동아시아
        # 한국 여행지 목록
        ('서울', '서울'),
        ('부산', '부산'),
        ('인천', '인천'),
        ('경기도', '경기도'),
        ('강원도', '강원도'),
        ('충청도', '충청도'),
        ('경상도', '경상도'),
        ('전라도', '전라도'),
        ('제주도', '제주도'),
        ('울릉도', '울릉도'),
        # 몽골 여행지 목록
        ('울란바토르', '울란바토르'),
        # 중국 여행지 목록
        ('베이징', '베이징'),
        ('서안', '서안'),
        ('충칭', '충칭'),
        ('장가계', '장가계'),
        ('항저우', '항저우'),
        ('하이난', '하이난'),
        ('광저우', '광저우'),
        ('청두', '청두'),
        ('칭다오', '칭다오'),
        ('상하이', '상하이'),
        # 대만 여행지 목록
        ('타이페이', '타이페이'),
        ('타이난', '타이난'),
        ('가오슝', '가오슝'),
        ('타이중', '타이중'),
        # 마카오 여행지 목록
        ('마카오', '마카오'),
        # 홍콩 여행지 목록
        ('홍콩', '홍콩'),
        # 일본 여행지 목록
        ('도쿄', '도쿄'),
        ('오사카', '오사카'),
        ('나가노', '나가노'),
        ('후쿠오카', '후쿠오카'),
        ('오키나와', '오키나와'),
        ('나고야', '나고야'),
        ('히로시마', '히로시마'),
        ('훗카이도', '훗카이도'),
        ('교토', '교토'),

        # 동남아시아
        # 인도네시아 여행지 목록
        ('자카르타', '자카르타'),
        ('수라바야', '수라바야'),
        ('반둥', '반둥'),
        ('족자카르타', '족자카르타'),
        ('바탐', '바탐'),
        ('롬복', '롬복'),
        ('발리', '발리'),
        # 태국 여행지 목록
        ('방콕', '방콕'),
        ('코창', '코창'),
        ('후야힌', '후야힌'),
        ('끄라비', '끄라비'),
        ('코사무이', '코사무이'),
        ('푸켓', '푸켓'),
        ('치앙마이', '치앙마이'),
        ('파타야', '파타야'),
        ('피피섬', '피피섬'),
        ('치앙라이', '치앙라이'),
        # 베트남 여행지 목록
        ('하노이', '하노이'),
        ('호치민', '호치민'),
        ('후에', '후에'),
        ('호이안', '호이안'),
        ('다낭', '다낭'),
        ('푸꾸옥', '푸꾸옥'),
        ('사파', '사파'),
        ('나트랑', '나트랑'),
        ('달랏', '달랏'),
        # 싱가포르 여행지 목록
        ('싱가포르', '싱가포르'),
        # 말레이시아 여행지 목록
        ('쿠알라룸푸르', '쿠알라룸푸르'),
        ('코타키나발루', '코타키나발루'),
        ('페낭', '페낭'),
        ('랑카위', '랑카위'),
        ('조호바루', '조호바루'),
        ('켄팅 하이랜드', '켄팅 하이랜드'),
        # 필리핀 여행지 목록
        ('마닐라', '마닐라'),
        ('수빅 클락', '수빅 클락'), # '수빅 & 클락'이 아닌 이유 : JSON 에서 & 를 사용할 때 오류 발생
        ('보홀', '보홀'),
        ('팔라완', '팔라완'),
        ('세부', '세부'),
        ('보라카이', '보라카이'),
        # 미얀마 여행지 목록
        ('나팔리', '나팔리'),
        ('이레호수', '이레호수'),
        ('만달레이', '만달레이'),
        ('바간', '바간'),
        ('양곤', '양곤'),
        # 캄보디아 여행지 목록
        ('프놈펜', '프놈펜'),
        ('씨엠립', '씨엠립'),
        # 라오스 여행지 목록
        ('비엔티안', '비엔티안'),
        ('방비엥', '방비엥'),
        ('루앙프라방', '루앙프라방'),
        # 동티모르 여행지 목록
        # 브루나이 여행지 목록

        # 중앙아시아
        # 아제르바이잔 여행지 목록
        # 부탄 여행지 목록
        # 아프가니스탄 여행지 목록
        # 타지키스탄 여행지 목록
        # 키르기스스탄 여행지 목록
        # 카자흐스탄 여행지 목록
        # 투르크메니스탄 여행지 목록
        # 우즈베키스탄 여행지 목록
        # 방글라데시 여행지 목록
        # 티베트 여행지 목록

        # 서남아시아
        # 아르메니아 여행지 목록
        # 카타르 여행지 목록
        ('도하', '도하'),
        # 이스라엘 여행지 목록
        ('예루살렘', '예루살렘'),
        ('텔아비브', '텔아비브'),
        # 네팔 여행지 목록
        ('카트만두', '카트만두'),
        ('포카라', '포카라'),
        # 인도 여행지 목록
        ('델리', '델리'),
        ('우다이푸르', '우다이푸르'),
        ('자이푸르', '자이푸르'),
        ('뭄바이', '뭄바이'),
        ('바라나시', '바라나시'),
        ('아그라', '아그라'),
        # 오만 여행지 목록
        ('무스카트', '무스카트'),
        # 아랍에미리트 여행지 목록
        ('아부다비', '아부다비'),
        ('두바이', '두바이'),
        # 몰디브 여행지 목록
        # 스리랑카 여행지 목록
        # 키프로스 여행지 목록
        # 파키스탄 여행지 목록
        # 이란 여행지 목록
        # 시리아 여행지 목록
        # 예멘 여행지 목록
        # 요르단 여행지 목록
        # 바레인 여행지 목록
        # 이라크 여행지 목록
        # 팔레스타인 여행지 목록
        # 쿠웨이트 여행지 목록
        # 사우디아라비아 여행지 목록
        # 레바논 여행지 목록

        # 유럽
        # 크로아티아 여행지 목록
        # 우크라이나 여행지 목록
        # 에스토니아 여행지 목록
        # 알바니아 여행지 목록
        # 안도라 여행지 목록
        # 슬로바키아 여행지 목록
        # 세르비아 여행지 목록
        # 산마리노 여행지 목록
        # 불가리아 여행지 목록
        # 보스니아헤르체고비나 여행지 목록
        # 조지아 여행지 목록
        # 벨라루스 여행지 목록
        # 스웨덴 여행지 목록
        ('스톡홀름', '스톡홀름'),
        # 핀란드 여행지 목록
        ('헬싱키', '헬싱키'),
        # 아이슬란드 여행지 목록
        ('레이캬비크', '레이캬비크'),
        # 폴란드 여행지 목록
        ('크라쿠프', '크라쿠프'),
        # 포르투갈 여행지 목록
        ('리스본', '리스본'),
        ('포르투', '포르투'),
        # 스위스 여행지 목록
        ('루체른', '루체른'),
        ('제네바', '제네바'),
        ('인터라켄', '인터라켄'),
        ('취리히', '취리히'),
        # 독일 여행지 목록
        ('베를린', '베를린'),
        ('뮌헨', '뮌헨'),
        ('함부르크', '함부르크'),
        ('프랑크푸르트', '프랑크푸르트'),
        # 네덜란드 여행지 목록
        ('암스테르담', '암스테르담'),
        # 오스트리아 여행지 목록
        ('비엔나', '비엔나'),
        # 영국 여행지 목록
        ('런던', '런던'),
        ('에딘버러', '에딘버러'),
        ('맨체스터', '맨체스터'),
        ('리버풀', '리버풀'),
        # 노르웨이 여행지 목록
        ('오슬로', '오슬로'),
        ('베르겐', '베르겐'),
        ('트롬쇠', '트롬쇠'),
        # 덴마크 여행지 목록
        ('코펜하겐', '코펜하겐'),
        # 슬로베니아 여행지 목록
        ('류블랴나', '류블랴나'),
        # 체코 여행지 목록
        ('프라하', '프라하'),
        ('크룸로프', '크룸로프'),
        # 벨기에 여행지 목록
        ('브뤼셀', '브뤼셀'),
        ('브뤼헤', '브뤼헤'),
        # 헝가리 여행지 목록
        ('부다페스트', '부다페스트'),
        # 아일랜드 여행지 목록
        ('더블린', '더블린'),
        # 러시아 여행지 목록
        ('모스크바', '모스크바'),
        ('상트페테르부르크', '상트페테르부르크'),
        ('블라디보스톡', '블라디보스톡'),
        ('이르쿠츠크', '이르쿠츠크'),
        # 그리스 여행지 목록
        ('아테네', '아테네'),
        ('산토리니', '산토리니'),
        # 스페인 여행지 목록
        ('마드리드', '마드리드'),
        ('바르셀로나', '바르셀로나'),
        ('그라나다', '그라나다'),
        ('세비야', '세비야'),
        ('톨레도', '톨레도'),
        # 터키 여행지 목록
        ('이스탄불', '이스탄불'),
        ('카파도키아', '카파도키아'),
        # 이탈리아 여행지 목록
        ('로마', '로마'),
        ('피사', '피사'),
        ('나폴리', '나폴리'),
        ('밀라노', '밀라노'),
        ('베네치아', '베네치아'),
        ('피렌체', '피렌체'),
        # 프랑스 여행지 목록
        ('파리', '파리'),
        ('마르세유', '마르세유'),
        ('알자스', '알자스'),
        ('니스', '니스'),
        # 바티칸 여행지 목록
        # 몰타 여행지 목록
        # 몰도바 여행지 목록
        # 몬테네그로 여행지 목록
        # 모나코 여행지 목록
        # 마케도니아 여행지 목록
        # 리히텐슈타인 여행지 목록
        # 리투아니아 여행지 목록
        # 룩셈부르크 여행지 목록
        # 루마니아 여행지 목록
        # 라트비아 여행지 목록

        # 오세아니아
        # 나우루 여행지 목록
        # 마셜제도 여행지 목록
        # 피지 여행지 목록
        # 팔라우 여행지 목록
        # 파푸아뉴기니 여행지 목록
        # 통가 여행지 목록
        # 키리바시 여행지 목록
        # 솔로몬제도 여행지 목록
        # 사모아 여행지 목록
        # 바누아투 여행지 목록
        # 미크로네시아 여행지 목록
        # 뉴질랜드 여행지 목록
        ('퀸즈타운', '퀸즈타운'),
        ('오클랜드', '오클랜드'),
        ('로토루아', '로토루아'),
        ('크라이스트처치', '크라이스트처치'),
        # 호주 여행지 목록
        ('시드니', '시드니'),
        ('퍼스', '퍼스'),
        ('케언즈', '케언즈'),
        ('멜버른', '멜버른'),
        ('브리즈번', '브리즈번'),

        # 아프리카
        # 르완다 여행지 목록
        # 레소토 여행지 목록
        # 라이베리아 여행지 목록
        # 니제르 여행지 목록
        # 남수단 여행지 목록
        # 나이지리아 여행지 목록
        # 기니비사우 여행지 목록
        # 기니 여행지 목록
        # 감비아 여행지 목록
        # 가봉 여행지 목록
        # 가나 여행지 목록
        # 리비아 여행지 목록
        # 튀니지 여행지 목록
        # 토고 여행지 목록
        # 콩고민주공화국 여행지 목록
        # 콩고공화국 여행지 목록
        # 코트디부아르 여행지 목록
        # 코모로 여행지 목록
        # 카보베르데 여행지 목록
        # 카메룬 여행지 목록
        # 차드 여행지 목록
        # 짐바브웨 여행지 목록
        # 지부티 여행지 목록
        # 중앙아프리카공화국 여행지 목록
        # 적도기니 여행지 목록
        # 상투메프린시페 여행지 목록
        # 부르키나파소 여행지 목록
        # 부룬디 여행지 목록
        # 보츠와나 여행지 목록
        # 베냉 여행지 목록
        # 모잠비크 여행지 목록
        # 모리타니 여행지 목록
        # 모리셔스 여행지 목록
        # 말리 여행지 목록
        # 말라위 여행지 목록
        # 서사하라 여행지 목록
        # 세네갈 여행지 목록
        # 잠비아 여행지 목록
        # 우간다 여행지 목록
        # 에리트레아 여행지 목록
        # 앙골라 여행지 목록
        # 알제리 여행지 목록
        # 시에라리온 여행지 목록
        # 에스와티니 여행지 목록
        # 수단 여행지 목록
        # 소말리아 여행지 목록
        # 세이셸 여행지 목록
        # 마다가스카르 여행지 목록
        # 나미비아 여행지 목록
        ('빈트후크', '빈트후크'),
        ('스와콥문트', '스와콥문트'),
        # 케냐 여행지 목록
        ('나이로비', '나이로비'),
        # 에티오피아 여행지 목록
        ('아디스아바바', '아디스아바바'),
        # 탄자니아 여행지 목록
        ('다르에스살람', '다르에스살람'),
        ('잔지바르', '잔지바르'),
        ('킬리만자로', '킬리만자로'),
        ('아루샤', '아루샤'),
        # 남아프리카공화국 여행지 목록
        ('케이프타운', '케이프타운'),
        ('요하네스버그', '요하네스버그'),
        # 이집트 여행지 목록
        ('카이로', '카이로'),
        ('후루가다', '후루가다'),
        ('아스완', '아스완'),
        ('룩소르', '룩소르'),
        # 모로코 여행지 목록
        ('카사블랑카', '카사블랑카'),
        ('페스', '페스'),
        ('마라케시', '마라케시'),

        # 북아메리카
        # 가이아나 여행지 목록
        # 파나마 여행지 목록
        # 트리니다드토바고 여행지 목록
        # 코스타리카 여행지 목록
        # 자메이카 여행지 목록
        # 온두라스 여행지 목록
        # 엘살바도르 여행지 목록
        # 과테말라 여행지 목록
        # 니카라과 여행지 목록
        # 엔티가바부다 여행지 목록
        # 아이티 여행지 목록
        # 세인트키츠 네비스 여행지 목록
        # 세인트빈센트그레나딘 여행지 목록
        # 세인트루시아 여행지 목록
        # 벨리즈 여행지 목록
        # 바하마 여행지 목록
        # 도미니카연방 여행지 목록
        # 도미니카공화국 여행지 목록
        # 멕시코 여행지 목록
        ('칸쿤', '칸쿤'),
        # 캐나다 여행지 목록
        ('토론토', '토론토'),
        ('캘거리', '캘거리'),
        ('벤쿠버', '벤쿠버'),
        ('퀘벡', '퀘벡'),
        # 미국 여행지 목록
        ('워싱턴 D.C.', '워싱턴 D.C.'),
        ('뉴욕', '뉴욕'),
        ('샌프란시스코', '샌프란시스코'),
        ('로스앤젤레스', '로스앤젤레스'),
        ('라스베가스', '라스베가스'),
        ('시카고', '시카고'),
        ('사이판', '사이판'),
        ('괌', '괌'),
        ('하와이', '하와이'),
        ('샌디에이고', '샌디에이고'),
        ('보스턴', '보스턴'),
        ('시애틀', '시애틀'),
        ('마이애미', '마이애미'),
        ('필라델피아', '필라델피아'),
        ('올랜도', '올랜도'),
        # 쿠바 여행지 목록
        ('아바나', '아바나'),

        # 남아메리카
        # 콜롬비아 여행지 목록
        # 우루과이 여행지 목록
        # 에콰도르 여행지 목록
        # 수리남 여행지 목록
        # 브라질 여행지 목록
        # 베네수엘라 여행지 목록
        # 파라과이 여행지 목록
        # 그린란드 여행지 목록
        # 그레나다 여행지 목록
        # 바베이도스 여행지 목록
        # 페루 여행지 목록
        ('리마', '리마'),
        # 볼리비아 여행지 목록
        ('라파스', '라파스'),
        ('우유니', '우유니'),
        # 아르헨티나 여행지 목록
        ('부에노스아이레스', '부에노스아이레스'),
        # 칠레 여행지 목록
        ('산티아고', '산티아고'),
        ('산페드로데아타카마', '산페드로데아타카마'),
    ]

    area = models.CharField(max_length=20, choices=AREA_CHOICES, null=True)
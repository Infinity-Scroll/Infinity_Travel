import random


def generate_random_nickname():
    first = [
        "즐거운",
        "행복한",
        "도전하는",
        "용감한",
        "고독한",
        "친절한",
        "신비한",
        "멋진",
        "호기심많은",
        "똑똑한",
        "무한",
        "나만의",
        "당당한",
    ]
    second = [
        "나무늘보",
        "초코칩",
        "앵무새",
        "악어",
        "사자",
        "청설모",
        "도룡뇽",
        "오징어",
        "독수리",
        "기린",
        "까치",
        "카피바라",
        "미어캣",
        "고슴도치",
        "사슴",
        "북극곰",
        "토끼",
        "용",
        "너구리",
        "하마",
    ]
    first = random.choice(first)
    second = random.choice(second)

    return first + " " + second

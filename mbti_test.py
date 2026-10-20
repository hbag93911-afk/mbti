
# 성격유형검사 프로그램
# MBTI와 유사한 16가지 성격유형을 판별하는 간단한 검사

questions = [
    ("사람들과 함께 있을 때 에너지가 생긴다.", "E", "I"),
    ("혼자 있는 시간이 있어야 에너지가 충전된다.", "I", "E"),
    ("새로운 사람을 만나는 것이 즐겁다.", "E", "I"),

    ("실제 경험과 구체적인 사실을 중요하게 생각한다.", "S", "N"),
    ("미래의 가능성과 상상력을 중요하게 생각한다.", "N", "S"),
    ("설명할 때 구체적인 사례를 선호한다.", "S", "N"),

    ("결정을 내릴 때 논리와 객관적인 기준을 우선한다.", "T", "F"),
    ("결정을 내릴 때 사람들의 감정을 중요하게 생각한다.", "F", "T"),
    ("문제를 해결할 때 사실과 논리를 먼저 살펴본다.", "T", "F"),

    ("계획을 세우고 일정에 맞춰 행동하는 편이다.", "J", "P"),
    ("상황에 따라 계획을 유연하게 바꾸는 편이다.", "P", "J"),
    ("미리 일을 끝내 놓으면 마음이 편하다.", "J", "P"),
]

descriptions = {
    "ISTJ": "책임감이 강하고 체계적이며 현실적입니다.",
    "ISFJ": "세심하고 배려심이 많으며 성실합니다.",
    "INFJ": "통찰력이 있고 타인을 이해하려는 성향이 있습니다.",
    "INTJ": "전략적이고 독립적이며 목표 지향적입니다.",
    "ISTP": "실용적이고 분석적이며 문제 해결에 강합니다.",
    "ISFP": "온화하고 감수성이 풍부하며 자유를 중시합니다.",
    "INFP": "이상적이고 공감 능력이 높으며 가치관을 중시합니다.",
    "INTP": "호기심이 많고 논리적이며 분석을 즐깁니다.",
    "ESTP": "활동적이고 현실적이며 즉각적인 대응에 강합니다.",
    "ESFP": "사교적이고 활기차며 즐거운 경험을 중시합니다.",
    "ENFP": "창의적이고 열정적이며 새로운 가능성을 즐깁니다.",
    "ENTP": "아이디어가 풍부하고 토론과 도전을 즐깁니다.",
    "ESTJ": "조직적이고 실용적이며 책임감이 강합니다.",
    "ESFJ": "친절하고 협조적이며 공동체를 중시합니다.",
    "ENFJ": "공감 능력이 높고 사람들을 이끄는 데 관심이 있습니다.",
    "ENTJ": "목표 지향적이고 결단력이 있으며 계획적으로 행동합니다.",
}


def run_personality_test():
    scores = {"E": 0, "I": 0, "S": 0, "N": 0,
              "T": 0, "F": 0, "J": 0, "P": 0}

    print("=" * 40)
    print("       성격유형검사 프로그램")
    print("=" * 40)
    print("각 질문에 가장 가까운 답을 선택하세요.")
    print("1. 그렇다 / 나와 비슷하다")
    print("2. 아니다 / 나와 다르다")
    print()

    for number, (question, first, second) in enumerate(questions, 1):
        while True:
            print(f"{number}. {question}")
            answer = input("답변 (1 또는 2): ").strip()

            if answer in ("1", "2"):
                break

            print("잘못된 입력입니다. 1 또는 2를 입력하세요.\n")

        if answer == "1":
            scores[first] += 1
        else:
            scores[second] += 1

        print()

    # 각 지표에서 점수가 높은 유형을 선택
    personality = ""
    pairs = [("E", "I"), ("S", "N"), ("T", "F"), ("J", "P")]

    for first, second in pairs:
        if scores[first] > scores[second]:
            personality += first
        elif scores[second] > scores[first]:
            personality += second
        else:
            # 동점이면 첫 번째 지표를 선택
            personality += first

    print("=" * 40)
    print(f"당신의 성격유형은 {personality} 입니다!")
    print("=" * 40)
    print(descriptions[personality])
    print("\n[성격 지표별 점수]")

    for first, second in pairs:
        print(f"{first}: {scores[first]}점 / "
              f"{second}: {scores[second]}점")

    print("\n검사 결과는 참고용이며 성격을 확정하는 진단이 아닙니다.")


if __name__ == "__main__":
    run_personality_test()


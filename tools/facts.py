"""바뀔 수 있는 규정값·통계 수치를 한곳에서 관리한다.

레슨 빌더는 수치를 직접 쓰지 않고 F("키")로 문장 조각을 가져온다.
값이 바뀌면 이 파일만 고치고 해당 챕터를 다시 빌드한다.
tools/check_facts.py가 점검 주기가 지난 항목과 각 값이 쓰인 레슨을 보여 준다.

항목 필드
- text: 레슨에 들어가는 문장 조각 (기준 시점을 함께 적는다)
- value: 문항 정답으로 쓰는 값 (없으면 None)
- as_of: 수치의 기준 시점
- source: 확인한 출처
- checked: 마지막으로 확인한 날짜 (YYYY-MM-DD)
- cycle: 점검 주기(일)
"""

FACTS = {
    "tfr_latest": dict(
        text="2025년 합계 출산율은 0.80명",
        value="0.80", as_of="2025년", source="국가데이터처 인구동향(출생 통계), 2026 보도",
        checked="2026-10-13", cycle=365),
    "tfr_prev": dict(
        text="2024년 합계 출산율은 0.75명",
        value="0.75", as_of="2024년", source="통계청 2024년 출생 통계(확정)",
        checked="2026-10-13", cycle=730),
    "elderly_census": dict(
        text="2025년 인구주택총조사(11월 1일 기준)에서 65세 이상 인구 비율은 20.7%",
        value="20.7", as_of="2025-11-01", source="국가데이터처 2025 인구주택총조사 발표(2026-07-28)",
        checked="2026-10-13", cycle=365),
    "superaged_entry": dict(
        text="2024년 12월 주민등록 인구 기준 65세 이상 인구 비율이 20%를 넘어",
        value="2024", as_of="2024-12", source="행정안전부 주민등록 인구 통계(2024-12-24 발표)",
        checked="2026-10-13", cycle=3650),
    "stats_agency": dict(
        text="국가데이터처(옛 통계청)",
        value="국가데이터처", as_of="2025-10", source="정부 조직 개편(2025-10)",
        checked="2026-10-13", cycle=365),
}


def F(key):
    return FACTS[key]["text"]


def V(key):
    return FACTS[key]["value"]

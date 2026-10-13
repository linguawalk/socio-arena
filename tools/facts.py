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
    # 지리Ⅰ(c6)
    "world_pop_8b": dict(
        text="2022년 11월 15일 세계 인구가 80억 명을 넘었다고",
        value="80", as_of="2022-11-15", source="국제 연합(UN) 발표",
        checked="2026-10-14", cycle=3650),
    "world_pop_latest": dict(
        text="2025년 세계 인구는 약 82억 명",
        value="82", as_of="2025년", source="국제 연합 세계 인구 전망(World Population Prospects 2024)",
        checked="2026-10-14", cycle=730),
    "global_temp_2024": dict(
        text="2024년 지구 평균 기온은 산업화 이전보다 약 1.55℃ 높아, 한 해 평균으로는 처음 1.5℃를 넘었다",
        value="1.55", as_of="2024년", source="세계 기상 기구(WMO) 발표(2025-01)",
        checked="2026-10-14", cycle=365),
    "korea_ndc_2035": dict(
        text="2035년까지 온실가스 배출량을 2018년보다 53~61% 줄이는",
        value="53~61", as_of="2025-11-11", source="2035 국가 온실가스 감축 목표(국무회의 의결 2025-11-11)",
        checked="2026-10-14", cycle=730),
    # 지리Ⅱ(c7)
    "capital_half": dict(
        text="2020년 말 주민등록 인구 기준으로 수도권 인구가 전체의 50.2%를 차지해",
        value="50", as_of="2020-12", source="행정안전부 주민등록 인구 통계(2021-01 발표)",
        checked="2026-10-14", cycle=3650),
    # 정치와 법Ⅰ(c8)
    "voting_age": dict(
        text="2019년 공직 선거법 개정으로 선거권 연령이 만 18세로 낮아졌습니다",
        value="18", as_of="2019-12", source="공직선거법 개정(2020-01-14 공포)",
        checked="2026-10-14", cycle=1460),
    "candidacy_age": dict(
        text="2021년 공직 선거법 개정으로 국회의원과 지방 선거의 피선거권 연령도 만 18세로 낮아졌습니다",
        value="18", as_of="2021-12", source="공직선거법 개정(2022-01-18 공포)",
        checked="2026-10-14", cycle=1460),
    "party_age": dict(
        text="2022년 정당법 개정으로 만 16세부터 정당에 가입할 수 있게 되었습니다",
        value="16", as_of="2022-01", source="정당법 개정(2022-01-11 국회 의결)",
        checked="2026-10-14", cycle=1460),
    "assembly_seats": dict(
        text="국회의원 정수는 300명이며, 2024년 제22대 국회의원 선거에서는 지역구 254명, 비례 대표 46명을 뽑았습니다",
        value="300", as_of="2024-04", source="중앙선거관리위원회 제22대 국회의원선거 결과",
        checked="2026-10-14", cycle=1460),
    "pr_system": dict(
        text="2020년과 2024년 국회의원 선거에서는 준연동형 비례 대표제가 적용되었습니다",
        value="준연동형", as_of="2024-04", source="공직선거법(2019-12 개정), 제22대 총선",
        checked="2026-10-14", cycle=1460),
    "metro_count": dict(
        text="2026년 7월 전라남도와 광주광역시가 합쳐진 전남광주통합특별시가 출범하면서 광역 자치 단체는 16개가 되었습니다",
        value="16", as_of="2026-07-01", source="전남광주통합특별시 출범(2026-07-01), 제9회 전국동시지방선거",
        checked="2026-10-14", cycle=365),
    "un_members": dict(
        text="국제 연합(UN) 회원국은 193개국입니다",
        value="193", as_of="2011-07", source="국제 연합 회원국 목록(남수단 가입 2011-07)",
        checked="2026-10-14", cycle=730),
}


def F(key):
    return FACTS[key]["text"]


def V(key):
    return FACTS[key]["value"]

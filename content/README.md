# socio-arena 레슨 스키마 v1.0

sci-arena·math-arena 레슨 스키마 v1.0을 그대로 따른다. 플레이어(player.html)와 코스 목록(browse.html)도 sci-arena에서 가져와 문구와 채점 정규화만 바꾸었다.

경로: content/level{N}/{course}/ch{NN}/l{NN}.json
- 코스 목록: content/level1/courses.json (11과목, available로 공개 여부 표시)
- 코스 요약: content/level1/{course}/course.json (tools/make_course_index.py가 생성)
- 챕터 목록: content/level1/{course}/ch{NN}/chapter.json
- 챕터 복습 세트: content/level1/{course}/ch{NN}/review.json

## 코스 번호
| id | 과목 | 상태 |
| --- | --- | --- |
| c1 | 한국사Ⅰ | 공개 (8챕터, 레슨 32개, 569문항) |
| c2 | 한국사Ⅱ | 공개 (8챕터, 레슨 32개, 560문항) |
| c3 | 세계사Ⅰ | 준비 중 |
| c4 | 세계사Ⅱ | 준비 중 |
| c5 | 사회와 문화 | 준비 중 |
| c6 | 지리Ⅰ | 준비 중 |
| c7 | 지리Ⅱ | 준비 중 |
| c8 | 정치와 법Ⅰ | 준비 중 |
| c9 | 정치와 법Ⅱ | 준비 중 |
| c10 | 윤리Ⅰ | 준비 중 |
| c11 | 윤리Ⅱ | 준비 중 |

코스 0(중학 과정)은 두지 않는다. 각 과목 첫 단원의 도입 화면이 기초를 다진다.

## 레슨 파일
- course / chapter / lesson: id, 번호, 제목 (lesson.minutes = 예상 소요 시간)
- tags.domain: ["한국사"] 등 과목 태그, tags.region = KR, tags.curriculum = 2022-high
- screens: 화면 배열. stage = intro | discover | summary | apply
- 분량 기준: 레슨당 화면 20~24개, 문항 15~17개, 예제 3개

## 화면 유형
- explain: title, body(문단 배열)
- example: 자료 해석 예제. problem, steps(풀이 단계), answer
- question
  - fill_blank: 사건·인물·제도 이름. blanks[n].answers에 허용 표기(띄어쓰기 변형, 별칭)를 모두 넣는다
  - numeric: 연도. 기원전 연도는 문제에 "기원전 몇 년"으로 묻고 양수로 답한다
  - ordering: 사건 순서 배열
  - written: 서술형. rubric.keyword_groups 중 min_groups_matched개 이상 포함되면 통과
- 공통: hint(적용·복습 문항은 필수), explanation(20자 이상, 줄바꿈으로 단계 구분)

## 채점 정규화 (sci-arena와 다른 점)
- 공백, 가운뎃점(·ㆍ), 따옴표·낫표를 무시한다 ("한일 의정서" = "한일의정서")
- 괄호 속 한자 병기를 무시한다 ("녹읍(祿邑)" = "녹읍")
- 영문은 대소문자를 구분하지 않는다 ("SI" = "si")

## 빌드
```
python3 tools/build_c1_ch01.py content   # 챕터마다 실행 (ch01~ch08)
python3 tools/make_course_index.py content
```
- 공용 도구 tools/sk.py: 저장 전에 문항 수, 화면 수, 예제 수, 풀이 길이, 힌트, 빈칸 수, 복습 출처 레슨을 검사하고 기준을 벗어나면 실패한다
- 코스 공통: tools/c{코스}common.py (복습 문항의 source_lesson 지정)

## 바뀔 수 있는 내용
한국사Ⅱ 챕터 7(역대 정부 목록, 탄핵 심판)과 챕터 8(남북 관계)은 현재 상황에 따라 갱신이 필요하다. 그 밖의 역사는 내용이 거의 바뀌지 않지만, 세계 유산·기록 유산 등재 현황과 문화재 반환 상태는 바뀔 수 있다. 정치와 법, 사회와 문화 과목부터는 tech-arena의 점검 구조(규정값 한곳 관리·점검 스크립트)를 함께 넣는다.

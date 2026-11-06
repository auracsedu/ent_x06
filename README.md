# 시작하기

vscode에서 프로젝트를 열고, 아래 명령어를 실행하세요.
(명령어 대신 [VS Code 작업으로 실행하기](#vs-code-작업으로-실행하기)의 `환경 설정` 작업을 써도 됩니다.)

Windows:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\setup.ps1
```

MacOS:

```bash
chmod +x ./setup.sh
./setup.sh
```

# 테스트 돌리기

터미널에서 다음을 붙여넣으면 테스트가 됩니다.

## 전체 테스트하기

```bash
python -m pytest
```

## 특정 번호만 테스트하기

```bash
python -m pytest -k problem_01
```

# VS Code 작업으로 실행하기

터미널 명령어 대신 VS Code 메뉴 `Terminal > Run Task...` (한국어 UI: `터미널 > 작업 실행...`)에서 아래 작업을 선택해도 됩니다.

| 작업                 | 하는 일                                                                       |
| -------------------- | ----------------------------------------------------------------------------- |
| `환경 설정`          | `setup.ps1` / `setup.sh` 실행 (Windows에서는 실행 정책 설정 없이 바로 됩니다) |
| `전체 테스트`        | `python -m pytest`                                                            |
| `특정 번호만 테스트` | 문제 번호를 입력받아 `python -m pytest -k problem_번호` 실행                  |

# 문제 목록 (6주차: 매직 메서드)

각 파일 맨 위의 설명을 읽고, `raise NotImplementedError` 를 지우고 그 자리에 코드를 쓰세요.
"완성된 코드입니다"라고 적힌 클래스는 고치지 않습니다. 1~3은 지난주(클래스) 복습, 4~5가 이번 주 본 내용,
6은 상속 맛보기입니다. extra 1은 어떤 메서드를 만들지 스스로 고르는 설계 문제, extra 2는 도전 문제입니다.

| 파일                  | 주제                              | 새로 배우는 것                                        |
| --------------------- | --------------------------------- | ----------------------------------------------------- |
| `problem_01.py`       | 로봇과 배터리                     | 복습: 클래스, 인스턴스 메서드, 다른 객체 받기          |
| `problem_02.py`       | 부품 번호표                       | 복습: 클래스 변수, `@classmethod`, `@staticmethod`     |
| `problem_03.py`       | 정비소                            | 복습: 객체를 담는 객체, 다른 객체에게 일 시키기        |
| `problem_04.py`       | 분수                              | **매직 메서드 입문** -- `__str__`/`__repr__`, `__eq__`와 `NotImplemented`, 사칙연산, `__lt__`/`__le__` 만으로 `sorted` |
| `problem_05.py`       | 다항식                            | `__call__` (객체를 함수처럼), `__radd__`/`__rmul__` (왼쪽 피연산자), 경우 나누기 |
| `problem_06.py`       | 캐릭터와 영웅                     | **상속 맛보기** -- `super().__init__`, 덮어쓰기         |
| `problem_extra_01.py` | [숙제] 가방을 상자처럼            | `__len__` `__getitem__` `__setitem__` `__contains__` `__iter__` |
| `problem_extra_02.py` | [도전] 호가창                     | 클래스 설계 종합: 가격·시간 우선 체결 `submit`, `cancel`  |

## 다 못 풀어도 괜찮습니다

수업에서는 **1 -> 2 -> 3 -> 4 -> 5 -> 6** 순서로 갑니다. 4는 네 단계로 나뉘어 있고 테스트도 같은 순서입니다. 문제는 수업 시간보다 많이 준비되어
있으니, 끝까지 못 가도 뒤처진 것이 아닙니다. 나머지(extra 1, extra 2)는 숙제입니다.
숙제는 `python -m pytest -k problem_extra_01` 처럼 테스트합니다.

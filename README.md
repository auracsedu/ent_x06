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

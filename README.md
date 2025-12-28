# Google Antigravity 설치 및 실습 가이드

이 문서는 Google Antigravity의 설치 과정과 주요 기능을 이해하고, 간단한 실습을 통해 사용법을 익히기 위해 작성되었습니다.

## 1. 설치 안내

### 1) 다운로드
- Google Antigravity 공식 배포 사이트에서 Windows 또는 MacOS용 설치 파일을 다운로드합니다.   
- 아래의 링크를 CTRL키를 누른 상태에서 클릭하시면 이동이 됩니다.   
- https://antigravity.google/download

### 2) 설치
- 다운로드한 파일을 실행하여 설치를 진행합니다.   
- 설치폴더는 기본값을 추천합니다.   
- 예시: C:\Users\Ben\AppData\Local\Programs\Antigravity   
- 최근에는 개발과 관련된 앱들이 시스템폴더에 설치하는 것보다 사용자폴더에 설치하는 것을 선호하는 경향이 반영된 것이라 판단됩니다.   


### 3) 최초 실행과 초기 설정
- 최초 실행 시에는 초기 설정이 진행됩니다.
- VS Code로부터 설정을 가져오거나 설정을 가져오지 않고 진행하는 것을 선택하시면 됩니다.
- Editor Theme이라고 편집기의 배경색 등을 선택하시면 됩니다. (어두운 것을 선호하시면 Tokyo Night 추천)
- Antigravity Agent의 사용옵션을 어떻게 할지 선택을 하시면 됩니다.
   - Secure Modes를 선택한다면 아래의 옵션으로 설정하게 됩니다.
      - Browser URL Allowlist에 있는 사이트만 접속가능
      - Terminal 실행: 사용자가 승인을 해야 진행
      - Browser Javascript Execution도 사용자 승인이 필요
      - Artifact Review: 사용자 승인 필요
      - Respect .gitignore: .gitignore 파일에는 접속하지 않음
      - Workspace Isolation: workspace는 일종의 작업폴더개념이며 이 바운더리 이외에는 agent가 접근하지 않음.
   - Review-driven development/Agent-driven development/Custom configuration의 선택에 따라 아래의 설정들이 달라집니다. (처음 사용해보시는 분들은 Review-driven development를 추천합니다.)
      - Terminal excution policy: Request Review or Always Proceed
      - Review policy: 사용자의 요청을 agent가 어떻게 구혈하지 계획을 수립한 후 사용자에거 검토를 요청할지에 대한 설정입니다. Always Proceed or Agent Decide or Request Review
      - Javascriipts excution policy: agent가 특정 웹사이트에 접속한 후 이 웹사이트를 분석하기 위해서 자바스크립트 코드를 자동생성하여 실행하기 전에 승인을 요청할지에 대한 설정입니다.   
- Keybindings는 편집기의 입력을 일반적인 방식으로 할지 전문개발자들 사이에서 일부 선호되는 Vim 방식으로 할지이며Vim이 뭔지 모르는 상황이면 당연히 일반적인 방식을 선택하면 됩니다.
- Extensions는 Antigravity에 설치하고자 하는 확장기능으로 연구회의 내공을 고려할 때, Configure를 선태갛여 Python만 선택하시는 것을 추천합니다.
- Sign with Google: Antigravity에서 AI agent 기능을 사용하고자 한다면 반드시 자신의 goole 계정으로 sign in 해야 합니다.
   - 계정을 선택한 후에는
   - Google을 통해서 다운로드 했는지 확인한 후 로그인을 진행하게 됩니다.
   - 해당 PC에서 이 과정을 최초로 진행한 경우에는 검증코드를 문자로 전송받고 이를 PC에 입력하는 과정이 있을 수 있습니다.

## 2. 사용법

### 1) 원하는 프로젝트 폴더 만들기
- open folder로 원하는 위치에 원하는 폴더를 만들어 열면 자신의 프로젝트를 시작할 수 있습니다. (예시는 C:\Users\<사용자명>\projects\antigravity_exercise)


---

## 2. 주요 설정

Google Antigravity를 효과적으로 사용하기 위해 필요한 주요 설정입니다.

### 1) 터미널 명령 승인 설정
에이전트가 터미널 명령을 실행할 때, 사용자의 승인을 받도록 설정할 수 있습니다. 이를 통해 의도치 않은 명령 실행을 방지할 수 있습니다.   
설정/Agent 설정 항목에서   
Terminal Command Auto Execution을   
Always Proceed와 Request Review 중 토글로 설정할 수 있습니다. 

### 2) 외부 파일 인식 설정
내 컴퓨터(로컬) 내에서 현재 열려 있는 프로젝트 폴더 외부의 파일을 에이전트가 인식하고 참조할 수 있도록 설정합니다.   
설정/Agent 설정 항목에서   
File Access 중   
Agent Non-Workspace File Access   
를 on/off 할 수 있습니다. 

### 3) 브라우저 사용 설정   
에이전트가 웹 브라우저를 제어하여 정보를 검색하거나 웹 기반 작업을 수행할 수 있도록 권한과 설정을 확인합니다.   
General 설정항목 중  Enable Agent Web Tools를 on/off 할 수 있습니다. 
---

## 3. 주요 기능

Google Antigravity의 핵심적인 에이전트 기능입니다.

### 1) Implementation Plan (구현 계획) 작성 및 승인
사용자의 요청을 받으면 에이전트는 먼저 **Implementation Plan**을 스스로 작성합니다. 사용자는 이 계획을 검토하고 피드백을 주거나 승인할 수 있습니다.

### 2) Task 생성 및 진행
사용자의 승인이 완료되면, 에이전트는 구체적인 **Task** 목록을 생성하고 작업을 순차적으로 진행합니다.

### 3) Walkthrough (검증 결과)
모든 작업이 완료되면 **Walkthrough**를 통해 작업 결과와 검증 내용을 사용자에게 제시하여 최종 확인을 돕습니다.

---

## 4. 실습 가이드

아래 순서대로 실습을 진행하며 Antigravity의 기능을 체험해 보세요.

1.  **설치 파일 다운로드**: 공식 사이트 접속 및 다운로드.
2.  **설치**: 프로그램 설치 완료.
3.  **구글 계정 로그인**: 인증 절차 완료.
4.  **브라우저 확장 프로그램 설치**: 필요한 경우 브라우저 연동을 위한 확장 프로그램 설치.
5.  **프로젝트 폴더 열기**: Antigravity에서 실습할 프로젝트 폴더 열기.
6.  **파이썬 경로 확인하기 (터미널 활용 예시)**
    *   채팅창에 현재 시스템에서 사용 가능한 파이썬 경로를 알아내도록 명령합니다.
    *   이때 필요한 프롬프트는 `01_프롬프트-파이썬경로.txt` 파일을 참고하여 입력하세요.
7.  **가상환경(.venv) 활성화하기**
    *   채팅창에 명령하여 현재 프로젝트의 `.venv` 가상환경을 활성화합니다.
    *   이때 필요한 프롬프트는 `02_프롬프트-파이썬가상환경.txt` 파일을 참고하여 입력하세요.
8.  **웹사이트 크롤링하기 (브라우저 활용 예시)**
    *   채팅창에 명령하여 특정 웹사이트를 크롤링합니다.
    *   이때 필요한 프롬프트는 `03_프롬프트-웹사이트크롤링.txt` 파일을 참고하여 입력하세요.
9.  **그래프 그리기**
    *   수집된 데이터를 시각화해달라고 채팅창에 명령합니다.
    *   이때 필요한 프롬프트는 `04_프롬프트-그래프그리기.txt` 파일을 참고하여 입력하세요.
10. **R 경로 확인 및 프로젝트 설정**
    *   시스템에 설치된 R의 경로를 확인하고 `renv` 패키지를 이용해 프로젝트 환경을 초기화합니다.
    *   이때 필요한 프롬프트는 `05_프롬프트-R경로.txt` 파일을 참고하여 입력하세요.
11. **R 그래프 그리기**
    *   Python으로 수집한 CSV 데이터를 R(`ggplot2`)을 사용하여 시각화합니다.
    *   이때 필요한 프롬프트는 `06_프롬프트-R그래프그리기.txt` 파일을 참고하여 입력하세요.

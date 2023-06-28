# Project : <img src = "https://github.com/AIVLE-School-Third-Big-Project/Big_project_3_9/assets/124108607/9ccd7bd2-54e3-4789-b3be-c0f1f3a533a0" width="3%"></img>Hear-o(실시간 위험 상황 감지 자동 신고 서비스)
**HEAR On-call** : 서비스가 응급 상황을 감지하면 해당 응급 상황에 대처할 수 있는 대상을 호출하거나 알림을 보내는 역할을 나타냄

## Description

위급 상황 발생 시 안전 확보가 어려운 1인가구의 증가와 범죄에 노출되기 쉬운 여성,아동 등 사회적 취약계층을 겨냥한 범죄가 증가함에 따라 개인의 안전 확보의 중요성이 부각되고 있다.
이에 따라 예상치 못한 위급 상황 발생 시 스스로 안전 확보가 어려운 모든 국민들을 보호하기 위해 인공지능 모델을 활용하여 실시간으로 음성 및 주변음향을 분석, 위급 상황으로 판단될 때 자동으로 구조 요청을 하는 어플리케이션이다.
위급 상황을 유형별로 분류하여 각 유형에 맞게 기관에 신고한다.

### class

|**번호**|**유형**|**신고**|
|:------:|---|---|
|0|일반 상황(실내, 실외)||
|1|치안 안전(강제추행, 강도범죄, 절도범죄, 폭력범죄)|112|
|2|갇힘|119|
|3|전기사고|119|
|4|가스사고|119|
|5|화재|119|
|6|응급의료|119|
|7|안전사고(낙상,붕괴)|119|
|8|일반 도움요청|119|

## Dataset

[**AI HUB**](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=170) 에 공개된 위급상황 음성/음향 데이터 35만여개 중 5만개를 추출하여 사용

### 위급 상황 음성/음향 데이터
    - 성별 : 남성, 여성
    - 연령대 : 유아, 청소년, 노인, 기타
    - 상황 : 치안안전, 소방안전, 자연재해, 사고활동, 일반(위급), 일반(정상)
### 위급 상황 AI 학습용 데이터셋
    - 16개 클래스(중분류)1,000건 이상의 상황‧3,500시간
    - 음성/음향 단일 데이터셋, 음성/음향 복합 데이터셋

## Model : BEATs

[**BEATs**](https://github.com/microsoft/unilm/tree/master/beats)는 Audio classification 과제에서 음소 시퀀스로 인해 쉽게 얻을 수 없었던 음향 토크나이저의 문제를 SSL(self-supervised learning)모델의 반복적인 학습으로 해결한 모델이다. 또한 [**ESC-50 dataset**](https://paperswithcode.com/sota/audio-classification-on-esc-50)에서 98.1% 정확도를 보이는 SOTA 모델인 audio pretrained framework BEATs를 Pretrained model로 사용하여 Fine-Tuning 하였다.<br>
![chart (1)](https://github.com/AIVLE-School-Third-Big-Project/Big_project_3_9/assets/124108607/1c5a554a-1d27-41fe-99d6-03c896ff47cd)<br>
**위험 상황 음향 데이터 약 5만개를 사용하여 학습한 결과 약 95% 정확도를 예상할 수 있다.**

## Scenario
1. 사용자 : 84세 분당 혼자 거주하는 여성<br>
2. 혼자 사는 노인이다 보니 위험성을 느껴 히어로 앱 설치<br>
3. 앱 실행 후 첫번째로 나오는 앱 설명 확인<br>
4. 실시간 음향 감지를 위해 위치, 음성 녹음, 메시지 전달 등 개인 정보 동의와 함께 회원 가입<br>
5. 메인화면에서 SOS 버튼을 클릭하여 실시간 음향 인식 시작<br>
6. 어느 날 밤 강도 침입하여 창문 깨는 소리가 들림<br>
7. 범죄 소리를 인식해 여성 핸드폰에 위험 상황 감지 팝업 실행<br>
8. 여성은 자느라 인지하지 못하였지만 제한 시간(60초) 초과로 112에 위치, 시간, 음향 녹음 파일, 신고 내역이 메시지를 통해 자동 신고됨<br>
9. 경찰은 신고자의 위치, 시간, 음향 파일, 신고 내역을 확인해 곧바로 출동<br>
10. 빠르게 범인을 검거하여 앱 사용자 안전을 확보


## Stacks
- JS<br>
- JSX<br>
- Html<br>
- CSS<br>
- Python<br>
- MySQL<br>
- Django<br>

## 만든 사람들
- AI

[이준민](https://github.com/Jun9min9)

Transformer 기반 audio classfication modeling

[정재웅](https://github.com/UngCoding)

Beat’s model fine tuning

[이한나](https://github.com/hnnaaa95)

데이터 분석 및 CNN modeling

- Backend

[유용주](https://github.com/yyy5618)

계정관련 기능 구현, 실시간 위치 가져오기, AWS S3에 파일저장,불러오기

[박지훈](https://github.com/RedOff34)

모델폼을 이용한 게시글, 댓글 기능 구현, 음성녹음기능, sms 문자 전송, 

- Frontend

[이유진](https://github.com/leeyujin21)

게시판(목록, 작성, 뷰), 로그인, 회원가입, 비밀번호찾기, 메인화면

[홍아현](https://github.com/oaho)

회원정보 수정, 환경설정, 위급상황감지 화면, 신고접수 화면, 메인화면

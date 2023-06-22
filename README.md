# Project : Hearo

실시간 음성 및 주변음향 분석을 통한 자동 구조 요청 어플리케이션

## Description

위급 상황 발생 시 안전 확보가 어려운 1인가구의 증가와 범죄에 노출되기 쉬운 여성,아동 등 사회적 취약계층을 겨냥한 범죄가 증가함에 따라 안전 확보의 중요성이 부각되고 있습니다.
이에 따라 예상치 못한 위급 상황 발생 시 스스로 안전 확보가 어려운 모든 국민들을 보호하기 위해 인공지능 모델을 활용하여 실시간으로 음성 및 주변음향을 분석, 위급상황으로 판단될 때 자동으로 구조 요청을 하는 어플리케이션입니다.

## Dataset

**AI HUB**(https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=170) 에 공개된 위급상황 음성/음향 데이터 35만여개 중 5만개 추출

### 위급 상황 음성/음향 데이터
    - 성별 : 남성, 여성
    - 연령대 : 유아, 청소년, 노인, 기타
    - 상황 : 치안안전, 소방안전, 자연재해, 사고활동, 일반(위급), 일반(정상)
### 위급 상황 AI 학습용 데이터셋
    - 16개 클래스(중분류)1,000건 이상의 상황‧3,500시간
    - 음성/음향 단일 데이터셋, 음성/음향 복합 데이터셋

## Model

Beats(https://github.com/microsoft/unilm/tree/master/beats)

시나리오, 기술 스택 적기)

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

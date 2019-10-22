# Hangeul-cli-date
> Command line interface에서 한글 날짜, 시간을 확인할 수 있는 실행파일입니다.

[![](http://img.youtube.com/vi/gqjJuYX41us/0.jpg)](http://www.youtube.com/watch?v=gqjJuYX41us "")

## 설치 및 설정

지원 OS : MacOS

1) 다운로드: 아래 script를 terminal에서 붙여넣습니다.

```sh
curl https://raw.githubusercontent.com/Hangeuler/Hangeul-cli-date/master/dist/kdate > ~/.kdate && chmod u+x ~/.kdate
```

2) 설정: 환경변수로 설정이 필요합니다. 사용하는 쉘스크립트에 따라 아래와 같이 환경변수를 추가합니다. (아래는 bash shell을 사용할 경우의 예시)

```sh
$ vi ~/.bash
```

아래 줄을 추가하여 저장합니다.

```sh
alias kdate="~/.kdate"
```

## 실행 방법

Shell 설정에서 환경변수로 설정하고 나면 어느 디렉토리에서든 아래 명령어로 한글 날짜를 확인할 수 있습니다.

<p align="center">
  <img src="https://github.com/Hangeuler/Hangeul-cli-date/blob/master/image/example.png?raw=true">
</p>

```sh
$ kdate
이천십구년 시월 구일 일곱시 십구분 삼십사초
```

## 기여한 사람

- 이소민 <https://github.com/iSOMin>
- 최원영 <https://github.com/AndersonChoi>

상기 프로젝트는 Apache License 2.0 라이센스를 따릅니다.  ``LICENSE`` 파일에서 관련 내용을 확인할 수 있습니다.

## 기여하는 방법

1. 포크 (<https://github.com/Hangeuler/Hangeul-cli-date/fork>)
2. 새로운 브랜치 만들기 (`git checkout -b feature/fooBar`)
3. 버그/기능을 commit하기 (`git commit -am 'Add some fooBar'`)
4. 버그/기능을 push하기 (`git push origin feature/fooBar`)
5. Pull request 요청하기

혹은 아래와 같이 새로운 기능을 요청하거나 버그를 신고할 수 있습니다.

1. 새로운 기능 요청하기(<https://github.com/Hangeuler/Hangeul-cli-date/issues>)
2. 버그 이슈에 등록하기(<https://github.com/Hangeuler/Hangeul-cli-date/issues>)

## 실행파일 만드는 방법

python을 실행파일로 만들기 위해서 pyinstaller(<https://pyinstaller.readthedocs.io/en/stable/index.html>)을 사용해야 합니다. 새로운 기능, 버그 수정으로 pull request 요청하기전에 반드시 아래 명령어로 실행가능한 binary파일을 만들어주세요.

```sh
$ pyinstaller --onefile kdate.py
```

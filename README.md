# 파이썬으로 배우는 리팩토링(Python Refactoring)

## 리팩토링에 대한 간단한 설명
리팩토링은 구현된 소프트웨어의 소스코드를 점검하고 수정하는 작업을 의미합니다.
리팩토링을 하면 다음과 같은 효과를 얻을 수 있습니다.
1. 가독성 (Readablility) 향상
2. 미래에 기능 추가/확장할 때 편리
3. 유지보수 용이

주의할 점: 리팩토링을 하더라도 소프트웨어의 기능은 바뀌지 않습니다. 
리팩토링 결과 기능이 변경되었다면, 리팩토링을 한 것이 아니라 
```SW 기능변경```을 한 것이 됩니다.

## 학습 전략
리팩토링은 추천사항은 개발자마다 다를 수 있습니다.
그리고 리팩토링의 최종 결과가 사람마다 다르게 나올수도 있습니다.
하지만, 일반적인 추천사항은 엄연히 존재합니다.

리팩토링 추천사항들은 수많은 개발자들이 다양한 시도를 해보고 종합한 것이 되겠습니다. 
일반적으로 `리팩토링 컨벤션 (refactoring convention)` 또는 
`리팩토링 경헙 법칙 (rule of thumb)`이라고 불리는 것들입니다. 
우리는 그 중에서 대표적인 몇 가지 사례를 실습할 것입니다.

리팩토링을 처음 알게된 분들이나 아직 친숙하지 않은 개발자를 위해 
이론과 소스코드를 설명하는 유튜브 동영상을 업로드 하였으니 [여기](https://www.youtube.com/playlist?list=PLRUS1nW-CfncA0l5UyKmU6srnPrakR00V)를 
참고하기 바랍니다.

- 리팩토링 이론 살펴보기  
    - 리팩토링 개념, 필요성, 나쁜 냄새(bad smells)에 대하여 살펴봅니다.
- 코드 준비
    - 리팩토링을 하려면 리팩토링 할 소스코드가 있어야 합니다.
    - 실습코드는 포켓몬 정보가 있는 웹페이지 데이터를 수집하는 로봇(웹 크롤러)을 구현합니다.
    - 목표 웹페이지를 확인하려면 [여기(click here)](http://pokemondb.net/pokedex/all) 클릭하세요
    - 리팩토링 하기 전 포켓몬 크롤러 코드는 [pycon_refactor_before.py](pycon_refactor_before.py) 입니다.
    - 크롤러 구현 코드는 [Syed S. Nazrul 블로그](https://towardsdatascience.com/web-scraping-html-tables-with-python-c9baba21059) 참고하여 작성하였습니다.

- 리팩토링 실습
    - 리팩토링을 수행하는 기법은 다양하기 때문에 모든 것을 다룰 수 없습니다. 파이썬 관련 내용 중 일부를 실습하도록 합니다.
    - 실습코드는 [PyCon 2020](https://us.pycon.org/2020/about/) ```Talks```에서 발표된 [Conor Hoekstra이 Talk 세션](https://us.pycon.org/2020/schedule/presentation/162/)에서 발표한 [유튜브 튜토리얼](https://www.youtube.com/watch?v=KTIl1MugsSY)을 참고하여 작성하였습니다.
    - 리팩토링 과정을 포함한 코드는 [pycon_refactor_middle.py](./pycon_refactor_middle.py) 입니다.
    - 리팩토링 결과 코드는 [pycon_refactor_after.py](./pycon_refactor_after.py) 입니다.
    - `__name__`과 `main` 함수를 적용한 최종 리팩토링 결과는 [pycon_refactor_after_final.py](./pycon_refactor_after_final.py) 입니다.


## 강의 동영상 (유튜브)
주제별로 유튜브를 시청하려면 관심있는 아래 목록 중에서 관심있는 제목을 클릭하세요.
1. [[이론 1] 리팩토링이 뭔가요?](https://youtu.be/8DXPBG-242o)
2. [[이론 2] Bad Smells 그리고 리팩토링](https://youtu.be/XMM9BePQ6ao)
3. [[코드준비 1] Toy Project - 포켓몬 크롤러 코딩 1](https://www.youtube.com/watch?v=7VRAY4qRqrQ)
4. [[코드준비 2] Toy Project - 포켓몬 크롤러 코딩 2](https://www.youtube.com/watch?v=MMu5SZ5mbmI)
5. [[리팩토링 실습 1] ITM anti pattern 수정](https://www.youtube.com/watch?v=3sdTOF5fcF4)
6. [[리팩토링 실습 2] 중첩 반복문 단순화, 불필요 조건문 제거, 람다 함수를 적용한 리팩토링](https://www.youtube.com/watch?v=CyGj5Qn-wOc)
7. [[리팩토링 실습 3] Comprehension, unpacking, zip을 이용한 리팩토링](https://www.youtube.com/watch?v=_FpkHS5NwQ4)

## 강의 슬라이드
- 이론 강의 슬라이드: [Python_Refactoring_theory.pdf](./01.%20Python_Refactoring_theory.pdf)
- 실습 강의 슬라이드: [Python_Refactoring_with_code_example.pdf](./02.%20Python_Refactoring_with_code_example.pdf)

  `[참고]` MS .ppt 파일은 디바이스 또는 OS에 따라 안 열리거나 깨질 확률이 있어서 .pdf 양식으로 제공합니다.

## 참고 자료
- 포켓몬 크롤러 코딩: [Syed S. Nazrul 블로그](https://towardsdatascience.com/web-scraping-html-tables-with-python-c9baba21059)
- PyCon 2020 Talks: [Beautiful Python Refactoring](https://us.pycon.org/2020/schedule/presentation/162/), 유튜브 링크 [바로가기](https://www.youtube.com/watch?v=KTIl1MugsSY)
- 포켓몬 정보: 포켓몬 인터넷 상세정보 $\to$ [웹페이지](http://pokemondb.net/pokedex/all)

# 2020-광인사-해커톤 - 장려상 (광주인공지능사관학교장 상) 🏆

## 🎈 Makers
* 고정환
* 박성찬
* 이민기
* 이윤환

## 💡 해커톤 주제
* 코로나19로 인한 언택트 시대에 알맞은 서비스 개발
  * 인공지능
  * 웹서비스
  * 언택트

## 💡 아이디어
* "꼭 만나서만 봉사활동을 해야 하나요?" 몸은 언택트! 마음은 컨택트! 
* 언택트 시대에 맞춤화된 비대면 봉사활동 웹서비스 개발
* 코로나19의 장기화로 인해 봉사활동이 필요하지만 코로나로 인하여 불안한 사람들! 하지만 봉사활동을 찾을 수 있는 대부분의 서비스는 대면을 요구하는 봉사활동이며, 일부 비대면을 통한 봉사활동이 올라와 있으나 사용자가 일일이 검색을 하여 찾아야 하는 번거로움이 있음

## 💡 서비스 계획
* 초기에는 각 봉사 사이트를 크롤링하여 비대면 봉사활동을 수집해 각 봉사활동에 해당하는 정보와 함께 출처 링크를 제공
* 이후 사용자가 늘어남에 따라 봉사관계자 분들이 직접 사이트로 들어와서 모집 공고를 올리도록 유도
* 초기 단계와 같이 직접적인 봉사활동 데이터 수집의 비중은 줄이고 관리 위주로 운영 가능
* 봉사관계자와 봉사자들로 자체 내부적으로 돌아가게끔 운영하는 것이 최종 목표

## 💡 구현 계획
* Django를 이용하여 웹사이트 제작
  * 사용자 회원가입(봉사관계자, 봉사자 구별하여 생성)
  * 사용자가 원하는 검색을 위한 리스트
  * 전체 봉사 리스트가 올라와 있는 목록 현황 테이블
  * 봉사 관계자가 글을 적을 수 있도록 하는 페이지와 해당 정보들이 적혀 있는 페이지
* 사용자 회원가입과 봉사활동 데이터들이 들어간 DB 구축
* 크롤링을 통하여 봉사활동 데이터 추가

## 💡 [시연영상](https://youtu.be/AreOYdSksYI)

## 💡 개선사항
* 회원가입 페이지 개선
* 봉사목록 현황 테이블 css 작업
* 모집 공고 페이지 작성시 비율 조절
* 검색 리스트 페이지 개선

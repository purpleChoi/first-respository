# 파이썬 고급 프로그래밍 15주차 강의계획서 (2025년 개정판)

## 1. 교과목 개요

이 교과목은 파이썬의 고급 문법과 현대적 개발 방법론을 심화 학습하여, 데이터 처리, 비동기 프로그래밍, 타입 힌팅, 성능 최적화, AI/ML 도구 활용, 클린 코드 설계 능력을 배양하고, 실무 중심의 프로젝트를 통해 문제 해결 능력을 강화하는 것을 목표로 한다.

## 2. 주차별 수업계획

| 주차 | 주제 | 세부 내용 | 과제/실습 |
|------|------|-----------|-----------|
| **1주차** | 모던 파이썬 개발 환경 | - Poetry, UV 패키지 관리 - Pre-commit, Black, Ruff 코드 포맷팅 - pyproject.toml 설정 - VS Code/PyCharm 고급 설정 | 개발환경 구축 및 프로젝트 템플릿 생성 |
| **2주차** | 타입 힌팅 & 정적 분석 | - Type hints 심화 (Generic, Protocol) - mypy, pyright 활용 - Pydantic v2로 데이터 검증 - TypedDict, Literal 활용 | 타입 안전한 데이터 처리 함수 작성 |
| **3주차** | 고급 자료구조 & 알고리즘 | - collections.abc, typing 활용 - dataclasses vs Pydantic 모델 - 커스텀 컨테이너 구현 - 알고리즘 복잡도 분석 | LRU 캐시 구현 및 성능 비교 |
| **4주차** | 함수형 프로그래밍 심화 | - functools 고급 활용 - operator 모듈, partial 응용 - 커링, 모나드 패턴 - 함수 파이프라인 설계 | 데이터 변환 파이프라인 구축 |
| **5주차** | 고급 객체지향 & 디자인 패턴 | - Protocol과 구조적 서브타이핑 - Dependency Injection - Factory, Observer, Strategy 패턴 - 클린 아키텍처 원칙 | 플러그인 시스템이 있는 계산기 |
| **6주차** | 메타프로그래밍 & 리플렉션 | - 메타클래스, __init_subclass__ - descriptor, property 고급 - inspect 모듈 활용 - 동적 클래스 생성 | ORM 스타일 모델 클래스 구현 |
| **7주차** | 성능 최적화 & 프로파일링 | - cProfile, line_profiler - 메모리 프로파일링 (memory_profiler) - Cython, Numba 소개 - 병목 지점 분석 및 최적화 | 성능 개선 전후 비교 리포트 |
| **8주차** | 비동기 프로그래밍 심화 | - asyncio 고급 패턴 - aiohttp, httpx 활용 - 비동기 컨텍스트 매니저 - asyncio.gather vs TaskGroup | 비동기 웹 스크래퍼 구현 |
| **9주차** | 데이터 처리 & 스트리밍 | - Polars vs Pandas 비교 - Apache Arrow, Parquet 활용 - 스트리밍 데이터 처리 - 메모리 효율적 처리 기법 | 대용량 데이터 ETL 파이프라인 |
| **10주차** | API 개발 & 웹 프레임워크 | - FastAPI 심화 (의존성 주입, 미들웨어) - Pydantic 모델 활용 - OpenAPI/Swagger 자동 생성 - 테스팅 (pytest-asyncio) | RESTful API 서버 구축 |
| **11주차** | 데이터베이스 & ORM | - SQLAlchemy 2.0 스타일 - 비동기 데이터베이스 연동 - 마이그레이션 관리 (Alembic) - 쿼리 최적화 기법 | 사용자 관리 시스템 구현 |
| **12주차** | AI/ML 도구 통합 | - LangChain, OpenAI API 활용 - Hugging Face transformers - 벡터 데이터베이스 (ChromaDB) - Streamlit으로 AI 앱 배포 | AI 챗봇 또는 텍스트 분석 도구 |
| **13주차** | 컨테이너화 & 배포 | - Docker 멀티스테이지 빌드 - docker-compose 활용 - 환경변수 관리 (python-dotenv) - CI/CD 파이프라인 (GitHub Actions) | 앱 컨테이너화 및 자동 배포 |
| **14주차** | 최종 프로젝트 개발 | - 팀별 프로젝트 진행 - 코드 리뷰 및 협업 - 실시간 멘토링 - 예: 실시간 데이터 대시보드, AI 웹앱, 마이크로서비스 | 프로젝트 중간 발표 |
| **15주차** | 프로젝트 발표 & 회고 | - 최종 프로젝트 발표 - 기술 스택 선택 근거 설명 - 성능 측정 결과 공유 - 배운 내용 회고 및 토론 | 기술 블로그 포스트 작성 |

## 3. 주요 개선사항

### 최신 도구 및 기술 반영
- **Poetry/UV**: 모던 패키지 관리
- **Ruff**: 차세대 린터/포맷터 (Black + isort + flake8 대체)
- **Pydantic v2**: 성능 개선된 데이터 검증
- **FastAPI**: 현대적 웹 API 프레임워크
- **Polars**: 고성능 데이터프레임 라이브러리

### 실무 중심 강화
- 타입 힌팅을 통한 코드 품질 향상
- 성능 프로파일링 및 최적화 기법
- CI/CD 파이프라인 구축
- 컨테이너화 및 배포 자동화

### AI/ML 시대 대응
- LangChain을 활용한 AI 애플리케이션 개발
- 벡터 데이터베이스 활용법
- AI 모델 API 통합 기법

### 협업 및 코드 품질
- 코드 리뷰 문화 도입
- 정적 분석 도구 활용
- 클린 코드 및 아키텍처 원칙

## 4. 평가 기준
- **중간고사**: 30% (코딩 테스트 + 이론)
- **과제/실습**: 30% (주차별 실습 과제)
- **최종 프로젝트**: 40% (기술적 구현 + 발표 + 문서화)

## 5. 권장 사전 지식
- Python 기초 문법 및 객체지향 프로그래밍
- Git/GitHub 기본 사용법
- Linux/macOS 터미널 기본 명령어
- 데이터베이스 기본 개념 (SQL)
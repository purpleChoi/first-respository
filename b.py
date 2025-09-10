# 파이썬 기본 문법 리뷰 - 고급과정 준비
*2
시간
집중
리뷰
과정 *

## 목차
1.[변수와
데이터
타입](  # 1-변수와-데이터-타입-20분)
    2.[제어 구조](  # 2-제어-구조-25분)
3.[함수](  # 3-함수-30분)
4.[객체지향 프로그래밍 기초](  # 4-객체지향-프로그래밍-기초-25분)
5.[예외 처리와 파일 I / O](  # 5-예외-처리와-파일-io-20분)

---

## 1. 변수와 데이터 타입 (20분)

### 1.1 기본 데이터 타입과 동적 타이핑

파이썬은 동적 타이핑 언어로, 변수의 타입이 런타임에 결정됩니다.

```python
# 기본 타입들
number = 42  # int
pi = 3.14159  # float
name = "Python"  # str
is_active = True  # bool
nothing = None  # NoneType

# 타입 확인
print(type(number))  # <class 'int'>
print(isinstance(pi, float))  # True
```

### 1.2 컬렉션 타입

```python
# 리스트 (가변, 순서 있음)
fruits = ['apple', 'banana', 'cherry']
fruits.append('date')
print(fruits[0])  # 'apple'

# 튜플 (불변, 순서 있음)
coordinates = (10, 20)
x, y = coordinates  # 언패킹

# 딕셔너리 (가변, 키-값 쌍)
person = {'name': 'Alice', 'age': 30}
person['city'] = 'Seoul'

# 집합 (가변, 중복 없음)
unique_numbers = {1, 2, 3, 2, 1}  # {1, 2, 3}
```

### 1.3 문자열 조작

```python
# 문자열 포매팅
name = "Python"
version = 3.9
message = f"I love {name} {version}"  # f-string (권장)

# 문자열 메서드
text = "  Hello World  "
print(text.strip().upper())  # "HELLO WORLD"
print(text.split())  # ['Hello', 'World']

# 슬라이싱
word = "Programming"
print(word[3:7])  # "gram"
print(word[::-1])  # "gnimmargorP" (역순)
```

### 1.4 실습 예제

```python


def analyze_data(data_list):
    """데이터 분석 함수"""
    return {
        'count': len(data_list),
        'sum': sum(data_list) if all(isinstance(x, (int, float)) for x in data_list) else 0,
        'unique': len(set(data_list)),
        'types': list(set(type(x).__name__ for x in data_list))
    }


# 테스트
sample_data = [1, 2, 3, 2, 'hello', 1, 3.14]
result = analyze_data(sample_data)
print(result)
```

---

## 2. 제어 구조 (25분)

### 2.1 조건문

```python
# 기본 조건문
age = 25
if age >= 18:
    status = "성인"
elif age >= 13:
    status = "청소년"
else:
    status = "어린이"

# 삼항 연산자
status = "성인" if age >= 18 else "미성년자"

# 조건문에서의 Truthy/Falsy
data = []
if data:  # False: 빈 리스트
    print("데이터가 있습니다")
else:
    print("데이터가 비어있습니다")
```

### 2.2 반복문

```python
# for 반복문
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        print(f"{num}은 짝수")
    else:
        print(f"{num}은 홀수")

# enumerate 활용
for index, value in enumerate(numbers):
    print(f"인덱스 {index}: {value}")

# zip 활용
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name}: {age}세")

# while 반복문
count = 0
while count < 5:
    print(f"카운트: {count}")
    count += 1
```

### 2.3 컴프리헨션

```python
# 리스트 컴프리헨션
squares = [x ** 2 for x in range(1, 6)]  # [1, 4, 9, 16, 25]
even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]

# 딕셔너리 컴프리헨션
word_lengths = {word: len(word) for word in ['hello', 'world', 'python']}

# 집합 컴프리헨션
unique_lengths = {len(word) for word in ['hello', 'world', 'hi', 'python']}
```

### 2.4 실습 예제: 간단한 성적 관리 시스템

```python


def grade_analyzer(scores):
    """성적 분석기"""
    grade_map = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}

    for score in scores:
        if score >= 90:
            grade_map['A'] += 1
        elif score >= 80:
            grade_map['B'] += 1
        elif score >= 70:
            grade_map['C'] += 1
        elif score >= 60:
            grade_map['D'] += 1
        else:
            grade_map['F'] += 1

    return grade_map


# 사용 예시
student_scores = [95, 87, 76, 89, 92, 58, 73, 84, 91, 67]
grade_distribution = grade_analyzer(student_scores)
print("성적 분포:", grade_distribution)
```

---

## 3. 함수 (30분)

### 3.1 함수 정의와 매개변수

```python


# 기본 함수
def greet(name, greeting="안녕하세요"):
    return f"{greeting}, {name}님!"


# 가변 매개변수
def calculate_sum(*args):
    return sum(args)


# 키워드 가변 매개변수
def create_profile(**kwargs):
    profile = {}
    for key, value in kwargs.items():
        profile[key] = value
    return profile


# 사용 예시
print(greet("Alice"))  # 안녕하세요, Alice님!
print(calculate_sum(1, 2, 3, 4, 5))  # 15
profile = create_profile(name="Bob", age=30, city="Seoul")
```

### 3.2 고급 함수 개념

```python


# 함수를 변수에 할당
def multiply(x, y):
    return x * y


operation = multiply
result = operation(5, 3)  # 15


# 함수를 매개변수로 전달
def apply_operation(func, x, y):
    return func(x, y)


result = apply_operation(multiply, 4, 6)  # 24

# 람다 함수
square = lambda x: x ** 2
numbers = [1, 2, 3, 4, 5]
squared = list(map(square, numbers))  # [1, 4, 9, 16, 25]
```

### 3.3 데코레이터 기초

```python


def timing_decorator(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 실행 시간: {end - start:.4f}초")
        return result

    return wrapper


@timing_decorator
def slow_function():
    import time
    time.sleep(1)
    return "완료"


# 사용
slow_function()
```

### 3.4 실습 예제: 계산기 모듈

```python


class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ValueError("0으로 나눌 수 없습니다")
        return x / y

    @classmethod
    def batch_calculate(cls, operations):
        results = []
        for op, x, y in operations:
            if op == '+':
                results.append(cls.add(x, y))
            elif op == '-':
                results.append(cls.subtract(x, y))
            elif op == '*':
                results.append(cls.multiply(x, y))
            elif op == '/':
                results.append(cls.divide(x, y))
        return results


# 사용 예시
calc = Calculator()
operations = [('+', 10, 5), ('*', 3, 4), ('/', 20, 4)]
results = calc.batch_calculate(operations)
print(results)  # [15, 12, 5.0]
```

---

## 4. 객체지향 프로그래밍 기초 (25분)

### 4.1 클래스와 객체

```python


class Student:
    # 클래스 변수
    school_name = "파이썬 고등학교"

    def __init__(self, name, age, grade):
        # 인스턴스 변수
        self.name = name
        self.age = age
        self.grade = grade
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def get_info(self):
        return f"이름: {self.name}, 나이: {self.age}, 학년: {self.grade}"

    def __str__(self):
        return f"Student({self.name}, {self.grade}학년)"

    def __repr__(self):
        return f"Student('{self.name}', {self.age}, {self.grade})"


# 객체 생성 및 사용
student1 = Student("김철수", 17, 2)
student1.add_subject("수학")
student1.add_subject("영어")
print(student1.get_info())
```

### 4.2 상속

```python


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"안녕하세요, 저는 {self.name}입니다."


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # 부모 클래스 초기화
        self.student_id = student_id
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def introduce(self):  # 메서드 오버라이딩
        return f"{super().introduce()} 학번은 {self.student_id}입니다."


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        return f"{super().introduce()} {self.subject}을 가르칩니다."


# 사용 예시
student = Student("이영희", 20, "2023001")
teacher = Teacher("박교수", 45, "파이썬")
print(student.introduce())
print(teacher.introduce())
```

### 4.3 특별 메서드와 프로퍼티

```python


class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self._balance = initial_balance  # protected 변수

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("잔액은 음수가 될 수 없습니다")
        self._balance = amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("입금액은 양수여야 합니다")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("출금액은 양수여야 합니다")
        if amount > self._balance:
            raise ValueError("잔액이 부족합니다")
        self._balance -= amount

    def __str__(self):
        return f"{self.owner}의 계좌 (잔액: {self._balance:,}원)"


# 사용 예시
account = BankAccount("김고객", 100000)
account.deposit(50000)
print(account)  # 김고객의 계좌 (잔액: 150,000원)
```

---

## 5. 예외 처리와 파일 I/O (20분)

### 5.1 예외 처리

```python


def safe_divide(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다")
        return None
    except TypeError:
        print("숫자만 입력해주세요")
        return None
    except Exception as e:
        print(f"예상치 못한 오류 발생: {e}")
        return None
    else:
        print("나눗셈이 성공적으로 완료되었습니다")
    finally:
        print("나눗셈 연산 종료")


# 커스텀 예외
class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def validate_age(age):
    if age < 0:
        raise CustomError("나이는 음수가 될 수 없습니다")
    if age > 150:
        raise CustomError("나이가 너무 큽니다")
    return True


```

### 5.2 파일 I/O

```python


# 파일 쓰기
def write_student_data(filename, students):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("이름,나이,학년\n")
            for student in students:
                file.write(f"{student['name']},{student['age']},{student['grade']}\n")
        print(f"데이터가 {filename}에 저장되었습니다")
    except IOError as e:
        print(f"파일 쓰기 오류: {e}")


# 파일 읽기
def read_student_data(filename):
    students = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines[1:]:  # 헤더 제외
                name, age, grade = line.strip().split(',')
                students.append({
                    'name': name,
                    'age': int(age),
                    'grade': int(grade)
                })
        return students
    except FileNotFoundError:
        print(f"{filename} 파일을 찾을 수 없습니다")
        return []
    except IOError as e:
        print(f"파일 읽기 오류: {e}")
        return []


# 사용 예시
student_list = [
    {'name': '김철수', 'age': 17, 'grade': 2},
    {'name': '이영희', 'age': 16, 'grade': 1},
    {'name': '박민수', 'age': 18, 'grade': 3}
]
write_student_data('students.csv', student_list)
loaded_students = read_student_data('students.csv')
```

---

## 종합 실습 문제

### 문제 1: 도서 관리 시스템 (난이도: 중)

다음
요구사항을
만족하는
도서
관리
시스템을
작성하세요:

1.
Book
클래스: 제목, 저자, ISBN, 대출
상태를
속성으로
가짐
2.
Library
클래스: 도서
목록을
관리하고
대출 / 반납
기능
제공
3.
예외
처리: 존재하지
않는
책
대출
시도, 이미
대출된
책
재대출
시도
4.
파일
I / O: 도서
목록을
파일로
저장 / 로드

```python


# 여기에 코드를 작성하세요
class Book:
    pass


class Library:
    pass


# 테스트 코드
if __name__ == "__main__":
    # 라이브러리 생성 및 테스트
    pass
```

### 문제 2: 데이터 분석기 (난이도: 중상)

CSV
형태의
판매
데이터를
분석하는
프로그램을
작성하세요:

1.
데이터
읽기: CSV
파일에서
판매
데이터
로드
2.
통계
계산: 총
매출, 평균
매출, 월별
매출
등
3.
데이터
필터링: 특정
조건에
맞는
데이터
추출
4.
결과
저장: 분석
결과를
새
파일로
저장

```python


# 예시 데이터 형식:
# date,product,quantity,price
# 2024-01-15,노트북,2,1500000
# 2024-01-16,마우스,5,30000

class SalesAnalyzer:
    def __init__(self):
        self.data = []

    def load_data(self, filename):
        # 구현하세요
        pass

    def calculate_total_sales(self):
        # 구현하세요
        pass

    def get_monthly_sales(self):
        # 구현하세요
        pass


```

### 문제 3: 미니 게임 (난이도: 상)

숫자
맞추기
게임을
객체지향으로
구현하세요:

1.
Game
클래스: 게임
로직
관리
2.
Player
클래스: 플레이어
정보
관리(이름, 점수, 게임
기록)
3.
난이도
시스템: 쉬움(1 - 50), 보통(1 - 100), 어려움(1 - 500)
4.
게임
기록: 플레이어별
게임
기록을
파일로
저장
5.
예외
처리: 잘못된
입력값
처리

---

## 테스트 문제

### 1. 다음 코드의 출력 결과는?

```python


def modify_list(lst):
    lst.append(4)
    lst = [1, 2, 3]
    lst.append(5)


my_list = [1, 2]
modify_list(my_list)
print(my_list)
```

** 답: [1, 2, 4] **

### 2. 다음 중 올바른 클래스 상속 구조는?

```python


# A
class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "멍멍"


# B
class Animal:
    def __init__(self):
        super().__init__()


class Dog(Animal):
    def __init__(self):
        super().__init__()


```

** 답: A가
올바름(B는
Animal이
다른
클래스를
상속하지
않으므로
super()
불필요) **

### 3. 다음 코드에서 예외가 발생하는 부분과 해결 방법을 설명하세요.

```python
data = {'a': 1, 'b': 2}
try:
    print(data['c'])
except KeyError:
    print("키가 존재하지 않습니다")
    print(data.get('c', '기본값'))
```

### 4. 리스트 컴프리헨션을 사용하여 1부터 20까지 숫자 중 3의 배수만 제곱한 리스트를 만드세요.

** 답: **
```python
result = [x ** 2 for x in range(1, 21) if x % 3 == 0]
# [9, 36, 81, 144, 225, 324]
```

### 5. 다음 코드의 문제점과 개선 방법을 설명하세요.




class Counter:
    count = 0

    def increment(self):
        Counter.count += 1

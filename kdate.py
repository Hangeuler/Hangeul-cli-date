import datetime


def convert_to_korean(number, datetime_type=""):
    korean_number = ["영", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]
    korean_pronoun_number = ["영", "한", "두", "세", "네", "다섯", "여섯", "일곱", "여덟", "아홉", "열"]
    result = ""

    if number / 1000 >= 1:
        if int(number / 1000) == 1:
            result += "천"
        else:
            result += convert_to_korean(int(number / 1000)) + "천"
        number = number % 1000
    if number / 100 >= 1:
        if int(number / 100) == 1:
            result += "백"
        else:
            result += convert_to_korean(int(number / 100)) + "백"
        number = number % 100
    if number / 10 >= 1:
        if datetime_type == "month" and number / 10 == 1:
            result += "시"
        elif datetime_type == "hour" and int(number / 10) == 1:
            result += "열"
        elif int(number / 10) == 1:
            result += "십"
        else:
            result += convert_to_korean(int(number / 10)) + "십"
        number = number % 10
    if number < 10 and number / 1 >= 1:
        if datetime_type == "month" and number / 10 == 6:
            result += "유"
        elif datetime_type == "hour":
            result += korean_pronoun_number[number]
        else:
            result += korean_number[number]

    return result


dt = datetime.datetime.now()

print(convert_to_korean(dt.year) + "년 "
      + convert_to_korean(dt.month, "month") + "월 "
      + convert_to_korean(dt.day) + "일 "
      + convert_to_korean(int(dt.strftime("%I")), "hour") + "시 "
      + convert_to_korean(dt.minute) + "분 "
      + convert_to_korean(dt.second) + "초")



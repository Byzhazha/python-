# -*- coding:utf-8 -*-
import openai


def main():
    openai.api_key = "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"
    messages = []
    while True:
        msg = ""
        print("请输入你的问题：", end="")
        msg = input()
        messages.append(
            {"role": "user", "content": msg}
        )
        completion = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=messages
        )
        print(completion.choices[0].message.content)
        print('使用token：' + str(completion.usage.total_tokens))


if __name__ == '__main__':
    main()
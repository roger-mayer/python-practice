num = 1
while num <= 5:
    print(num)
    num += 1

prompt = "\nTell me something and I will repeat it back"
prompt += "\nenter 'exit' to end program: "

message = ""
while message != 'exit':
    message = input(prompt)
    if message != 'exit':
        print(message)




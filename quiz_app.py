import sys
import random


def main():

    nameFile=sys.argv[1]
    subject=int(sys.argv[2])

    with open (rf'questions\{nameFile}.txt','r') as file:
        count_answer_correct=0

        
        for _ in range(subject):
            line = file.readline().split(";")
            question=line[0].strip()
            correct_answer=int(line[1].strip())
            answers = [answer.strip() for answer in line[2].split(",")]
            answers.append(correct_answer)
            random.shuffle(answers)
        # הדפסת השאלה
            print (question)
            
            # הדפסת התשובות
            lst=[1,2,3,4]
            dictionary = {i+1: answer for i, answer in enumerate(answers)}
            
            for index, answer in dictionary.items():
                print(f"{index}. {answer}") 

            correct_key = next(key for key, value in dictionary.items() if value == correct_answer)   
            
            # בדיקה והדפסת התשובה
            num_answer=int (input("Select the correct answer: "))

            if num_answer==correct_key:
                count_answer_correct+=1
        print (f'you answered {count_answer_correct}/{subject} correct answers')

    

if __name__ == '__main__':
    main()

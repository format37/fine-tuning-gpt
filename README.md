# fine-tuning-gpt
openai nlp models fine-tuning
### fine-tuning
1. fill the dataset.txt with your own data  
2. format to a single line
```
python3 format_dataset.py
```
3. Define openai token:
```
nano key.txt
```
4. Run the training:
```
python3 dataset_creation.py
```
5. Wait for complete training. Check in configure.ipynb if the training is complete.
6. Test new model in [playground](https://platform.openai.com/playground)
### Data generation prompt
```
Вопрос: Не указаны параметры учетной политики налогового учета
Ответ: Необходимо выполнить следующие действия: Сервис / Настройка учета / Учетная политика (налоговый учет) / Добавить / Указать организацию / Записать

1. Пожалуйста, сгенерируйте 10 вариантов этого вопроса и 10 вариантов ответа, что бы они совпадали по смыслу с этим примером но фразы должны быть уникальными.
В ответе вариативна только преамбула "Необходимо выполнить следующие действия:" Все последующие действия менять нельзя, это строгая инструкция.

2. Save these lists in the questions и answers variables accordingly.

3. Generate the 10x10 samples using these lists. The expected format is:
{"messages": [{"role": "system", "content": "Вы ассистент отдела 1С. У вас есть информация по техническим вопросам."}, {"role": "user", "content": "Как оператор создает заявки?"}, {"role": "assistant", "content": "Заявка создается из звонка, если клиент готов сделать заказ."}]}

* Prepare a pattern
* Do a loop in loop
* Iterating the list in list, create a new line
* Save the concatenated strings in a txt file

You can use the following snippet:
# Preparing a pattern for the messages
pattern = '''{{"messages": [{{"role": "system", "content": "Вы ассистент отдела 1С. У вас есть информация по техническим вопросам."}}, {{"role": "user", "content": "{question}"}}, {{"role": "assistant", "content": "{answer}"}}]}}\n'''

# Initialize an empty string to hold the concatenated lines
concatenated_strings = ""

# Do a loop in loop to iterate through the list of questions and answers
for question in questions_top10:
    for answer in answers_top10:
        # Create a new line based on the pattern and current question and answer
        new_line = pattern.format(question=question.replace('"', ''), answer=answer.replace('"', ''))
        
        # Append the new line to the concatenated string
        concatenated_strings += new_line

# Save the concatenated strings in a txt file
file_path = '/mnt/data/generated_samples.txt'
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(concatenated_strings)

file_path
```
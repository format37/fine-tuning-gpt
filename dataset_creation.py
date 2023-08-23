import openai
import os
import time

# Read key from key.txt
with open('key.txt', 'r') as file:
    openai_key = file.read().replace('\n', '')

openai.api_key = openai_key

result = openai.File.create(
  file=open("dataset.jsonl", "rb"),
  purpose='fine-tune'
)

print('File created:')
print(result)
file_id = result['id']

time_to_sleep = 20
# Sleep time_to_sleep sec
print('Sleeping for {} sec'.format(time_to_sleep))
time.sleep(time_to_sleep)

result = openai.FineTuningJob.create(training_file=file_id, model="gpt-3.5-turbo")
print(result)

print('Done')
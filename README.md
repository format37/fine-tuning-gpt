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
dataset_creation.py
```
5. Wait for complete training. Check in configure.ipynb if the training is complete.
6. Test new model in [playground](https://platform.openai.com/playground)

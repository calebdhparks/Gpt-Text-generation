# Gpt-Text-generation
This project's goal was to become familiar with the transformer architecture as a part of learning about GPTs. Using code based on this gpt from scratch found here {https://colab.research.google.com/drive/1JMLa53HDuA-i7ZBmqV7ZnA3c_fvtXnx-?usp=sharing#scrollTo=hoelkOrFY8bN} and original code to create the input file, I was able to produce a chapter of Harry Potter and the Deathly Hallows as well as a speech from Donald Trump from his 2020 campaign. 
# Install Requirements 
pip install -r requirements.txt
# Move to One of The Directories
cd donald_trump_generation \
or \
cd harry_potter_generation
## Next either run the generation or train from scratch and then run the generation
# Run Generation Only
python3 donald_trump_generator.py \
or \
python3 harry_potter_generator.py
# Train and Generate
python3 train_donald_trump_gpt.py \
or \
python3 train_harry_potter_gpt.py\
## Reference the file generated_hp_chapter.txt and generated_dt_speech.txt to see an example of the results 

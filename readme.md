# Text Generation

The goal of this project is to train a one Character level language model to automatically generate
text (dogs Names).

## Data set

The model was trained on the dog names [dataset](https://catalog.data.gov/dataset/dog-names) of the `Municipality of Anchorage — Names of registered dogs from Anchorage Animal Care and Control as of 10/17/2017 in the Municipality of Anchorage`.

```csv
DogName, Count
BELLA,111
BUDDY,81
SADIE,69
BAILEY,65
```

## Generate a cool name for your dog

The code takes one parameter, how many names to generate
for example i'd like to generate six names, i'll pass 5

```shell
python dogGenerator.py 5
```

this is my try ;)  

```shell
Kuke
Fare
Uika
Bee
Jeinie
```
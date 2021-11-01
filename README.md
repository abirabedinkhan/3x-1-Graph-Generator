# 3x+1 Graph Generator

The 3x+1 problem concerns an iterated function and the question of whether it always reaches 1 when starting from any positive integer. It is also known as the Collatz problem or the hailstone problem.

In this project, you can input a number and it will give a Graph that how you can reach 1, 2, 4 loops at the end.


## How it works?

User inputs a <b>positive integer</b>. 

+ If the number is even the following operation is carried out:

```
<the number> / 2
```

+ If the number is odd:

```
3 * <the number> + 1
```

This process is repeated with the result of one of the operations over and over.  As it appears, every number will eventually come to an infinate loop. When number 1 is reached -> 

```
3 * 1 + 1 = 4

4 / 2 = 2

2 / 2 = 1

3 * 1 + 1 = 4

...
```

## Installation

Install 3x+1 Graph Generator with pip3

```bash
  cd my-project
  pip3 install -r requirements.txt
  flask run
```
    
## License

[MIT](https://choosealicense.com/licenses/mit/)

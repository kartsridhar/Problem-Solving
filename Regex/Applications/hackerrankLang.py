# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

pattern = re.compile(r'^[1-9]\d{4}\s(C|CPP|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|CLOJURE|BASH|SCALA|ERLANG|CLISP|LUA|BRAINFUCK|JAVASCRIPT|GO|D|OCAML|R|PASCAL|SBCL|DART|GROOVY|OBJECTIVEC)$')
n = int(input())
for _ in range(n):
    string = input()
    if pattern.match(string):
        print("VALID")
    else:
        print("INVALID")
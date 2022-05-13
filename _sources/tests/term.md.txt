# Terminal tests

```{terminhtml}
---
echo:
---
echo $TERM
```

```{terminhtml}
---
echo:
---
export TERM=xterm-256color
echo $TERM
python -m rich
```
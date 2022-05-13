# Echo Tests

```{terminhtml}
---
cwd: .
echo:
---
echo 'Should always echo due to directive echo'
ls -l
```

```{terminhtml}
---
cwd: .
---
echo 'Should only echo when config terminhtml_echo=True'
ls -l
```
# CWD Tests

```{terminhtml}
---
cwd: .
disable-cache:
---
echo 'cwd .'
ls -l
```

```{terminhtml}
---
cwd: .
cwd-relative-to: cwd
---
echo 'cwd ., cwd-relative-to: cwd'
ls -l
```

```{terminhtml}
---
cwd: .
cwd-relative-to: current_source
---
echo 'cwd ., cwd-relative-to: current_source'
ls -l
```

```{terminhtml}
---
cwd: .
cwd-relative-to: sources_root
---
echo 'cwd ., cwd-relative-to: sources_root'
ls -l
```

```{terminhtml}
---
cwd: /home/nick/Dropbox/Python/sphinx-terminhtml/docsrc/source/binder
cwd-relative-to: sources_root
---
echo 'cwd absolute, cwd-relative-to: sources_root'
ls -l
```